# 高级用户路径

本页适合已经熟悉串口通信、Python、虚拟环境和硬件供电的用户。

## 最短流程

```text
连接硬件 → 找串口 → clone SDK → 改 port / ID / baudrate → 运行 ping/read → 进入产品功能页
```

## 命令模板

=== "Linux"

    ```bash
    git clone https://github.com/LygionRobotics/lygion_devs_py.git
    cd lygion_devs_py
    python3 -m venv .venv
    source .venv/bin/activate
    ls /dev/ttyUSB* /dev/ttyACM* 2>/dev/null
    python3 ttlsd_ping.py
    ```

=== "MacOS"

    ```bash
    git clone https://github.com/LygionRobotics/lygion_devs_py.git
    cd lygion_devs_py
    python3 -m venv .venv
    source .venv/bin/activate
    ls /dev/tty.usb* /dev/cu.usb* 2>/dev/null
    python3 ttlsd_ping.py
    ```

=== "Windows"

    ```powershell
    git clone https://github.com/LygionRobotics/lygion_devs_py.git
    cd lygion_devs_py
    py -3 -m venv .venv
    .\.venv\Scripts\Activate.ps1
    python .\ttlsd_ping.py
    ```

## 需要修改的三个位置

大多数脚本只需要先确认这三个参数：

```python
portHandler = PortHandler('/dev/ttyUSB0')
packetHandler = TTLSDClass(portHandler)
portHandler.setBaudRate(1000000)
```

以及具体读写函数中的设备 ID：

```python
packetHandler.ReadPosSpeed(1)
packetHandler.WritePosEx(1, 3200, 200, 10, 150)
```

## 产品功能入口

- [TTL Encoder E02 Python 读取](../reference/bus-devices/ttl-encoder-e02/python-quickstart.md)
- [TTL Encoder E02 C++ / Arduino](../reference/bus-devices/ttl-encoder-e02/cpp-arduino.md)
- [TTL Stepper Driver (A) Python 控制](../reference/bus-devices/ttl-stepper-driver-a/python-quickstart.md)
- [TTL Stepper Driver (A) 运行模式](../reference/bus-devices/ttl-stepper-driver-a/operating-modes.md)
- [TTL Stepper Driver (A) 参数说明](../reference/bus-devices/ttl-stepper-driver-a/parameters.md)

!!! tip "调试顺序"
    单设备通信稳定后，再接入多个设备；同步读写前先确认每个设备的 ID、波特率和供电都正常。
