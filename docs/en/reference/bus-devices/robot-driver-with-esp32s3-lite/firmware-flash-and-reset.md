# Firmware Flashing and Reset

Download the [complete Windows tool package](../../../assets/files/robocore-s3/download-tool.zip), extract it, and open `Start_Download_Tool.bat`. It contains matching images and preset addresses for RoboCore S3 and Robot Driver with ESP32S3 Lite. Choose the actual COM port manually; no automatic flashing is enabled. The package includes bilingual instructions, `manifest.json` and a read-only `Verify_Package.ps1` checksum check. After flashing, reset the board and check the console before reconnecting actuators.

Use the official repository for prebuilt firmware, the Windows download tool, and the PlatformIO source project:

[Robot Driver with ESP32S3 Lite firmware repository](https://github.com/LygionOrganization/robocore_s3)

## Before Flashing

- Disconnect or disable actuator power.
- Save any mission scripts and Wi-Fi settings you need.
- Use a reliable USB data cable.
- Confirm that the selected serial port belongs to this board.

## Flash the Prebuilt Firmware on Windows

The official repository contains:

```text
download_tool/RoboCore_S3_Download_Tool/
```

This folder includes Espressif Flash Download Tool 3.9.9 and matching bootloader, partition, and firmware binaries.

The provided configuration uses:

| Image | Flash offset |
| --- | --- |
| `bootloader.bin` | `0x0` |
| `partitions.bin` | `0x8000` |
| `firmware.bin` | `0x10000` |

Use the included configuration rather than changing offsets manually. Select the board's COM port, flash the images, then reset or power-cycle the board.

## Build and Upload from Source

The source project uses PlatformIO with the `esp32-s3-devkitc-1-n8r8` environment and an 8 MB flash configuration.

```bash
pio run
pio run --target upload
pio device monitor --baud 921600
```

See [Advanced firmware development](advanced-development.md) before changing board assignments or feature flags.

## Reset Commands

| Operation | JSON command | Effect |
| --- | --- | --- |
| Reboot | `{"T":600}` | Restarts the ESP32-S3 |
| Clear NVS | `{"T":601}` | Removes saved nonvolatile configuration |
| Reset LittleFS | `{"T":602}` | Erases saved missions and LittleFS data |

!!! danger "Reset commands erase saved data"
    Do not run `T:601` or `T:602` unless you understand what will be removed.
