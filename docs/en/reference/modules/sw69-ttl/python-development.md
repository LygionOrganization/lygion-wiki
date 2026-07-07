# SW69-TTL Python Development

This page explains the Python control flow for one SW69-TTL module:

1. Read the steering encoder.
2. Synchronize the steering stepper driver's current position.
3. Command steering angles.
4. Drive the wheel in speed mode.

Complete [Quick Start and FD Setup](quickstart.md) before running the program.

[Download Python example](../../../../reference/modules/sw69-ttl/assets/sw69_example.py){ .md-button .md-button--primary }
[Download Python SDK](../../../../assets/files/lygion_devs_py.zip){ .md-button }

## Files

Place the example next to the Python SDK package:

```text
sw69-python-demo/
├─ sw69_example.py
└─ lygion_devs_py/
   └─ lydevs_sdk/
```

## Environment

Install Python and `pyserial`. If you are new to the SDK, start with [Python First Demo](../../../quickstart/python-first-demo.md).

## Edit the Port and IDs

Open the example and update:

```python
ENCODER_ID = 10
TURNING_ID = 11
WALKING_ID = 12
portHandler = PortHandler("COM18")
```

Common serial port names:

| System | Examples |
| --- | --- |
| Windows | `COM3`, `COM18` |
| Linux | `/dev/ttyUSB0`, `/dev/ttyACM0` |
| macOS | `/dev/cu.usbserial-xxxx` |

## Startup Synchronization

The steering motor is open-loop. At power-on, the driver does not know the real steering angle. The example reads the E02 encoder and calls offset calibration on the steering driver so the software coordinate matches the physical joint.

```python
joint_init(ENCODER_ID, TURNING_ID)
```

The simplified conversion is:

```text
encoder delta = encoder reading - ENCODER_CENTER
sync position = JOINT_MID + encoder delta × ENCODER2STEPS
target position = target radians × RAD2STEPS + STEERING_ZERO
```

After FD center calibration, the mechanical center usually reads `2047` or `2048`. If your actual center is different, change `ENCODER_CENTER`.

## Steering Control

Use degrees for application code:

```python
joint_deg_ctrl(TURNING_ID, 45, 400, 15, 200)
joint_deg_ctrl(TURNING_ID, -45, 400, 15, 200)
```

In the example, `0°` is the calibrated steering center.

## Drive Wheel Control

The drive motor driver must be configured in speed mode:

```python
walking_motor_ctrl(WALKING_ID, 50, 15, 200)
walking_motor_ctrl(WALKING_ID, 0, 15, 200)
walking_motor_ctrl(WALKING_ID, -50, 15, 200)
```

If heartbeat protection is enabled, keep sending speed commands periodically while the wheel should continue moving.

## Safe First Run

Before running:

- Lift the wheel off the desk or floor.
- Keep steering clear of cables and fingers.
- Use low speed and non-zero acceleration.
- Confirm external power is connected.

The example will run:

1. Startup steering sync.
2. Steering to `0°`, `+45°`, `-45°`, and back to `0°`.
3. Drive wheel forward, stop, reverse, and stop.

## Parameter Notes

| Parameter | Example value | Notes |
| --- | ---: | --- |
| Steering speed | `400` or lower | Conservative first-test speed |
| Acceleration | `15` | Avoid `0` during normal bring-up |
| Current | `200` | About 1.32 A phase current |
| Wheel speed | `50` / `-50` | Low speed for first test |

Approximate phase current:

```text
phase current (A) ≈ 3.3 × 2 × current / 1000
```
