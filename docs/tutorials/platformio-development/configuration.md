# 配置 platformio.ini

`platformio.ini` 是工程的可复现说明书。开发板、框架、依赖、构建宏、串口和文件系统配置都应尽量写在这里。

## 基本示例

```ini
[env:esp32-s3]
platform = espressif32
board = esp32-s3-devkitc-1
framework = arduino
monitor_speed = 115200
lib_deps =
  bblanchon/ArduinoJson@^7.0.0
```

!!! warning "示例不能代替产品配置"
    同为 ESP32-S3 的开发板也可能具有不同 Flash、PSRAM、USB 接线和分区。已有产品项目应优先使用仓库自带配置。

## 多环境项目

可用公共环境减少重复：

```ini
[env]
framework = arduino
monitor_speed = 115200
lib_deps =
  bblanchon/ArduinoJson@^7.0.0

[env:debug]
platform = espressif32
board = esp32-s3-devkitc-1
build_type = debug
build_flags =
  -D APP_DEBUG=1

[env:release]
platform = espressif32
board = esp32-s3-devkitc-1
build_flags =
  -D APP_DEBUG=0
```

构建指定环境：

```bash
pio run -e debug
pio run -e release
```

## 常用字段

| 字段 | 用途 |
| --- | --- |
| `platform` | 芯片平台及工具链 |
| `board` | 开发板定义 |
| `framework` | Arduino、ESP-IDF 等 |
| `lib_deps` | 自动安装依赖 |
| `build_flags` | 宏定义和编译参数 |
| `monitor_speed` | 串口监视器波特率 |
| `upload_port` | 固定上传端口 |
| `monitor_port` | 固定监视端口 |
| `board_build.partitions` | 自定义分区表 |
| `board_build.filesystem` | 文件系统类型 |
| `extra_scripts` | 自定义构建脚本 |

## 构建宏

```ini
build_flags =
  -D APP_DEBUG=1
  -D DEVICE_ROLE=2
  -D DEFAULT_BAUD=1000000
```

代码中使用：

```cpp
#if APP_DEBUG
  Serial.println("debug enabled");
#endif
```

宏适合编译期功能开关。用户可修改的运行参数更适合保存在配置文件、NVS 或 EEPROM。

## 端口配置

通常让 PlatformIO 自动识别端口更便于跨电脑使用。只有多设备同时连接时才建议固定：

=== "Windows"

    ```ini
    upload_port = COM11
    monitor_port = COM11
    ```

=== "Linux"

    ```ini
    upload_port = /dev/ttyACM0
    monitor_port = /dev/ttyACM0
    ```

=== "macOS"

    ```ini
    upload_port = /dev/cu.usbmodem12345
    monitor_port = /dev/cu.usbmodem12345
    ```

不要把个人电脑端口提交到共享仓库。可建立不提交 Git 的本地配置，或通过命令行指定端口。

## 串口监视过滤器

```ini
monitor_speed = 115200
monitor_filters =
  time
  esp32_exception_decoder
```

`time` 添加时间戳；异常解码器可帮助定位 ESP32 崩溃位置。具体过滤器支持情况取决于平台和工具版本。

## 分区与文件系统

项目包含 Web 页面、任务或配置文件时，需要同时考虑程序分区和文件系统空间：

```ini
board_build.partitions = partitions.csv
board_build.filesystem = littlefs
```

修改分区表会改变 Flash 布局，可能导致旧文件系统无法读取。升级已有设备前必须制定数据迁移或恢复方案。

## 锁定版本

生产或长期维护项目应避免所有依赖自动跟随最新版本：

```ini
platform = espressif32@6.10.0
lib_deps =
  bblanchon/ArduinoJson@7.2.1
```

升级平台或依赖时单独提交，并重新进行编译、启动、通信和执行器测试。

## 配置检查

修改 `platformio.ini` 后：

1. 保存文件。
2. 运行 `pio run -t clean`。
3. 重新构建。
4. 核对输出中的环境、开发板和平台版本。
5. 检查 Flash/RAM 占用是否异常变化。
