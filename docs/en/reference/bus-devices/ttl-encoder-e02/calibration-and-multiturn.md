# TTL Encoder E02 Calibration and Multi-Turn Data

## Set the Current Position Reference

Reference calibration assigns a requested position value to the encoder's current physical angle. It is not limited to setting zero.

Python:

```python
packetHandler.reOfsCal(1, 1024)
```

C++:

```cpp
ttlsd.CalibrationOfs(1, 1024);
```

Both examples assign position 1024 to the current angle of encoder ID 1.

| Position | Angle |
| --- | --- |
| 0 | 0 degrees |
| 1024 | 90 degrees |
| 2048 | 180 degrees |
| 3072 | 270 degrees |
| 4095 | Almost 360 degrees |

The single-turn reference calibration is retained after power loss.

## Multi-Turn Position

The encoder supports a multi-turn position range of:

```text
0-65534
```

At 12-bit resolution, this represents approximately 16 revolutions.

!!! warning "The accumulated turn count is not retained after power loss"
    Applications that depend on a multi-turn absolute reference must re-establish it in the host or controller after power is restored.

## Typical Calibration Uses

- Assign mechanical zero to position `0`
- Assign a joint center to `2048`
- Define a known assembled pose as a requested angle
- Align the reference positions of several installed encoders
