# Control TTL Stepper Driver (A) with C++ / Arduino

The C++ / Arduino SDK supports ESP32S3, ESP32, Arduino Mega2560, STM32 Arduino Core, and other compatible MCU platforms.

- [C++ SDK on GitHub](https://github.com/LygionOrganization/lygion_devs_cpp)
- [Download the C++ / Arduino SDK](../../../../assets/files/lygion_devs_cpp.zip)

## Initialize the UART

ESP32S3:

```cpp
Serial1.begin(1000000, SERIAL_8N1, 18, 17);
ttlsd.pSerial = &Serial1;
```

Mega2560:

```cpp
Serial1.begin(1000000);
ttlsd.pSerial = &Serial1;
```

## Included Examples

| Example | Purpose |
| --- | --- |
| `FeedBack.ino` | Read position, speed, voltage, temperature, and other feedback |
| `WritePos.ino` | Position-mode control |
| `WriteSpe.ino` | Speed-mode control |
| `SyncRead.ino` | Read several devices in one transaction |
| `SyncWritePos.ino` | Send positions to several devices |
| `SyncWriteSpe.ino` | Send speeds to several devices |
| `RegWritePos.ino` | Stage commands, then execute them together |
| `ProgramEprom.ino` | Edit stored parameters |
| `CalibrationOfs.ino` | Assign the current position reference |

## Position Control

```cpp
ttlsd.WritePosEx(1, 3200, 200, 10, 150);
```

## Speed Control

```cpp
ttlsd.WheelMode(1);
ttlsd.WriteSpe(1, 100, 10, 150);
delay(2000);
ttlsd.WriteSpe(1, 0, 10, 150);
```

## Development Guidance

- Read feedback before sending motion commands.
- Use low speed and a nonzero acceleration for the first motion test.
- Confirm every device individually before using synchronous commands.
- Use a hardware UART for the 1 Mbps bus.
