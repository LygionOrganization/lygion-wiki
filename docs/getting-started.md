# 快速开始

本章节介绍 LYgion TTL 总线设备的基础使用方法，包括接线方式、供电方式、设备 ID 设置、FD 软件调参、Python SDK 调参和 C++ / Arduino SDK 调参。

无论您使用的是 TTL 编码器、TTL 步进驱动器、节点模块、总线舵机，还是基于 TTL 总线的机器人模组，都建议先阅读本章节，熟悉总线通信、设备供电和 ID 配置的基本流程。

!!! note "适用范围"
    本章节主要面向 LYgion TTL 总线设备。  
    LYgion TTL 总线设备可以与飞特 STS / HLS 系列 TTL 总线舵机接入同一条总线使用，但需要确保每个设备具有唯一的 ID。

---

## 1. 使用前需要了解的基本概念

TTL 总线设备通常由三部分组成：

| 项目 | 说明 |
| --- | --- |
| 通信接口 | 用于上位机、MCU 或控制板与总线设备通信 |
| 电源输入 | 为总线设备提供工作电压和工作电流 |
| 设备 ID | 用于区分同一条总线上的不同设备 |

在同一条 TTL 总线上，可以连接多个总线设备。主控设备通过设备 ID 区分每一个模块，并向指定 ID 的设备发送控制指令。

!!! warning "不要直接把多个新设备同时接入总线"
    大多数总线设备出厂默认 ID 可能相同，例如默认 ID 为 `1`。  
    如果多个相同 ID 的设备同时接入总线，会导致通信冲突，表现为搜索异常、控制异常或设备无响应。  
    建议先逐个连接设备，分别设置不同 ID 后，再将多个设备接入同一条总线统一控制。

---

## 2. 接线方式

LYgion TTL 总线设备可以通过 PC / SBC 上位机控制，也可以通过 ESP32、STM32 等嵌入式控制器控制。

### 2.1 使用 PC / SBC 通过 USB 控制

如果您使用的是 PC、树莓派、Jetson、RK 等上位机或单板电脑，推荐使用 [TTL Adapter (A)](bus-devices/ttl-adapter-a.md) 连接 TTL 总线设备。

TTL Adapter (A) 板载 USB-TTL 芯片，可以将电脑的 USB 接口转换为 TTL 总线通信接口。连接后，电脑会识别出一个串口设备，用户可以通过 FD 软件、Python SDK 或其他串口程序与总线设备通信。

![TTL Adapter USB Connection](assets/images/g01.png)

典型连接方式如下：

```text
PC / SBC USB Port
        │
        │ USB Cable
        │
TTL Adapter (A)
        │
        │ TTL Bus
        │
TTL Bus Device
```

需要注意的是，USB 线通常只用于通信，不能作为总线设备的主要供电来源。

部分低功耗设备或单个设备在仅连接 USB 时，可能可以完成参数读取、ID 修改等操作，但不建议直接控制电机、舵机或其他执行器动作。执行器类设备工作时需要额外接入符合规格的外部电源。

!!! warning "USB 供电不能替代设备工作电源"
仅通过 USB 连接 TTL Adapter (A) 时，USB 接口提供的电压和电流通常无法满足总线舵机、步进电机驱动器等执行器的工作需求。
如果需要控制设备运动，请务必接入符合设备电压和电流要求的外部电源。

### 2.2 使用 MCU UART 控制

如果您使用 ESP32、STM32 或其他嵌入式控制器，可以通过 MCU 的 UART 接口连接 TTL Adapter (A)。

TTL Adapter (A) 可以将 MCU 的双线 UART 信号转换为单线 TTL 总线信号，从而控制 LYgion TTL 总线设备或兼容的 TTL 总线舵机。

典型连接方式如下：

| MCU | TTL Adapter (A) |
| --- | --- |
| TX | RX |
| RX | TX |
| GND |	GND |

TTL Adapter (A) 的 UART 通信电平为 3.3V TTL。

!!! warning "请确认 UART 电平"
    TTL Adapter (A) 的 UART 接口为 3.3V 电平。

    如果您的 MCU 或控制器使用 5V UART 电平，请确认其 IO 是否兼容 3.3V 输入，必要时需要增加电平转换电路。

## 3. 供电方式

TTL 总线设备在实际使用时，需要根据设备类型和工作负载配置合适的电源。

选择电源时需要同时考虑：

- 工作电压是否符合设备规格
- 电源电流是否满足设备峰值负载需求
- 同一路供电下连接了多少个设备
- 设备是否为电机、舵机、驱动器等大电流负载
- 应用场景是否存在堵转、加速、大负载启动等高电流工况

