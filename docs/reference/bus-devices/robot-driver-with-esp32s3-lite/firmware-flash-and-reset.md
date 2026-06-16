# 固件恢复

当文件系统损坏、固件无法启动或需要恢复出厂程序时，可以使用项目内的下载工具重新刷写固件。

!!! danger "刷机前断开执行器"
    刷机只需要 USB 连接。建议先断开舵机、电机和外部动力电源，避免设备在重启后意外动作。

## 下载工具

1. 打开[开源项目](https://github.com/EffectsMachine/robot_driver_with_esp32s3_lite)。
2. 点击 `Code` → `Download ZIP`。
3. 解压项目。
4. 进入 `download_tool/RD_ESP32S3_LITE_Download_Tools`。

当前资料包提供的是 Espressif Windows 图形化下载工具流程。

## 连接

1. 使用 Type-C 数据线连接驱动板的 `UART` 接口与 Windows 电脑。
2. 不要连接到中间的原生 `USB` 接口。
3. 打开设备管理器，记下新增的 COM 端口。

## 配置下载工具

运行：

```text
flash_download_tool_3.9.9_R2.exe
```

选择：

| 项目 | 值 |
| --- | --- |
| ChipType | `ESP32-S3` |
| WorkMode | `Factory` |
| LoadMode | `UART` |

![下载工具启动模式](assets/flash-tool-mode.png){ .img-rounded width="360" }

点击 `OK` 进入主界面。

## 开始刷写

1. 选择驱动板对应的 COM 端口。
2. 将上传波特率设为 `921600`。
3. 点击 `START`。
4. 等待状态显示完成。
5. 断开并重新给驱动板上电。

![固件下载工具](assets/flash-tool-main.png){ .img-rounded width="760" }

批量生产时可以配置多个 COM 端口，然后使用 `START ALL`。

## 无法进入下载模式

板载自动下载电路通常会自动处理启动状态。如果自动下载失败：

1. 按住 `IO0`。
2. 短按 `EN`。
3. 松开 `IO0`。
4. 再次点击下载工具的 `START`。

## 刷写后

- 重新连接默认热点 `Robot`。
- 默认密码为 `12345678`。
- 打开 `http://192.168.4.1`。
- 重新配置 STA Wi-Fi 和自定义任务。

固件恢复会覆盖程序；恢复包是否同时格式化文件系统取决于下载工具中的出厂镜像配置。
