# PAING HEIN KHANT

*Electronics Engineer (BE Ec)*

Electronics Engineer with 1+ years of technical service in Topcon & Sokkia instrumentation and the design of high-density embedded PCBs (RF & Mixed-Signal). Currently developing Edge AI models to bridge industrial hardware with intelligent computer vision.

---

## TECHNICAL CORE

| Domain | Specialization | Tools |
| :--- | :--- | :--- |
| **PCB Design** | 4-Layer FR4 / 50Ω Matching / Differential Pairs | Altium / KiCad / LTspice |
| **Service Engineering** | OEM Standards / RCA / Optical Calibration | OEM Standard Collimators |
| **Hardware Debug** | Board-Level Recovery / Signal Analysis / Rework | Oscilloscope / Multimeter / Soldering |
| **Embedded AI** | Edge CV (EAR) / Computer Vision | ESP32-CAM / Python / C |

---

### INDUSTRIAL SERVICE & RECOVERY
**[Hardware Diagnostics Portfolio](./hardware-diagnostics/)**

* **OEM Factory Expertise** — Received on-site training from **Topcon Malaysia** experts; strictly following **SOPs** for the calibartion and board-level repair of Topcon & Sokkia systems.
* **Max Precision Validation** — **Standard Collimator Calibrations** and rigorous inspections to guarantee sub-millimeter field accuracy.
* **Operational Impact** — Consistently maintained a high **First-Time Fix Rate (FTFR)** through expert diagnostics and fault isolation.
---



## EMBEDDED SYSTEMS PCB ARCHITECTURE
**Featured Engineering Portfolio**

#### **[STM32 Wireless Control Unit](./stm32-pcb/)** — *4-Layer RF Design*
* **RF & Impedance** — Implemented a $50\Omega$ matched 2.4GHz path with a discrete Pi-network and Low Pass Filter (LPF) for the **STM32WB55** dual-core SoC.
* **Industrial Hardening** — Integrated dedicated **USB-C ESD protection** and optimized dual-crystal clocking (HSE/LSE) to ensure high-speed signal stability and timing precision.

#### **[Precision Motion & Power Platform](./motion-pcb/)** — *Multi-Domain System Design*
* **Engineered Power Delivery** — Developed a high-efficiency power stage utilizing the **TPS63001** Buck-Boost converter to maintain stable +3.3V/5V rails from fluctuating battery inputs.
* **Synthesized Sensor Fusion** — Integrated an **MPU-6050** IMU with an **STM32F4** core, implementing mixed-signal layout techniques to preserve high-fidelity motion data against switching noise.
---

## 03 // EDGE AI & IoT INTEGRATION
**[Intelligence Hub](./ai-learning/)** — *Computer Vision & IoT Research*

#### **Driver Drowsiness System (PoC)**
* **Inference Logic** — Developed a real-time **Eye Aspect Ratio (EAR)** algorithm utilizing **Mediapipe** and **OpenCV** to monitor fatigue thresholds via local vision stream.
* **Algorithm Validation** — Successfully prototyped facial landmark detection to calculate drowsiness metrics with high temporal resolution on a local environment.

#### **ESP32-CAM IoT Implementation**
* **Remote Capture System** — Engineered a **Telegram Bot API** interface allowing remote image acquisition via secure `/photo` command triggers.
* **Firmware Optimization** — Implemented Wi-Fi stack management on the ESP32 to handle asynchronous HTTP requests and JPEG stream buffering.
