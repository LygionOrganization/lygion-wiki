# SW69-TTL C++ / Arduino 程序开发

本页提供 SW69-TTL 的 ESP32 Arduino 完整例程。例程逻辑与 [Python 程序开发](python-development.md) 中的 `sw69_example.py` 一致：读取转向编码器、同步转向电机当前位置、控制转向角度，并使用速度模式控制行走轮。

[下载 ESP32 Arduino 示例](assets/sw69_esp32_example.ino){ .md-button .md-button--primary }
[下载 C++ / Arduino SDK](../../../assets/files/lygion_devs_cpp.zip){ .md-button }

## 开发前提

开始前请确认：

- 已完成 [快速上手与 FD 配置](quickstart.md)。
- 每个 TTL 总线设备都具有唯一 ID。
- 转向电机驱动器处于位置模式。
- 行走电机驱动器已经设置为速度模式，并建议开启心跳保护。
- ESP32 与 TTL Adapter (A) 或板载 TTL 总线接口已经正确接线并共地。
- TTL 总线通信波特率为 `1000000` bps。

本页示例默认使用以下 ID：

| 设备 | ID |
| --- | ---: |
| TTL Encoder E02 | `10` |
| 转向电机驱动器 | `11` |
| 行走电机驱动器 | `12` |

如你的 ID 分配不同，请修改 `.ino` 文件顶部的常量。

## 硬件串口配置

示例默认使用 ESP32 / ESP32S3 的 `Serial1` 作为 TTL 总线通信串口：

```cpp
const int TTL_RX_PIN = 5;
const int TTL_TX_PIN = 4;

Serial1.begin(1000000, SERIAL_8N1, TTL_RX_PIN, TTL_TX_PIN);
ttlsd.pSerial = &Serial1;
```

接线方式：

| ESP32 | TTL Adapter (A) UART 口 |
| --- | --- |
| GPIO5 / RX | RX |
| GPIO4 / TX | TX |
| GND | GND |

!!! note "RX / TX 接法"
    使用 TTL Adapter (A) 的 UART 口时，通常采用 `RX 接 RX`、`TX 接 TX`、`GND 接 GND`。如果你使用的是其它 UART 转单线 TTL 电路，请以对应硬件说明为准。

!!! warning "外部供电"
    SW69-TTL 的电机不能只依赖 ESP32 或 USB 供电。请为 TTL 总线和电机驱动器接入符合规格的外部电源，并确认所有通信设备共地。

## 示例执行流程

上传后，示例会在 `setup()` 中执行一次完整测试：

1. 初始化 USB 调试串口 `Serial`，波特率为 `115200`。
2. 初始化 TTL 总线串口 `Serial1`，波特率为 `1000000`。
3. 读取编码器当前位置。
4. 将编码器读数换算为转向电机驱动器位置值。
5. 调用 `CalibrationOfs()` 同步转向电机当前位置。
6. 控制转向关节依次转到 `0°`、`+45°`、`-45°`、`0°`。
7. 控制行走轮低速正转、停止、低速反转、停止。
8. 在 `loop()` 中持续发送停止指令，避免行走轮继续运动。

第一次运行前，请将行走轮抬离桌面或地面。

## Python 与 Arduino 接口对应关系

| 功能 | Python 示例 | Arduino 示例 |
| --- | --- | --- |
| 读取编码器位置 | `ReadPosSpeed(id)` | `ReadPos(id)`、`ReadSpeed(id)` |
| 同步转向电机当前位置 | `reOfsCal(id, position)` | `CalibrationOfs(id, position)` |
| 转向位置控制 | `WritePosEx(id, position, speed, acc, current)` | `WritePosEx(id, position, speed, acc, current)` |
| 行走速度控制 | `WriteSpec(id, speed, acc, current)` | `WriteSpe(id, speed, acc, current)` |

## 角度换算

示例使用与 Python 例程相同的换算关系：

