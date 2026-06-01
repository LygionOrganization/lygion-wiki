# 快速开始

如果你刚拿到 Lygion TTL 总线设备，请先选择你的开发方式:

<div class="dev-route-grid">

  <div class="dev-route-card dev-route-python">
    <div class="dev-route-label">推荐快速上手</div>
    <div class="dev-route-title">Python 开发路线</div>
    <div class="dev-route-desc">
      适合电脑、Raspberry Pi、Jetson、RK 等单板电脑（SBC）设备。
    </div>
    <div class="dev-route-points">
      <div>USB 连接 TTL Adapter (A)</div>
      <div>运行 Python 示例脚本与总线设备通信</div>
      <div>适合在电脑或支持 Python 的开发板上快速开发机器人项目</div>
    </div>
    <a class="dev-route-button" href="../quickstart/python-first-demo/">
      开始 Python 路线 →
    </a>
  </div>

  <div class="dev-route-card dev-route-cpp">
    <div class="dev-route-label">适合嵌入式开发</div>
    <div class="dev-route-title">C++ 开发路线</div>
    <div class="dev-route-desc">
      适合 ESP32S3、ESP32、STM32、Arduino 等嵌入式 MCU。
    </div>
    <div class="dev-route-points">
      <div>MCU UART 转 TTL 总线</div>
      <div>使用 Arduino IDE 或 PlatformIO</div>
      <div>运行 C++ 例程与总线设备通信</div>
      <div>适合在嵌入式设备上开发机器人项目</div>
    </div>
    <a class="dev-route-button" href="../quickstart/cpp-first-demo/">
      开始 C++ 路线 →
    </a>
  </div>

</div>

!!! tip "不知道该选哪条路线？"
    如果你使用电脑、树莓派、Jetson 或 N100 小主机，建议选择 **Python 开发路线**。  
    如果你使用 ESP32、STM32、Arduino 等单片机开发板，建议选择 **C++ 开发路线**。

## 两条路线的区别

| 路线 | 常见硬件 | 连接方式 | 使用语言 | 适合场景 |
| --- | --- | --- | --- | --- |
| Python 路线 | PC、Mac、Raspberry Pi、Jetson、RK、N100 小主机 | USB → TTL Adapter (A) → TTL 总线 | Python | 基于支持 Python 和串口通信（USB）的设备进行机器人开发 |
| C++ 路线 | ESP32S3、ESP32、STM32、Arduino | MCU UART → TTL Adapter (A) 或 UART 转单线 TTL 电路 | C++ / Arduino | 基于嵌入式设备进行机器人开发，通常用做机器人的下位机开发 |

## 第一次使用建议

- 第一次只连接 **一个** TTL 总线设备，避免新产品默认 ID 相同而导致的冲突。
- 优先运行 `ping` 或读取类示例，不要一开始就运行高速运动程序。
- 初期使用，为保证产品稳定运行，需要接入与总线设备匹配的外部电源，不建议只依赖 USB 供电。
- 如果遇到问题，先检查串口、波特率、设备 ID、供电和接线。

## 常用基础教程

!!! note "说明"
    部分操作涉及终端、串口、开发环境、设备通信等基础知识。为避免在每篇产品文档中重复说明，我们将这些通用操作整理为独立的基础教程。

    在阅读具体产品教程时，如果遇到不熟悉的操作，可以通过文档中的相关链接跳转到对应基础教程，补充必要的前置知识后再继续操作。

[查看全部基础教程](../tutorials/index.md){ .md-button }