# Embedded Systems & Diagnostics

Focused on embedded systems, mixed-signal hardware, and field-level diagnostics and calibration.

---

## Core Skills / Tools

**Embedded / Hardware**
- STM32 (F4 series)
- Mixed-signal PCB design (4-layer)
- RF layout (Sub-GHz, 50Ω matching)
- Power systems (buck-boost, LDO, battery management)
- Sensor integration (IMU, camera)

**Software**
- Python (real-time processing)
- OpenCV
- MediaPipe / Dlib
- Signal processing (temporal filtering, heuristic models)

**Tools**
- Altium Designer, KiCad
- Multimeter
- Oscilloscope (planned validation)
- VNA / Spectrum Analyzer (planned RF validation)
- Manufacturer service tools (Topcon systems)

---

### Precision Instrument Service Technician

Repair and calibration of Topcon total stations and automatic levels.

![Optical Calibration](Stand_Collimator.png)

- Serviced 200+ units in authorized environment  
- Performed optical alignment (collimation, reticle, compensator)  
- Diagnosed PCB-level faults (power and signal issues)  
- Repaired vertical encoders and mechanical assemblies  
- Verified calibration using manufacturer procedures and fixtures  

---
## Projects

### STM32 Wireless RF Communication Platform (Pre-Fabrication)

4-layer PCB designed to evaluate RF performance under mixed digital noise conditions.

![RF Board](./3d_visualization.png)

- Designed RF path with 50Ω matching and edge-mounted connector  
- Routed compact mixed-signal layout (RF, USB, power sharing same board)  
- Maintained continuous ground plane with via stitching  
- Implemented discrete RF matching network  
- Prepared for VNA, spectrum, and range testing post-fabrication  

---

### STM32 Mixed-Signal Control Board (Pre-Fabrication)

Embedded system combining MCU, IMU sensor, and buck-boost power stage.

![Mixed Signal Board](STM32_PCBA_3D_Top_Assembly.png)

- Designed 4-layer PCB with dedicated ground and power planes  
- Placed switching regulator away from sensor/control domain  
- Routed short I2C lines over continuous ground reference  
- Minimized high-current loops in power stage layout  
- Prepared validation for ripple, I2C integrity, and sensor stability  

---
### Driver Monitoring System (DMS) — Prototype

Real-time webcam-based system for fatigue detection using facial signals.

![DMS Telemetry](assets/Screenshot_2026-04-20.png)

- Built real-time pipeline using OpenCV and MediaPipe  
- Extracted EAR (eye), MAR (mouth), and head pose signals  
- Applied temporal filtering to stabilize noisy signals  
- Implemented heuristic fusion model for fatigue scoring  
- Tested under different lighting and motion conditions  

## Work Approach

- Start from system-level behavior, not assumptions  
- Trace faults through power, signal, and physical layout paths  
- Use measurement and verification instead of guesswork  
- Keep designs simple where possible, visible where not  
- Focus on restoring function before replacing components  
