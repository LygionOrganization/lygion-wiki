# JSON 指令参考

驱动板的 Web 控制台、USB CDC、HTTP、WebSocket 和 GPIO UART 使用同一套 JSON 指令。字段 `T` 表示指令类型。

!!! note "一条指令一行"
    USB CDC 和 UART 通信时，应在 JSON 字符串末尾发送换行符 `\n`。任务文件中也要求每条 JSON 独占一行。

## 系统与通信

### 停止任务

```json
{"T":0}
```

### 设置总线波特率

```json
{"T":10,"baud":1000000}
```

支持 3 Mbps 及以下的自定义波特率。该值必须与总线设备一致。

### 设置消息输出

```json
{"T":604,"echo":1,"uart":0,"usb":1}
```

| 参数 | 含义 |
| --- | --- |
| `echo` | 是否回显收到的控制指令 |
| `uart` | 是否通过 UART0 输出调试信息 |
| `usb` | 是否通过 USB CDC 输出调试信息 |

UART0 输出可能给主循环带来延迟，默认关闭。

### UART0 透传模式

```json
{"T":605,"sf":1}
```

- `sf: 1`：启用串口透传，UART 接口可供 FD 软件访问舵机。
- `sf: 0`：关闭透传，UART0 接收 JSON 指令。

### 重启和重置

```json
{"T":600}
```

重启设备。

```json
{"T":601}
```

清理 NVS。Wi-Fi 或 ESP-NOW 配置异常时可以尝试。

```json
{"T":602}
```

格式化文件系统并重置设备，会删除任务和网络配置。

## STS / SMS 舵机

### 动作控制

```json
{"T":11,"id":1,"pos":2047,"spd":0,"acc":0}
```

### 设置中位

```json
{"T":12,"id":1}
```

### 修改 ID

```json
{"T":13,"old_id":1,"new_id":2}
```

### 扭矩锁

```json
{"T":14,"id":1,"state":1}
```

`state: 0` 释放扭矩，`state: 1` 锁定扭矩。

### 读取反馈

```json
{"T":15,"id":1}
```

## HLS 舵机

### 动作控制

```json
{"T":21,"id":1,"pos":2047,"spd":500,"acc":0,"cl":500}
```

`cl` 为最大电流限制。`spd` 不能为 `0`。

### 设置中位

```json
{"T":22,"id":1}
```

### 修改 ID

```json
{"T":23,"old_id":1,"new_id":2}
```

### 扭矩锁

```json
{"T":24,"id":1,"state":1}
```

### 读取反馈

```json
{"T":25,"id":1}
```

## SCS 舵机

### 动作控制

```json
{"T":31,"id":1,"pos":511,"time":0,"spd":0}
```

`time` 单位为毫秒。`time` 和 `spd` 都为 `0` 时使用最高速度。

### 修改 ID

```json
{"T":33,"old_id":1,"new_id":2}
```

### 扭矩锁

```json
{"T":34,"id":1,"state":1}
```

### 读取反馈

```json
{"T":35,"id":1}
```

## 延时、OLED 与蜂鸣器

### 延时

```json
{"T":51,"delay":1000}
```

### 设置单行文字

```json
{"T":202,"line":1,"text":"Hello, world!","update":1}
```

`update: 0` 暂不刷新，适合连续设置多行；`update: 1` 立即刷新。

### 刷新屏幕

```json
{"T":203}
```

### 一次设置四行

```json
{"T":204,"l1":"Line 1","l2":"Line 2","l3":"Line 3","l4":"Line 4"}
```

### 清空屏幕

```json
{"T":205}
```

### 蜂鸣器

```json
{"T":206,"freq":1000,"duration":1000}
```

`freq` 单位 Hz，`duration` 单位 ms。

## Wi-Fi 与 ESP-NOW

### 配置 Wi-Fi

```json
{"T":400,"mode":1,"ap_ssid":"Robot","ap_password":"12345678","channel":1,"sta_ssid":"ssid","sta_password":"password"}
```

### 设置 ESP-NOW 接收模式

```json
{"T":411,"mode":1}
```

`mode: 1` 接收 ESP-NOW 指令，`mode: 0` 禁用接收。

### 添加 Peer

```json
{"T":414,"mac":"FF:FF:FF:FF:FF:FF"}
```

发送前需要先将目标 MAC 加入 Peer。全 `FF` 为广播地址。

### 发送 ESP-NOW 指令

```json
{"T":413,"mac":"FF:FF:FF:FF:FF:FF","data":"{\"T\":206,\"freq\":500,\"duration\":30}"}
```

`data` 中嵌套的 JSON 引号必须转义。

## 任务文件 { #mission-files }

### 创建

```json
{"T":301,"name":"mission1","intro":"Mission description"}
```

### 追加一条指令

```json
{"T":303,"name":"mission1","json":"{\"T\":51,\"delay\":1000}"}
```

### 在指定步骤插入

```json
{"T":304,"name":"mission1","step":2,"json":"{\"T\":51,\"delay\":1000}"}
```

### 替换指定步骤

```json
{"T":305,"name":"mission1","step":2,"json":"{\"T\":51,\"delay\":500}"}
```

### 删除指定步骤

```json
{"T":306,"name":"mission1","step":2}
```

### 运行指定步骤

```json
{"T":307,"name":"mission1","step":2}
```

### 运行任务

```json
{"T":308,"name":"mission1","interval":0,"loop":1}
```

### 删除任务

```json
{"T":309,"name":"mission1"}
```

## 在哪里发送

- 浏览器即时测试：[Web 控制台](web-console.md#json-interface)
- 保存多步任务：[动作脚本与任务文件](action-scripting.md)
- Python / 上位机程序：[上位机通信](host-communication.md)
