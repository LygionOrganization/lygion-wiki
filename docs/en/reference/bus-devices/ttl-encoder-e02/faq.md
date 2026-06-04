# TTL Encoder E02 FAQ

## The encoder cannot be read

Verify the serial port, actual device baud rate, device ID, HC-1.25-3P wire order, bus power, and duplicate IDs.

## Angle readings jump or fluctuate

Check that the radial magnet is centered over the encoder IC, approximately 1 mm above it, firmly mounted, and rotating without eccentricity or wobble. Also secure the PCB and verify stable power.

## Why do examples refer to `TTLSD` or motors?

TTL Encoder E02 shares several SDK interfaces with TTL Stepper Driver (A). Use only the position, speed, synchronous-read, and reference-calibration functions for encoder applications.

## Can the encoder share a bus with servos or stepper drivers?

Yes. Compatible Feetech TTL bus servos, TTL Encoder E02, and TTL Stepper Driver (A) can share a bus when all IDs are unique, baud rates match, and the supply voltage is safe for every device.

## Must calibration be repeated after power-up?

The single-turn reference is retained. The accumulated multi-turn count is not.
