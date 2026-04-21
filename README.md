# Embedded systems and diagnostics  
STM32, RF boards, Python vision systems  
Focus on debugging, integration, and field repair  

---

## Core Skills

**Embedded Systems**
- STM32F411, 4-layer PCB design  
- Sub-GHz RF, 50Ω matching  
- Buck-boost power, Li-ion charging (BQ25303)  
- IMU integration (MPU-6050)  

**Software**
- Python 3.x  
- OpenCV, MediaPipe, Dlib  
- Real-time signal processing (EAR, MAR)  

**Tools / Work**
- Altium Designer, KiCad 9  
- Multimeter  
- Topcon calibration tools  
- Field repair and diagnostics  

---

## Project Overview

### Precision Instrument Service Technician

Repair and calibration of Topcon total stations and auto levels.

- Calibrated optical systems using collimator alignment setups  
- Adjusted reticle, line-of-sight, and compensators  
- Diagnosed PCB faults (power and signal issues)  
- Repaired vertical encoders without full replacement  
- Verified calibration using manufacturer procedures  

---

### Driver Monitoring System (DMS)

Webcam-based fatigue detection prototype for algorithm validation.

- Built real-time pipeline using OpenCV and MediaPipe  
- Extracted EAR, MAR, and head pose from facial landmarks  
- Applied temporal filtering to stabilize signals  
- Implemented heuristic fatigue scoring model  
- Tested under lighting and motion variation  

---

### STM32 Wireless RF Communication Platform

4-layer RF board testing performance under digital noise conditions.

- Designed Sub-GHz RF path with discrete L/C matching  
- Routed short RF trace without vias  
- Integrated USB interface with shared 3.3V supply  
- Maintained continuous ground plane with via stitching  
- Prepared VNA, spectrum, and range validation  

---

### STM32 Mixed-Signal Control Board

STM32 + IMU system running with switching power noise.

- Designed 4-layer PCB with dedicated ground and power planes  
- Integrated BQ25303 buck-boost and Li-ion charging  
- Minimized switching loop area in power stage  
- Routed short I2C lines over continuous ground  
- Planned validation for ripple and I2C signal integrity  

---

## Example Work

![Optical Calibration Setup](Stand_Collimator.png)

- Collimator setup used for line-of-sight calibration  

![DMS Telemetry Output](assets/Screenshot_2026-04-20.png)

- Real-time EAR/MAR tracking with fatigue state output  

![RF PCB 3D View](3d_visualization.png)

- RF connector placement and layout separation  

![Mixed-Signal Board 3D](STM32_PCBA_3D_Top_Assembly.png)

- Separation between switching power and sensor domain  

---

## Work Approach

- Start from system behavior, not assumptions  
- Trace faults through power, signal, and layout  
- Use measurement to confirm issues  
- Fix root cause before replacing parts  
- Keep designs simple and testable  
