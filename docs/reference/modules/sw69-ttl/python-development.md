# SW69-TTL Python 程序开发

本页以单个 SW69-TTL 舵轮模组为例，说明如何使用 Python 示例完成转向关节开机同步、角度控制和行走轮速度控制。

开始前请先完成 [快速上手与 FD 配置](quickstart.md)，确保编码器、转向电机驱动器和行走电机驱动器已经具有唯一 ID。

## 示例文件结构

按照以下结构来建立 Python 示例目录：

```text
sw69-python-demo/
├─ sw69_example.py
└─ lygion_devs_py/
   └─ lydevs_sdk/
```

其中：

| 文件或目录 | 说明 |
| --- | --- |
| `sw69_example.py` | [SW69-TTL 示例程序](assets/sw69_example.py) |
| `lygion_devs_py` | Python SDK，可以从 [GitHub 克隆](https://github.com/LygionOrganization/lygion_devs_py)，也可以从[本站下载](../../../assets/files/lygion_devs_py.zip) |

## 创建 Python 环境

进入你建立的示例目录后，按当前系统执行对应命令。

=== "Linux"

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install --upgrade pip
    python3 -m pip install pyserial
    ```

=== "macOS"

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install --upgrade pip
    python3 -m pip install pyserial
    ```

=== "Windows"

    ```powershell
    py -3 -m venv .venv
    .\.venv\Scripts\Activate.ps1
    python -m pip install --upgrade pip
    python -m pip install pyserial
    ```

如果不熟悉 Python 环境配置，请先阅读 [快速上手（Python）](../../../quickstart/python-first-demo.md)。

## 修改串口号和设备 ID

打开 `sw69_example.py`，根据实际配置修改以下内容：

```python
ENCODER_ID = 10
TURNING_ID = 11
WALKING_ID = 12
portHandler = PortHandler('COM18')
```

常见串口名称示例：

| 系统 | 串口名称示例 |
| --- | --- |
| Windows | `COM3`、`COM18` |
| Linux | `/dev/ttyUSB0`、`/dev/ttyACM0` |
| macOS | `/dev/cu.usbserial-xxxx` |

## 控制逻辑说明

示例程序包含 3 个核心控制过程。

### 开机同步

转向电机是开环步进系统，驱动器本身不知道机械关节的绝对朝向。示例中的 `joint_init()` 会读取 TTL Encoder E02 的绝对位置，并调用 `set_position()` 将转向电机驱动器的当前位置同步到相同角度。

```python
joint_init(ENCODER_ID, TURNING_ID)
```

完成同步后，程序才能可靠地使用角度命令控制转向关节。

示例会先计算编码器读数相对机械中位的偏移量，再将该偏移量换算为转向电机驱动器的位置值：

```text
编码器相对中位差值 = 编码器读数 - ENCODER_CENTER
同步位置 = JOINT_MID + 编码器相对中位差值 × ENCODER2STEPS
目标位置 = 目标弧度 × RAD2STEPS + STEERING_ZERO
```

!!! note "编码器中位"
    FD 中位校准后，转向机械中位通常对应编码器读数 `2047` 或 `2048`，示例中使用 `ENCODER_CENTER = 2048`。如果实测中位读数不同，请按实际读数修改该常量。

### 转向角度控制

`joint_deg_ctrl()` 使用角度值控制转向关节。示例中，`0°` 对应 FD 中校准过的机械中位，正负角度分别表示中位两侧的转向偏移。

```python
joint_deg_ctrl(TURNING_ID, 45, 400, 15, 200)
joint_deg_ctrl(TURNING_ID, -45, 400, 15, 200)
```

### 行走轮速度控制

行走电机驱动器应配置为速度模式。示例中的 `walking_motor_ctrl()` 调用速度模式接口控制车轮正转、反转和停止。

```python
walking_motor_ctrl(WALKING_ID, 50, 15, 200)
walking_motor_ctrl(WALKING_ID, 0, 15, 200)
walking_motor_ctrl(WALKING_ID, -50, 15, 200)
```

如果已经配置心跳保护，程序应周期性发送速度指令。否则在超时后，行走电机会自动停止。

## 参数建议

| 参数 | 示例值 | 说明 |
| --- | ---: | --- |
| `speed` | `400` 或以下 | 为保证电机稳定运行，建议不超过 `400` |
| `acc` | `15` | 加速度参数，`0` 表示最高加速度，不建议用于常规调试 |
| `current` | `200` | 相电流约 `1.32 A`，兼顾扭矩和发热 |

相电流估算：

```text
相电流(A) ≈ 3.3 × 2 × (current / 1000)
```

## 运行示例

确认舵轮模组接线和外部电源正常后，在示例目录中执行：

=== "Linux"

    ```bash
    python3 sw69_example.py
    ```

=== "macOS"

    ```bash
    python3 sw69_example.py
    ```

=== "Windows"

    ```powershell
    python .\sw69_example.py
    ```

示例将依次执行：

1. 读取编码器并同步转向电机当前位置。
2. 转向到 `0°`。
3. 转向到 `45°`。
4. 转向到 `-45°`。
5. 回到 `0°`。
6. 行走轮低速正转、停止、低速反转、停止。

!!! warning "运行前抬起行走轮"
    第一次运行示例时，请将行走轮抬离桌面或地面，避免轮体转动带动模组移动。

## 示例源码

```python
--8<-- "docs/reference/modules/sw69-ttl/assets/sw69_example.py"
```
