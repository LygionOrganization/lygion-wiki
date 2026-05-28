# TTL Adapter (A)

![TTL Adapter (A)](assets/images/ttla04.png){ .img-rounded width="300" }

> Compact TTL Bus Interface for Robotics and Embedded Motion Control

---

# TTL Bus Device Interface Board

TTL Adapter (A) is a compact USB/UART-to-TTL bus interface board designed for robotics developers, embedded systems, and multi-device motion control applications.

It supports both:

- Lygion TTL bus devices
- Feetech TTL bus servos

The board is optimized for:

- Robotic arms
- Quadruped robots
- Humanoid robots
- Mobile robots
- Embedded controllers
- Multi-axis motion systems

It also supports multi-board cascading and grouped power distribution for larger robot systems.

**Model:** TTL Adapter (A)

---

# 1. Overview

TTL Adapter (A) converts:

- USB
- UART RX/TX

into a single-wire TTL bus interface.

It can be used to communicate with:

- Lygion TTL bus devices
- Feetech STS / HLS / SCS bus servos
- Mixed TTL bus systems

!!! note "Protocol Compatibility"
    TTL Adapter (A) is fully compatible with the official Feetech TTL protocol and supports baud rates up to **3 Mbps** for low-latency control and high-speed feedback.

Because Lygion devices follow the same underlying communication structure, they can operate on the same bus together with Feetech servos.

Example mixed-device systems:

- Bus servos
- Stepper motor drivers
- Absolute encoders
- TTL node modules

---

# 2. Supported Devices

## Lygion TTL Bus Devices

- [TTL Stepper Driver (A)](ttl-stepper-driver-a.md)
- [TTL Encoder E02](ttl-encoder-e02.md)
- [TTL Node (A)](ttl-node-a.md)

Future Lygion TTL bus products will also be supported.

---

## Feetech Devices

- STS Series
- HLS Series
- SCS Series

---

# 3. Important Notes About Device IDs

All devices on the same TTL bus must use unique IDs.

!!! warning "Duplicate IDs Will Cause Communication Errors"
    If two devices share the same ID, the bus may become unstable or devices may fail to respond.

---

# 4. Key Features

## Plug-and-Play USB Communication

A single USB cable is enough for:

- Device scanning
- Parameter configuration
- Firmware upgrades
- Debugging

No external power supply is required for firmware upgrades or basic parameter configuration.

---

## Multiple Communication Interfaces

TTL Adapter (A) supports:

- USB
- UART RX/TX
- Single-wire TTL bus

All interfaces can remain connected simultaneously without manual switching.

---

## High-Speed Bus Communication

Supports baud rates up to:

- 3 Mbps

Benefits:

- Lower communication latency
- Faster status feedback
- Smoother multi-axis robot motion
- Better real-time control performance

---

## Wide Voltage & High Current Support

Supported input voltage:

- 5V ~ 25.2V

Power connector:

- DC5521 (5.5 × 2.1 mm)

Recommended maximum current:

- Approximately 7A

Suitable for:

- High torque servos
- Stepper joints
- Multi-voltage robot systems

---

# 5. Specifications

| Item | Specification |
|---|---|
| Model | TTL Adapter (A) |
| Input Voltage | 5V ~ 25.2V |
| Power Connector | DC5521 (5.5 × 2.1 mm) |
| USB Interface | USB Type-C |
| UART Interface | RX / TX / GND |
| UART Header Pitch | 2.54 mm |
| TTL Bus Interface | GH1.25-3P |
| Maximum Baud Rate | 3 Mbps |
| Board Size | 27 × 35 mm |
| Mounting Hole Diameter | 2.1 mm |
| Mounting Hole Spacing | 13 × 20 mm |

---

# 6. Board Layout

![Board Resources](assets/images/ttla02.png){ width="500" .img-rounded }

---

# 7. Mechanical Dimensions

![Product Dimensions](assets/images/ttla01.png){ width="300" .img-rounded }

---

# 8. Power Supply

## USB Communication

TTL Adapter (A) includes an onboard USB-to-TTL chip, allowing PCs or SBCs such as Raspberry Pi or Jetson boards to communicate with TTL bus devices over USB.

!!! warning "USB Power Is Not Intended For Motion Systems"
    Motors, servos, and other actuators require a properly sized external power supply.

---

# 9. Communication Methods

## USB Control

Recommended for:

- Raspberry Pi
- Jetson
- Windows PCs
- Linux systems

## UART RX/TX Control

Recommended for:

- ESP32
- STM32
- Arduino

TTL Adapter (A) uses **3.3V TTL logic levels**.

---

# 10. Device Feedback

Supported feedback may include:

- Position
- Speed
- Voltage
- Current
- Temperature
- Torque state
- Error status

---

# 11. CH343 Driver Information

TTL Adapter (A) uses the CH343 USB-to-UART chip.

Linux and Raspberry Pi systems usually recognize it automatically.

Typical device names:

```bash
/dev/ttyUSB0
```

or:

```bash
/dev/ttyACM0
```

---

# 12. Feetech FD Software

TTL Adapter (A) supports the Feetech FD debugging software.

- [Download FD Software](../assets/files/FD.7z)

Supported functions:

- Scan device IDs
- Configure parameters
- Upgrade firmware

---

# 13. SDK Support

## Lygion SDK

[Python SDK](https://github.com/LygionOrganization/lygion_devs_py)

[C++ SDK](https://github.com/LygionOrganization/lygion_devs_cpp)

## Feetech SDK

[Feetech SDK on GitHub](https://github.com/ftservo)

---

# 14. 3D Models

![TTL Adapter (A) Step](assets/images/ttla03.png){ .img-rounded width="300" }

[Download STEP Model](assets/files/ttl-adapter-a.step)
