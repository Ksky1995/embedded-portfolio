import cv2
import mediapipe as mp
import numpy as np
import time
from collections import deque

# ---------------- INITIALIZATION ---------------- #
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

def calculate_ear(eye_points):
    v1 = np.linalg.norm(np.array(eye_points[1]) - np.array(eye_points[5]))
    v2 = np.linalg.norm(np.array(eye_points[2]) - np.array(eye_points[4]))
    h = np.linalg.norm(np.array(eye_points[0]) - np.array(eye_points[3]))
    return (v1 + v2) / (2.0 * h)

def calculate_mar(mouth_points):
    vertical = np.linalg.norm(np.array(mouth_points[0]) - np.array(mouth_points[1]))
    horizontal = np.linalg.norm(np.array(mouth_points[2]) - np.array(mouth_points[3]))
    return vertical / horizontal

def get_head_tilt(face):
    left_eye = face.landmark[33]
    right_eye = face.landmark[263]

    dx = right_eye.x - left_eye.x
    dy = right_eye.y - left_eye.y

    angle = np.degrees(np.arctan2(dy, dx))
    return angle

# ---------------- LANDMARKS ---------------- #
LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]
MOUTH = [13, 14, 78, 308]

# ---------------- PARAMETERS ---------------- #
COUNTER = 0
BLINK_MAX_FRAMES = 10
EYE_AR_CONSEC_FRAMES = 30
SMOOTHING_WINDOW = 5

EAR_HISTORY = []
BASELINE_EAR = []
CALIBRATION_FRAMES = 50
EYE_AR_THRESH = 0.17

EAR_BUFFER = deque(maxlen=100)

NO_FACE_COUNTER = 0
NO_FACE_LIMIT = 20

# NEW PARAMETERS
MAR_THRESH = 0.6
YAWN_FRAMES = 15
yawn_counter = 0

HEAD_TILT_THRESH = 15

cap = cv2.VideoCapture(0)
p_time = 0

print("DMS System Online. Press 'q' to exit.")

# ---------------- GRAPH FUNCTION ---------------- #
def draw_ear_graph(frame, ear_buffer):
    graph_h, graph_w = 100, 300
    graph = np.zeros((graph_h, graph_w, 3), dtype=np.uint8)

    if len(ear_buffer) > 1:
        max_ear = max(ear_buffer)
        min_ear = min(ear_buffer)
        range_ear = max_ear - min_ear if max_ear != min_ear else 1

        for i in range(1, len(ear_buffer)):
            x1 = int((i - 1) * graph_w / len(ear_buffer))
            y1 = int(graph_h - ((ear_buffer[i - 1] - min_ear) / range_ear) * graph_h)
            x2 = int(i * graph_w / len(ear_buffer))
            y2 = int(graph_h - ((ear_buffer[i] - min_ear) / range_ear) * graph_h)

            cv2.line(graph, (x1, y1), (x2, y2), (0, 255, 0), 1)

    frame[10:110, 10:310] = graph

# ---------------- MAIN LOOP ---------------- #
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    status = "AWAKE"
    color = (0, 255, 0)
    confidence = 0

    fatigue_score = 0
    mar = 0
    tilt = 0
    yawning = False
    looking_away = False

    if results.multi_face_landmarks:
        NO_FACE_COUNTER = 0
        face = results.multi_face_landmarks[0]

        def get_pts(indices):
            return [(int(face.landmark[i].x * w), int(face.landmark[i].y * h)) for i in indices]

        # ---------------- EYES ---------------- #
        left_eye = get_pts(LEFT_EYE)
        right_eye = get_pts(RIGHT_EYE)

        for pt in left_eye + right_eye:
            cv2.circle(frame, pt, 2, (0, 255, 0), -1)

        left_ear = calculate_ear(left_eye)
        right_ear = calculate_ear(right_eye)
        current_ear = (left_ear + right_ear) / 2.0

        # ---------------- MOUTH (YAWN) ---------------- #
        mouth_pts = get_pts(MOUTH)
        for pt in mouth_pts:
            cv2.circle(frame, pt, 2, (255, 0, 0), -1)

        mar = calculate_mar(mouth_pts)

        if mar > MAR_THRESH:
            yawn_counter += 1
        else:
            yawn_counter = 0

        yawning = yawn_counter > YAWN_FRAMES

        # ---------------- HEAD POSE ---------------- #
        tilt = get_head_tilt(face)
        looking_away = abs(tilt) > HEAD_TILT_THRESH

        # ---------------- CALIBRATION ---------------- #
        if len(BASELINE_EAR) < CALIBRATION_FRAMES:
            BASELINE_EAR.append(current_ear)
            status = "CALIBRATING..."
            color = (255, 255, 0)

        else:
            if len(BASELINE_EAR) == CALIBRATION_FRAMES:
                EYE_AR_THRESH = np.mean(BASELINE_EAR) * 0.75
                BASELINE_EAR.append(999)

            # ---------------- SMOOTHING ---------------- #
            EAR_HISTORY.append(current_ear)
            if len(EAR_HISTORY) > SMOOTHING_WINDOW:
                EAR_HISTORY.pop(0)

            smoothed_ear = sum(EAR_HISTORY) / len(EAR_HISTORY)

            EAR_BUFFER.append(smoothed_ear)

            # ---------------- EAR LOGIC ---------------- #
            if smoothed_ear < EYE_AR_THRESH:
                COUNTER += 1

                if BLINK_MAX_FRAMES < COUNTER < EYE_AR_CONSEC_FRAMES:
                    status = "Eyes Closing..."
                    color = (0, 255, 255)

                elif COUNTER >= EYE_AR_CONSEC_FRAMES:
                    fatigue_score += 2

            else:
                COUNTER = 0

            # ---------------- FUSION MODEL ---------------- #
            if yawning:
                fatigue_score += 1

            if looking_away:
                fatigue_score += 1

            # ---------------- FINAL STATE ---------------- #
            if fatigue_score >= 3:
                status = "!!! HIGH DROWSINESS !!!"
                color = (0, 0, 255)

            elif fatigue_score == 2:
                status = "Drowsy"
                color = (0, 165, 255)

            elif fatigue_score == 1:
                status = "Warning"
                color = (0, 255, 255)

            else:
                status = "AWAKE"
                color = (0, 255, 0)

            cv2.putText(frame, f"EAR: {smoothed_ear:.2f}", (30, 140),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    else:
        # ---------------- FAIL SAFE ---------------- #
        NO_FACE_COUNTER += 1

        if NO_FACE_COUNTER > NO_FACE_LIMIT:
            status = "NO FACE DETECTED"
            color = (0, 0, 255)
            COUNTER = 0
            fatigue_score = 0

    # ---------------- GRAPH ---------------- #
    draw_ear_graph(frame, EAR_BUFFER)

    # ---------------- UI ---------------- #
    cv2.putText(frame, f"Frames: {COUNTER}", (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

    cv2.putText(frame, f"Fatigue Score: {fatigue_score}", (30, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.putText(frame, f"MAR: {mar:.2f}", (30, 110),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.putText(frame, f"Tilt: {tilt:.1f}", (30, 140),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.putText(frame, status, (30, 180),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)

    # ---------------- FPS ---------------- #
    c_time = time.time()
    fps = 1 / (c_time - p_time)
    p_time = c_time

    cv2.putText(frame, f"FPS: {int(fps)}", (w - 120, 40),
                cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 255, 255), 2)

    cv2.imshow("DMS - Multi-Signal Fusion", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
