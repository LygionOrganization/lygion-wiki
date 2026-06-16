# TTL Node (A) Power and Wiring

Use USB for communication and logic power. Add a DC 9-12.6 V supply through HX-5264-3P or PH2.0-3P when servos or PWM loads require power.

All bus devices must share ground, use compatible voltage levels, and use the same communication baud rate.

## S.BUS Receiver

The S.BUS connector supplies 5 V at up to 500 mA. Confirm that the receiver is compatible with 5 V and verify signal, power, and ground before connecting it.

## PWM Power Outputs

Each PH2.0-2P output supports up to 3 A. PWM changes the load's average power; it is not a regulated variable-voltage DC output.

!!! danger "Protect inductive loads"
    Motors, solenoids, and relays can generate voltage spikes. Use suitable flyback protection and allow margin for startup and stall current.

!!! danger "Never apply power to GH1.25-3P"
    That connector is signal and ground only.

