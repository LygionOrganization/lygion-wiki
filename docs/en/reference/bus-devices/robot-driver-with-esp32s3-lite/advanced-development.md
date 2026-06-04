# Advanced Firmware Development

The official firmware is an Arduino-framework PlatformIO project for ESP32-S3-N8R8:

[Open the firmware repository](https://github.com/LygionOrganization/robot_driver_with_esp32s3_lite)

## Project Structure

| Path | Responsibility |
| --- | --- |
| `src/main.cpp` | Startup, JSON dispatch, HTTP, WebSocket, USB CDC, missions, and main loop |
| `src/Config.h` | Device profile, feature flags, pin assignments, and JSON command IDs |
| `src/jointsCtrl.*` | Bus-servo, joint, arm, and hub-motor control |
| `src/Wireless.*` | Wi-Fi, AP/STA, and ESP-NOW |
| `src/FilesCtrl.*` | LittleFS mission storage |
| `src/Can.h` | CAN transmission and reception |
| `src/Web_page.h` | Embedded Web App |
| `python_example/` | USB CDC, HTTP, WebSocket, and UART host examples |

## Build Configuration

The PlatformIO environment targets `esp32-s3-devkitc-1-n8r8`, uses Arduino, enables USB CDC on boot, and builds with C++17.

```bash
pio run
pio run --target upload
pio device monitor --baud 921600
```

## Feature Selection

`src/Config.h` selects one device profile:

```cpp
#define DEV_TYPE_RD_LITE
// #define DEV_TYPE_LINKARM_LT
// #define DEV_TYPE_SBUS_UGV_A
```

It also controls optional features such as hub motors, ESP-NOW, the file system, UI controls, and S.BUS.

## Add a JSON Command

1. Assign a unique command ID in `Config.h`.
2. Document the expected JSON fields beside the definition.
3. Add a matching case to `jsonCmdReceiveHandler()` in `main.cpp`.
4. Validate ranges and IDs before operating hardware.
5. Add a host-side example and test through at least one communication transport.

All transports feed the same command queue, so a well-designed command can be used through the Web App, USB CDC, HTTP, WebSocket, UART, or ESP-NOW.

## Timing and Safety

- Commands are queued; the default queue length is finite.
- USB CDC commands require a newline.
- Long blocking operations reduce responsiveness.
- Motion commands must validate IDs, ranges, and safe states.
- Define behavior for communication loss before deploying an autonomous robot.

!!! warning "Pin assignments are board-specific"
    Review the physical schematic and connector labels before changing GPIO definitions. A wrong assignment can short a signal or drive an attached peripheral incorrectly.
