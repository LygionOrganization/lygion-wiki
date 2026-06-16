# 理解工程结构

PlatformIO 使用统一目录结构。不同项目可以增加自己的文件夹，但核心职责应保持清晰。

## 标准目录

| 路径 | 用途 | 是否通常提交 Git |
| --- | --- | :---: |
| `platformio.ini` | 开发板、依赖、构建和上传配置 | 是 |
| `src/` | 程序入口与源文件 | 是 |
| `include/` | 项目级头文件和配置 | 是 |
| `lib/` | 只属于当前项目的本地库 | 是 |
| `data/` | LittleFS/SPIFFS 等文件系统资源 | 是 |
| `test/` | 单元测试或硬件测试 | 是 |
| `.pio/` | 编译缓存、下载包和产物 | 否 |
| `.vscode/` | 编辑器设置 | 视团队约定 |

`.pio/` 可以删除后重新生成，不应手动修改其中的库源码。

## 程序入口

Arduino 框架通常包含：

```cpp
void setup() {
  // 上电后执行一次
}

void loop() {
  // 持续循环
}
```

大型工程应让入口只负责初始化和调度：

```cpp
#include "app.h"

RobotApp app;

void setup() {
  app.begin();
}

void loop() {
  app.update();
}
```

具体的网络、设备、任务和 UI 逻辑分别放入独立模块。

## `.h` 与 `.cpp`

头文件声明模块提供什么：

```cpp
// status_led.h
#pragma once

class StatusLed {
 public:
  void begin();
  void setError(bool active);
};
```

源文件实现具体行为：

```cpp
// status_led.cpp
#include "status_led.h"

void StatusLed::begin() {
  // 初始化硬件
}

void StatusLed::setError(bool active) {
  // 更新状态
}
```

## 推荐模块边界

复杂机器人项目可按职责拆分：

```text
src/
  main.cpp
  app.cpp
  communication/
  motion/
  tasks/
  ui/
include/
  app.h
  project_config.h
lib/
  device_bus/
  robot_model/
data/
  index.html
  config.json
```

- `communication`：USB、UART、HTTP、WebSocket
- `motion`：运动控制、插值、限位
- `tasks`：状态机、任务编排
- `ui`：OLED、按键、蜂鸣器、Web
- `project_config.h`：引脚、功能开关和默认参数

## 初始化顺序

机器人固件常见初始化顺序：

1. 安全输出状态
2. 日志接口
3. 配置和文件系统
4. 传感器与通信总线
5. 网络服务
6. 执行器
7. 自动任务

!!! danger "先安全，再联网和执行"
    上电时先关闭电机使能、PWM 和高功率输出。只有配置、限位和通信检查通过后，才允许执行器动作。

## 避免阻塞主循环

长时间 `delay()`、等待网络或同步动作会阻塞其他功能。复杂项目优先使用：

- 基于 `millis()` 的定时
- 状态机
- 事件队列
- 必要时使用 RTOS 任务

不要为了“更工程化”过早引入多线程。只有任务确实需要独立周期或会阻塞时再拆分。
