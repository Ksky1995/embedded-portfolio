# Driver Monitoring System (DMS)  
### Real-Time Computer Vision Prototype (Webcam-Based Validation)

---

## System Reality Statement

This project is a **desktop-based real-time prototype** developed in Python and validated using a laptop webcam via Visual Studio Code.

It is **not an embedded or production automotive system**. The objective is to validate multi-signal fatigue detection logic under real-world visual noise conditions.

---

## What Was Actually Built

A real-time processing pipeline that extracts facial behavioral signals from live video input:

- Eye closure behavior (EAR – Eye Aspect Ratio)
- Mouth opening patterns (MAR – Mouth Aspect Ratio)
- Head orientation (2D approximation)

These signals are combined using a **heuristic scoring model** to estimate driver fatigue state in real time.

---

## Key Engineering Focus

Instead of model training, this project focuses on:

- Real-time signal stability under noisy inputs  
- Temporal filtering of biological signal fluctuations  
- Multi-feature decision fusion design  
- Separation of blink events vs fatigue states  

---

## Known System Behavior (Honest Evaluation)

### Strengths
- Works reliably under frontal face conditions  
- Handles short blinks correctly  
- Stable under moderate lighting conditions  
- Low-latency real-time execution on CPU  

---

### Failure Conditions
- Performance degrades under strong head rotation  
- Face tracking loss causes temporary state reset  
- Extreme lighting reduces landmark stability  
- EAR threshold sensitivity varies between users  

---

## Model Limitations

- No machine learning model (rule-based system only)  
- Fusion weights are heuristic (not statistically optimized)  
- No dataset-based validation or benchmarking performed  
- No embedded system deployment integration yet  

---

## Engineering Insight

This system demonstrates:

- Practical implementation of real-time facial signal extraction  
- Early-stage sensor fusion architecture design  
- Temporal filtering applied to physiological signals  
- Prototype-level validation of fatigue detection logic  

---

## Correct Positioning Summary

This project is a **real-time webcam-based computer vision prototype** that validates multi-signal fatigue detection logic using **heuristic fusion and temporal signal filtering techniques**.
