# Quick Start

The quickest way to verify a new Lygion TTL bus device is to connect one device, apply the correct power, and run a read-only example.

## Choose a Development Route

| Route | Typical controller | Bus connection | Language | Recommended use |
| --- | --- | --- | --- | --- |
| [Python](python-first-demo.md) | PC, Mac, Raspberry Pi, Jetson, RK, or another Linux SBC | USB -> TTL Adapter (A) -> TTL bus | Python | Fast setup, testing, automation, and high-level robot control |
| [C++ / Arduino](cpp-first-demo.md) | ESP32S3, ESP32, STM32, Arduino, or a custom MCU | Hardware UART -> TTL Adapter (A) or a single-wire TTL circuit | C++ / Arduino | Embedded controllers and real-time robot firmware |

## Before the First Test

- Connect only **one** new bus device. New devices may share the same factory-default ID.
- Start with a `ping` or feedback-reading example. Do not begin with a high-speed motion example.
- Use an external power supply that matches the bus device. USB power is not recommended as the main supply for actuators.
- If communication fails, check the serial port, baud rate, device ID, power, and wire order.

## Need More Help?

The [tutorial library](../tutorials/index.md) explains common tasks such as installing tools, finding a serial port, wiring an MCU UART, assigning device IDs, and troubleshooting communication.
