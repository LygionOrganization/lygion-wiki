# Install PlatformIO

PlatformIO is a VS Code-based embedded development environment suited to maintainable MCU projects. New MCU users may find [Arduino IDE](install-arduino-ide.md) easier for the first test.

## 1. Install VS Code and PlatformIO

1. Install Visual Studio Code.
2. Open the Extensions view.
3. Search for `PlatformIO IDE`.
4. Install the extension and restart VS Code.

## 2. Create or Open a Project

To create a project, open PlatformIO, choose **New Project**, select the board and framework, and create the project.

To open an existing PlatformIO project, choose **File -> Open Folder** and select its root folder.

## 3. Example `platformio.ini`

For an ESP32S3 using the Arduino framework:

```ini
[env:esp32-s3-devkitc-1]
platform = espressif32
board = esp32-s3-devkitc-1
framework = arduino
monitor_speed = 115200
```

Change `board` to match your development board.

## 4. Build, Upload, and Monitor

| Action | Purpose |
| --- | --- |
| Build | Compile the project |
| Upload | Compile and upload firmware |
| Monitor | Open the serial monitor |
| Upload and Monitor | Upload, then open the monitor |

The monitor rate must match the debug serial configuration:

```cpp
Serial.begin(115200);
```

## Next Steps

- [Run the first C++ demo](../quickstart/cpp-first-demo.md)
- [MCU UART wiring](mcu-uart-wiring.md)
- [Use a serial monitor](serial-monitor.md)
