# 编译、上传与调试

复杂项目应把“能编译”“能上传”“能启动”“真实硬件工作”视为四个独立检查点。

## 常用操作

| 操作 | VS Code | 终端 |
| --- | --- | --- |
| 编译 | 状态栏 `✓` | `pio run` |
| 清理 | PlatformIO: Clean | `pio run -t clean` |
| 上传程序 | 状态栏 `→` | `pio run -t upload` |
| 串口监视 | 插头/终端图标 | `pio device monitor` |
| 上传并监视 | PlatformIO 任务 | `pio run -t upload && pio device monitor` |
| 上传文件系统 | PlatformIO 任务 | `pio run -t uploadfs` |

PowerShell 5.1 不支持所有 shell 中的 `&&` 行为时，请分两条命令执行。

## 编译

首次修改前确认原始工程可编译：

```bash
pio run
```

关注构建摘要：

- 使用了哪个环境
- Flash 占用
- RAM 占用
- 是否接近分区容量
- 第一条真实错误

!!! tip "从第一条错误开始"
    后续几十条报错常由第一个头文件、类型或语法错误连锁产生。不要从输出末尾开始逐条修。

## 安全上传

1. 断开外部动力电源。
2. 断开舵机、电机和高功率负载。
3. 保留开发板所需 USB 或调试供电。
4. 关闭串口监视器和其他占用端口的软件。
5. 上传固件。
6. 先检查日志和板载指示，再连接执行器。

```bash
pio run -t upload
```

## 选择端口

查看设备：

```bash
pio device list
```

临时指定端口：

=== "Windows"

    ```powershell
    pio run -t upload --upload-port COM11
    ```

=== "Linux"

    ```bash
    pio run -t upload --upload-port /dev/ttyACM0
    ```

=== "macOS"

    ```bash
    pio run -t upload --upload-port /dev/cu.usbmodem12345
    ```

## 进入下载模式

许多开发板支持自动下载。若一直等待连接，可尝试常见手动流程：

1. 按住 `BOOT/IO0`。
2. 短按 `RESET/EN`。
3. 松开 `BOOT/IO0`。
4. 重新上传。

具体按键和接口以产品硬件文档为准。

## 串口日志

代码：

```cpp
void setup() {
  Serial.begin(115200);
  delay(1000);
  Serial.println("boot");
}
```

配置：

```ini
monitor_speed = 115200
```

打开：

```bash
pio device monitor
```

## 推荐日志层级

```cpp
#define LOG_INFO(fmt, ...)  Serial.printf("[I] " fmt "\n", ##__VA_ARGS__)
#define LOG_ERROR(fmt, ...) Serial.printf("[E] " fmt "\n", ##__VA_ARGS__)
```

至少记录：

- 固件版本
- 复位原因
- 配置加载结果
- 文件系统挂载结果
- 总线和网络初始化结果
- 执行器使能原因
- 严重错误码

避免在高频运动循环中持续打印，串口输出可能破坏实时性。

## 分阶段验证

1. **编译验证**：没有编译和链接错误。
2. **启动验证**：无反复复位、看门狗或崩溃。
3. **板载验证**：LED、OLED、蜂鸣器、按键正常。
4. **通信验证**：USB/UART/Wi-Fi/API 正常。
5. **空载验证**：执行器低速运行。
6. **负载验证**：逐步增加速度和负载。
7. **异常验证**：断线、低电压、超时和重启行为可控。

## 导出构建产物

固件通常位于：

```text
.pio/build/<环境名>/
```

常见文件包括：

- `firmware.bin`
- `bootloader.bin`
- `partitions.bin`
- 文件系统镜像

单个 `firmware.bin` 不一定足以恢复整机。制作发布包时应记录地址、分区表、平台版本和刷写方式。
