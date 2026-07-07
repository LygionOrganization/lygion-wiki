# 关节执行器 DM42-G7220-E02

DM42-G7220-E02 是一款面向机器人关节应用的同步带关节执行器。模组将 42 系列步进电机、同步带传动结构和 E02 绝对值编码器安装结构集成在同一机械单元中，适合用于机械臂、转向机构、教学平台和需要角度反馈的低速关节。

![DM42-G7220-E02 joint actuator](assets/hero.webp){ .img-rounded }

## 产品特点

- 采用步进电机驱动，适合位置控制和低速角度控制场景。
- 同步带传动结构便于将电机布置在关节侧面，降低输出轴附近的结构占用。
- 集成 E02 编码器安装位置，可读取输出侧绝对角度。
- 提供多组安装孔，便于固定到铝板、型材、机械臂连杆或自定义支架。
- 可配合 [TTL Stepper Driver (A)](../../bus-devices/ttl-stepper-driver-a/index.md) 和 [TTL Encoder E02](../../bus-devices/ttl-encoder-e02/index.md) 组成 TTL 总线控制关节。

## 典型应用

- 教学机械臂关节
- 小型机器人转向或摆动机构
- Leader-Follower 结构中的角度采集与执行端
- 实验平台中的可编程旋转关节

## 系统组成

DM42-G7220-E02 的典型系统由机械执行器、电机驱动器、编码器和上位机或 MCU 组成。编码器用于读取输出侧角度，步进驱动器用于控制电机运行。驱动器和编码器是两个独立的总线设备，使用时应分配不同 ID。

```text
上位机 / MCU
    │
    ▼
TTL Adapter (A) 或 TTL 总线主控
    ├── TTL Stepper Driver (A) ── 步进电机
    └── TTL Encoder E02 ─────── 输出侧角度反馈
```

![DM42-G7220-E02 bus system](assets/bus-system.webp){ .img-rounded }

!!! note "驱动器与编码器"
    步进电机驱动器不会自动读取 E02 编码器。若项目需要闭环同步、上电角度恢复或角度校准，应由上位机或 MCU 分别读取编码器并向驱动器发送控制指令。

## 机械结构

模组使用同步带连接电机端和输出端。输出侧可安装连杆、轮架、转盘或其它自定义结构。

![DM42-G7220-E02 front view](assets/product-front.webp){ .img-rounded }

![DM42-G7220-E02 rear structure](assets/product-rear-structure.webp){ .img-rounded }

## 机械尺寸

下图为 DM42-G7220-E02 的主要安装尺寸。正式设计时请以 PDF、DXF 或 STEP 文件为准。

![DM42-G7220-E02 dimensions](assets/dimensions.webp){ .img-rounded }

| 项目 | 参数 |
| --- | --- |
| 安装板参考尺寸 | 120 × 60 mm |
| 主安装孔距 | 108 × 40 mm |
| 安装板孔位 | 8 × M4 |
| 输出端安装孔 | 8 × M3，PCD Ø60 |
| 结构参考高度 | 42.05 mm |
| 电机参考高度 | 50.5 mm |

## 使用建议

1. 首次装配前，先确认同步带张紧、输出端旋转是否顺畅。
2. 将步进电机连接到驱动器时，确认 A/B 相线序正确。
3. 将 E02 编码器接入 TTL 总线后，为编码器和驱动器设置不同 ID。
4. 若使用绝对角度反馈，请先完成编码器中位或参考位置校准。
5. 第一次运行应使用较低速度、较低加速度和较小负载，确认运动方向和机械限位。

## FD 参数配置

若使用 [TTL Stepper Driver (A)](../../bus-devices/ttl-stepper-driver-a/index.md) 和 [TTL Encoder E02](../../bus-devices/ttl-encoder-e02/index.md) 控制 DM42-G7220-E02，建议先使用 FD 调试软件完成驱动器 ID、编码器 ID、位置模式和编码器中位配置。

### 准备物料

| 物料 | 用途 |
| --- | --- |
| DM42-G7220-E02 | 被调试的关节执行器 |
| TTL Stepper Driver (A) | 控制关节步进电机 |
| TTL Adapter (A) | 将电脑 USB 转换为 TTL 总线 |
| 外部直流电源 | 为步进电机和驱动器供电 |
| Windows 电脑 | 运行 FD 调试软件 |

!!! warning "固定执行器"
    第一次调试前，请固定执行器本体，并确认输出端附近没有线缆、手指或其它障碍物。关节输出端转动时可能带动连杆或安装件摆动。

