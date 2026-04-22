# Paing Hein Khant

**Embedded Hardware Engineer | Precision Instrument Diagnostics | PCB Design**

STM32 • Mixed-Signal Systems • RF Design • Hardware Debugging

---

## Overview

Electronics engineer with hands-on work in **precision instrument repair and PCB fault diagnosis**, now focused on **embedded hardware design and system integration**.

Serviced and calibrated **200+ high-precision surveying instruments** under a **Topcon authorized dealer**, diagnosing failures across optical, electronic, and mechanical subsystems.

Currently building embedded hardware with focus on:
- Signal integrity in mixed-signal systems  
- Power behavior under changing load conditions  
- Layout decisions to reduce noise  

---

## Field Engineering Experience

### Precision Instrument Service Technician

Calibration and repair of Topcon and Sokkia total stations and auto levels.

- Serviced 200+ instruments following manufacturer procedures  
- Adjusted optical alignment and compensator systems  
- Repaired PCB faults including vertical encoder issues affecting angle measurement  
- Isolated faults across analog, digital, and mechanical subsystems  

<p align="center">
  <img src="Topcon_sokkia_service_technician/Vertical_Encoder_Repair.png" width="320"/>
</p>

<p align="center">
  <em>Encoder disassembly and fault correction impacting angle measurement precision</em>
</p>

---

## Hardware Projects

### STM32 Mixed-Signal Control Board

4-layer embedded system integrating MCU, IMU, and switching power stage.

- Used a dedicated ground plane to keep return paths continuous for I2C and switching currents  
- Routed I2C close to ground and kept it away from high di/dt switching nodes  
- Separated power stage from sensor area to reduce noise coupling into IMU  
- Integrated buck-boost regulator and Li-ion charging on the same board  

<p align="center">
  <img src="Embedded-hardware-design/stm32-mixed-signal-control-board/PCB_Layout_Top_Layer_Signal_Paths.png" width="420"/>
</p>

<p align="center">
  <em>Layout partitioning: switching regulator isolated from IMU signal region</em>
</p>

---

### RF Embedded Development Board

Sub-GHz RF platform designed under shared digital and power constraints.

- Built RF path with discrete 50Ω matching network based on trace geometry and placement  
- Kept impedance consistent by avoiding vias and sudden width changes  
- Controlled return path through ground to reduce coupling and radiation  
- Checked interaction between RF and digital circuits sharing the same 3.3V rail  

<p align="center">
  <img src="Embedded-hardware-design/rf-embedded-development-board/pcb_top_layer.png" width="520"/>
</p>

<p align="center">
  <em>RF trace routing with matching network placed close to output stage</em>
</p>

---

## Software Project

### Driver Monitoring System (DMS)

Real-time fatigue detection using computer vision.

- Built real-time pipeline using OpenCV and MediaPipe  
- Extracted EAR, MAR, and head pose from video  
- Applied temporal filtering to stabilize detection  

---

## Engineering Approach

- Identify noise sources and control return paths early in layout  
- Solve problems through placement, grounding, and routing before adding complexity  
- Apply field repair experience to anticipate failure points  
- Keep designs practical and serviceable  

---

## Core Skills

### Embedded Hardware
- STM32F411, 4-layer PCB design  
- Mixed-signal layout and grounding strategy  
- RF routing and impedance awareness  
- Buck-boost power systems, Li-ion charging  
- IMU integration (MPU-6050)  

### Diagnostics & Field Work
- PCB fault isolation and repair  
- Optical alignment and calibration  
- Signal integrity troubleshooting  

### Software
- Python, OpenCV, MediaPipe  
- Real-time signal processing  

### Tools
- Altium Designer, KiCad  
- Oscilloscope (signal analysis)  
- Multimeter  
- Precision calibration equipment  

---

## Direction

Focused on roles in:
- Embedded hardware design  
- PCB design and system integration  
- Hardware debugging and validation  

---

## Contact

Yangon, Myanmar  
paingheinkhant00@gmail.com  
WhatsApp: +95 758653198  
LinkedIn: https://www.linkedin.com/in/paing-hein-khant-307640385
