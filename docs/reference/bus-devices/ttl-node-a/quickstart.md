# TTL Node (A) 快速开始

本页帮助你确认供电方式、完成第一次连接，并选择适合自己的控制方式。

## 开始前

准备以下设备：

- TTL Node (A)
- 支持数据传输的 USB Type-C 线
- Windows、Linux 或 macOS 电脑，或 Raspberry Pi、Jetson 等主机
- 如需驱动舵机或 PWM 负载：DC 9~12.6V 电源

出厂默认参数：

| 项目 | 默认值 |
| --- | --- |
| 设备 ID | `0` |
| 波特率 | `1,000,000 bps` |

## 选择供电方式

| 功能 | 仅连接 USB | USB + 9~12.6V 外部供电 |
| --- | :---: | :---: |
| 与电脑通信 | 支持 | 支持 |
| 配置设备参数 | 支持 | 支持 |
| 控制 RGB 灯 | 支持 | 支持 |
| 为 5V、最大 500mA 的接收机供电 | 支持 | 支持 |
| 读取 S.BUS 信号 | 支持 | 支持 |
| 驱动总线舵机转动 | 不支持 | 支持 |
| 使用两路 PWM 电源输出 | 不支持 | 支持 |

!!! danger "外部电源只能接入带供电的总线接口"
    从 HX-5264-3P 或 PH2.0-3P 接入 9~12.6V 电源。GH1.25-3P 仅包含 TTL 信号和 GND，不能用于供电。

## 连接设备

=== "直接连接 USB"

    适合使用电脑或单板电脑进行调参、读取 S.BUS 和编程控制。

    ```text
    PC / Raspberry Pi / Jetson
               │ USB Type-C
               ▼
          TTL Node (A)
    ```

    需要驱动舵机或 PWM 负载时，再从 HX-5264-3P 或 PH2.0-3P 接入外部电源。

=== "通过 TTL Adapter (A)"

    TTL Adapter (A) 同时连接 USB 和电源，再通过任意一个带供电的总线接口连接 TTL Node (A)。

    ![TTL Node (A) 通过 TTL Adapter (A) 连接电脑](assets/ttl-adapter-connection.png){ .img-rounded }

=== "通过 Robot Driver"

    使用 Robot Driver with ESP32S3 Lite 作为主控，通过单线 TTL 总线访问节点板。

    ![TTL Node (A) 连接 Robot Driver with ESP32S3 Lite](assets/robot-driver-connection.png){ .img-rounded }

## 第一次确认通信

=== "Windows：FD 图形化工具"

    1. 连接设备，确认系统出现新的 `COM` 端口。
    2. 打开 FD，选择对应端口。
    3. 波特率选择 `1000000`，打开端口。
    4. 点击“搜索”，列表中应出现 `TTL-Node-A`，出厂 ID 通常为 `0`。
    5. 需要修改 ID 或波特率时，继续阅读[使用 FD 配置](fd-configuration.md)。

=== "Windows / Linux / macOS：Python"

    1. [安装 Python](../../../tutorials/install-python.md)。
    2. [查找串口设备](../../../tutorials/find-serial-port.md)。
    3. 下载 [Python SDK](../../../assets/files/lygion_devs_py.zip)。
    4. 先运行 `lynode/ttln_ping.py` 或 `lynode/ttln_adc.py`，并按实际情况修改串口和设备 ID。

=== "ESP32-S3 / Arduino"

    1. 安装 Arduino IDE 和 ESP32 开发板支持。
    2. 安装 `lygion_devs` 库。
    3. 连接 TTL 总线并确认共地。
    4. 从 `example/lyttln` 打开对应示例。
    5. 继续阅读[Arduino 开发](arduino-development.md)。

## 多设备接入

!!! warning "先逐个配置，再并联"
    TTL Node (A) 的出厂 ID 都是 `0`。同一条总线上不能存在两个相同 ID 的设备。请在总线上只保留一个待配置设备，分别修改 ID 后再并联。

并联后的所有设备还必须使用相同波特率。供电方面则要同时满足各设备的电压范围，并为舵机和负载预留足够的峰值电流。

## 下一步

- [查看板载接口与尺寸](hardware-overview.md)
- [了解供电与接线限制](power-and-wiring.md)
- [使用 FD 修改 ID 和波特率](fd-configuration.md)
- [运行 Arduino 示例](arduino-development.md)