例如，如果同一条总线上连接了多个步进电机驱动器或多个大扭矩舵机，就需要为这些设备配置足够电流余量的外部电源。

!!! tip "电源电流建议留有余量"
    电机、舵机、驱动器类设备在启动、加速、堵转或负载变化时，瞬时电流可能明显高于静态电流。
    
    建议电源电流不要只按平均工作电流选择，应根据实际负载和设备数量留出足够余量。

## 4. 分组供电与通信解耦

Lygion TTL 总线系统支持分组供电，也就是将通信总线和设备供电进行解耦。

这种方式适用于以下场景：

- 同一条总线上设备数量较多
- 不同设备的工作电压不同
- 舵机、步进电机等大电流设备需要独立供电
- 希望将通信线统一连接，但电源分成多组管理
- 需要降低单一路电源的电流压力

TTL Adapter (A) 左右两侧提供 GH1.25-3P 通信接口，该接口主要用于 TTL 总线通信扩展，不作为大电流供电接口使用。

用户可以将 TTL Adapter (A) 连接到以下 HUB 分线板：

- [TTL-5264 8P Hub (A)](bus-devices/ttl-5264-8p-hub-a.md)
- [HC-1.25 8P Hub (A)](bus-devices/hc-1.25-8p-hub-a.md)

### 4.1 如何选择 HUB

| HUB 类型 | 适合设备 |	说明 |
| --- | --- | --- |
| TTL-5264 8P Hub (A) |	步进驱动器、总线舵机、大电流模块 | 接口和线材更适合较大电流设备 |
| HC-1.25 8P Hub (A) | 编码器、小型节点模块、低功耗设备 | 接口更小，适合低功耗信号类设备 |

例如：

- 如果您需要扩展多个 TTL 步进电机驱动器，建议使用 TTL-5264 8P Hub (A)。
- 如果您需要扩展多个 TTL 编码器，例如用于灵巧手或多关节位置反馈，建议使用 HC-1.25 8P Hub (A)。

### 4.2 分组供电的基本原则

TTL 总线通常包括：

| V+ | GND | S |
| --- | --- | --- |
| 电源正极 | 电源负极 | 通信总线 |

如果需要使用多组电源，可以断开不同供电组之间的 V+，但需要保留 GND 和 DATA 的连接。

也就是说：

不同电源组之间：

| V+ | GND | S |
| --- | --- | --- |  
| 不连接 | 需要连接 | 需要连接 |

这样可以让所有设备仍然处于同一条通信总线上，但不同设备组由不同电源供电。

!!! warning "多组电源必须共地"
    如果不同电源组之间没有共地，通信信号将缺少统一参考电平，可能导致通信不稳定或完全无法通信。
    
    分组供电时，通常应保持 GND 共地，只断开不同供电组之间的 V+。

### 4.3 不同电压设备混用

通过通信与供电解耦，也可以在同一条 TTL 总线上同时使用不同电压的设备。

例如：

- 一组 12V 总线舵机
- 一组 24V 步进电机驱动器
- 一组低功耗 TTL 编码器

这些设备可以共享同一条 S 通信线，并保持 GND 共地，但各自使用独立的 V+ 电源输入。

!!! note "简单理解"

    TTL 总线通信可以理解为“所有设备共用一条数据线”。

    只要通信线和地线连接正确，不同设备可以由不同电源供电。
    
    这样既能统一控制，又能避免所有设备都挤在同一路电源上。

## 5. 控制前准备：设置设备 ID

在控制多个总线设备之前，必须先为每个设备设置唯一 ID。

推荐流程如下：

1. 只连接一个待设置设备。
2. 使用 FD 软件、Python SDK 或 C++ SDK 搜索设备。
3. 修改该设备 ID。
4. 记录设备型号、安装位置和对应 ID。
5. 断开当前设备，连接下一个设备。
6. 重复以上步骤，直到所有设备 ID 设置完成。
7. 将所有设备接入同一条总线，进行统一控制。

建议记录表格如下：

| 设备名称 | 安装位置 |	设置 ID | 备注 |
| --- | --- | --- | --- |
| TTL Stepper Driver (A) | 左轮驱动 | 1 | 速度模式 |
| TTL Stepper Driver (A) | 右轮驱动	| 2 | 速度模式 |
| TTL Encoder E02 | 关节 1 | 11 |	绝对角度反馈 |
| TTL Node (A) | 末端模块 |	21 | RGB / S.BUS |

