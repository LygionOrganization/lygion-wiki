# SW69-TTL 快速上手与 FD 配置

本页说明如何使用 FD 调试软件完成单个 SW69-TTL 舵轮模组的初始配置。完成后，模组中的 3 个 TTL 总线设备应具有唯一 ID，并可以分别完成转向、编码器反馈和行走轮测试。

## 准备物料

每套 SW69-TTL 包含舵轮模组、步进电机驱动板和配套连接线。

![SW69-TTL package](assets/package.webp){ .img-rounded }

首次调试建议额外准备：

| 物料 | 用途 |
| --- | --- |
| [TTL Adapter (A)](../../bus-devices/ttl-adapter-a/index.md) | 将电脑 USB 或控制器 UART 转换为 TTL 总线 |
| [TTL-5264 8P Hub (A)](../../bus-devices/hub-boards/ttl-5264-8p-hub-a.md) | 扩展多个 TTL 总线设备，并支持分组供电 |
| 外部电源 | 推荐 `9 V` 到 `25.2 V` 直流电源；可使用 5S 或 6S 锂电池组 |
| USB Type-C 数据线 | 连接 TTL Adapter (A) 和电脑 |
| Windows 电脑 | 运行 FD 调试软件 |

![TTL Adapter (A)](../../bus-devices/ttl-adapter-a/assets/ttla04.png){ .img-rounded width="240" }

![TTL-5264 8P Hub (A)](../../bus-devices/hub-boards/assets/ttl-5264-8p-hub.webp){ .img-rounded width="360" }

!!! note "非 Windows 用户"
    FD 调试软件主要用于 Windows。Linux、macOS 或嵌入式控制器用户可参考 [设备 ID 与波特率](../../../tutorials/device-id-and-baudrate.md)，使用 Python 或 C/C++ 设置设备 ID 和参数。

## 默认通信参数

| 参数 | 默认值 |
| --- | --- |
| 波特率 | `1000000` bps |
| 新设备常见默认 ID | `1` |
| 可用 ID 范围 | `1` 到 `253` |

!!! warning "同一总线不允许重复 ID"
    新设备出厂 ID 可能相同。配置 ID 时，请一次只连接一个未配置的设备。多个设备配置完成后，再并入同一根总线进行统一控制。

## 1. 设置转向电机驱动器 ID

SW69-TTL 的转向电机本体不保存 ID。ID、运行模式和电流等参数保存在与该电机连接的 TTL Stepper Driver (A) 中。因此，后续装配时应保持驱动板和对应电机的功能关系清晰，避免混用。

![Turn motor ID wiring](assets/change_id_connection.webp){ .img-rounded }

接线步骤：

1. 取一块未配置或准备作为转向驱动器使用的 TTL Stepper Driver (A)。
2. 使用包装内较粗的 5264 3P 连接线，将驱动板接入 TTL Adapter (A)。
3. 使用 2.0-4P 电机线连接转向步进电机和驱动板。
4. 使用 USB 线连接 TTL Adapter (A) 和 Windows 电脑。
5. 在电脑中确认 TTL Adapter (A) 的串口号，可参考 [查找串口设备](../../../tutorials/find-serial-port.md)。

FD 操作步骤：

1. 打开 FD 软件。
2. 选择 TTL Adapter (A) 对应的串口号。
3. 将波特率设置为 `1000000`。
4. 点击 `打开`。
5. 点击 `搜索`，等待设备列表出现 `TTL_SD01`。
6. 点击 `停止`，然后选择左侧搜索到的 `TTL_SD01` 设备。

![FD serial settings](assets/fd_01_cn.webp){ .img-rounded }

![FD search](assets/fd_02_cn.webp){ .img-rounded }

进入 `编程` 页面后：

1. 选择参数 `ID`，不要选择 `从ID`。
2. 在右下角输入新的设备 ID。本文示例将转向电机驱动器设置为 `11`。
3. 点击 `保存`。
4. 出现参数保存成功提示后，点击确定。

![FD set turning ID](assets/fd_03_cn.webp){ .img-rounded }

## 2. 测试转向电机

