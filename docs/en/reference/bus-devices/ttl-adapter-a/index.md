# TTL Adapter (A)

TTL Adapter (A) connects a computer USB port or an MCU UART to the single-wire TTL bus used by Lygion devices and compatible Feetech TTL bus servos.

![TTL Adapter (A)](../../../../reference/bus-devices/ttl-adapter-a/assets/ttla04.png){ .img-rounded width="360" }

## Typical Uses

- Connect a PC, Mac, Raspberry Pi, Jetson, or Linux SBC to TTL bus devices.
- Read feedback and send commands with the Lygion Python SDK.
- Scan and configure devices from Windows with FD.
- Connect an MCU hardware UART to the single-wire TTL bus.
- Provide a communication and power entry point for a small device group.

## Specifications

| Item | Specification |
| --- | --- |
| Communication interfaces | USB, UART RX/TX, single-wire TTL bus |
| USB connector | USB Type-C |
| External supply input | DC 5-25.2 V |
| Maximum baud rate | 3 Mbps |
| Compatible devices | Lygion TTL devices and compatible Feetech STS / HLS / SCS TTL bus servos |
| Board size | 27 x 35 mm |

## Documentation

- [Hardware overview](hardware-overview.md)
- [Power and wiring](power-and-wiring.md)
- [Drivers and serial ports](drivers-and-ports.md)
- [SDKs and tools](sdk-and-tools.md)

## First Test

Start with the [Python first demo](../../../quickstart/python-first-demo.md) or [C++ / Arduino first demo](../../../quickstart/cpp-first-demo.md).

!!! warning "USB power is limited"
    USB is suitable for communication and low-power configuration. Do not use it as the main operating supply for servos, stepper drivers, or other actuators.