!!! warning "避免 ID 冲突"
    同一条总线上不能存在两个相同 ID 的设备。
    
    如果两个设备 ID 相同，主控发送指令时两个设备会同时响应，可能导致通信错误或控制异常。

### 5.1 主 ID 与从 ID

部分设备支持从 ID 或同步 ID，用于实现多个设备的同步响应。

设置从 ID 时，也建议总线上只保留当前正在配置的单个设备。
如果多个设备同时存在，并且其中某些设备已经配置了从 ID，可能会出现多个设备同时响应同一条指令的情况，导致参数写入或控制结果不符合预期。

!!! note "设置参数时建议单设备操作"
    在修改 ID、从 ID、波特率、工作模式、限位参数等关键参数时，建议总线上只连接一个设备。
    
    参数设置完成后，再将多个设备接入总线统一控制。

## 6. 使用 FD 软件调参

对于 Windows 用户，可以使用 FD 软件进行设备搜索、状态查看、参数修改和基础控制。

下载地址：

- [下载 FD 软件]()

### 6.1 连接设备

使用 FD 软件前，请先完成以下连接：

1. 使用 USB 线连接电脑和 TTL Adapter (A)。
2. 将 TTL Adapter (A) 连接到待设置的 TTL 总线设备。
3. 根据设备要求接入外部电源。
4. 确认设备上电正常。

### 6.2 查看串口号

连接 TTL Adapter (A) 后，Windows 通常会识别出一个新的 COM 串口设备。

可以通过以下方式查看：

1. 右键点击 Windows 开始菜单。
2. 打开 设备管理器。
3. 展开 端口（COM 和 LPT）。
4. 查找类似以下名称的设备：

```text
USB-Enhanced-SERIAL CH343 (COMX)
```

其中 COMX 中的 X 是 Windows 分配的串口编号，例如 COM3、COM5 或 COM12。

### 6.3 打开 FD 软件

打开 FD 软件后，按以下步骤操作：

1. 在端口号中选择刚才识别到的 COM 端口。
2. 设置波特率（大部分总线设备为`1000000`，有部分`SCS`型号舵机是`500000`）。
3. 点击**打开**。
4. 点击**搜索**。
5. 等待设备出现在左侧设备列表中。
6. 设备出现后，点击**停止**。
7. 在左侧设备列表中选择需要调试的设备。

!!! note "为什么搜索后需要点击停止"
    FD 软件搜索设备时，会连续向总线发送查询指令。
    
    搜索完成后建议点击 停止，否则持续搜索可能影响后续调试和控制操作。

### 6.4 搜索设备

FD 软件会从较小的 ID 开始依次查询总线设备。

如果设备 ID 较小，例如出厂默认 ID 为 `1`，通常会很快出现在设备列表中。
如果设备之前被设置为较大的 ID，搜索时间可能会更长。

同一条 TTL 总线上最多可支持多个设备，具体数量取决于设备协议、供电能力、线材长度和通信稳定性。

### 6.5 修改设备 ID

成功搜索到设备后，可以通过 FD 软件修改设备 ID。

操作步骤如下：

1. 点击左侧设备列表中的目标设备。
2. 切换到**编程**页面。
3. 找到`ID`参数。
4. 点击 ID 参数对应的数值。
5. 在右下角输入新的 ID。
6. 点击**保存**。
7. 重新点击**搜索**。
8. 在设备列表中选择新的 ID。

ID 的有效范围通常为：

```text
1 ~ 252
```

!!! warning "修改 ID 后需要重新选择设备"
    修改 ID 后，FD 软件中原来的设备 ID 已经失效。

    需要重新搜索设备，并点击新的 ID，才能继续读取状态或进行控制。

### 6.6 设置下一个设备

设置多个设备 ID 时，可以按以下方式操作：

1. 保持 FD 软件打开。
2. 断开当前设备。
3. 接入下一个待设置设备。
4. 点击**搜索**。
5. 选择设备。
6. 修改 ID。
7. 保存并记录。

建议逐个设置，避免多个新设备默认 ID 相同导致通信冲突。

!!! warning "不要随意修改未知参数"
    FD 软件的“编程”页面包含设备内部参数。

    如果不清楚某个参数的含义，请不要随意修改。错误参数可能导致设备无法正常工作、控制方向异常、限位异常或通信失败。

## 7. 使用 Python SDK 调参

对于 PC、树莓派、Jetson、RK 等可以运行 Python 的设备，可以使用 Lygion Python SDK 进行参数设置和设备控制。

该方式适用于：

- Windows
- Linux
- macOS
- 树莓派
- Jetson
- RK 系列单板电脑

Python SDK 主要依赖串口通信库`pyserial`。