### 接线步骤

1. 使用 4P 电机线连接关节步进电机和 TTL Stepper Driver (A)。
2. 使用 5264 3P 连接线连接 TTL Stepper Driver (A) 和 TTL Adapter (A)。
3. 将 E02 编码器接入 TTL 总线。驱动板上的 HC1.25-3P 接口可作为编码器接入总线的连接节点。
4. 为 TTL Stepper Driver (A) 接入符合规格的外部电源。
5. 使用 USB 线连接 TTL Adapter (A) 和电脑。
6. 打开 FD 软件，选择 TTL Adapter (A) 对应串口，波特率设置为 `1000000`。
7. 点击 `打开`，再点击 `搜索`。

!!! note "驱动器和编码器是两个设备"
    TTL Stepper Driver (A) 和 TTL Encoder E02 需要使用不同 ID。驱动器负责控制步进电机，编码器负责反馈输出端角度，上位机或 MCU 需要分别读取和控制。

### 推荐 ID 与参数

本文示例默认使用以下 ID。若你的项目中已经规划了其它 ID，请保持总线上唯一即可。

| 设备 | 示例 ID |
| --- | ---: |
| TTL Stepper Driver (A) | `1` |
| TTL Encoder E02 | `2` |

进入驱动器的 `编程` 页面后，建议先确认以下参数：

| 参数 | 推荐值 | 说明 |
| --- | ---: | --- |
| ID | `1` | 单关节测试时的驱动器 ID，可按项目修改 |
| 运行模式 | `0` | 位置模式，用于控制关节转到指定角度 |
| 加速度 | `15` | 调试时使用较小但非 0 的值 |
| 目标电流 | `200` | 相电流约 `1.32 A` |

![DM42 FD driver parameters](assets/fd-software-b-cn.webp){ .img-rounded }

!!! note "截图中的数值"
    FD 截图用于说明参数所在位置和操作界面。截图中的 ID 或实时位置可能与本文示例不同，实际使用时请以你在设备中保存的参数为准。

### 编码器中位校准

编码器中位用于定义关节的 `0°` 参考位置。校准前应将输出端移动到你希望作为机械中位的位置，例如连杆水平、转台正前方或机构装配基准位。

1. 断开电机输出力矩，或在安全条件下手动移动关节到机械中位。
2. 在 FD 中选择 `TTL_E02` 编码器设备。
3. 进入 `编程` 页面，点击 `中位校准`。
4. 切换到 `调试` 页面，确认当前位置读数通常接近 `2047` 或 `2048`。

![DM42 FD encoder debug](assets/fd-software-cn.webp){ .img-rounded }

!!! tip "中位会掉电保存"
    E02 编码器的中位校准结果会保存到编码器内部。正常使用时，通常不需要每次上电重新校准；程序只需要读取编码器位置并同步驱动器当前位置。

### 运动测试

在 FD 的 `调试` 页面选择关节电机驱动器，使用保守参数进行小范围测试：

| 参数 | 推荐值 | 说明 |
| --- | ---: | --- |
| 加速度 | `15` | 不建议使用 `0`，`0` 表示接近最高加速度 |
| 速度 | `400` 或更低 | 第一次测试使用低速 |
| 扭矩 | `200` | 对应相电流约 `1.32 A` |
| 目标值 | 小范围变化 | 先确认方向和机械限位，再扩大运动范围 |

相电流估算公式：

```text
相电流(A) ≈ 3.3 × 2 × (电流参数 / 1000)
```

当电流参数为 `200` 时：

```text
3.3 × 2 × (200 / 1000) = 1.32 A
```

## 角度控制逻辑

DM42-G7220-E02 的步进电机为开环驱动，驱动器上电后不知道输出端的真实绝对角度。因此，程序上电后应先读取 E02 编码器，再将驱动器当前位置同步到与编码器对应的位置值。

示例使用以下换算关系：

```text
总减速比 = (72 / 20) × 5.181818182
编码器单圈计数 = 4096
编码器中位 = 2048
步进电机单圈微步数 = 3200
关节总步数 = 步进电机单圈微步数 × 总减速比
编码器相对中位差值 = 编码器读数 - 编码器中位
开机同步位置 = 关节中位 + 编码器相对中位差值 × 编码器转步数系数
目标位置 = 目标弧度 × 弧度转步数系数 + JOINT_ZERO
```

