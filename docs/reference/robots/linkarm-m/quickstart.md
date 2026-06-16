# LinkArm-M 快速开始

本页带你从零完成 LinkArm-M 的第一次连接。请严格按照顺序操作，尤其不要跳过机身贴纸上的中位参数。

## 1. 固定并检查机械臂

1. 将机械臂可靠固定到桌面或底盘。
2. 清空机械臂和夹爪的运动范围。
3. 检查线缆没有缠绕或被关节夹住。
4. 让儿童、眼睛和易碎物品远离机械臂。

## 2. 连接电源与 USB

1. 连接 12V、至少 3A 的电源，或满足要求的 3S 锂电池。
2. 将 USB 数据线连接到 **TTL Node (A) 的 Type-C 接口**。
3. USB 另一端连接电脑、Raspberry Pi 或 Jetson。

!!! warning "确认 USB 接口"
    LinkArm-M 使用 TTL Node (A) 的 Type-C。SDK 默认波特率为 `500000`，无需改成 LinkArm-LT 使用的 `1000000`。

## 3. 获取 SDK

=== "Windows"

    ```powershell
    git clone https://github.com/LygionOrganization/linkarm_python_sdk.git
    cd linkarm_python_sdk
    python -m venv venv
    .\venv\Scripts\activate
    python -m pip install -r requirements.txt
    ```

    没有 Git 时，可从 GitHub 下载 ZIP 并解压，然后在解压目录中打开 PowerShell。

=== "macOS"

    ```bash
    git clone https://github.com/LygionOrganization/linkarm_python_sdk.git
    cd linkarm_python_sdk
    python3 -m venv venv
    source venv/bin/activate
    python3 -m pip install -r requirements.txt
    ```

=== "Linux / Raspberry Pi / Jetson"

    ```bash
    git clone https://github.com/LygionOrganization/linkarm_python_sdk.git
    cd linkarm_python_sdk
    python3 -m venv venv
    source venv/bin/activate
    python3 -m pip install -r requirements.txt
    ```

建议使用 Python 3.8 或更高版本。

## 4. 查找串口

=== "Windows"

    打开“设备管理器 → 端口（COM 和 LPT）”，查找类似：

    ```text
    USB-Enhanced-SERIAL CH343 (COM7)
    ```

    也可以运行：

    ```powershell
    python -m serial.tools.list_ports
    ```

=== "macOS"

    ```bash
    python3 -m serial.tools.list_ports
    ls /dev/cu.usbserial* /dev/cu.wchusbserial*
    ```

    以系统实际出现的设备名为准。

=== "Linux / Raspberry Pi / Jetson"

    ```bash
    python3 -m serial.tools.list_ports
    ls /dev/ttyUSB* /dev/ttyACM*
    dmesg | tail
    ```

详细方法见：[查找串口设备](../../../tutorials/find-serial-port.md)。

## 5. 修改 arm_config.json

打开 `arm_config.json`，至少确认以下三项：

```json
{
  "linkarm": {
    "default_device_serial_ports": "COM7",
    "serial_baudrate": 500000,
    "servo_middle": [513, 508, 327, 632]
  }
}
```

- 串口改为你刚查到的实际端口。
- LinkArm-M 波特率保持 `500000`。
- `servo_middle` 必须使用当前机械臂机身贴纸上的四个数字，示例数字不能照抄。

[查看完整配置与校准说明](configuration-and-calibration.md){ .md-button }

## 6. 先做只读测试

=== "Windows"

    ```powershell
    python linkarm.py status
    ```

=== "macOS"

    ```bash
    python3 linkarm.py status
    ```

=== "Linux / Raspberry Pi / Jetson"

    ```bash
    python3 linkarm.py status
    ```

确认没有串口错误后，再进行动作测试。

## 7. 安全动作测试

!!! danger "第一条动作指令也可能使整机回到初始姿态"
    即使只控制夹爪，机械臂也可能快速移动到初始位置。再次确认中位值、固定状态和工作空间。

依次测试：

=== "Windows"

    ```powershell
    python linkarm.py gripper -1
    python linkarm.py gripper 0
    python linkarm.py joint 3 -1 --reliable
    ```

=== "macOS"

    ```bash
    python3 linkarm.py gripper -1
    python3 linkarm.py gripper 0
    python3 linkarm.py joint 3 -1 --reliable
    ```

=== "Linux / Raspberry Pi / Jetson"

    ```bash
    python3 linkarm.py gripper -1
    python3 linkarm.py gripper 0
    python3 linkarm.py joint 3 -1 --reliable
    ```

确认关节与夹爪方向正确后，再按照 [CLI 命令控制](cli-control.md) 中的说明测试 IK。LinkArm-M 的笛卡尔坐标单位统一为毫米（mm）。

## 下一步

- [了解全部 CLI 命令](cli-control.md)
- [编写 Python 控制程序](python-sdk.md)
- [控制 LED、PWM 和扭矩](peripherals-and-maintenance.md)