### 7.1 下载 SDK

[GitHub Python SDK 链接](https://github.com/LygionOrganization/lygion_devs_py)

如果无法访问 GitHub，也可以通过本站下载：

[本站 Python SDK 链接]()

### 7.2 安装 Python

Windows 用户需要先安装 Python。

建议安装 Python 3.10 或更高版本，并在安装时勾选：

```text
Add Python to PATH
```

安装完成后，可以在终端中检查：

```
python --version
pip --version
```

Linux / macOS 通常自带 Python，也可以通过以下命令检查：

```
python3 --version
pip3 --version
```

### 7.3 创建虚拟环境

进入 SDK 目录后，建议创建 Python 虚拟环境。

Windows：

```
python -m venv .venv
.venv\Scripts\activate
```

Linux / macOS：

```
python3 -m venv .venv
source .venv/bin/activate
```

### 7.4 安装依赖

安装串口通信依赖：

```
pip install pyserial
```

### 7.5 确认串口名称

不同系统下，串口名称不同。

| 系统 | 常见串口名称 |
| --- | --- |
| Windows | COM3、COM5、COM12 |
| Linux | /dev/ttyUSB0、/dev/ttyACM0 |
| macOS | /dev/tty.usbserial-*、/dev/tty.usbmodem-* |
| 树莓派 | GPIO UART | /dev/serial0 或 /dev/ttyAMA0 |

Windows 用户可以在设备管理器中查看 COM 口。
Linux 用户可以在连接 USB 设备前后执行：

```
ls /dev/ttyUSB*
ls /dev/ttyACM*
```

树莓派、Jetson 或 RK 用户如果使用板载 UART，需要确认系统是否已经启用 UART，并检查对应串口名称和权限。

!!! note "Linux 串口权限"
    如果 Linux 下无法打开串口，可能是当前用户没有串口权限。

    可以尝试将用户加入`dialout`组，或临时使用`sudo`运行程序。

### 7.6 使用广播 ID 设置设备 ID

以 TTL Stepper Driver (A) 为例，可以参考 SDK 中的参数设置例程：

[lygion_devs_py/lyttlsd/ttlsd_eprom.py](https://github.com/LygionOrganization/lygion_devs_py/blob/main/lyttlsd/ttlsd_eprom.py)

在某些情况下，用户可能不知道设备当前 ID。此时可以使用广播`ID 254`向当前总线上的设备发送设置指令。

示例代码：

```python
scs_comm_result, scs_error = packetHandler.SetID(254, 1)

if scs_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(scs_comm_result))
elif scs_error != 0:
    print("%s" % packetHandler.getRxPacketError(scs_error))
```

以上代码表示：将当前总线上响应广播指令的设备 ID 设置为 1


!!! danger "使用广播 ID 前必须只连接一个设备"
    广播 ID 254 会对当前总线上所有支持广播指令的设备生效。
    
    如果总线上连接了多个设备，执行广播设置 ID 可能会把所有设备都改成同一个 ID，导致后续通信冲突。

    使用广播 ID 修改参数时，请确保总线上只连接一个设备。

### 7.7 修改串口和波特率

运行 Python 示例前，需要根据实际情况修改：

- 串口名称
- 波特率
- 目标设备 ID
- 需要写入的参数

例如：

```python
DEVICENAME = "COM5"
BAUDRATE = 1000000
```

Linux 下可能需要改为：

```python
DEVICENAME = "/dev/ttyUSB0"
BAUDRATE = 1000000
```

不同产品的默认波特率可能不同，请以对应产品文档为准。

## 8. 使用 C++ / Arduino SDK 调参

对于 ESP32、STM32 等嵌入式设备用户，可以使用 Lygion C++ SDK 或 Arduino 框架示例进行开发。

[GitHub C++ SDK 链接](https://github.com/LygionOrganization/lygion_devs_cpp)

如果无法访问 GitHub，也可以通过本站下载：

[本站 C++ SDK 链接](https://github.com/LygionOrganization/lygion_devs_cpp)

### 8.1 适用开发环境

C++ / Arduino SDK 适用于以下开发方式：

- Arduino IDE
- PlatformIO
- ESP32 Arduino Core
- 其他兼容 Arduino 风格串口通信的嵌入式平台

### 8.2 安装 SDK

Arduino IDE 用户可以将 SDK 库文件放入 Arduino 的`libraries`目录中。

常见路径如下：

Windows：

```
Documents/Arduino/libraries/
```

macOS：

```
~/Documents/Arduino/libraries/
```

PlatformIO 用户可以将 SDK 放入项目的`lib`目录中：

```
your_project/
├─ src/
├─ lib/
│  └─ lygion_devs_cpp/
└─ platformio.ini
```

## 8.3 参考示例

以 TTL Stepper Driver (A) 为例，可以参考以下示例：

[lyttlsd/ProgramEprom/ProgramEprom.ino](https://github.com/LygionOrganization/lygion_devs_cpp/blob/main/example/lyttlsd/ProgramEprom/ProgramEprom.ino)

该示例演示了如何通过 C++ / Arduino 程序修改设备参数，例如将 ID 为`1`的设备修改为 ID`2`。

也可以使用广播 ID`254`进行参数设置，但同样需要确保总线上只连接一个设备。

!!! danger "嵌入式程序中使用广播 ID 也需要谨慎"
    无论是 Python SDK 还是 C++ SDK，广播 ID 都会影响当前总线上的所有设备。
    使用广播 ID 修改 ID、波特率等关键参数时，请确保总线上只有一个目标设备。

### 8.4 ESP32-S3 串口初始化注意事项

ESP32-S3 通常具有多个硬件串口，例如：

- Serial
- Serial1
- Serial2

如果使用自定义 UART 引脚，需要在初始化串口时明确指定 RX 和 TX 引脚。

例如：

```cpp
Serial1.begin(1000000, SERIAL_8N1, 18, 17);
```

其中：

| 参数 | 含义 |
| --- | --- |
| 1000000 | 波特率 |
| SERIAL_8N1 | 8 位数据位，无校验，1 位停止位 |
| 18 | RX 引脚 |
| 17 | TX 引脚 |

而不是只写：

```cpp
Serial1.begin(1000000);
```

因为只写波特率时，开发板会使用默认 UART 引脚。默认引脚不一定连接到了 TTL Adapter (A)，可能导致程序运行正常但设备没有响应。

!!! tip "确认 RX/TX 是否交叉连接"
    MCU 的 TX 应连接到 TTL Adapter (A) 的 RX。

    MCU 的 RX 应连接到 TTL Adapter (A) 的 TX。

    GND 必须连接到 GND。

## 9. 常见问题排查

### 9.1 FD 软件搜索不到设备

请检查以下项目：

- TTL Adapter (A) 是否正确连接电脑
- 设备管理器中是否识别出 COM 口
- FD 软件是否选择了正确 COM 口
- 波特率是否正确
- 总线设备是否已经供电
- TX / RX / GND 是否接线正确
- 总线上是否存在多个相同 ID 的设备
- 是否使用了过长或接触不良的线材

### 9.2 设备可以搜索到，但不能正常动作

可能原因包括：

- 只连接了 USB，没有接入设备工作电源
- 电源电压不符合设备要求
- 电源电流不足
- 电机或舵机负载过大
- 设备处于错误工作模式
- 速度、加速度、扭矩等参数未正确设置

### 9.3 修改 ID 后设备消失

修改 ID 后，原来的 ID 已经失效，需要重新搜索设备。
搜索到新的 ID 后，需要点击新的设备 ID，再继续读取状态或控制设备。

### 9.4 多个设备接入后通信异常

请重点检查：

- 是否存在重复 ID
- 电源电流是否不足
- 多组供电是否共地
- 通信线是否过长
- HUB 或连接线是否接触不良
- 是否有设备波特率与其他设备不同

## 10. 建议的首次使用流程

如果您是第一次使用 LYgion TTL 总线设备，建议按以下流程操作：

1. 阅读对应产品的电压、电流和接口说明。
2. 参数配置完成前，只连接一个设备。
3. 使用 TTL Adapter (A) 连接电脑。
4. 接入符合要求的外部电源。
5. 使用 FD 软件搜索设备。
6. 修改设备 ID。
7. 记录设备 ID 和安装位置。
8. 使用 FD 软件或 SDK 测试基础控制。
9. 对其他设备重复以上步骤。
10. 所有设备 ID 设置完成后，再接入同一条总线进行系统联调。

## 11. 总结

完成本章节后，您应该已经了解以下内容：

- 如何通过 USB 或 MCU UART 连接 TTL 总线设备
- 为什么总线设备需要独立供电
- 如何使用 HUB 实现总线扩展和分组供电
- 为什么多个设备接入前需要先设置唯一 ID
- 如何使用 FD 软件修改设备 ID
- 如何使用 Python SDK 和 C++ SDK 进行基础参数设置
- 如何排查常见的通信和供电问题

后续各产品文档将重点介绍具体产品的功能、参数和控制方式，不再重复说明本章节中的基础接线和 ID 设置流程。