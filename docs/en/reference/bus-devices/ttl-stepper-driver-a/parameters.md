# TTL Stepper Driver (A) Motion and Current Parameters

This page explains the position, speed, acceleration, and current values used by the driver APIs.

## Position

With default settings:

```text
One motor revolution = 3200 microsteps
Position range = 0-65534
Maximum position-mode travel = 65534 / 3200 = approximately 20.48 turns
```

To increase the multi-turn range, change the angle-resolution parameter, typically within `1-128`. For example, with a value of `3`:

```text
Effective steps per turn = 3200 / 3
Maximum travel = 65534 / (3200 / 3) = approximately 61.44 turns
```

Increasing the range reduces position resolution.

## Speed

The default speed parameter represents:

```text
50 microsteps per second
```

Convert it to RPM with:

```text
RPM = speed parameter x 50 x 60 / 3200
```

For a speed parameter of `400`:

```text
400 x 50 x 60 / 3200 = 375 RPM
```

Begin at `100` or `200`. Excessive speed can cause missed steps, vibration, or a motor that only makes noise.

## Acceleration

The acceleration parameter represents:

```text
100 microsteps per second squared
```

!!! warning "An acceleration value of 0 means near-maximum acceleration"
    It can produce a hard start, vibration, or missed steps. Begin with a small nonzero value that suits the load.

## Current

The current setting controls motor winding phase current, not the current displayed by the DC supply.

Approximate phase-current relationship:

```text
Phase current = approximately 3.3 x 2 x (parameter / 1000)
```

For a current parameter of `200`:

```text
Phase current = approximately 3.3 x 2 x 0.2 = 1.32 A
```

The DC supply displays bus input current, which varies with supply voltage, winding resistance and inductance, speed, load, microstepping, and driver efficiency.
