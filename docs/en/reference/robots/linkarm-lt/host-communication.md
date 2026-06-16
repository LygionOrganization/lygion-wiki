# LinkArm-LT Host Communication

LinkArm-LT accepts newline-delimited JSON through USB CDC, HTTP, and WebSocket.

| Method | Typical use |
| --- | --- |
| USB CDC | Reliable high-rate wired control |
| HTTP | Simple requests and configuration |
| WebSocket | Bidirectional low-latency wireless control |

For USB, connect the controller's data USB port, locate the serial device, and send one command per line.

For HTTP:

```text
http://<device-ip>/api/cmd
```

For WebSocket:

```text
ws://<device-ip>:80/ws
```

Clients should validate responses, serialize motion commands, use timeouts, reconnect safely, and expose an emergency-stop path. See [JSON Command Reference](json-commands.md).

