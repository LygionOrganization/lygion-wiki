# Servos and Bus Devices

Before connecting an actuator, verify its rated voltage, protocol, baud rate, connector polarity, and device ID. External DC input powers the actuator ports; USB Type-C is not actuator power.

## Configure IDs

Connect one factory-default servo at a time when changing IDs. Two devices with the same ID cannot be controlled reliably on one bus.

The web console supports:

- STS/SMS position, speed, acceleration, midpoint, torque, and feedback
- HLS position, speed, midpoint, torque, and feedback
- SCS position, speed/time parameters, torque, ID changes, and feedback

!!! warning "HLS speed must not be zero"
    Use a valid nonzero speed value when sending HLS motion commands.

When control fails, check external power, common ground, selected servo family, bus baud rate, ID, torque state, and physical travel limits.

