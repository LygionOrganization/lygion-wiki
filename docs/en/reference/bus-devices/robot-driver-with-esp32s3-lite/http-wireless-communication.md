# HTTP Wireless Communication

The built-in HTTP API accepts JSON commands from any host on the same Wi-Fi network.

## Endpoints

| Method and path | Purpose |
| --- | --- |
| `GET /` | Open the Web App |
| `GET /api/info` | Read basic ESP32-S3 information |
| `POST /api/cmd` | Queue one JSON command |

Use `192.168.4.1` while connected to the board's default hotspot, or use the STA IP shown on the OLED after joining an existing network.

## Python Example

Install the dependency:

```bash
python -m pip install requests
```

Send a command:

```python
import requests

ESP32_IP = "192.168.4.1"
url = f"http://{ESP32_IP}/api/cmd"

command = {
    "T": 202,
    "line": 1,
    "text": "HTTP command",
    "update": 1,
}

response = requests.post(url, json=command, timeout=2)
print(response.status_code, response.text)
```

The command endpoint acknowledges a queued command with an HTTP response. Use WebSocket or USB CDC when your application also needs asynchronous feedback.

## Browser or `curl` Test

```bash
curl -X POST http://192.168.4.1/api/cmd ^
  -H "Content-Type: application/json" ^
  -d "{\"T\":202,\"line\":1,\"text\":\"HTTP\",\"update\":1}"
```

Adapt line continuation and quoting for your shell.

## Troubleshooting

- Confirm the host and board are on the same network.
- Use the AP IP `192.168.4.1` only while connected directly to the board's hotspot.
- Check the OLED for the current STA IP.
- Use a short timeout and handle Wi-Fi disconnects in production code.

The official repository includes examples under `python_example/http`.
