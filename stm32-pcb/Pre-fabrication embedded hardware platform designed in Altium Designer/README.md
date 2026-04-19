# STM32 Motion Control Hardware Platform [Pre-Fabrication]

4-Layer PCB | STM32F411 + Power Management + MPU-6050 | Altium Designer

---

## Overview

This project presents a **pre-fabrication embedded hardware platform** designed for motion control and sensing applications.

The system integrates **Li-ion power management, an STM32 microcontroller, and an IMU sensor** into a compact 4-layer PCB. The primary design challenge was maintaining signal integrity while handling high-frequency switching noise from the power stage.

---

## System Architecture & Component Selection

**MCU:** STM32F411CEU6 (ARM Cortex-M4)

* Selected for sufficient processing capability for future control and sensor-processing tasks
* Provides flexible peripheral interfaces (I2C, SPI, UART)

**Power Stage:** TPS63001 Buck-Boost Converter

* Maintains a stable system rail under varying battery conditions
* Chosen for high efficiency and wide input range

**Battery Charging / Power Management:** BQ25306

* Integrated Li-ion charging with thermal regulation (NTC support)
* Designed for USB-powered charging scenarios

**Sensor:** MPU-6050 (6-axis IMU)

* Provides motion and orientation data
* Routed with minimized trace length to reduce I2C bus noise sensitivity

---

## Stackup & PCB Layout Strategy

The design uses a **4-layer stackup** to improve signal and power integrity:

* **Top Layer:** High-speed routing, critical component placement
* **Inner Layer 1 (GND):** Continuous ground plane for low-impedance return paths
* **Inner Layer 2 (Power):** Dedicated power distribution (3.3V / system rails)
* **Bottom Layer:** Low-speed signals, GPIO routing, and test points

### Design Intent

* Ensure clean return paths for switching and digital signals
* Reduce EMI through tight current loop control
* Provide stable power delivery to MCU and sensor subsystems

---

## Engineering Challenges & Design Decisions

### Thermal Management (Power Path)

Initial estimates indicated significant heat dissipation in the power switching path.
To address this:

* Expanded copper area for heat spreading
* Added thermal vias to couple heat into internal planes

---

### EMI Mitigation

The switching regulator introduced potential high-frequency noise risks.

Mitigation strategies:

* Minimized high di/dt loop area around the regulator and inductor
* Physically separated switching nodes from IMU signal routing
* Maintained solid ground reference under sensitive traces

---

### Signal Integrity (I2C / Sensor)

* Short trace routing for SDA/SCL lines
* Continuous ground reference to reduce impedance
* Avoided routing near switching nodes

---

## Design Review Notes

* Critical current loops identified and minimized
* Power and signal domains carefully separated
* Potential risk areas:

  * Noise coupling from switching stage into sensor lines
  * Power transient behavior under dynamic load

---

## Project Status

PCB design completed (not yet fabricated or validated)

---

## Future Work

* Fabrication and bring-up
* Power rail validation (ripple, load response)
* STM32 firmware development
* IMU data acquisition and processing

---
