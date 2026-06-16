# TTL Node (A) Arduino Development

Install the Arduino IDE or PlatformIO, add the ESP32 board package when using an ESP32 controller, and install the `lygion_devs` library.

Initialize the hardware UART used for the TTL bus with the bus baud rate, then create the TTL Node device object with the node ID. The exact UART and direction-control pins depend on the controller board.

Examples are provided under `example/lyttln` for:

- pinging the node
- changing the device ID
- reading bus voltage
- controlling both PWM outputs
- controlling RGB LEDs
- reading S.BUS channels

!!! warning "Use the new ID after changing it"
    Update the device object or restart the program after writing a new ID.

!!! danger "PWM loads require external power"
    USB alone cannot supply servo or high-current PWM loads.

Start with one device, confirm read-only communication, then add output control and additional bus devices.

