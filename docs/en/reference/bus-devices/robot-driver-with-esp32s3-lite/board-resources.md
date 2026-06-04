# Board Resources and Power

The controller combines an ESP32-S3-N8R8, robot bus interfaces, network control, and common onboard user-interface devices.

## Functional Resources

| Resource | Purpose |
| --- | --- |
| ESP32-S3-N8R8 | Main controller |
| TTL and RS485 bus interfaces | Compatible bus servos and devices |
| CAN bus | Hub motors, joint actuators, and custom CAN devices |
| USB Type-C / USB CDC | Board power, firmware upload, and host JSON communication |
| Wi-Fi AP + STA | Built-in Web App, HTTP, WebSocket, and network integration |
| ESP-NOW | Direct ESP32-to-ESP32 control |
| OLED display | Shows AP IP, STA IP, MAC address, and status |
| Buzzer, RGB LEDs, joystick buttons | Local status and stored-action control |
| LittleFS storage | Stores missions and configuration |

## Power Domains

### Controller and Onboard Functions

USB Type-C powers the ESP32-S3, OLED, buzzer, joystick, Wi-Fi, and other onboard logic. Connecting USB powers these functions regardless of the peripheral power-switch position.

### Servos, Motors, and Actuators

Apply a supply through the DC jack or XT30 (2+2) connector. The peripheral power switch controls this power path.

!!! warning "Match the supply to the connected devices"
    The peripheral supply rail connects directly to the robot-control ports. It does not convert the voltage for each device. Use 12 V only with devices rated for 12 V, for example.

The rail is designed to tolerate brief high-current actuator peaks, but the external supply, wiring, and connectors must still be sized for the actual load.

## Interfaces in the Default Open-Source Firmware

The following assignments are defined by the official firmware and are useful when modifying it:

| Function | ESP32-S3 assignment |
| --- | --- |
| Bus-servo UART RX / TX | GPIO 5 / GPIO 4 |
| CAN RX / TX | GPIO 13 / GPIO 14 |
| I2C SDA / SCL | GPIO 6 / GPIO 7 |
| Buzzer | GPIO 21 |
| RGB LEDs | GPIO 26 |
| Joystick Up / Down / Left / Right / OK | GPIO 10 / 11 / 12 / 9 / 2 |

Treat these as firmware assignments, not a substitute for checking the physical connector labels before wiring.
