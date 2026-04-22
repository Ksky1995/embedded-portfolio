# STM32 Mixed-Signal Control Board [Pre-Fabrication]

**Altium Designer | 4-Layer PCB | STM32F411 | Battery System | Power Integrity | Sensor Fidelity**

---

## System Overview

This project is a **pre-fabrication mixed-signal embedded system** designed to operate a motion sensor (IMU) under **non-ideal power conditions**, including battery voltage variation and switching regulator noise.

Unlike simple MCU + sensor designs, this board addresses a key challenge:

> Maintaining **low-noise, stable sensor communication** while a **buck-boost power stage injects high-frequency switching noise into the system**.

<p align="center">
  <img src="./STM32_PCBA_3D_Top_Assembly.png" width="500"/>
</p>

<p align="center"><em>3D view used to validate physical separation between switching power stage and low-noise sensor/control domains.</em></p>

---

## System Architecture

The system is intentionally partitioned to control noise propagation paths:

- **Control Domain:** STM32F411CEU6 (high-speed Cortex-M4 for real-time processing)  
- **Sensor Domain:** MPU-6050 (I2C-based IMU, sensitive to supply and ground noise)  
- **Power Domain:** Buck-boost regulator + Li-ion charger (BQ25303)  

### Engineering Constraint

The IMU operates on **low-level analog sensing internally**, meaning:

- Power ripple  
- Ground bounce  
- I2C edge distortion  

can directly degrade measurement quality.

---

## Schematic-Level Design (Where Most Noise Problems Begin)

![Figure 1: STM32F4 & IMU Control Schematic](STM32F4_IMU_Control_Schematic.png)

**What matters here:**
- Local decoupling at MCU and IMU supply pins  
- Short I2C topology (no branching, minimal parasitics)  

**Design Risk:**
- I2C is not differential → highly vulnerable to ground noise and ringing  

---

![Figure 2: BMS and Buck-Boost Power Stage](BQ25303_BMS_Lithium_Charger.png)

**What matters here:**
- Integrated Li-ion charging + regulation in same domain  
- High-frequency switching node introduces EMI source  

**Engineering Tension:**
- Power stage must be efficient  
- But switching noise must not corrupt sensor data  

---

## PCB Stackup & Layout Strategy

A 4-layer stackup is used not for convenience, but to control **return current behavior**:

- **Top Layer:** Critical routing and component placement  
- **Inner Layer 1:** Continuous ground plane (low impedance return path)  
- **Inner Layer 2:** 3.3V power plane  
- **Bottom Layer:** Signal routing and escape  

<p align="center">
  <img src="./Four_layers_stack.png" width="500"/>
</p>

<p align="center"><em>Top layer showing deliberate separation between switching power stage and sensor/control region.</em></p>

---

## Layout Execution (Where Design Either Works or Fails)

### Top Layer – Domain Separation & Noise Containment
<p align="center">
  <img src="./PCB_Layout_Top_Layer_Signal_Paths.png" width="500"/>
</p>

**What this shows:**
- Physical isolation between:
  - Switching regulator  
  - MCU + IMU  
- Short high-current loops near power stage  

**Reviewer Hook:**
> How effective is physical separation alone without filtering?

---

### Bottom Layer – Return Path Control & Signal Escape
<p align="center">
  <img src="./PCB_Layout_Bottom_Layer_Signal_Paths.png" width="500"/>
</p>


**What this shows:**
- Controlled via transitions  
- Signal escape routing without fragmenting ground return paths  

**Design Insight:**
Poor via strategy here would create **hidden EMI issues**.

---

## Design Considerations

### Power Integrity (Core Challenge)

- Buck-boost regulator selected to handle full battery discharge range  
- High di/dt loops minimized via tight placement of:
  - Switching IC  
  - Inductor  
  - Input/output capacitors  

**Unresolved Question (Intentional):**
> Is output ripple low enough to avoid affecting IMU readings?

---

### Signal Integrity (I2C / IMU)

- Short SDA/SCL traces routed over continuous ground  
- IMU placed away from switching node and inductor  

**Critical Limitation:**
- No dedicated analog ground or filtering stage → potential noise injection path  

---

### EMI Mitigation

- Loop area minimization in switching stage  
- Ground plane continuity maintained  

**Trade-off:**
- No ferrite bead or LC isolation between power and sensor domains  
→ simpler design, but higher noise risk  

---

### Thermal Behavior

- Copper areas used for passive heat spreading  
- Thermal vias connected to internal planes  

**Potential Issue:**
- Thermal rise could shift regulator characteristics under load  

---

## Design Review Notes

- Switching loop identified and minimized (layout-driven noise control)  
- Sensor placement optimized for noise avoidance, not routing convenience  
- Ground continuity preserved across layers  

---

## Known Risks & Open Questions

This design intentionally exposes real engineering uncertainty:

- Will switching ripple couple into IMU measurements?  
- Is I2C robust under dynamic load conditions?  
- Does layout alone sufficiently isolate noise without filtering?  

---

## Project Status

- PCB design complete  
- Pre-fabrication (no electrical validation yet)  

---

## Planned Validation

- **Power Analysis:**
  - Output ripple measurement  
  - Load transient response  

- **Signal Integrity:**
  - I2C waveform quality (rise/fall, ringing)  
  - Noise injection testing under load  

- **Sensor Validation:**
  - IMU stability vs power load variation  

- **Thermal Testing:**
  - Regulator and inductor temperature profiling  

---
