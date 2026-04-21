# STM32 Wireless RF Communication Platform [Pre-Fabrication]

**KiCad 9 | 4-Layer PCB | STM32WB55 | Sub-GHz RF | 50Ω Matching | RF Signal Integrity**

---

## System Overview

This project is a **pre-fabrication mixed-signal RF embedded system** designed for wireless communication in the sub-GHz band.

Unlike typical MCU + RF designs, this board addresses a key challenge:

> Maintaining a **low-noise, impedance-controlled RF signal path** while high-speed digital switching and USB activity introduce broadband interference into the system.

![3D Visualization](./3d_visualization.png)

*3D visualization used to validate physical separation between RF front-end, MCU, and USB/power domains.*

**What this shows:**

* RF connector placed at board edge (controlled launch region)
* MCU centrally located with dense decoupling
* USB + power circuitry positioned to limit direct coupling into RF path

---

## System Architecture

The system is partitioned to control **noise propagation paths**, not just functionality:

* **Control Domain:** STM32WB55 (integrated wireless MCU, digital switching source)
* **RF Domain:** On-chip RF front-end with external matching network
* **Power Domain:** USB-C input → LDO → shared 3.3V rail

### Engineering Constraint

The RF front-end operates with high sensitivity, meaning:

* Power ripple
* Digital harmonics
* Ground discontinuities

can directly degrade:

* Receiver sensitivity
* Link reliability
* Effective communication range

---

## Schematic-Level Design (Where RF Problems Begin)

![Schematic](./schematic.png)

*System schematic showing USB interface, power regulation, MCU, and RF matching network.*

**What matters here:**

* **RF Matching Network:** Discrete L/C network approximating 50Ω impedance
* **USB Interface:** High-speed differential signals introducing noise sources
* **Shared Power Rail:** RF and digital circuits powered from same 3.3V domain
* **Clock Sources:** Stability directly impacts RF performance

**Design Risk:**

* Matching network is **theoretical without VNA validation**
* USB + MCU switching introduces **broadband noise sources**

**Reviewer Hook:**

> Does USB activity measurably degrade RF sensitivity or noise floor?

---

## PCB Stackup & Layout Strategy

A 4-layer stackup is used to control **return current behavior**:

* **Top Layer:** RF routing + critical components
* **Inner Layer 1:** Continuous ground plane (RF reference)
* **Inner Layer 2:** Power plane
* **Bottom Layer:** Signal routing + return continuity

---

## Layout Execution (Where Design Either Works or Fails)

### Top Layer – RF Path Integrity & Noise Proximity

![Top Layer](./pcb_top_layer.png)

*Top layer showing RF trace, matching network, MCU, and surrounding digital routing.*

**What this shows:**

* Short RF path from MCU → matching network → antenna
* Matching components placed close to RF output pin
* Dense digital routing near RF region

**Key Observations:**

* RF trace geometry is controlled but exists within a mixed-signal environment
* USB and digital signals are physically close to RF structures

**Critical Decision:**

* No vias in RF signal path → avoids inductive discontinuities

**Reviewer Hook:**

> Is physical separation alone sufficient to prevent digital noise coupling into RF?

---

### Bottom Layer – Return Path & Ground Behavior

![Bottom Layer](./pcb_bottom_layer.png)

*Bottom layer showing ground continuity and return paths beneath critical signals.*

**What this shows:**

* Continuous ground plane beneath RF trace
* Extensive via stitching across the board
* Shared return paths between RF, USB, and digital domains

**Design Insight:**

RF current flows in the **return path directly beneath the signal trace**.

If that path is:

* Shared with high-current digital switching
* Disrupted or fragmented

→ RF performance will degrade.

---

## Design Considerations

### RF Signal Integrity (Primary Constraint)

* Maintain continuous 50Ω impedance
* Minimize reflections and discontinuities
* Keep RF path short and consistent

**Unresolved Question (Intentional):**

> What is the insertion loss and reflection at the antenna connector interface?

---

### Power Integrity (Core Trade-off)

* Single LDO supplies both RF and digital circuits
* Local decoupling used at MCU and RF pins

**Engineering Trade-off:**

* Simpler design
* Increased risk of RF noise coupling through supply

---

### Digital Noise Coupling

* USB introduces high-speed switching activity
* MCU GPIO/SPI generate harmonics across wide frequency range

**Critical Limitation:**

* No dedicated filtering between RF and digital domains

---

### EMI Mitigation

* Ground stitching used to confine fields
* Continuous ground plane maintained

**Limitation:**

* No shielding or RF isolation enclosure

---

## Design Review Notes

* RF path prioritized over routing convenience
* Matching network placement optimized for tuning
* Ground continuity preserved across layers
* Design explicitly considers **noise coupling mechanisms**

---

## Known Risks & Open Questions

This design intentionally exposes real engineering uncertainty:

* Will USB activity degrade RF sensitivity?
* Is impedance truly 50Ω after fabrication?
* Does shared power introduce measurable RF noise?
* How significant is connector-induced loss?

---

## Project Status

* PCB design complete (KiCad 9)
* Pre-fabrication stage
* No RF validation performed

---

## Planned Validation

* **VNA Testing:** Measure (S_{11}), tune matching network
* **Range Testing:** RSSI / SNR vs distance
* **Spectrum Analysis:** Harmonics and spurious emissions
* **Power Analysis:** Ripple and transient response

---

## Summary

This project demonstrates:

* Mixed-signal RF PCB design under real constraints
* Controlled impedance routing (50Ω path)
* Awareness of coupling, noise, and layout-driven RF behavior
* Engineering decisions driven by **failure modes, not convenience**

---

