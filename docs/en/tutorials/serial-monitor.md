# Use a Serial Monitor

A serial monitor displays debug messages printed by MCU firmware through `Serial.print()`.

## Arduino IDE

Open **Tools -> Serial Monitor** and set the rate to:

```text
115200
```

It must match:

```cpp
Serial.begin(115200);
```

## PlatformIO

Click **Monitor** in the PlatformIO toolbar or run:

```bash
pio device monitor
```

Set the rate in `platformio.ini`:

```ini
monitor_speed = 115200
```

## Debug Serial vs. TTL Bus Baud Rate

```cpp
Serial.begin(115200);
Serial1.begin(1000000, SERIAL_8N1, 18, 17);
```

| Configuration | Purpose |
| --- | --- |
| `Serial.begin(115200)` | Debug connection between the MCU and computer |
| `Serial1.begin(1000000, ...)` | Communication between the MCU and TTL bus devices |

!!! warning "Do not set the serial monitor to the TTL bus rate"
    The monitor normally displays `Serial` at `115200`. The default TTL bus rate of `1000000` applies to `Serial1`.

## No Output

Check that the firmware uploaded, the correct MCU port is selected, the monitor uses `115200`, the firmware calls `Serial.begin(115200)`, and the board has been reset if required.

## Debug Output Appears but Device Reads Fail

The computer-to-MCU link works, but the MCU-to-bus link does not. Verify the selected hardware UART, RX/TX pins, adapter wiring, device ID, baud rate, GND, and device power.
