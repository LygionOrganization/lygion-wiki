# Web 控制台

出厂固件内置 Web 应用。只要浏览器能访问驱动板 IP，就可以配置网络、控制舵机、编排动作和发送 JSON 指令，无需安装 App。

## 打开控制台

| 网络模式 | 地址 |
| --- | --- |
| 直连驱动板热点（AP） | `http://192.168.4.1` |
| 驱动板加入路由器（STA） | OLED 或 `STA STATUS` 显示的局域网 IP |

推荐浏览器：Chrome、Edge、Safari 或 Firefox。

## Device Information

此区域显示：

- **Uptime**：设备运行时间。持续递增表示 WebSocket 连接正常。
- **Current Baud Rate**：驱动板与 TTL/RS485 总线设备通信的当前波特率。
- **MAC**：ESP32-S3 的网络接口地址，ESP-NOW 配对时会使用。
- **115200 / 500K / 1M / 3M**：快速切换总线通信波特率。

!!! warning "所有总线设备应使用相同波特率"
    总线上混用不同波特率的设备会导致部分设备无法响应。默认波特率为 1 Mbps。

## Wi-Fi Settings

驱动板同时支持：

- **AP 模式**：驱动板创建热点，默认名称 `Robot`。
- **STA 模式**：驱动板连接现有路由器。

页面中的 `AP_SSID` 和 `AP_PWD` 会显示出厂默认值，即使你已经修改过实际热点信息。真实 AP 名称会在设备启动时显示于 OLED。

修改 STA 设置后，等待 `STA STATUS` 出现路由器分配的 IP。以后可以让控制设备与驱动板连接同一个路由器，通过该 IP 访问。

## 舵机控制组件

控制台按照舵机系列提供不同组件：

- `ST/SM SERVO CTRL`：STS / SMS
- `HL SERVO CTRL`：HLS
- `SC SERVO CTRL`：SCS

不要仅因为界面相似就混用组件。各系列的位置范围、速度参数和功能不同。

## Automation Scripts

此区域用于将多条 JSON 指令保存成任务文件：

- `Up`、`Down`、`Left`、`Right`：绑定到五向开关方向。
- `On Boot`：保存为开机自动循环任务。
- `STOP MISSION`：停止当前任务。
- `Delete Mission`：删除对应任务文件。

每行只能包含一条完整 JSON 指令。详细说明见[动作脚本与任务文件](action-scripting.md)。

## JSON Interface

此区域用于即时发送一条 JSON 指令：

1. 从下方指令列表选择模板，或手动输入。
2. 修改参数。
3. 点击 `SEND`。

![JSON Interface](assets/json-interface.png){ .img-rounded width="620" }

`JSON Interface` 与 `Automation Scripts` 的区别：

| 功能 | JSON Interface | Automation Scripts |
| --- | --- | --- |
| 指令数量 | 单条 | 多条，每行一条 |
| 执行方式 | 立即发送 | 先保存任务，再运行 |
| 典型用途 | 调试、查询、临时控制 | 动作编排、按键触发、开机运行 |

## 页面无响应时

1. 检查 `Uptime` 是否仍在更新。
2. 确认浏览器设备与驱动板仍在同一网络。
3. 刷新页面。
4. AP 模式下确认地址仍是 `192.168.4.1`。
5. STA 模式下查看 OLED，确认 IP 是否因路由器重新分配而变化。

更多问题见[故障排查](faq.md)。
