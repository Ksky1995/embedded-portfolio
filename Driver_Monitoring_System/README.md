## Driver Monitoring System (DMS)  
### Algorithm Prototype & Evaluation Phase (Webcam-Based System)

---

## Project Overview

This repository contains a **real-time computer vision prototype** developed to evaluate multi-signal fatigue detection logic in a controlled desktop environment using a standard laptop webcam.

The objective of this work is to validate the **feasibility of temporal filtering and heuristic signal fusion** before transitioning to embedded hardware platforms such as STM32 or ESP32-CAM.

This implementation represents a **prototype evaluation stage**, not a deployed or production system.

## 🖥️ System Demonstration
![DMS Telemetry Validation](assets/Screenshot_2026-04-20.png)
*Figure 1: Real-time telemetry showing EAR/MAR tracking, temporal signal graph (top-left), and heuristic state classification (Drowsy).*

---

## Tech Stack & Environment

- **Language:** Python 3.x  
- **Computer Vision:** OpenCV  
- **Facial Landmark Model:** MediaPipe / Dlib  
- **Execution Environment:** Visual Studio Code (Desktop)  
- **Input Source:** Laptop integrated webcam (real-time stream)  
- **Future Interface Design:** UART / Serial communication prepared conceptually  

---
![Uploading Screenshot 2026-04-20 141951.png…]()

## System Processing Pipeline

The system processes real-time video frames through the following stages:

### Feature Extraction Layer
Physiological behavioral signals are extracted from facial landmarks:

- **Eye Aspect Ratio (EAR):** Detects eyelid closure patterns for fatigue estimation  
- **Mouth Aspect Ratio (MAR):** Detects yawning events and duration  
- **Head Pose Approximation:** Estimates 2D orientation for attention tracking  

---

### Signal Processing Layer
Raw signals are refined using:

- Temporal smoothing (moving average filtering)  
- Frame-based persistence logic  
- Blink rejection thresholding  

This stage reduces instability caused by natural facial micro-movements and tracking noise.

---

### Decision Fusion Layer
A heuristic scoring model combines multiple signals:

- EAR contributes primary fatigue weighting  
- MAR contributes secondary fatigue confirmation  
- Head pose contributes attention deviation factor  

Final output is computed as a **Fatigue Index score**, mapped to system states.

---

## Observed System Behavior (Experimental Conditions)

### Observed Strengths
- Real-time execution on CPU without GPU dependency  
- Stable detection under frontal face orientation  
- Effective suppression of short-duration blink artifacts  
- Functional temporal noise filtering under normal lighting  

---

### Observed Limitations
- Degraded performance under large head rotations (> moderate angle deviation)  
- Reduced landmark stability under low-light conditions  
- Sensitivity to individual EAR baseline variation  
- Occasional face-loss resets under fast motion  

---

## Engineering Constraints Identified

- No dataset-based statistical validation performed  
- Rule-based fusion model (non-trained heuristic system)  
- No formal accuracy or confusion matrix evaluation  
- Thresholds require per-user calibration during initialization  

---

## Embedded System Transition Intent

This prototype is designed as a **pre-embedded validation layer** for future hardware deployment.

Planned transitions include:

- Porting logic to C++ for STM32 / ESP32 platforms  
- Implementing UART-based fatigue signal output  
- Integrating camera module into embedded hardware system  
- Optimizing inference for low-power edge execution  

---

## Engineering Insight

This project demonstrates:

- Real-time facial signal extraction under noisy conditions  
- Early-stage multi-sensor fusion architecture design  
- Temporal filtering applied to physiological signals  
- Prototype-level validation of fatigue detection logic in a constrained environment  

---

## Summary

This work represents a **real-time computer vision prototype evaluation phase**, focused on validating multi-signal fatigue detection logic using heuristic fusion and temporal signal processing techniques prior to embedded system deployment.
