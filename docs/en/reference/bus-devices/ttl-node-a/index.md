# TTL Node (A)

TTL Node (A) is a multifunction TTL-bus node that combines S.BUS input, status indicators, adjustable PWM power outputs, USB communication, and several TTL-bus connectors. It is intended for robots, remote-control systems, unmanned vehicles, and automation projects.

![TTL Node (A), front and back](../../../../reference/bus-devices/ttl-node-a/assets/ttl-node-a-front-back.png){ .img-rounded }

## Main Features

- S.BUS receiver input
- Two groups of 3 x 8-bit RGB status LEDs
- Two PWM-controlled power outputs
- USB Type-C communication
- HX-5264-3P, PH2.0-3P, and GH1.25-3P TTL-bus connectors
- Configurable device ID for multi-device buses

## Factory Settings

| Item | Default |
| --- | --- |
| Device ID | `0` |
| Baud rate | `1,000,000 bps` |
| Response level | `1`, reply to every command |

## Specifications

| Item | Specification |
| --- | --- |
| Size | 30 x 35 mm |
| Input voltage | DC 9-12.6 V, suitable for a 3S lithium battery |
| Receiver supply | 5 V, up to 500 mA |
| PWM outputs | Two PH2.0-2P outputs, up to 3 A each |
| USB | USB Type-C |

!!! warning "GH1.25-3P does not provide device power"
    This connector carries TTL data and ground only. Use it with independently powered devices such as a servo hub.

!!! warning "Configure IDs before connecting devices in parallel"
    Every device on one TTL bus must have a unique ID and use the same baud rate.

## Documentation

- [Quick Start](quickstart.md)
- [Hardware Overview](hardware-overview.md)
- [Power and Wiring](power-and-wiring.md)
- [Drivers and Serial Ports](drivers-and-ports.md)
- [Configure with FD](fd-configuration.md)
- [Arduino Development](arduino-development.md)
- [SDKs and Tools](sdk-and-tools.md)