!!! note "按实际中位修改"
    FD 中位校准后，机械中位通常对应编码器读数 `2047` 或 `2048`。如果实测中位读数不同，请修改例程中的 `ENCODER_CENTER`。

## Python 例程

Python 示例会读取 E02 编码器位置，同步关节电机驱动器当前位置，然后依次控制关节转到 `0°`、`+45°`、`-45°`、`0°`。

运行前请确认：

- 已安装 Lygion Python SDK。
- `PORT_NAME` 已改成当前电脑上的实际串口号。
- `ENCODER_ID` 与 FD 中配置的编码器 ID 一致。
- `JOINT_DRIVER_ID` 与 FD 中配置的驱动器 ID 一致。
- 驱动器处于位置模式。

[下载 Python 例程](assets/dm42_example.py){ .md-button }

```python
--8<-- "docs/reference/modules/dm42-g7220-e02/assets/dm42_example.py"
```

## ESP32 Arduino 例程

Arduino 示例使用 ESP32 的 `Serial1` 与 TTL Adapter (A) 通信，并通过 `ReadPos()`、`CalibrationOfs()` 和 `WritePosEx()` 完成编码器读取、驱动器同步和角度控制。

运行前请确认：

- 已安装 Lygion C++ / Arduino SDK。
- ESP32 的 RX/TX/GND 与 TTL Adapter (A) 正确连接。
- `ENCODER_ID` 与 FD 中配置的编码器 ID 一致。
- `JOINT_DRIVER_ID` 与 FD 中配置的驱动器 ID 一致。
- 驱动器处于位置模式。

[下载 ESP32 Arduino 例程](assets/dm42_esp32_example.ino){ .md-button }

```cpp
--8<-- "docs/reference/modules/dm42-g7220-e02/assets/dm42_esp32_example.ino"
```

## 常见问题

| 现象 | 可能原因 | 处理建议 |
| --- | --- | --- |
| 读取不到编码器 | 编码器 ID、波特率、接线或供电错误 | 检查 `ENCODER_ID`、`1000000` 波特率、TTL 总线接线和外部供电 |
| 关节角度不正确 | 编码器中位未校准；上电后未同步成功 | 重新执行中位校准，并确认程序中的 `joint_init()` 或 `jointInit()` 成功 |
| 关节抖动或只响不转 | 电机线序错误、速度过高、加速度过高或电流不足 | 检查 A/B 相线序，降低速度，使用非 0 加速度，适当提高电流 |
| 运动方向与预期相反 | 电机相序、安装方向或角度定义与项目不一致 | 在程序中取反目标角度，或调整项目中的正方向定义 |
| 运行范围受限 | 位置值被限制在 `0~65534`，或机构存在机械限位 | 检查目标角度、减速比、限位结构和驱动器角度分辨率参数 |

## 安装示例

![DM42-G7220-E02 arm installation example](assets/arm-installation-example.webp){ .img-rounded }

## 包装内容

![DM42-G7220-E02 package contents](assets/package-contents.webp){ .img-rounded }

## 资料下载

| 资料 | 文件 |
| --- | --- |
| STEP 3D 模型 | [DW42-G7220-E02.step](assets/DW42-G7220-E02.step) |
| 机械图纸 PDF | [DM42-G7220-E02.pdf](assets/DM42-G7220-E02.pdf) |
| DXF 图纸 | [DM42-G7220-E02.dxf](assets/DM42-G7220-E02.dxf) |
| Python 例程 | [dm42_example.py](assets/dm42_example.py) |
| ESP32 Arduino 例程 | [dm42_esp32_example.ino](assets/dm42_esp32_example.ino) |

## 相关资料

- [TTL Stepper Driver (A)](../../bus-devices/ttl-stepper-driver-a/index.md)
- [TTL Encoder E02](../../bus-devices/ttl-encoder-e02/index.md)
- [TTL Encoder E02：校准与多圈](../../bus-devices/ttl-encoder-e02/calibration-and-multiturn.md)
- [TTL Stepper Driver (A)：运行模式](../../bus-devices/ttl-stepper-driver-a/operating-modes.md)
- [TTL Stepper Driver (A)：C++ / Arduino](../../bus-devices/ttl-stepper-driver-a/cpp-arduino.md)
- [TTL Encoder E02：C++ / Arduino](../../bus-devices/ttl-encoder-e02/cpp-arduino.md)
- [FD 调试软件](../../../tutorials/fd-tool.md)
