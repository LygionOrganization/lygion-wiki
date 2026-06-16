# LinkArm-LT JSON Command Reference

Send one JSON object per line through the web JSON panel, USB CDC, HTTP, WebSocket, or a mission file.

!!! warning "Start from a safe pose and low speed"
    Validate commands individually before adding them to automation.

The firmware provides commands for:

- joint angles and joint radians
- fast and smooth Cartesian motion
- fast and smooth FPV motion
- feedback and continuous control
- individual servo access
- delays, TTL Node RGB LEDs, OLED text, and buzzer
- Wi-Fi and ESP-NOW configuration
- restart, reset, and filesystem operations
- mission creation, editing, execution, and deletion

Use the examples in the firmware repository and the web console as the authoritative schema for the installed firmware version.

## Mission Files { #mission-files }

Mission commands create a file, append or insert a step, replace or delete a step, run one step, run the complete mission, or delete the mission.

!!! danger "Formatting storage deletes saved data"
    Back up missions and calibration/configuration files before using reset or format commands.

