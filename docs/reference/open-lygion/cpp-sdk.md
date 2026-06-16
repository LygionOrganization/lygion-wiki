# C++ SDK

Lygion C++ / Arduino SDK 适合在 ESP32S3、ESP32、Arduino Mega2560、STM32 Arduino Core、RP2040 / Raspberry Pi Pico、PlatformIO 等环境中控制 Lygion TTL 总线设备。

- [Lygion C++ SDK 仓库](https://github.com/LygionOrganization/lygion_devs_cpp)
- [本站下载 C++ / Arduino SDK](../../assets/files/lygion_devs_cpp.zip)

## 获取 SDK

```bash
git clone https://github.com/LygionOrganization/lygion_devs_cpp.git
cd lygion_devs_cpp
```

无法访问 GitHub 时，可以使用本站压缩包：

[下载 C++ / Arduino SDK](../../assets/files/lygion_devs_cpp.zip){ .md-button }

## Arduino IDE

将 SDK 库文件放入 Arduino 的 `libraries` 目录，然后重启 Arduino IDE。

常见位置：

| 系统 | 目录 |
| --- | --- |
| Windows | `Documents\Arduino\libraries` |
| macOS | `~/Documents/Arduino/libraries` |
| Linux | `~/Arduino/libraries` |

基础教程：

- [安装 Arduino IDE](../../tutorials/install-arduino-ide.md)
- [上传 Arduino 示例程序](../../tutorials/upload-arduino-sketch.md)
- [打开串口监视器](../../tutorials/serial-monitor.md)

## PlatformIO

PlatformIO 用户可以把 SDK 放到工程的 `lib` 目录中：

```text
your_project/
├─ platformio.ini
├─ src/
│  └─ main.cpp
└─ lib/
   └─ lygion_devs_cpp/
```

也可以直接用 VS Code 打开 SDK 仓库内已有的 PlatformIO 工程或示例目录。

[PlatformIO 开发教程](../../tutorials/platformio-development/index.md){ .md-button }

## 示例入口

| 设备 / 功能 | 示例入口 |
| --- | --- |
| TTL Node (A) | [`example/lyttln`](https://github.com/LygionOrganization/lygion_devs_cpp/tree/main/example/lyttln) |
| TTL Stepper Driver (A) | [`example/lyttlsd`](https://github.com/LygionOrganization/lygion_devs_cpp/tree/main/example/lyttlsd) |
| 修改设备参数 | `ProgramEprom` / `*_eprom` 类示例 |
| 读取反馈 | `FeedBack` / `Read` 类示例 |
| 位置或速度控制 | `WritePos` / `WriteSpe` 类示例 |

## 串口初始化示意

不同开发板的硬件串口写法不同，示例中的 RX / TX 引脚需要按实际接线修改。

=== "ESP32S3 / ESP32"

    ```cpp
    Serial.begin(115200);
    Serial1.begin(1000000, SERIAL_8N1, 18, 17);

    ttlsd.pSerial = &Serial1;
    ```

=== "Arduino Mega2560"

    ```cpp
    Serial.begin(115200);
    Serial1.begin(1000000);

    ttlsd.pSerial = &Serial1;
    ```

!!! warning "不要一上来运行高速运动示例"
    第一次调试建议先运行读取反馈类示例。运动控制示例可能会驱动电机或机械结构动作，请固定设备并确认供电能力后再运行。

相关页面：

- [设备 ID 与波特率](../../tutorials/device-id-and-baudrate.md)
- [MCU UART 接线基础](../../tutorials/mcu-uart-wiring.md)
- [TTL Adapter (A) SDK 与工具](../bus-devices/ttl-adapter-a/sdk-and-tools.md)
