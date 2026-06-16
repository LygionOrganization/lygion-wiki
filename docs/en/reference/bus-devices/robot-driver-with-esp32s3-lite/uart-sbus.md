# UART Passthrough and S.BUS

UART0 on the HAT header can operate as a TTL-bus passthrough, a JSON command channel, or an S.BUS input when the corresponding firmware option is enabled.

## FD Passthrough

Passthrough lets a host use FD or another serial-bus tool through the controller. Distinguish the host UART baud rate from the actuator-bus baud rate; they describe different links.

## UART JSON

Send one newline-terminated JSON command at a time. Share ground and verify the host logic voltage before wiring TX and RX.

## S.BUS

S.BUS mode requires compatible firmware, correct signal inversion/level handling, and explicit channel-to-action mapping.

!!! warning "Implement failsafe behavior first"
    Define what happens on receiver timeout, invalid frames, or out-of-range channels before enabling actuator motion.

