# IX-ThermaForge Bill of Materials (BOM)

Author: Bryce Wooster  
Date: 2025-07-15

---

## Overview

This BOM lists all core components and materials required to build the IX-ThermaForge triangular harmonic energy beam system as designed.

All parts specified are commercially available or standard industrial-grade components. No proprietary or controlled military hardware is included.

---

## Core Components

| Item # | Component                         | Specification / Details                                      | Quantity | Approx. Cost (USD) | Notes                          |
|--------|---------------------------------|-------------------------------------------------------------|----------|--------------------|--------------------------------|
| 1      | High-Power Laser Diode Module   | 850nm - 940nm wavelength, 6-inch x 3-inch aperture size     | 3        | $1,500 each        | Custom or OEM module           |
| 2      | Triangular Beam Shaping Optics  | High-precision fused silica prisms and slits                | 3 sets   | $750 per set       | Includes phase control slits   |
| 3      | Magnetic Coil Assemblies         | Copper wire coil, 18 AWG, custom wound for harmonic control | 3        | $300 each          | Includes bobbin and connectors |
| 4      | Thermal Management Heat Sink    | Copper/aluminum hybrid, active liquid cooling compatible     | 3        | $200 each          | Must sustain up to 100W heat   |
| 5      | Liquid Cooling Pump & Reservoir | Closed-loop system compatible with heat sinks               | 1        | $400               | High flow, vibration dampened  |
| 6      | Microcontroller Unit (MCU)       | ARM Cortex-M7 or better, real-time control capable           | 1        | $50                | For harmonic control sequencing|
| 7      | FPGA Module                     | Xilinx or Intel equivalent, for real-time phase modulation   | 1        | $250               | Optional but recommended       |
| 8      | Power Supply Unit (PSU)         | 24V DC, 600W output, stable, low ripple                      | 1        | $150               | Overcurrent and thermal protection |
| 9      | Spintronic Field Emitter Units  | Commercial spintronic devices or lab-grade waveguides        | 3        | $1,000 each        | Specialized, research grade    |
| 10     | Structural Housing              | Aluminum alloy 6061, machined for beam alignment             | Custom   | $500 approx        | Includes mounts and shielding  |
| 11     | Wiring and Connectors           | High-current rated, shielded cables                          | Various  | $100 approx        | Includes EMI shielding         |
| 12     | Sensors (Temp, Magnetic, Phase)| High-precision sensors for feedback loops                    | Various  | $150 approx        | Critical for real-time control |

---

## Additional Materials

| Item # | Material                         | Specification                                              | Quantity   | Approx. Cost (USD) | Notes                      |
|--------|---------------------------------|------------------------------------------------------------|------------|--------------------|----------------------------|
| 13     | Optical-grade Fused Silica       | For lenses and beam shaping elements                        | Various    | $300 approx        | High purity recommended     |
| 14     | Insulation Materials             | Thermal and electromagnetic shielding                       | Various    | $200 approx        | Use non-conductive, heat-resistant |
| 15     | Cooling Fluid                   | Deionized water with corrosion inhibitors                   | 5 liters   | $50                | Maintain fluid quality      |

---

## Notes and Recommendations

- All components must be sourced from reputable industrial or scientific suppliers.  
- Spintronic units may require custom orders or research collaborations.  
- Assembly requires precision machining and optical alignment facilities.  
- Safety protocols must be strictly followed for high-power laser operation.  
- Costs are approximate and will vary by supplier and quantity.  

---

For detailed assembly instructions, see [BUILD_GUIDE.md](./BUILD_GUIDE.md).

