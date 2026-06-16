# TTL Bus Servos

This section covers the Feetech TTL serial bus servos commonly used in Lygion projects. They connect to the same single-wire TTL bus as other Lygion bus devices, and can be brought online through [TTL Adapter (A)](../ttl-adapter-a/index.md), [Robot Driver with ESP32S3 Lite](../robot-driver-with-esp32s3-lite/index.md), [TTL Node (A)](../ttl-node-a/index.md), or an MCU UART configured for single-wire TTL communication.

## Product Lineup

| Model | Output structure | Recommended supply | Stall torque | No-load speed | Guide |
| --- | --- | --- | --- | --- | --- |
| SC-0090-C043 | Single shaft, compact metal gears | 8-12.6V | 5.5kg.cm | 0.12sec/60deg | [Open guide](sc-0090-c043.md) |
| SC-0090-C049 | Dual shaft, compact metal gears | 8-12.6V | 5.5kg.cm | 0.12sec/60deg | [Open guide](sc-0090-c049.md) |
| SC-1500-C023 | Dual shaft, 15kg.cm class, brass gears | 9-12.6V | 15.6kg.cm | 0.167sec/60deg | [Open guide](sc-1500-c023.md) |
| SC-1500-C024 | Single shaft, 15kg.cm class, brass gears | 9-12.6V | 15.6kg.cm | 0.167sec/60deg | [Open guide](sc-1500-c024.md) |

## Images and CAD

| Model | Image | 3D model |
| --- | --- | --- |
| SC-0090-C043 | ![SC-0090-C043](../../../reference/bus-devices/bus-servos/assets/SC-0090-C043.webp){ width="180" } | [Servo STEP](../../../reference/bus-devices/bus-servos/assets/SC-0090-C043.step) · [Round horn](../../../reference/bus-devices/bus-servos/assets/arms-0090/cycle.stp) · [Cross horn](../../../reference/bus-devices/bus-servos/assets/arms-0090/tenarm.stp) |
| SC-0090-C049 | ![SC-0090-C049](../../../reference/bus-devices/bus-servos/assets/SC-0090-C049.webp){ width="180" } | [Servo STEP](../../../reference/bus-devices/bus-servos/assets/SC-0090-C049.step) · [Round horn](../../../reference/bus-devices/bus-servos/assets/arms-0090/cycle.stp) · [Cross horn](../../../reference/bus-devices/bus-servos/assets/arms-0090/tenarm.stp) |
| SC-1500-C023 | ![SC-1500-C023](../../../reference/bus-devices/bus-servos/assets/SC-1500-C023.webp){ width="180" } | [Servo STEP](../../../reference/bus-devices/bus-servos/assets/SC-1500-C023.step) |
| SC-1500-C024 | ![SC-1500-C024](../../../reference/bus-devices/bus-servos/assets/SC-1500-C024.webp){ width="180" } | [Servo STP](../../../reference/bus-devices/bus-servos/assets/SC-1500-C024.stp) |

The 0090 series horn models include round, half-arm, single-arm, and cross horn options. See each model page for the full list.

## Basic Workflow

1. Connect the servo through TTL Adapter (A), Robot Driver, or a compatible MCU UART.
2. Power the servo from a suitable external supply, and make sure the controller and servo share ground.
3. When configuring a new servo, keep only one unconfigured servo on the bus.
4. Use the FD utility to find the servo and confirm its default ID and baud rate.
5. Assign a unique ID before connecting multiple servos to the same bus.
6. Use the Feetech SDK to send position, speed, and parameter commands.

## Recommended Reading

- [Power and Wiring](../../../tutorials/power-and-wiring-basics.md)
- [Power Grouping and Isolation](../../../tutorials/power-grouping-and-decoupling.md)
- [Device IDs and Baud Rates](../../../tutorials/device-id-and-baudrate.md)
- [FD Device Utility](../../../tutorials/fd-tool.md)
- [Find the Serial Port](../../../tutorials/find-serial-port.md)
- [Communication Troubleshooting](../../../tutorials/communication-troubleshooting.md)

## Default Communication Settings

| Item | Default / range |
| --- | --- |
| Bus | Single-wire TTL half-duplex serial |
| Frame format | 8 data bits, 1 stop bit, no parity |
| ID range | `0-253` |
| Factory ID | `1` |
| Baud-rate range | `38400 bps - 500000 bps` |
| Factory baud rate | `500000 bps` |
| Center position | `511` |
| Maximum position update rate | `1 ms` |
| Logic high | `2-5V` |
| Logic low | `0-0.45V` |

## Tools

- [FD Device Utility](../../../tutorials/fd-tool.md): discover servos, change IDs and baud rates, read feedback, and adjust parameters.
- [Feetech SDK](https://gitee.com/ftservo): control compatible bus servos from Python, C/C++, Arduino, and other host software.
- [TTL Adapter (A)](../ttl-adapter-a/index.md): recommended adapter for PC or SBC debugging.
- [Robot Driver with ESP32S3 Lite](../robot-driver-with-esp32s3-lite/index.md): suitable for robot projects that need servo control, actions, and onboard peripherals.

!!! warning "Assign IDs before wiring multiple servos together"
    Multiple servos with the same ID will cause discovery, control, and feedback problems. Keep only one unconfigured servo on the bus while changing IDs.

!!! danger "Check every device before applying bus power"
    The bus power rail is shared by all connected devices. Before using a 3S lithium battery pack, confirm that every device on the bus supports that voltage.

!!! tip "Start with low speed and small moves"
    For the first motion test, use low speed, small travel, and light load. Increase speed and load only after ID, direction, mechanical limits, and power stability are confirmed.
