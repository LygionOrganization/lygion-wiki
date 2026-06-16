# Configure TTL Node (A) with FD

!!! warning "Connect only one unconfigured device"
    Factory-default nodes share ID `0`. Isolate the target device before changing its ID.

1. Connect the device and open FD.
2. Select the correct serial port and `1000000` baud.
3. Open the port and search for devices.
4. Select `TTL-Node-A` to open its parameter page.
5. Change the device ID to an unused value and write the setting.
6. Search again using the new ID.

When changing the baud rate, update the host, every node, and every servo on that bus. A device at a different baud rate will appear offline.

Use low-power loads for the first PWM test and provide external power. RGB and S.BUS values can be checked without actuator power.

