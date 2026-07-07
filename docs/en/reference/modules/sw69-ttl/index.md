# SW69-TTL Steering Wheel Module

SW69-TTL is a compact TTL-bus steering wheel module for mobile robot bases. It combines a steering joint, a drive wheel, stepper drivers, and an absolute encoder into a single wheel unit, making it suitable for omnidirectional bases, teaching platforms, and experimental mobile robots.

[Quick Start](quickstart.md){ .md-button .md-button--primary }
[Python Example](python-development.md){ .md-button }
[ESP32 Arduino Example](cpp-arduino.md){ .md-button }

![SW69-TTL package](../../../../reference/modules/sw69-ttl/assets/package.webp){ .img-rounded }

## What Is Inside

| Subsystem | Purpose | Related products |
| --- | --- | --- |
| Steering joint | Rotates the wheel direction and reads the real steering angle | [DM42-G7220-E02](../dm42-g7220-e02/index.md), [TTL Encoder E02](../../bus-devices/ttl-encoder-e02/index.md), [TTL Stepper Driver (A)](../../bus-devices/ttl-stepper-driver-a/index.md) |
| Drive wheel | Spins continuously to move the robot base | [DW69](../dw69/index.md), [TTL Stepper Driver (A)](../../bus-devices/ttl-stepper-driver-a/index.md) |

The stepper motors themselves do not store IDs or control parameters. Device ID, operating mode, current, speed, and protection settings are stored in the corresponding TTL Stepper Driver (A).

## Key Features

- TTL bus communication for multi-wheel robot bases.
- Output-side E02 encoder for absolute steering angle feedback.
- Speed-mode drive wheel control with heartbeat protection.
- Same driver type for steering and driving, which simplifies wiring and maintenance.
- Python and ESP32 Arduino examples for startup synchronization, steering angle control, and wheel speed control.

## Recommended Bring-Up Flow

1. Prepare TTL Adapter (A), TTL-5264 8P Hub (A), external power, and cables.
2. Configure the steering motor driver ID and test steering motion.
3. Configure the E02 encoder ID and calibrate the steering center.
4. Configure the drive motor driver ID, speed mode, and heartbeat protection.
5. Connect all three devices on the same TTL bus and run an integrated test.
6. Assign unique IDs before adding multiple SW69-TTL modules to one bus.
7. Run the Python or ESP32 Arduino example.

For detailed steps, start with [Quick Start and FD Setup](quickstart.md).

## Suggested ID Plan

| Wheel | Encoder ID | Steering driver ID | Drive driver ID |
| --- | ---: | ---: | ---: |
| 1 | 10 | 11 | 12 |
| 2 | 13 | 14 | 15 |
| 3 | 16 | 17 | 18 |

!!! warning "Do not duplicate IDs"
    New devices often ship with the same default ID. During setup, connect and configure one unconfigured device at a time.

## Power

SW69-TTL requires external DC power for the motors and drivers. A 5S or 6S lithium battery pack is recommended, or another DC supply within the supported driver voltage range.

For a three-wheel base, choose the power supply based on motor current, load, and motion profile. Start with conservative current settings during bench testing.

!!! warning "USB is not motor power"
    USB is for communication only. Always check voltage, polarity, cable order, and power capacity before enabling the motors.

## Documentation

| Page | What it covers |
| --- | --- |
| [Quick Start and FD Setup](quickstart.md) | Wiring, ID assignment, encoder center calibration, speed mode setup, and first test |
| [Python Development](python-development.md) | Python SDK setup, startup sync, angle control, and wheel speed control |
| [ESP32 Arduino Development](cpp-arduino.md) | ESP32 wiring, Arduino SDK calls, angle conversion, and complete example flow |

## Downloads

| Resource | File |
| --- | --- |
| STEP model | [SW69-TTL_STEP.step](../../../../reference/modules/sw69-ttl/assets/SW69-TTL_STEP.step) |
| Mechanical drawing PDF | [SW69-TTL.pdf](../../../../reference/modules/sw69-ttl/assets/SW69-TTL.pdf) |
| DXF drawing | [SW69-TTL.dxf](../../../../reference/modules/sw69-ttl/assets/SW69-TTL.dxf) |
| Python example | [sw69_example.py](../../../../reference/modules/sw69-ttl/assets/sw69_example.py) |
| ESP32 Arduino example | [sw69_esp32_example.ino](../../../../reference/modules/sw69-ttl/assets/sw69_esp32_example.ino) |

## Related Pages

- [TTL Adapter (A)](../../bus-devices/ttl-adapter-a/index.md)
- [TTL-5264 8P Hub (A)](../../bus-devices/hub-boards/ttl-5264-8p-hub-a.md)
- [TTL Stepper Driver (A)](../../bus-devices/ttl-stepper-driver-a/index.md)
- [TTL Encoder E02](../../bus-devices/ttl-encoder-e02/index.md)
- [FD Device Utility](../../../tutorials/fd-tool.md)
