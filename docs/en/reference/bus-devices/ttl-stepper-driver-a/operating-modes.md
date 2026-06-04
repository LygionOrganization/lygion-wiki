# TTL Stepper Driver (A) Operating Modes

The driver supports position control, continuous-speed control, and low-level EDS follower synchronization.

| Mode | Name | Typical use |
| --- | --- | --- |
| 0 | Position mode | Move to a requested position |
| 1 | Speed mode | Rotate continuously forward, reverse, or stop |
| 2 | EDS follower mode | Make one or more followers track a leader through the EDS interface |

Use FD or the EEPROM programming examples to change the operating mode.

!!! warning "Disconnect EDS before changing modes"
    Disconnect the EDS interface before changing an operating mode. Power-cycle the driver after changing the mode.

## Position Mode

Position mode moves the motor to a requested target:

```python
packetHandler.WritePosEx(ID, position, speed, acc, current)
```

| Argument | Meaning |
| --- | --- |
| `ID` | Device ID |
| `position` | Target position |
| `speed` | Speed parameter |
| `acc` | Acceleration parameter |
| `current` | Target phase-current parameter |

Typical applications include rotary tables, robot joints, linear stages, grippers, and lead-screw mechanisms.

## Speed Mode

Speed mode runs continuously:

```python
packetHandler.WheelMode(ID)
packetHandler.WriteSpec(ID, speed, acc, current)
```

```text
speed > 0  forward
speed < 0  reverse
speed = 0  stop
```

!!! warning "Enable heartbeat protection in speed mode"
    Without a heartbeat timeout, a motor can continue running after the host program crashes or communication is lost.

## EDS Follower Mode

EDS follower mode is intended for mechanisms that require tight low-level synchronization, including multi-screw lifts, dual-motor drives, and parallel mechanisms.

Setup sequence:

1. Set each follower to operating mode 2.
2. Set each follower's secondary ID to the leader's primary ID.
3. Connect the EDS chain with GH-1.25-3P cables.
4. Send commands only to the leader's primary ID.

!!! note "Primary IDs must still be unique"
    Every primary bus ID must be unique. Multiple followers may share a secondary ID that matches the leader's primary ID.

For a synchronized mechanism using limit switches, connect the switch to the leader so its low-level stop action also reaches the followers.

## EDS Follower vs. Bus SyncWrite

| Method | Behavior |
| --- | --- |
| Bus SyncWrite | The host sends target parameters to several device IDs in one bus transaction |
| EDS follower | Followers track the leader through the low-level EDS signal |

Use SyncWrite for coordinated starts. Prefer EDS follower mode for mechanically coupled systems that require tighter synchronization.
