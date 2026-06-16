# LinkArm-LT

LinkArm-LT is a lightweight robotic arm with a built-in ESP32-S3 web application, mission scripting, synchronized teaching, and USB or wireless host interfaces.

![LinkArm-LT](../../../../reference/robots/linkarm-lt/assets/A.png){ .img-rounded }

## Main Capabilities

- browser control from a phone, tablet, or computer
- FPV and Cartesian end-effector control
- ESP-NOW one-to-one or one-to-many synchronized teaching
- saved, looping, and boot-time mission scripts
- USB CDC, HTTP, and WebSocket host control
- JSON control of the arm, servos, OLED, buzzer, Wi-Fi, and files

| Item | Value |
| --- | --- |
| Working voltage | DC 9-12.6 V |
| Recommended supply | 12 V, 3 A |
| Default access point | `Robot` |
| Default password | `12345678` |
| AP address | `http://192.168.4.1` |
| HTTP endpoint | Port `80`, `/api/cmd` |
| WebSocket | `ws://<device-ip>:80/ws` |

!!! danger "Secure the arm before use"
    Clamp it to a desk or bolt it to a stable base. Keep fragile objects, children, and faces outside the workspace.

## Documentation

- [Quick Start](quickstart.md)
- [Web Control](web-control.md)
- [ESP-NOW Synchronized Teaching](sync-teaching.md)
- [Action Scripting](action-scripting.md)
- [JSON Command Reference](json-commands.md)
- [Host Communication](host-communication.md)
- [Firmware Recovery and Midpoint Calibration](firmware-and-calibration.md)
- [Integration and Dimensions](integration.md)
- [Troubleshooting](faq.md)