切换到 `调试` 页面，并选择转向电机驱动器。

推荐测试参数：

| 参数 | 推荐值 | 说明 |
| --- | ---: | --- |
| 加速度 | `15` | 速度变化较平缓，适合调试 |
| 速度 | `400` 或更低 | 超过 `400` 时，电机可能无法稳定转动 |
| 扭矩 | `200` | 对应相电流约 `1.32 A` |

相电流估算公式：

```text
相电流(A) ≈ 3.3 × 2 × (电流参数 / 1000)
```

当电流参数为 `200` 时：

```text
3.3 × 2 × (200 / 1000) = 1.32 A
```

左右拖动位置滑块。如果转向关节可以小幅摆动，说明转向电机和驱动器通信正常。

![FD turning motor test](assets/fd_04_cn.webp){ .img-rounded }

!!! note "GUI 滑块行程"
    FD 调试页面的滑块范围通常为 `0` 到 `4095`，因此在该页面中看到的转向摆动幅度较小。程序控制时可以使用步数或角度换算实现更大的转向范围。

## 3. 设置编码器 ID

转向组件的大同步轮内部集成 TTL Encoder E02，用于反馈转向关节的真实绝对角度。编码器同样是 TTL 总线设备，需要单独设置 ID。

![Encoder location](assets/e02_01.webp){ .img-rounded }

接线步骤：

1. 使用包装内较细的 GH1.25-3P 延长线，将 TTL Encoder E02 接入 TTL Stepper Driver (A) 上的 TTL 总线接口。
2. 驱动板在这里仅作为总线连接节点使用，不会由驱动板 MCU 直接读取编码器。
3. 后续闭环或开机同步逻辑由上位机程序读取编码器并计算完成。

FD 操作步骤：

1. 点击 `搜索`。
2. 等待设备列表出现 `TTL_E02`。
3. 点击 `停止`，并选择 `TTL_E02`。
4. 进入 `编程` 页面。
5. 选择参数 `ID`，不要选择 `从ID`。
6. 输入新的编码器 ID。本文示例设置为 `10`。
7. 点击 `保存`。

![FD encoder search](assets/fd_05_cn.webp){ .img-rounded }

![FD set encoder ID](assets/fd_06_cn.webp){ .img-rounded }

## 4. 校准编码器中位

编码器中位用于定义舵轮的转向零点。后续程序中，转向角 `0°` 对应该机械中位。

![Encoder center calibration position](assets/cali_01.webp){ .img-rounded }

校准步骤：

1. 断开转向步进电机的 4P 电机线，使转向关节可以用手转动。
2. 将舵轮转到机械中位。该位置应对应底盘正前方或正后方行进方向。
3. 保持关节位置不动。
4. 在 FD 中选择 `TTL_E02`。
5. 进入 `编程` 页面，点击右上角 `中位校准`。
6. 出现校准成功提示后，点击确定。
7. 切换到 `调试` 页面，确认当前位置读数约为 `2047` 或 `2048`。
8. 重新连接转向步进电机的 4P 电机线。

![FD encoder center calibration](assets/fd_07_cn.webp){ .img-rounded }

![FD encoder readback](assets/fd_08_cn.webp){ .img-rounded }

!!! note "校准参数掉电保持"
    中位校准参数会保存到编码器内部。后续正常使用时，通常不需要每次上电重新执行中位校准。

## 5. 设置行走电机驱动器 ID 和运行模式

断开当前驱动板与 TTL Adapter (A) 的连接，并保留这块驱动板作为转向电机驱动器使用。再取另一块驱动板，用于行走轮电机。

![Walking motor wiring](assets/dw69_01.webp){ .img-rounded }

接线步骤：

1. 使用 4P 电机线连接行走电机和新的 TTL Stepper Driver (A)。
2. 使用 5264 3P 连接线连接驱动板和 TTL Adapter (A)。
3. 在 FD 中重新搜索 `TTL_SD01`。
4. 选择搜索到的设备，并进入 `编程` 页面。

![FD walking driver search](assets/fd_09_cn.webp){ .img-rounded }

