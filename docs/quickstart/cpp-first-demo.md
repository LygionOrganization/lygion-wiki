# MCU C++ 路线：跑通第一个 Demo

本页适合使用 ESP32S3、ESP32、STM32、Arduino Mega2560 等 MCU 的用户。目标是让 MCU 通过硬件串口与 Lygion TTL 总线设备通信，并在串口监视器中看到设备反馈。

推荐第一次测试使用：

```text
PC
 │ USB
 ▼
MCU Development Board
 │ UART RX / TX / GND
 ▼
TTL Adapter (A) UART Port
 │ TTL Bus
 ▼
TTL Encoder E02 或 TTL Stepper Driver (A)
```

也可以使用你自己设计的 UART 转单线 TTL 电路：

```text
MCU UART
    │
    ▼
UART 转单线 TTL 电路
    │
    ▼
TTL Bus Device
```

!!! tip "第一次测试推荐 TTL Encoder E02"
    TTL Encoder E02 只需要读取位置和速度，不会突然带动机械结构运动，更适合作为 MCU C++ 路线的第一个 Demo。

## 1. 确认你属于 MCU C++ 用户

如果你的主控是以下设备，建议阅读本页：

- ESP32S3
- ESP32
- STM32
- Arduino Mega2560
- Arduino Due
- 其它带硬件 UART 的 MCU 控制板

如果你的主控是电脑、Raspberry Pi、Jetson、RK、N100 小主机等，请使用：[Python 路线：跑通第一个 Demo](python-first-demo.md)。

## 2. 准备硬件

你需要准备：

- 一个 MCU 开发板，例如 ESP32S3、ESP32、STM32 或 Arduino Mega2560
- TTL Adapter (A)，或其它 UART 转单线 TTL 电路
- 一个 TTL 总线设备，例如 TTL Encoder E02 或 TTL Stepper Driver (A)
- USB 数据线，用于连接电脑和 MCU
- 合适电压的外部电源
- 若需要插线连接，准备杜邦线或对应端子线

!!! warning "TTL Adapter (A) 的 UART 电平为 3.3V"
    如果你的 MCU 是 5V IO，请确认它的 UART 输入是否兼容 3.3V 电平。必要时需要增加电平转换电路。

## 3. 安装开发工具

你可以选择 Arduino IDE 或 VS Code + PlatformIO。

| 工具 | 适合用户 | 推荐程度 |
| --- | --- | --- |
| Arduino IDE | 第一次使用 MCU、希望界面简单 | 新手推荐 |
| PlatformIO | 已经使用 VS Code、希望管理多个工程 | 工程项目推荐 |

### 方式 A：Arduino IDE

请先安装 Arduino IDE：

- [安装 Arduino IDE](../tutorials/install-arduino-ide.md)

安装后需要：

1. 添加对应开发板支持包，例如 ESP32 或 STM32。
2. 选择正确的开发板型号。
3. 选择正确的上传端口。
4. 安装或导入 Lygion C++ SDK。

### 方式 B：PlatformIO

如果你使用 VS Code：

- [安装 PlatformIO](../tutorials/install-platformio.md)

PlatformIO 更适合后续维护机器人项目，但第一次配置会比 Arduino IDE 多一些步骤。

## 4. 打开串口监视器前，先理解两个“串口”

MCU C++ 路线经常会同时涉及两个串口：

| 串口 | 用途 | 常见写法 |
| --- | --- | --- |
| USB 调试串口 | MCU 向电脑打印调试信息 | `Serial` |
| TTL 总线通信串口 | MCU 与 TTL 总线设备通信 | `Serial1` / `Serial2` |

例如 ESP32S3 示例中：

```cpp
Serial.begin(115200);                         // 打印调试信息到电脑
Serial1.begin(1000000, SERIAL_8N1, 18, 17);   // 与 TTL 总线设备通信
```

其中：

```text
115200：电脑串口监视器波特率
1000000：TTL 总线设备波特率，默认 1 Mbps
18：ESP32S3 RX 引脚
17：ESP32S3 TX 引脚
```

!!! warning "不要混淆两个波特率"
    `Serial.begin(115200)` 是电脑串口监视器的波特率。

    `Serial1.begin(1000000, ...)` 是 TTL 总线通信波特率，需要与设备波特率一致。

## 5. 硬件接线

### 5.1 MCU 连接 TTL Adapter (A)

当 TTL Adapter (A) 作为 UART 转单线 TTL 总线转接板使用时，常见接法如下：

| MCU | TTL Adapter (A) |
| --- | --- |
| RX | RX |
| TX | TX |
| GND | GND |

