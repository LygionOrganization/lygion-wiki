# S.BUS Development

The open-source firmware includes optional S.BUS receiver support through the Bolder Flight Systems S.BUS library. S.BUS is an advanced firmware mode and is not enabled in the default `DEV_TYPE_RD_LITE` configuration.

## Enable the S.BUS Profile

In `src/Config.h`, select the intended profile or enable the relevant flag:

```cpp
// #define DEV_TYPE_RD_LITE
#define DEV_TYPE_SBUS_UGV_A
```

That profile enables:

```cpp
#define UART0_AS_SBUS
```

The firmware then uses `Serial0` for S.BUS reception instead of normal UART communication.

## Default S.BUS Calibration Values

```cpp
#define SBUS_MAX 1722.0
#define SBUS_MIN 282.0
#define SBUS_MID 1002.0
#define SBUS_RAN 720.0
```

The source creates the receiver on ESP32-S3 pins 44 and 43 with inverted input:

```cpp
bfs::SbusRx sbus(&Serial0, 44, 43, true);
```

Verify the physical connector, receiver voltage, signal polarity, and your transmitter's actual channel range before wiring or enabling motion.

## Development Guidance

- Read and print channels before connecting motors.
- Confirm the receiver's failsafe behavior.
- Map channels with deadbands and explicit range limits.
- Stop motion when frames are lost or failsafe is active.
- Test low speed with the robot raised or mechanically secured.

!!! danger "Radio loss must stop the robot"
    Production S.BUS control must treat lost frames and failsafe states as a stop condition. Do not depend only on the last received command.
