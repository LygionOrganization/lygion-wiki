# C++ / Arduino First Demo

This tutorial connects an Arduino-compatible MCU to a Lygion TTL bus device through a hardware UART. The goal is to upload a read-only example and view device feedback in Arduino IDE or PlatformIO.

```text
MCU development board
  | UART RX / TX / GND
  v
TTL Adapter (A) UART port
  | TTL bus
  v
TTL Encoder E02 / TTL Stepper Driver (A) / compatible TTL bus device
```

![MCU UART connection](../../assets/images/g02.png){ .img-rounded width="450" }

Choose Arduino IDE for the simplest first setup. Choose PlatformIO if you already manage embedded projects in VS Code.

## 1. Choose a Suitable MCU

| MCU family | Examples | Notes |
| --- | --- | --- |
| ESP32 | ESP32S3, ESP32, ESP32C3 | Use a free hardware UART such as `Serial1` or `Serial2` |
| STM32 | STM32F103, F4, G4, and others | Requires a compatible STM32 Arduino core |
| Arduino AVR | Mega2560 | Recommended because it provides several hardware UARTs |
| Arduino ARM | Due, GIGA | Usually provides several hardware UARTs |
| RP2040 | Raspberry Pi Pico / Pico W | Confirm the UART names and pin mapping for the selected core |
| Custom MCU board | Any board with a hardware UART | Confirm UART pins, logic level, and power |

!!! warning "Avoid a single-UART board for the first 1 Mbps test"
    Arduino Uno and Nano usually share their only hardware UART with USB upload and debugging. Software serial is unreliable at the default 1 Mbps bus rate. Prefer ESP32, ESP32S3, Mega2560, or STM32.

For a computer or Linux SBC, use the [Python first demo](python-first-demo.md).

## 2. Prepare the Hardware

- An Arduino-compatible MCU board
- [TTL Adapter (A)](../reference/bus-devices/ttl-adapter-a/index.md), or another UART-to-single-wire TTL circuit
- One TTL bus device
- A USB data cable for the MCU
- An external supply that matches the bus device
- Jumper wires or the required connector cables

Before testing:

- Confirm that the USB cable carries data.
- Wire MCU RX to adapter RX, MCU TX to adapter TX, and GND to GND.
- Connect only one new bus device.
- Apply a compatible external supply before operating an actuator.

See [Power and wiring fundamentals](../tutorials/power-and-wiring-basics.md) when in doubt.

## 3. Install a Development Tool

=== "Arduino IDE"

    Follow [Install Arduino IDE](../tutorials/install-arduino-ide.md), then install the board package for your MCU.

=== "PlatformIO"

    Follow [Install PlatformIO](../tutorials/install-platformio.md), then select the correct board and framework in `platformio.ini`.

## 4. Understand the Two Serial Connections

Most MCU examples use two separate UARTs:

| Connection | Purpose | Typical object |
| --- | --- | --- |
| MCU USB/debug serial <-> computer | Upload firmware and print results | `Serial` |
| MCU hardware UART <-> TTL Adapter (A) <-> bus device | Communicate with TTL devices | `Serial1` or `Serial2` |

ESP32S3 example:

```cpp
Serial.begin(115200);                         // Debug output to the computer
Serial1.begin(1000000, SERIAL_8N1, 18, 17);  // TTL bus at 1 Mbps
```

| Value | Meaning |
| --- | --- |
| `115200` | Serial monitor baud rate |
| `1000000` | Default TTL bus baud rate |
| `18` | ESP32S3 RX pin |
| `17` | ESP32S3 TX pin |

!!! warning "Do not confuse the two baud rates"
    A garbled serial monitor usually means the debug rate is wrong. A TTL bus communication failure usually points to the 1 Mbps setting, device ID, UART wiring, GND, or power.

## 5. Wire the MCU and Bus

### MCU to TTL Adapter (A)

| MCU | TTL Adapter (A) |
| --- | --- |
| RX | RX |
| TX | TX |
| GND | GND |

TTL Adapter (A) expects this straight-through connection because its UART pins feed the onboard single-wire conversion circuit. This differs from many conventional USB-to-UART adapters.

!!! warning "Verify the UART logic level"
    TTL Adapter (A) uses 3.3 V TTL logic. Use a level shifter if a 5 V MCU output is not confirmed safe.

See [MCU UART wiring](../tutorials/mcu-uart-wiring.md).

### Adapter to TTL Bus Device

Verify the three bus conductors:

```text
+   Positive supply
-   Supply return / GND
S   Single-wire TTL signal
```

Connect only one new device and power actuators externally.

## 6. Get the C++ SDK

