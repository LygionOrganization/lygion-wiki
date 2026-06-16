# Configuration and Midpoint Calibration

LinkArm-M requires the correct serial port, `500000` baud, joint IDs, TTL Node ID, link dimensions, limits, and four arm-specific `servo_middle` values in `arm_config.json`.

Midpoint values compensate for mechanical assembly offsets. Incorrect values can shift the zero pose, reduce travel, invalidate IK/FK results, or cause a collision.

## Enter Values from the Label

1. Locate the four midpoint values on the arm's label.
2. Copy them in joint order into `servo_middle`.
3. Validate the JSON syntax.
4. Run a read-only status command.
5. Test one joint at low speed and over a small range.

!!! danger "Never substitute example values"
    Each arm has its own calibration. Keep a backup of the original configuration.

Only record new midpoint values when the original calibration is unavailable or the mechanical assembly has changed. Support the arm, release torque carefully, align the reference pose, read the raw positions, and back up the result before further testing.

