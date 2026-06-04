# WebSocket Wireless Communication

WebSocket provides a persistent, low-latency connection for sending JSON commands and receiving asynchronous responses and telemetry.

Connect to:

```text
ws://BOARD_IP/ws
```

The board sends a hello message after connection and broadcasts device telemetry approximately once per second.

## Python Example

Install the dependency:

```bash
python -m pip install websocket-client
```

```python
import json
import websocket

BOARD_IP = "192.168.4.1"
WS_URL = f"ws://{BOARD_IP}/ws"

def on_open(ws):
    command = {
        "T": 202,
        "line": 1,
        "text": "WebSocket",
        "update": 1,
    }
    ws.send(json.dumps(command))

def on_message(ws, message):
    print("received:", message)

def on_error(ws, error):
    print("WebSocket error:", error)

def on_close(ws, status, message):
    print("connection closed")

client = websocket.WebSocketApp(
    WS_URL,
    on_open=on_open,
    on_message=on_message,
    on_error=on_error,
    on_close=on_close,
)
client.run_forever()
```

## Telemetry

The periodic `T: 50` message includes the bus baud rate, AP IP, STA IP, MAC address, connected SSID, and uptime.

Use WebSocket for interactive control panels and applications that need immediate feedback. Add reconnect logic and stop motion safely when the connection is lost.

The official repository includes examples under `python_example/webSocket`.
