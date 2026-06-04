# Install Arduino IDE

Arduino IDE is the most approachable tool for the MCU C++ route. It opens `.ino` examples, installs board packages, builds sketches, and uploads firmware.

## Supported Development Boards

Arduino IDE is a good starting point for:

- ESP32S3 and ESP32
- Arduino Mega2560 and Arduino Due
- STM32 boards supported by an Arduino core

## 1. Install Arduino IDE

Download and install Arduino IDE 2.x from the official Arduino website.

## 2. Install Board Support

### ESP32 / ESP32S3

1. Open **File -> Preferences**.
2. Add the Espressif board-manager URL under **Additional boards manager URLs**.
3. Open **Tools -> Board -> Boards Manager**.
4. Search for `esp32`.
5. Install the ESP32 package published by Espressif Systems.

The board-manager URL can change. If installation fails, use the current Arduino-ESP32 instructions from Espressif.

### Arduino Mega2560

Mega2560 support is included with Arduino IDE.

### STM32

Install the Arduino core recommended by your board manufacturer. STM32 board definitions and upload procedures vary by model.

## 3. Install the Lygion C++ SDK

- [C++ SDK on GitHub](https://github.com/LygionOrganization/lygion_devs_cpp)
- [Download the C++ / Arduino SDK](../../assets/files/lygion_devs_cpp.zip)

Copy the library into the Arduino libraries directory, then restart Arduino IDE:

=== "Windows"

    ```text
    Documents\Arduino\libraries
    ```

=== "macOS"

    ```text
    ~/Documents/Arduino/libraries
    ```

=== "Linux"

    ```text
    ~/Arduino/libraries
    ```

## 4. Open a Read-Only Example

Example paths include:

```text
example/lyttlsd/FeedBack.ino
example/lyttlsd/SyncRead.ino
example/lyttlsd/CalibrationOfs.ino
```

Start with `FeedBack.ino` to verify communication without commanding high-speed motion.

## 5. Select the Board and Port

Choose your board under **Tools -> Board**, then choose the MCU board's USB port under **Tools -> Port**.

!!! tip "This is the MCU upload port"
    The selected port uploads firmware and displays debug output. It is not the TTL bus device port.

## Next Steps

- [Run the first C++ demo](../quickstart/cpp-first-demo.md)
- [Upload an Arduino example](upload-arduino-sketch.md)
- [Use a serial monitor](serial-monitor.md)
