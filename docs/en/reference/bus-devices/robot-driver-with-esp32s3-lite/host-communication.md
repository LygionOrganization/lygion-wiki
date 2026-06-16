# Host Communication

The controller accepts newline-delimited JSON commands through USB CDC, HTTP, and WebSocket.

| Method | Best for |
| --- | --- |
| USB CDC | Stable, high-rate wired control and logs |
| HTTP | Configuration and low-frequency requests |
| WebSocket | Low-latency bidirectional wireless control |

Clone the firmware repository for current host examples:

```bash
git clone https://github.com/EffectsMachine/robot_driver_with_esp32s3_lite.git
```

## USB CDC

Connect the native USB port, locate the serial device, open it at the firmware's configured rate, and send one JSON object per line.

## HTTP

Send commands to:

```text
http://<device-ip>/api/cmd
```

## WebSocket

Connect to:

```text
ws://<device-ip>:80/ws
```

Production clients should implement timeouts, response validation, reconnection, command serialization, and an emergency-stop path.

See [JSON Command Interface](json-command-interaction.md) for supported payloads.