!!! note "为什么不是 RX 接 TX？"
    TTL Adapter (A) 的 UART 口是接入其板载转换电路的输入侧，实际使用中通常采用 `RX 接 RX`、`TX 接 TX` 的方式。它和普通 USB-TTL 模块的交叉接法不同。

更详细说明见：[MCU UART 接线基础](../tutorials/mcu-uart-wiring.md)。

### 5.2 TTL Adapter (A) 连接总线设备

```text
TTL Adapter (A)
        │ 5264-3P / HC-1.25-3P TTL Bus
        ▼
TTL Bus Device
```

请确认：

- `+ / - / S` 没有接反。
- 执行器类设备已经接入外部电源。
- 第一次测试只连接一个新设备。

## 6. 获取 C++ SDK

C++ SDK：

```text
https://github.com/LygionRobotics/lygion_devs_cpp
```

如果无法访问 GitHub，可以从下载中心下载压缩包：

- [C++ SDK 下载](../downloads/index.md#c-sdk)

Arduino IDE 用户通常需要把库文件放到：

```text
Documents/Arduino/libraries
```

复制后重启 Arduino IDE。

## 7. 打开第一个示例

对于 TTL Encoder E02，建议先使用读取反馈类示例，例如：

```text
example/lyttlsd/FeedBack.ino
```

对于 TTL Stepper Driver (A)，第一次也建议先使用读取或反馈类示例，确认通信后再运行运动控制示例。

!!! warning "先读后写"
    第一次使用时，不建议直接运行高速运动示例。请先确认可以读取位置、速度、电压或温度等反馈数据。

## 8. 修改串口初始化代码

### ESP32S3 示例

```cpp
Serial.begin(115200);
Serial1.begin(1000000, SERIAL_8N1, 18, 17);
ttlsd.pSerial = &Serial1;
```

根据你的硬件连接修改 RX / TX 引脚：

```text
18：MCU RX，引脚应连接到 TTL Adapter (A) RX
17：MCU TX，引脚应连接到 TTL Adapter (A) TX
```

### Arduino Mega2560 示例

```cpp
Serial.begin(115200);
Serial1.begin(1000000);
ttlsd.pSerial = &Serial1;
```

Mega2560 的 `Serial1` 硬件串口引脚通常是：

```text
RX1 = 19
TX1 = 18
```

### STM32 示例

STM32 Arduino Core 的串口名称可能因开发板而不同，常见为：

```cpp
Serial1.begin(1000000);
ttlsd.pSerial = &Serial1;
```

如果编译失败，请先确认当前开发板支持的硬件串口名称。

## 9. 上传程序

### Arduino IDE

1. 打开 `.ino` 示例。
2. 选择开发板。
3. 选择端口。
4. 点击上传按钮。
5. 打开串口监视器。
6. 将串口监视器波特率设置为 `115200`。

更详细说明见：[上传 Arduino 示例程序](../tutorials/upload-arduino-sketch.md)。

### PlatformIO

1. 打开工程文件夹。
2. 检查 `platformio.ini`。
3. 点击 Upload。
4. 打开 Serial Monitor。
5. 确认监视器波特率为 `115200`。

## 10. 观察串口监视器输出

如果通信正常，你会看到类似内容：

```text
Position:1200
Speed:0
```

或：

```text
ID:1
Position:1200
Speed:35
```

如果读取失败，可能会看到：

```text
FeedBack error
sync read error
```

## 11. 成功后继续学习

| 你使用的产品 | 下一步 |
| --- | --- |
| TTL Encoder E02 | [TTL Encoder E02：C++ / Arduino](../reference/bus-devices/ttl-encoder-e02/cpp-arduino.md) |
| TTL Stepper Driver (A) | [TTL Stepper Driver (A)：C++ / Arduino](../reference/bus-devices/ttl-stepper-driver-a/cpp-arduino.md) |
| TTL Adapter (A) | [TTL Adapter (A)：SDK 与工具](../reference/bus-devices/ttl-adapter-a/sdk-and-tools.md) |

## 12. 如果没有成功

| 现象 | 常见原因 | 处理方式 |
| --- | --- | --- |
| 程序无法上传 | 开发板型号或端口选择错误 | 检查 Board 和 Port |
| 串口监视器没有输出 | 监视器波特率错误；程序未运行 | 设置为 `115200`；按复位键 |
| 一直读取失败 | UART 引脚错误；ID 错误；波特率错误 | 检查 RX/TX/GND、设备 ID、`1000000` 波特率 |
| 连接执行器后复位 | 电源不足；USB 供电过载 | 执行器使用独立外部电源 |
| 多设备读取混乱 | 设备 ID 重复 | 一次只连接一个设备修改 ID |

更多问题见：[常见通信问题排查](../tutorials/communication-troubleshooting.md)。
