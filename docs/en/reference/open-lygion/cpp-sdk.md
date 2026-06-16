# C++ SDK

The Lygion C++ / Arduino SDK is for ESP32S3, ESP32, Arduino Mega2560, STM32 Arduino Core, RP2040 / Raspberry Pi Pico, PlatformIO, and similar embedded development environments.

- [Lygion C++ SDK on GitHub](https://github.com/LygionOrganization/lygion_devs_cpp)
- [Download the C++ / Arduino SDK](../../assets/files/lygion_devs_cpp.zip)

## Get the SDK

```bash
git clone https://github.com/LygionOrganization/lygion_devs_cpp.git
cd lygion_devs_cpp
```

If GitHub is not available, use the ZIP package from this Wiki.

[Download C++ / Arduino SDK](../../assets/files/lygion_devs_cpp.zip){ .md-button }

## Arduino IDE

Place the SDK library files in the Arduino `libraries` folder, then restart Arduino IDE.

| System | Common library folder |
| --- | --- |
| Windows | `Documents\Arduino\libraries` |
| macOS | `~/Documents/Arduino/libraries` |
| Linux | `~/Arduino/libraries` |

Helpful tutorials:

- [Install Arduino IDE](../../tutorials/install-arduino-ide.md)
- [Upload an Arduino Example](../../tutorials/upload-arduino-sketch.md)
- [Use a Serial Monitor](../../tutorials/serial-monitor.md)

## PlatformIO

PlatformIO users can place the SDK in the project `lib` folder:

```text
your_project/
|- platformio.ini
|- src/
|  `- main.cpp
`- lib/
   `- lygion_devs_cpp/
```

You can also open an existing SDK example or PlatformIO project directly in VS Code.

[PlatformIO Development Guide](../../tutorials/platformio-development/index.md){ .md-button }

## Example Areas

| Device / task | Example area |
| --- | --- |
| TTL Node (A) | [`example/lyttln`](https://github.com/LygionOrganization/lygion_devs_cpp/tree/main/example/lyttln) |
| TTL Stepper Driver (A) | [`example/lyttlsd`](https://github.com/LygionOrganization/lygion_devs_cpp/tree/main/example/lyttlsd) |
| Device parameter setup | `ProgramEprom` / `*_eprom` examples |
| Feedback readout | `FeedBack` / `Read` examples |
| Position or speed control | `WritePos` / `WriteSpe` examples |

## Serial Initialization

Hardware serial syntax varies by board. Update RX and TX pins in the examples to match your wiring.

=== "ESP32S3 / ESP32"

    ```cpp
    Serial.begin(115200);
    Serial1.begin(1000000, SERIAL_8N1, 18, 17);

    ttlsd.pSerial = &Serial1;
    ```

=== "Arduino Mega2560"

    ```cpp
    Serial.begin(115200);
    Serial1.begin(1000000);

    ttlsd.pSerial = &Serial1;
    ```

!!! warning "Do not start with high-speed motion examples"
    For first bring-up, use feedback examples. Motion examples may drive motors or mechanisms, so secure the hardware and confirm power capacity before running them.

Related pages:

- [Device IDs and Baud Rates](../../tutorials/device-id-and-baudrate.md)
- [MCU UART Wiring](../../tutorials/mcu-uart-wiring.md)
- [TTL Adapter (A) SDKs and Tools](../bus-devices/ttl-adapter-a/sdk-and-tools.md)