- [C++ SDK on GitHub](https://github.com/LygionOrganization/lygion_devs_cpp)
- [Download the C++ SDK](../../assets/files/lygion_devs_cpp.zip)

### Arduino IDE

Copy the SDK library into:

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

Restart Arduino IDE afterward.

### PlatformIO

Place the library under the project's `lib` directory:

```text
your_project/
|-- platformio.ini
|-- src/
|   `-- main.cpp
`-- lib/
    `-- lygion_devs_cpp/
```

## 7. Open a Read-Only Example

Use a `Ping`, `Read`, `FeedBack`, or similar example before any motion-control example.

| Device | Safe first example |
| --- | --- |
| TTL Encoder E02 | `FeedBack` or `Read` |
| TTL Stepper Driver (A) | `Ping`, `Read`, or `FeedBack` |
| Bus servo or another actuator | `Ping` or `Read` |

Secure the mechanism and keep a safe distance before running any example that commands motion.

## 8. Configure the Hardware UART

=== "ESP32S3 / ESP32"

    ```cpp
    Serial.begin(115200);
    Serial1.begin(1000000, SERIAL_8N1, 18, 17);
    ttlsd.pSerial = &Serial1;
    ```

    Change `18` and `17` to match the selected RX and TX pins. Avoid boot-strap, flash, PSRAM, USB, and occupied peripheral pins.

=== "Arduino Mega2560"

    ```cpp
    Serial.begin(115200);
    Serial1.begin(1000000);
    ttlsd.pSerial = &Serial1;
    ```

    `Serial1` normally uses RX1 on D19 and TX1 on D18.

=== "Arduino Due"

    ```cpp
    Serial.begin(115200);
    Serial1.begin(1000000);
    ttlsd.pSerial = &Serial1;
    ```

    Confirm the pins for the selected `Serial1`, `Serial2`, or `Serial3` port.

=== "STM32 Arduino Core"

    ```cpp
    Serial.begin(115200);
    Serial1.begin(1000000);
    ttlsd.pSerial = &Serial1;
    ```

    UART object names and pin mappings depend on the board and Arduino core.

=== "RP2040 / Raspberry Pi Pico"

    ```cpp
    Serial.begin(115200);
    Serial1.begin(1000000);
    ttlsd.pSerial = &Serial1;
    ```

    Confirm which UART and pins `Serial1` represents in the selected board package.

## 9. Confirm or Change the Device ID

A motion command includes the target ID:

```cpp
// ttlsd.WritePosEx(ID, goalPosition, speed, acceleration, current);
ttlsd.WritePosEx(1, 3200, 600, 0, 150);
```

Factory-new devices commonly use ID `1`. Keep that value for the first test.

To change an EEPROM-stored ID:

```cpp
// Enable EEPROM writes using the current ID.
hlscl.unLockEprom(1);

// Change ID 1 to ID 2.
hlscl.writeByte(1, HLSCL_ID, 2);

// Lock EEPROM using the new ID.
hlscl.LockEprom(2);
```

If the current ID is unknown, a broadcast ID may be used with only one device connected:

```cpp
hlscl.unLockEprom(254);
hlscl.writeByte(254, HLSCL_ID, 1);
hlscl.LockEprom(1);
```

!!! warning "Never broadcast an ID change to a multi-device bus"
    Every connected device may receive the write and end up with the same ID.

## 10. Upload and Open the Serial Monitor

=== "Arduino IDE"

    1. Open the `.ino` example.
    2. Select the correct board and MCU upload port.
    3. Update the UART configuration.
    4. Upload the sketch.
    5. Open Serial Monitor at `115200`.

    See [Upload an Arduino example](../tutorials/upload-arduino-sketch.md) and [Use a serial monitor](../tutorials/serial-monitor.md).

=== "PlatformIO"

    1. Open the project directory in VS Code.
    2. Verify the board in `platformio.ini`.
    3. Set `monitor_speed = 115200`.
    4. Update the UART configuration.
    5. Upload and open the serial monitor.

    ```ini
    [env:esp32-s3-devkitc-1]
    platform = espressif32
    board = esp32-s3-devkitc-1
    framework = arduino
    monitor_speed = 115200
    ```

## 11. Interpret the Result

Successful output may look like:

```text
Lygion TTL Bus Demo Start
ID: 1
Position: 1200
Speed: 0
```

or:

```text
Ping succeeded. ID: 1
Read position: 1200
Read speed: 0
```

If you see `FeedBack error`, `Ping failed`, or `Read failed`, check the debug rate, TTL bus rate, device ID, RX/TX/GND, `+ / - / S`, external power, selected UART object, and duplicate IDs.

## Common Board Configurations

| Board | Recommended bus UART | Example | Notes |
| --- | --- | --- | --- |
| ESP32S3 | `Serial1` | `Serial1.begin(1000000, SERIAL_8N1, RX, TX);` | Assign free RX/TX pins |
| ESP32 | `Serial2` or `Serial1` | `Serial2.begin(1000000, SERIAL_8N1, RX, TX);` | Avoid boot and upload pins |
| Mega2560 | `Serial1` | `Serial1.begin(1000000);` | RX1=D19, TX1=D18 |
| Due | `Serial1`, `Serial2`, or `Serial3` | `Serial1.begin(1000000);` | 3.3 V I/O |
| STM32 | `Serial1` or `Serial2` | `Serial1.begin(1000000);` | Depends on board and core |
| RP2040 | `Serial1` | `Serial1.begin(1000000);` | Depends on board package |

## Troubleshooting

| Symptom | Likely cause | Action |
| --- | --- | --- |
| Firmware will not upload | Wrong board, port, or driver | Verify the board definition, upload port, and driver |
| No serial monitor output | Wrong rate or firmware not running | Set `115200` and reset the board |
| Garbled monitor output | Debug baud mismatch | Set the monitor to `115200` |
| `Ping failed` | Wrong ID, bus rate, or UART wiring | Check ID, `1000000`, RX/TX/GND |
| `Read failed` | No power, reversed bus, wrong UART object | Check power, `+/-/S`, and `pSerial` |
| MCU resets when actuator connects | Supply overload | Power the actuator from a suitable external supply |
| Multi-device reads collide | Duplicate IDs | Configure one device at a time |

If the first test still fails, reduce the setup to one device, confirm ID `1`, confirm 1 Mbps, share GND, and cross-check the device with FD or the Python demo. See [Communication troubleshooting](../tutorials/communication-troubleshooting.md).
