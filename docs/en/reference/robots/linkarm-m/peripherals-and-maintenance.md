# Peripherals and Maintenance

The SDK can control the TTL Node (A) RGB indicators and PWM outputs, and can enable, disable, or limit servo torque.

!!! danger "PWM outputs are power outputs"
    Check load voltage, current, polarity, and inductive-load protection before enabling them.

!!! danger "The arm loses support when torque is disabled"
    Hold the links and gripper before releasing torque. Restore torque only after the mechanism is in a safe pose.

Regularly inspect mounting hardware, link fasteners, cable routing, connectors, abnormal servo temperature or noise, and the calibration backup. Stop safely by ending active commands, moving to a supported pose, disabling torque when appropriate, and then removing actuator power.

