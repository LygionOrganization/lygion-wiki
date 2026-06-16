# 上位机通信

USB CDC、HTTP 和 WebSocket 都使用相同的 JSON 指令。选择通信方式时，主要考虑是否需要无线、实时性和双向推送。

## 方式对比

| 方式 | 地址或端口 | 特点 | 推荐用途 |
| --- | --- | --- | --- |
| USB CDC | 系统虚拟串口 | 有线、高速、稳定 | 高频控制、调试、机器人大小脑架构 |
| HTTP | `http://设备IP/api/cmd` | 简单请求-响应 | 配置、低频控制、云端接口原型 |
| WebSocket | `ws://设备IP:80/ws` | 长连接、双向、低延迟 | 实时控制、状态主动上报 |

## 获取示例项目

- [GitHub 项目](https://github.com/EffectsMachine/robot_driver_with_esp32s3_lite)

=== "Windows"

    1. 在 GitHub 项目页面点击 `Code` → `Download ZIP`。
    2. 解压后进入 `Example for Robot Driver Lite/python_example`。
    3. 在目标示例文件夹空白处右键，选择“在终端中打开”。

=== "macOS"

    ```bash
    git clone https://github.com/EffectsMachine/robot_driver_with_esp32s3_lite.git
    cd robot_driver_with_esp32s3_lite
    ```

=== "Linux"

    ```bash
    sudo apt update
    sudo apt install git
    git clone https://github.com/EffectsMachine/robot_driver_with_esp32s3_lite.git
    cd robot_driver_with_esp32s3_lite
    ```

## 创建 Python 环境

在所选示例目录内执行：

=== "Windows"

    ```powershell
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    pip install -r requirements.txt
    ```

    如果 PowerShell 阻止激活脚本，可以改用 CMD：

    ```bat
    venv\Scripts\activate.bat
    ```

=== "macOS"

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

=== "Linux"

    ```bash
    sudo apt install python3 python3-pip python3-venv
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

## USB CDC

### 连接正确接口

使用数据线连接驱动板中间标有 `USB` 的原生 USB 接口，不是 `UART` 接口。

### 查找端口

=== "Windows"

    打开“设备管理器 → 端口（COM 和 LPT）”，查找 Espressif ESP32-S3 或新出现的 COM 端口，例如 `COM11`。

=== "macOS"

    ```bash
    ls /dev/tty.usbmodem* /dev/cu.usbmodem*
    ```

=== "Linux"

    ```bash
    ls /dev/ttyACM* /dev/ttyUSB*
    ```

### 终端测试

=== "Windows"

    可以使用支持 DTR 的串口终端。选择 ESP32-S3 对应端口并启用 `DTR on`。USB CDC 不依赖所选波特率。

=== "macOS"

    ```bash
    screen /dev/cu.usbmodem12345 115200
    ```

    退出：按 `Ctrl+A`，再按 `K`，输入 `y`。

=== "Linux"

    ```bash
    screen /dev/ttyACM0 115200
    ```

    `115200` 只是 `screen` 要求的占位参数，USB CDC 实际不使用 UART 波特率。

发送：

```json
{"T":204,"l1":"Hello!","l2":"world!","l3":"Hello!","l4":"world!"}
```

OLED 显示对应文字即表示通信成功。运行 Python 前，应关闭占用端口的串口终端。

### Python 示例

进入 `python_example/usb_cdc`，将 `PORT` 改为实际端口：

```python
import json
import serial
import time

PORT = "COM11"  # Linux: /dev/ttyACM0; macOS: /dev/cu.usbmodem...
BAUD = 1_000_000  # USB CDC 模式下只是占位值

with serial.Serial(PORT, BAUD, timeout=0.5) as ser:
    time.sleep(2)
    command = {"T": 202, "line": 1, "text": "Hello, world!", "update": 1}
    ser.write((json.dumps(command) + "\n").encode("utf-8"))
```

运行：

=== "Windows"

    ```powershell
    python .\usb_cdc_example.py
    ```

=== "macOS"

    ```bash
    python3 usb_cdc_example.py
    ```

=== "Linux"

    ```bash
    python3 usb_cdc_example.py
    ```

## HTTP

驱动板 HTTP 服务默认使用端口 `80`，指令接口为：

```text
http://<设备 IP>/api/cmd
```

- 电脑直连驱动板热点：设备 IP 为 `192.168.4.1`。
- 同一路由器 STA 模式：使用 OLED 显示的 IP。

```python
import requests

esp32_ip = "192.168.4.1"
url = f"http://{esp32_ip}/api/cmd"
command = {"T": 202, "line": 1, "text": "HTTP test", "update": 1}

response = requests.post(url, json=command, timeout=2)
response.raise_for_status()
print(response.text)
```

进入 `python_example/http` 后运行：

=== "Windows"

    ```powershell
    python .\http_example.py
    ```

=== "macOS"

    ```bash
    python3 http_example.py
    ```

=== "Linux"

    ```bash
    python3 http_example.py
    ```

## WebSocket

WebSocket 与 HTTP 共用端口 `80`，路径固定为 `/ws`：

```text
ws://<设备 IP>:80/ws
```

```python
import json
import websocket

esp32_ip = "192.168.4.1"
ws_url = f"ws://{esp32_ip}:80/ws"

def on_open(ws):
    command = {"T": 202, "line": 1, "text": "WebSocket test", "update": 1}
    ws.send(json.dumps(command))

def on_message(ws, message):
    print(f"recv: {message}")

ws = websocket.WebSocketApp(
    ws_url,
    on_open=on_open,
    on_message=on_message,
)
ws.run_forever()
```

进入 `python_example/webSocket` 后运行：

=== "Windows"

    ```powershell
    python .\webSocket_example.py
    ```

=== "macOS"

    ```bash
    python3 webSocket_example.py
    ```

=== "Linux"

    ```bash
    python3 webSocket_example.py
    ```

!!! tip "生产程序应增加自动重连"
    WebSocket 是长连接。网络波动或驱动板重启后，上位机应捕获断开事件并重新连接。

## 常见问题

| 现象 | 检查 |
| --- | --- |
| USB 端口不存在 | 数据线、USB/UART 接口是否接错、设备管理器或 `/dev` 是否更新 |
| 串口被占用 | 关闭 YAT、screen、串口监视器或其他 Python 进程 |
| HTTP `ConnectionError` | IP、Wi-Fi、端口和防火墙 |
| HTTP 404 | URL 必须是 `/api/cmd`，并确认固件支持 HTTP |
| WebSocket `connection refused` | 地址应为 `ws://IP:80/ws` |
| `ModuleNotFoundError: websocket` | 安装 `websocket-client` |

更多问题见[故障排查](faq.md)。
