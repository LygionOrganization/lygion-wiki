# TTL Bus Devices

Lygion TTL bus products share a single-wire half-duplex TTL bus. A controller can address multiple adapters, sensors, drivers, servos, hubs, and modules as long as their device IDs are unique, their baud rates match, and their supply voltages are compatible.

## Product Entry Points

| Category | Product | Best for | Guide |
| --- | --- | --- | --- |
| Bus adapter | TTL Adapter (A) | Connecting a PC, Raspberry Pi, Jetson, or MCU UART to a single-wire TTL bus | [Open guide](ttl-adapter-a/index.md) |
| Angle feedback | TTL Encoder E02 | Reading 12-bit absolute angle from joints, shafts, and mechanisms | [Open guide](ttl-encoder-e02/index.md) |
| Motor driver | TTL Stepper Driver (A) | Position, speed, and parameter control for stepper motors over TTL bus | [Open guide](ttl-stepper-driver-a/index.md) |
| Multifunction node | TTL Node (A) | S.BUS, RGB, PWM, ADC, USB, and TTL-bus bridging | [Open guide](ttl-node-a/index.md) |
| Actuator | TTL Bus Servos | Feetech TTL serial bus servos for joints, grippers, and pan-tilt mechanisms | [Open guide](bus-servos/index.md) |
| Controller | Robot Driver with ESP32S3 Lite | Robot action scripts, Web console, servo control, and onboard peripherals | [Open guide](robot-driver-with-esp32s3-lite/index.md) |
| Wiring expansion | Bus hubs | Expanding TTL bus wiring and power distribution | [TTL-5264](hub-boards/ttl-5264-8p-hub-a.md) · [HC-1.25](hub-boards/hc-1.25-8p-hub-a.md) |

## Recommended Path

1. [Quick Start](../../quickstart/index.md): complete one basic communication test.
2. [Power and Wiring](../../tutorials/power-and-wiring-basics.md): check external power, common ground, and current margin.
3. [Device IDs and Baud Rates](../../tutorials/device-id-and-baudrate.md): understand ID management on a shared bus.
4. [FD Device Utility](../../tutorials/fd-tool.md): discover devices, read feedback, and change IDs or baud rates.
5. [Communication Troubleshooting](../../tutorials/communication-troubleshooting.md): diagnose missing devices, abnormal feedback, or no response.

[Choose a quick-start route](../../quickstart/index.md){ .md-button }
[Open downloads](../../downloads/index.md){ .md-button }

!!! warning "Configure one new device at a time"
    New devices may share the same factory ID. When changing an ID or bringing up a new device, keep only one unconfigured device on the bus.

!!! danger "Bus power is shared"
    The Vcc rail is shared by all connected devices. Before applying battery power or a high-current supply, confirm that every device on the bus supports that voltage.
