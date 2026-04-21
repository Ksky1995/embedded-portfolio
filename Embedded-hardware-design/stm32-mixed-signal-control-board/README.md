# STM32 Mixed-Signal Control Board [Pre-Fabrication]

**Altium Designer | 4-Layer PCB | STM32F411 | Power + Sensor Integrity | Battery System**

---

## System Overview

This project is a **pre-fabrication mixed-signal embedded system** integrating motion sensing, battery management, and regulated power delivery into a compact 4-layer PCB.

The core design challenge is preserving **low-noise sensor communication (IMU)** while operating alongside a **switching power stage and dynamic battery conditions**.

<p align="center">
  <img src="./STM32_PCBA_3D_Top_Assembly.png" width="500"/>
</p>

<p align="center"><em>3D assembly used to validate domain separation, power component placement, and connector accessibility.</em></p>

---

## System Architecture

The system is partitioned into functional domains to control noise coupling and ensure stable operation:

- **Control Domain:** STM32F411CEU6 (Cortex-M4, high-performance control)  
- **Sensor Domain:** MPU-6050 (I2C-based IMU for motion sensing)  
- **Power Domain:** Buck-boost regulation + Li-ion charging (BQ25303)  

### Key Design Decisions

- **Buck-boost topology** selected to maintain stable 3.3V output across full battery discharge range  
- **External IMU (I2C)** used instead of integrated solutions to allow flexible placement and noise isolation  
- **4-layer PCB** chosen to ensure controlled return paths and reduce ground impedance  

---

## PCB Stackup & Layout

A 4-layer stackup is used to manage return currents and isolate noisy subsystems:

- **Top Layer:** Critical routing and component placement  
- **Inner Layer 1:** Continuous ground plane (primary return path)  
- **Inner Layer 2:** 3.3V power plane  
- **Bottom Layer:** Signal routing and breakout  

<p align="center">
  <img src="./Four_layers_stack.png" width="500"/>
</p>

<p align="center"><em>Top layer showing physical separation between switching power stage and low-noise control/sensor region.</em></p>

<p align="center">
  <img src="./PCB_Layout_Bottom_Layer_Signal_Paths.png" width="500"/>
</p>

<p align="center"><em>Bottom layer used for controlled signal escape routing and via distribution.</em></p>

---

## Design Considerations

### Power Integrity

- Buck-boost regulator ensures stable output under:
  - Battery voltage variation  
  - Dynamic load conditions  
- High di/dt switching loops minimized through tight placement of:
  - Inductor  
  - Switching IC  
  - Input/output capacitors  

**Design Focus:**  
Reducing ripple and preventing switching noise from propagating into sensitive domains

---

### Signal Integrity (IMU / I2C)

- SDA/SCL traces kept short and routed over continuous ground reference  
- IMU placed away from switching nodes to reduce conducted and radiated noise  
- Parasitic capacitance minimized to maintain clean I2C edges  

**Design Focus:**  
Maintaining stable communication and reducing jitter in sensor data acquisition

---

### EMI Mitigation

- Physical separation between:
  - Power stage (noisy)  
  - Control + sensor domain (sensitive)  
- Continuous ground plane ensures controlled return current paths  
- Switching loop area minimized to reduce radiated emissions  

---

### Thermal Management

- Power components allocated copper area for heat spreading  
- Thermal vias used to transfer heat into internal planes  

**Design Focus:**  
Preventing localized heating that could affect regulator stability and sensor accuracy  

---

## Design Review Notes

- Switching current loops identified and minimized at layout level  
- Ground continuity preserved to avoid unintended return paths  
- Sensor placement prioritized low-noise operation over routing convenience  

**Potential Risks:**
- Switching noise coupling into I2C lines under high load  
- Output ripple affecting IMU measurement stability  
- Transient response of buck-boost regulator under rapid load changes  

---

## Project Status

- PCB design complete  
- Pre-fabrication stage (no hardware validation yet)  

---

## Planned Validation

- Power rail characterization:
  - Ripple measurement (oscilloscope)  
  - Load transient response  

- Sensor validation:
  - I2C signal integrity (rise/fall behavior)  
  - IMU data stability under power load variation  

- Thermal testing:
  - Regulator and inductor temperature under load  

- Full system bring-up:
  - STM32 initialization  
  - IMU communication and data acquisition  

---
