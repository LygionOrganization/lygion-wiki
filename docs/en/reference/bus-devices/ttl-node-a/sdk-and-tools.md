# TTL Node (A) SDKs and Tools

## Python SDK

Download [lygion_devs_py.zip](../../../assets/files/lygion_devs_py.zip). Configure the serial port, baud rate, and node ID before running the `lynode` examples.

## C++ / Arduino SDK

Download [lygion_devs_cpp.zip](../../../assets/files/lygion_devs_cpp.zip) or install the library in the Arduino/PlatformIO project. Examples cover node discovery, ADC readings, PWM, RGB, and S.BUS input.

## FD Utility

FD is the Windows GUI utility for discovery, ID and baud-rate configuration, parameter inspection, and basic functional testing. See [Configure with FD](fd-configuration.md).

!!! tip "Different device types can share one bus"
    TTL nodes and compatible serial-bus servos may share the bus when IDs are unique, baud rates match, and the power system supports the combined load.

