# Product Reference

Use this section after completing a [first communication test](../quickstart/index.md). Each product guide collects the hardware specifications, wiring, software examples, operating notes, and troubleshooting information needed to integrate that product.

## TTL Bus Products

| Product | Purpose | Documentation |
| --- | --- | --- |
| TTL Adapter (A) | Converts USB or an MCU UART into a single-wire TTL bus interface | [Open guide](bus-devices/ttl-adapter-a/index.md) |
| TTL Encoder E02 | 12-bit absolute magnetic angle encoder with TTL bus feedback | [Open guide](bus-devices/ttl-encoder-e02/index.md) |
| TTL Stepper Driver (A) | TTL bus driver for bipolar stepper motors | [Open guide](bus-devices/ttl-stepper-driver-a/index.md) |
| TTL Node (A) | S.BUS, RGB, PWM, USB, and TTL-bus multifunction node | [Open guide](bus-devices/ttl-node-a/index.md) |
| TTL Bus Servos | Feetech TTL serial bus servos for joints, grippers, and pan-tilt mechanisms | [Open guide](bus-devices/bus-servos/index.md) |
| Robot Driver with ESP32S3 Lite | ESP32S3-based robot controller with multiple robot interfaces | [Open guide](bus-devices/robot-driver-with-esp32s3-lite/index.md) |

## Bus Hubs

- [TTL-5264 8P Hub (A)](bus-devices/hub-boards/ttl-5264-8p-hub-a.md)
- [HC-1.25 8P Hub (A)](bus-devices/hub-boards/hc-1.25-8p-hub-a.md)

## Robots

- [LinkArm-M](robots/linkarm-m/index.md)
- [LinkArm-LT](robots/linkarm-lt/index.md)

## Robot Modules

- [SW69-TTL Steering Wheel Module](modules/sw69-ttl/index.md)
- [4240BY-G5.2 Stepper Motor](modules/4240by-g5-2/index.md)
- [3M 72T Timing Pulley](modules/pulley-3m-72t/index.md)
- [DW69 Drive Wheel](modules/dw69/index.md)
- [DM42-G7220-E02 Joint Actuator](modules/dm42-g7220-e02/index.md)

## Open Lygion

- [Python SDK](open-lygion/python-sdk.md)
- [C++ SDK](open-lygion/cpp-sdk.md)
- [3D3S Omnidirectional Chassis](open-lygion/3d3s-chassis.md)
- [6x6 Rover](open-lygion/6x6-rover.md)
- [5+1 DOF Robotic Arm](open-lygion/5-plus-1-dof-robotic-arm.md)
- [Open Leader Arm](open-lygion/open-leader-arm.md)
- [Self-locking Gripper](open-lygion/self-locking-gripper.md)

## Before Integrating a Product

- Start with one device and a read-only example.
- Confirm that the power supply matches every device in the powered group.
- Assign a unique ID to every device on the shared bus.
- Use the [tutorial library](../tutorials/index.md) for common setup and troubleshooting tasks.