![FD walking driver programming](assets/fd_10_cn.webp){ .img-rounded }

需要配置的参数：

| 参数 | 推荐值 | 说明 |
| --- | ---: | --- |
| ID | `12` | 本文示例中，行走电机驱动器 ID 为 `12` |
| 驱动器相位 | `152` | 匹配行走轮驱动参数，并开启心跳保护相关能力 |
| 运行模式 | `1` | 速度模式，用于连续驱动车轮转动 |
| 心跳保护时间 | `20` | 单位为 `100 ms`，即约 `2 s` |

![FD walking driver parameters](assets/fd_11_cn.webp){ .img-rounded }

保存参数后，断开驱动板供电并等待数秒，再重新连接。更改驱动器相位后需要断电重启才能可靠生效。

!!! tip "心跳保护"
    行走电机处于速度模式时，建议开启心跳保护。若控制器在设定时间内没有继续发送指令，驱动器会自动停止车轮，降低通信中断或程序异常时持续运动的风险。

## 6. 测试行走电机

测试前将行走轮抬离桌面或地面，避免车轮转动时带动模组移动。

推荐测试参数：

| 参数 | 推荐值 | 说明 |
| --- | ---: | --- |
| 加速度 | `15` | 不建议使用 `0`，`0` 表示最高加速度 |
| 速度 | `400` 或更低 | 当前推荐相位下的保守速度范围 |
| 扭矩 | `200` | 对应相电流约 `1.32 A` |
| 目标值 | 任意 | 速度模式下该参数无效 |

点击 `设置` 后，行走电机会开始转动。若未持续发送新的设置指令，约 2 秒后电机应触发心跳保护并自动停止。

![FD walking motor test](assets/fd_12_cn.webp){ .img-rounded }

## 7. 舵轮整体测试

将转向电机驱动器、TTL Encoder E02 和行走电机驱动器同时接入 TTL Adapter (A) 或 TTL-5264 8P Hub (A)。

![Single SW69-TTL integrated wiring](assets/dw69_02.webp){ .img-rounded }

在 FD 中点击 `搜索`。正常情况下，应看到：

- `TTL_E02`：转向编码器
- `TTL_SD01`：转向电机驱动器
- `TTL_SD01`：行走电机驱动器

![FD integrated search](assets/fd_13_cn.webp){ .img-rounded }

测试建议：

1. 选择 `TTL_E02`，确认状态显示通信正常。
2. 选择转向电机驱动器，使用加速度 `15`、速度 `400`、扭矩 `200`，拖动滑块确认转向关节可摆动。
3. 选择行走电机驱动器，抬起车轮，使用加速度 `15`、速度 `400`、扭矩 `200`，点击设置确认车轮可转动并能触发心跳停止。

## 8. 连接多个舵轮

多个舵轮建议通过 [TTL-5264 8P Hub (A)](../../bus-devices/hub-boards/ttl-5264-8p-hub-a.md) 扩展。TTL Adapter (A) 与集线板之间的 GH1.25 连接线只用于通信连接，不包含主电源输入；电机供电应接入集线板的电源输入端。

![Multi-wheel wiring](assets/wiring.webp){ .img-rounded }

推荐 ID 分配：

| 舵轮 | 编码器 ID | 转向电机驱动器 ID | 行走电机驱动器 ID |
| --- | ---: | ---: | ---: |
| 1 | 10 | 11 | 12 |
| 2 | 13 | 14 | 15 |
| 3 | 16 | 17 | 18 |

只要 ID 不重复，同一根 TTL 总线最多可扩展到 `253` 个设备。实际项目中还需要同时考虑供电容量、线缆长度、接插件可靠性和通信稳定性。

## 下一步

完成硬件和 ID 配置后，可以继续阅读：

- [Python 程序开发](python-development.md)
- [C++ / Arduino 程序开发](cpp-arduino.md)
- [TTL Stepper Driver (A)：运行模式](../../bus-devices/ttl-stepper-driver-a/operating-modes.md)
- [TTL Encoder E02：校准与多圈](../../bus-devices/ttl-encoder-e02/calibration-and-multiturn.md)
