# STM32 Motion Control Hardware Platform [Pre-Fabrication]

**Technologies:** Altium Designer | 4-Layer PCB Design | STM32F4 | Embedded Systems | Power Management (BMS) | Signal Integrity

---

## 🚀 System Overview

This project is a **pre-fabrication embedded hardware platform** designed for robust motion control and sensing applications. It integrates a complete Lithium-ion power management system, an STM32 Cortex-M4 microcontroller, and a 6-axis IMU onto a compact, highly optimized 4-layer PCB. 

The core engineering objective was to design a manufacturable board that maintains strict signal integrity for sensitive sensor data while safely handling high-frequency switching noise from the integrated power stage.

![Figure 1: 3D Visualization of the Integrated Sensor & Power Management PCBA](STM32_PCBA_3D_Top_Assembly.png)
*Figure 1: 3D Assembly highlighting component density, connector placement, and physical layout strategy.*

---

## 🧠 System Architecture & Component Selection

The architecture is divided into clear logical domains to isolate high-current power paths from sensitive digital communications.

* **MCU (STM32F411CEU6):** ARM Cortex-M4 selected for DSP capabilities required in future motion-control algorithms. Features flexible peripheral routing (I2C, SPI, UART).
* **6-Axis Sensor (MPU-6050):** IMU placed with minimized trace lengths to the MCU to reduce I2C bus capacitance and noise susceptibility.
* **Power Regulation (TPS63001):** High-efficiency Buck-Boost converter chosen to maintain a rock-solid 3.3V system rail across the entire discharge curve of a Li-ion cell.
* **Battery Management (BQ25306):** Integrated charging IC featuring thermal regulation (NTC support) for safe, reliable USB-powered charging.

### Schematic Design

![Figure 2: STM32F4 & IMU Control Schematic](STM32F4_IMU_Control_Schematic.png)
*Figure 2: Logic and sensor domain schematics.*

![Figure 3: BMS and Buck-Boost Power Stage](BQ25303_BMS_Lithium_Charger.png)
*Figure 3: Power distribution and Lithium-ion battery management schematics.*

---

## 🏗️ Stackup & PCB Layout Strategy

A **4-layer stackup** was implemented to strictly control impedance, manage return currents, and shield sensitive communication lines. 

* **Layer 1 (Top):** High-speed routing, high-density component placement, and localized copper pours for thermal dissipation.
* **Layer 2 (Inner GND):** Continuous, unbroken ground plane to provide lowest-impedance return paths and contain EMI.
* **Layer 3 (Inner Power):** Dedicated power distribution for the 3.3V system rail.
* **Layer 4 (Bottom):** Low-speed GPIO signals, escape routing, and test points.

![Figure 4: High-Speed Signal Routing and Ground Plane Geometry (Top Layer)](Four_layers_stack.png)
*Figure 4: Top layer layout demonstrating solid GND copper pours for noise reduction and thermal mass.*

![Figure 5: Bottom Layer Signal Escape Routing and Via Strategy](PCB_Layout_Bottom_Layer_Signal_Paths.png)
*Figure 5: Bottom layer demonstrating clean escape routing and via placement.*

---

## ⚙️ Engineering Rigor & Problem Solving

During the layout phase, several system-level challenges were actively mitigated:

* **EMI Mitigation:** The switching regulator introduces high-frequency noise risks. This was mitigated by minimizing the high *di/dt* loop area around the TPS63001 and inductor, and physically isolating the switching nodes away from the IMU's I2C lines.
* **Signal Integrity:** Maintained a continuous ground reference under all sensitive traces. Shortened I2C routing to minimize parasitic capacitance. 
* **Thermal Management:** The power path required careful thermal consideration. Expanded top-layer copper areas were utilized for heat spreading, coupled with strategically placed thermal vias to sink heat into the internal ground plane.

---

## 📅 Project Status & Next Steps

* **Current Status:** Schematic and PCB Layout complete. Ready for manufacturing.
* **Phase 2:** Bare-board fabrication and PCBA bring-up.
* **Phase 3:** Power rail validation (measuring voltage ripple and dynamic load response under oscilloscope).
* **Phase 4:** STM32 firmware development for IMU data acquisition and sensor fusion.
