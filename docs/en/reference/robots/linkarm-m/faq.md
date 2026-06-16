# LinkArm-M Troubleshooting

## No Serial Port

Use a data-capable cable, connect to the TTL Node Type-C port, install the USB serial driver, and check `python -m serial.tools.list_ports`.

## Permission Denied on Linux

Add the user to the system's serial-device group or apply an appropriate udev rule, then sign out and back in.

## The Port Exists but the Arm Does Not Respond

Check external 12 V power, `500000` baud, the selected port, TTL Node ID `40`, joint IDs, common ground, and whether another program owns the port.

## The Pose Is Clearly Wrong

Stop motion and compare `servo_middle` with the label on this arm. Also verify joint order, direction, link dimensions, and limits.

## IK_FAILED

The target may be outside the workspace, too close to a singularity, or incompatible with the configured dimensions and limits. Test a nearby reachable point.

## A Move Does Not Finish

Check power, torque limits, mechanical obstruction, speed, timeout, and whether `--reliable` is waiting for an unreachable tolerance.

