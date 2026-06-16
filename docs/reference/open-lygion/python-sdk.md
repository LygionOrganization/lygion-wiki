# Python SDK

Lygion Python SDK 用于在 Windows、Linux、macOS、Raspberry Pi、Jetson 等上位机环境中访问 Lygion TTL 总线设备。代码仓库和示例以 GitHub 为准：

- [Lygion Python SDK 仓库](https://github.com/LygionOrganization/lygion_devs_py)
- [本站下载 Python SDK](../../assets/files/lygion_devs_py.zip)

## 获取 SDK

推荐使用 Git 获取最新版：

```bash
git clone https://github.com/LygionOrganization/lygion_devs_py.git
cd lygion_devs_py
```

如果无法访问 GitHub，可以下载本站压缩包后解压到一个容易找到的位置。

[下载 Python SDK](../../assets/files/lygion_devs_py.zip){ .md-button }

## 准备环境

Python SDK 通常需要 Python 3 和串口通信依赖。第一次使用可以参考这些基础教程：

- [安装 Python](../../tutorials/install-python.md)
- [查找串口设备](../../tutorials/find-serial-port.md)
- [运行 Python 脚本](../../tutorials/run-python-scripts.md)
- [设备 ID 与波特率](../../tutorials/device-id-and-baudrate.md)
- [供电与接线基础](../../tutorials/power-and-wiring-basics.md)

在 SDK 目录中创建虚拟环境并安装依赖：

=== "Windows"

    ```powershell
    py -3 -m venv .venv
    .\.venv\Scripts\Activate.ps1
    python -m pip install --upgrade pip
    python -m pip install pyserial
    ```

=== "macOS / Linux"

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install --upgrade pip
    python3 -m pip install pyserial
    ```

## 示例入口

SDK 仓库内按设备类型组织示例。运行前请先修改示例中的串口名、设备 ID 和波特率。

| 设备 / 功能 | 示例入口 |
| --- | --- |
| TTL Node (A) | [`lynode`](https://github.com/LygionOrganization/lygion_devs_py/tree/main/lynode) |
| TTL Stepper Driver (A) | `lyttlsd` 相关示例 |
| TTL Encoder E02 | 编码器读取与参数配置示例 |
| 设备参数配置 | `*_eprom.py` 示例 |

!!! warning "先读后写"
    第一次调试时，优先运行读取反馈或扫描类示例。确认串口、ID、波特率和供电都正确后，再运行会驱动电机或改变设备参数的示例。

## 常见调试流程

1. 只连接一个新设备，避免默认 ID 冲突。
2. 用 FD 调试软件或 SDK 读取设备反馈。
3. 确认设备 ID 和波特率。
4. 根据项目需要修改示例中的串口名和设备 ID。
5. 小幅度、低速度测试运动或输出控制。

相关工具：

- [FD 调试软件教程](../../tutorials/fd-tool.md)
- [TTL Adapter (A) SDK 与工具](../bus-devices/ttl-adapter-a/sdk-and-tools.md)
- [TTL Node (A) SDK 与工具](../bus-devices/ttl-node-a/sdk-and-tools.md)
