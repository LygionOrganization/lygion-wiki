# SW69-TTL ESP32 Arduino Development

This page describes the ESP32 Arduino example for SW69-TTL. It follows the same logic as the Python example: read the encoder, synchronize the steering driver, steer by angle, and drive the wheel in speed mode.

[Download ESP32 Arduino example](../../../../reference/modules/sw69-ttl/assets/sw69_esp32_example.ino){ .md-button .md-button--primary }
[Download C++ / Arduino SDK](../../../../assets/files/lygion_devs_cpp.zip){ .md-button }

## Before You Start

Complete [Quick Start and FD Setup](quickstart.md), then confirm:

- Encoder, steering driver, and drive driver have unique IDs.
- Steering driver is in position mode.
- Drive driver is in speed mode.
- External power is connected.
- ESP32 and the TTL adapter share GND.
- TTL baud rate is `1000000`.

Default IDs in the example:

| Device | ID |
| --- | ---: |
| TTL Encoder E02 | `10` |
| Steering driver | `11` |
| Drive driver | `12` |

## ESP32 UART Wiring

The example uses `Serial1`:

```cpp
const int TTL_RX_PIN = 5;
const int TTL_TX_PIN = 4;

Serial1.begin(1000000, SERIAL_8N1, TTL_RX_PIN, TTL_TX_PIN);
ttlsd.pSerial = &Serial1;
```

| ESP32 | TTL Adapter (A) UART |
| --- | --- |
| GPIO5 / RX | RX |
| GPIO4 / TX | TX |
| GND | GND |

!!! note "RX/TX wiring"
    With TTL Adapter (A)'s UART connector, use RX-to-RX, TX-to-TX, and GND-to-GND. If you use another TTL conversion circuit, follow that hardware's wiring guide.

## What the Example Does

After upload, `setup()` runs one test sequence:

1. Starts USB debug serial at `115200`.
2. Starts TTL bus serial at `1000000`.
3. Reads the E02 encoder.
4. Converts encoder position to steering driver position.
5. Calls `CalibrationOfs()` to synchronize the steering driver.
6. Commands steering to `0°`, `+45°`, `-45°`, and `0°`.
7. Drives the wheel forward, stops, reverses, and stops.
8. Keeps sending stop commands in `loop()`.

Lift the wheel before the first run.

## SDK Function Mapping

| Task | Python example | Arduino example |
| --- | --- | --- |
| Read encoder | `ReadPosSpeed(id)` | `ReadPos(id)`, `ReadSpeed(id)` |
| Synchronize current position | `reOfsCal(id, position)` | `CalibrationOfs(id, position)` |
| Steering position control | `WritePosEx(id, position, speed, acc, current)` | `WritePosEx(id, position, speed, acc, current)` |
| Wheel speed control | `WriteSpec(id, speed, acc, current)` | `WriteSpe(id, speed, acc, current)` |

## Angle Conversion

```text
total ratio = (72 / 20) × 5.181818182
encoder counts per turn = 4096
encoder center = 2048
stepper counts per motor turn = 3200
steering midpoint = stepper counts × total ratio / 2
steering zero target = STEERING_ZERO
encoder delta = encoder reading - encoder center
startup sync position = steering midpoint + encoder delta × encoder-to-step scale
target position = target radians × radian-to-step scale + STEERING_ZERO
```

The example constrains driver position to `0` through `65534`.

## Upload

### Arduino IDE

1. Install ESP32 board support.
2. Install or copy `lygion_devs_cpp` into your Arduino `libraries` folder.
3. Open `sw69_esp32_example.ino`.
4. Update `TTL_RX_PIN`, `TTL_TX_PIN`, and device IDs if needed.
5. Select your ESP32 or ESP32S3 board.
6. Upload and open Serial Monitor at `115200`.

### PlatformIO

Use the sketch as `src/main.cpp` or place the `.ino` in `src`. Example configuration:

```ini
[env:esp32-s3-devkitc-1]
platform = espressif32
board = esp32-s3-devkitc-1
framework = arduino
monitor_speed = 115200
```

## Troubleshooting

| Symptom | Likely cause | What to check |
| --- | --- | --- |
| No serial output | Monitor baud rate mismatch or board not running | Use `115200` and reset the board |
| Encoder read fails | Wrong ID, wiring, baud rate, or power | Check `ENCODER_ID`, bus wiring, and external power |
| Steering angle is wrong | Encoder center or startup sync is incorrect | Recalibrate center and confirm `jointInit()` succeeds |
| Drive wheel does not move | Drive driver is not in speed mode or lacks power | Set mode `1` and check external power |
| Wheel stops too soon | Heartbeat protection is active but commands are not resent | Keep the periodic command loop |
