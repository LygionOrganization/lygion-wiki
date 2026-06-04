# TTL Adapter (A) SDKs and Tools

TTL Adapter (A) is a communication interface. Choose the SDK that supports the bus device you intend to control.

## FD Device Utility

Use FD on Windows to scan devices, change IDs or baud rates, read feedback, and edit supported parameters.

[FD device utility guide](../../../tutorials/fd-tool.md)

## Lygion Python SDK

Use the Python SDK from a computer or Linux SBC to control and read Lygion TTL products.

- [Python SDK on GitHub](https://github.com/LygionOrganization/lygion_devs_py)
- [Download the Python SDK](../../../../assets/files/lygion_devs_py.zip)

## Lygion C++ / Arduino SDK

Use the C++ SDK from ESP32, ESP32S3, Arduino Mega2560, STM32 Arduino Core, and other supported MCU platforms.

- [C++ SDK on GitHub](https://github.com/LygionOrganization/lygion_devs_cpp)
- [Download the C++ / Arduino SDK](../../../../assets/files/lygion_devs_cpp.zip)

## Compatible Feetech Devices

Use the Feetech SDK when controlling compatible STS, HLS, or SCS bus servos.

- [Feetech SDK resources on Gitee](https://gitee.com/ftservo/)

!!! tip "Compatible products can share one bus"
    Lygion products and compatible Feetech TTL bus servos can share a signal line when all IDs are unique, baud rates match, and the powered bus voltage is safe for every device.
