STM32 Autonomous Motion Controller [Pre-Fabrication]
4-Layer PCB | STM32F411 + BQ25306 BMS + MPU-6050 | Altium Designer

Overview
This hardware design is a pre-fabrication prototype for an autonomous motion platform. The architecture integrates high-current Li-ion power management (2A charging), an STM32 microcontroller, and IMU sensor fusion into a single compact 4-layer PCB. The primary engineering challenge was isolating the high-frequency switching noise of the power stage from the sensitive I2C sensor lines.

System Architecture & Component Selection

MCU: STM32F411CEU6 (ARM Cortex-M4) handling core logic and future AI/Sensor Fusion algorithms.

Power Stage: TPS63001 Buck-Boost Converter maintaining a stable 5V rail as the 2S battery drops from 8.4V to 6.0V.

BMS / Charger: BQ25306 Fast Charger managing a 2A charge cycle via USB-C, complete with NTC thermal cutoff safety features.

Sensory Input: MPU-6050 (6-axis IMU) routed with minimized trace lengths to prevent I2C bus capacitance issues.

Stackup & PCB Layout Strategy
The board utilizes a 4-layer stackup to prioritize Signal Integrity (SI) and Power Integrity (PI):

Top Layer: High-speed MCU routing, localized component placement, and thermal pours.

Inner Layer 1 (GND): Unbroken ground plane providing a low-impedance return path for 400kHz I2C lines and switching currents.

Inner Layer 2 (3.3V / 5V): Split power planes to reduce voltage drop and isolate the MCU power supply from the battery charging rails.

Bottom Layer: Low-speed GPIO routing and test points for field diagnostics.

Engineering Challenges & Design Iterations

Thermal Management on Power Switch: Initial power path calculations revealed a potential 1.5W dissipation on the AOD4185 MOSFET power switch. The layout was iterated to include a larger top-layer copper polygon and thermal vias to safely sink this heat into the internal ground plane.

EMI Mitigation: The TPS63001 inductor and switching nodes were tightly grouped to minimize the AC current loop area, preventing high-frequency noise injection into the adjacent MPU-6050 analog supply lines.
