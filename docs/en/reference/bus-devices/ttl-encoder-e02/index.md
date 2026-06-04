# TTL Encoder E02

TTL Encoder E02 is a 12-bit absolute magnetic angle encoder that reports shaft position and speed over the single-wire TTL bus.

![TTL Encoder E02](../../../../reference/bus-devices/ttl-encoder-e02/assets/ttle02-01.png){ .img-rounded width="360" }

## Typical Applications

- Robot-arm and dexterous-hand joint feedback
- Gear, pulley, or gearbox output-angle sensing
- Rotary tables and steering mechanisms
- Leader-follower robot arms
- Low-cost closed-loop mechanisms

## Specifications

| Item | Specification |
| --- | --- |
| Communication | Single-wire TTL bus |
| Default baud rate | 1 Mbps |
| Factory-default ID | 1 |
| ID range | 1-252 |
| Supply voltage | DC 5-28 V |
| Angle feedback | 12-bit absolute angle |
| Single-turn position | 0-4095 |
| Multi-turn position | 0-65534; turn count is not retained after power loss |
| Connector | HC-1.25-3P |

## Documentation

- [Hardware installation](hardware-installation.md)
- [Read with Python](python-quickstart.md)
- [Read with C++ / Arduino](cpp-arduino.md)
- [Calibration and multi-turn data](calibration-and-multiturn.md)
- [FAQ](faq.md)

Start with the [Python](../../../quickstart/python-first-demo.md) or [C++ / Arduino](../../../quickstart/cpp-first-demo.md) first demo.
