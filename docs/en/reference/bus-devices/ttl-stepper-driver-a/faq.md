# TTL Stepper Driver (A) FAQ

## Ping succeeds, but the motor does not turn

Check the external DC 9-26 V supply, motor phase wiring, bipolar motor type, current setting, operating mode, limit inputs, torque state, and mechanical load.

## The motor vibrates, makes noise, or loses steps

Common causes include excessive speed, excessive or zero acceleration setting, insufficient phase current, low supply voltage, a high-inductance motor at high speed, and excessive load inertia.

Start unloaded. Reduce speed, use a small nonzero acceleration, set an appropriate current, then add load gradually.

## Why does the supply current differ from the configured current?

The configured value controls winding phase current. The supply displays DC bus input current, which depends on voltage, motor impedance, speed, load, microstepping, and driver efficiency.

## How is the speed parameter converted?

The default unit is 50 microsteps per second:

```text
RPM = speed parameter x 50 x 60 / 3200
```

## Why is the default position range about 20.5 turns?

The default uses 3200 microsteps per revolution and a `0-65534` position range:

```text
65534 / 3200 = approximately 20.48 turns
```

Increasing the angle-resolution parameter expands the range but reduces position precision.

## Can the driver share a bus with servos or TTL Encoder E02?

Yes, when all IDs are unique, baud rates match, the supply voltage is safe for every device, and the power system can support the load.

## Should I use SyncWrite or EDS follower mode?

Use SyncWrite for general coordinated starts. Prefer EDS follower mode for tightly coupled dual-motor or multi-screw mechanisms.