```text
总减速比 = (72 / 20) × 5.181818182
编码器单圈计数 = 4096
编码器中位 = 2048
步进电机单圈微步数 = 3200
转向中位 = 步进电机单圈微步数 × 总减速比 / 2
转向 0° 目标位置 = STEERING_ZERO
弧度转步数系数 = 步进电机单圈微步数 × 总减速比 / 2π
编码器转步数系数 = 转向关节总步数 / 编码器单圈计数
```

目标角度换算为电机目标位置：

```text
编码器相对中位差值 = 编码器读数 - 编码器中位
开机同步位置 = 转向中位 + 编码器相对中位差值 × 编码器转步数系数
目标位置 = 目标弧度 × 弧度转步数系数 + STEERING_ZERO
```

示例中会将计算结果限制在 `0` 到 `65534` 的驱动器位置范围内。FD 中位校准后，转向机械中位通常对应编码器读数 `2047` 或 `2048`；如果你的设备在机械中位读到的是其它值，请修改 `.ino` 中的 `ENCODER_CENTER`。

## 参数建议

| 参数 | 示例值 | 说明 |
| --- | ---: | --- |
| 转向速度 | `400` | 建议不超过 `400` |
| 转向加速度 | `15` | 不建议常规调试中使用 `0` |
| 行走速度 | `50` / `-50` | 首次测试使用低速 |
| 行走加速度 | `15` | 与 Python 示例保持一致 |
| 电流参数 | `200` | 相电流约 `1.32 A` |
| 行走指令周期 | `100 ms` | 周期发送速度指令，配合心跳保护 |

相电流估算：

```text
相电流(A) ≈ 3.3 × 2 × (电流参数 / 1000)
```

## 上传与运行

### Arduino IDE

1. 安装 ESP32 开发板支持包。
2. 安装或复制 `lygion_devs_cpp` 到 Arduino `libraries` 目录。
3. 打开 `sw69_esp32_example.ino`。
4. 根据实际接线修改 `TTL_RX_PIN` 和 `TTL_TX_PIN`。
5. 选择 ESP32 或 ESP32S3 开发板。
6. 上传程序。
7. 打开串口监视器，并将波特率设置为 `115200`。

### PlatformIO

将 `sw69_esp32_example.ino` 放入工程 `src` 目录，或改名为 `main.cpp` 后使用。示例配置：

```ini
[env:esp32-s3-devkitc-1]
platform = espressif32
board = esp32-s3-devkitc-1
framework = arduino
monitor_speed = 115200
```

## 示例源码

```cpp
--8<-- "docs/reference/modules/sw69-ttl/assets/sw69_esp32_example.ino"
```

## 常见问题

| 现象 | 可能原因 | 处理方式 |
| --- | --- | --- |
| 串口监视器没有输出 | 调试串口波特率不正确；程序未运行 | 设置串口监视器为 `115200`，按下复位键 |
| 读取编码器失败 | 编码器 ID、波特率、接线或供电错误 | 检查 `ENCODER_ID`、`1000000` 波特率、RX/TX/GND 和外部供电 |
| 转向角度不正确 | 编码器中位未校准；上电后未同步成功 | 重新执行 FD 中位校准，并确认 `jointInit()` 成功 |
| 行走轮不转 | 行走驱动器未设置为速度模式；电流或供电不足 | 按快速上手页面设置运行模式 `1`，检查外部电源 |
| 行走轮转一下就停 | 心跳保护生效但程序未周期发送速度 | 保留 `driveWheelFor()` 中的周期发送逻辑 |

## 参考资料

- [Python 程序开发](python-development.md)
- [快速上手（C++ / Arduino）](../../../quickstart/cpp-first-demo.md)
- [TTL Stepper Driver (A)：C++ / Arduino](../../bus-devices/ttl-stepper-driver-a/cpp-arduino.md)
- [TTL Encoder E02：C++ / Arduino](../../bus-devices/ttl-encoder-e02/cpp-arduino.md)
- [上传 Arduino 示例程序](../../../tutorials/upload-arduino-sketch.md)
