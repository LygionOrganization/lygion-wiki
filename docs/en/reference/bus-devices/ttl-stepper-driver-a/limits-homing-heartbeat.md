# TTL Stepper Driver (A) Limits, Homing, and Heartbeat Protection

## Limit Inputs

The driver provides two limit inputs:

```text
MIN
LIMIT
```

Each connector contains:

```text
S / + / -
```

The corresponding limit is active when `S` is pulled high.

## Mechanical Limit Switch

A normally open switch can be wired as:

```text
One switch terminal -> S
Other switch terminal -> +
```

Pressing the switch pulls `S` high.

## PNP Optical or Proximity Sensor

```text
Positive wire -> +
Negative wire -> -
Signal wire -> S
```

## Limit Behavior by Operating Mode

| Mode | MIN | LIMIT |
| --- | --- | --- |
| Position mode, mode `0` | Not checked because startup minimum position is already `0` | Blocks positive-direction motion |
| Speed mode, mode `1` | Blocks negative-direction motion | Blocks positive-direction motion |

After a limit activates, the motor can normally move away from that limit in the opposite direction.

## Homing in Speed Mode

A lead screw or linear stage can home with this sequence:

```text
1. Enter speed mode after startup.
2. Command a low negative speed toward MIN.
3. Stop when the MIN input activates.
4. Return to position mode.
5. Use reOfsCal() to assign the current position to 0.
6. Continue with position-mode control.
```

## Heartbeat Protection

Configure heartbeat protection with FD for speed-mode safety. If no new command is received within the timeout, the motor stops automatically.

The heartbeat value uses 100 ms units:

```text
30 x 100 ms = 3000 ms = 3 seconds
```

!!! warning "Enable heartbeat protection for continuous motion"
    Without it, a motor may continue running after the host crashes, disconnects, or loses communication.
