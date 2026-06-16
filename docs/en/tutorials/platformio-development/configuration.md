# Configure platformio.ini

`platformio.ini` defines how PlatformIO builds and uploads the project.

## Basic Example

```ini
[env:esp32s3]
platform = espressif32
board = esp32-s3-devkitc-1
framework = arduino
monitor_speed = 115200
lib_deps =
    bblanchon/ArduinoJson
```

!!! warning "Use the product project's actual configuration"
    Board IDs, flash size, partitions, USB mode, and build flags are hardware-specific. Do not replace a working product configuration with this generic example.

## Common Fields

| Field | Purpose |
| --- | --- |
| `platform` | Toolchain and board support package |
| `board` | Board definition |
| `framework` | Arduino, ESP-IDF, or another framework |
| `lib_deps` | Versioned dependencies |
| `build_flags` | Preprocessor definitions and compiler options |
| `upload_port` | Explicit upload port |
| `monitor_port` | Explicit serial-monitor port |
| `monitor_speed` | Serial-monitor baud rate |
| `board_build.partitions` | Flash partition table |
| `board_build.filesystem` | Device filesystem type |

Use multiple `[env:...]` sections when one repository targets different boards or feature sets. Pin important platform and library versions so that another developer can reproduce the build.

