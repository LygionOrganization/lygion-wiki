# Robot Driver with ESP32S3 Lite

Robot Driver with ESP32S3 Lite is an ESP32-S3 robot controller that can run robot logic independently or serve as a real-time sub-controller for a Raspberry Pi, Jetson, PC, or other host.

![Robot Driver with ESP32S3 Lite](assets/product.jpg){ .img-rounded width="500" }

## What It Can Do

- Control STS, SMS, HLS, and SCS serial-bus servos.
- Connect TTL, RS485, and CAN actuators.
- Save commands as mission files and bind them to local controls or boot.
- Accept JSON through USB CDC, HTTP, WebSocket, or GPIO UART.
- Communicate with other ESP32 devices through ESP-NOW.
- Read an S.BUS receiver with compatible firmware.
- Run the open-source Arduino firmware built with PlatformIO.

## Core Specifications

| Item | Specification |
| --- | --- |
| Module | ESP32-S3-WROOM-1 R8N8 |
| Input | DC 6-20 V; must match connected actuators |
| Actuator interfaces | Single-wire TTL, RS485, CAN |
| Host interfaces | USB CDC, GPIO UART, USB UART, HTTP, WebSocket |
| Wireless | Wi-Fi AP + STA, ESP-NOW |
| Local UI | 0.91-inch OLED, five-way switch, passive buzzer |
| Data format | JSON |
| Framework | Arduino; VS Code + PlatformIO recommended |

## Start Here

1. Follow the [Quick Start](quickstart.md).
2. Learn the [Web Console](web-console.md).
3. Connect [Servos and Bus Devices](servo-control.md).
4. Select a [Host Communication](host-communication.md) method.
5. Read [Advanced Firmware Development](advanced-development.md) before modifying firmware.

## Documentation

- [Quick Start](quickstart.md)
- [Web Console](web-console.md)
- [Servos and Bus Devices](servo-control.md)
- [Action Scripting](action-scripting.md)
- [JSON Command Interface](json-command-interaction.md)
- [Host Communication](host-communication.md)
- [Board Resources and Wiring](board-resources.md)
- [UART Passthrough and S.BUS](uart-sbus.md)
- [Firmware Flashing and Reset](firmware-flash-and-reset.md)
- [Advanced Firmware Development](advanced-development.md)
- [Troubleshooting](faq.md)

## Open-Source Firmware

[Robot Driver with ESP32S3 Lite firmware and examples](https://github.com/EffectsMachine/robot_driver_with_esp32s3_lite)

!!! warning "Match the supply to every actuator"
    The DC5521 and XT30 power rails feed the actuator interfaces. Verify the voltage rating of every servo, joint, and hub motor before applying power.
