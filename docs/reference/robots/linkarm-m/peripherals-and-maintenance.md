# 外设与维护

LinkArm-M 的 TTL Node (A) 不只承担总线转接，还提供 RGB LED、PWM 输出和舵机维护能力。

## RGB 状态灯

```bash
# 具体通道、颜色和亮度参数以当前版本 --help 为准
python linkarm.py led --help
python linkarm.py led-off
```

推荐约定统一的设备状态：

| 状态 | 建议颜色 |
| --- | --- |
| 初始化 | 蓝色 |
| 可接受任务 | 绿色 |
| 正在运动 | 黄色 |
| 错误或急停 | 红色 |

## PWM 输出

```bash
python linkarm.py pwm --help
```

!!! danger "PWM 接口是功率输出"
    输出负载、电流和电压必须符合 TTL Node (A) 的规格。首次接入灯、电磁铁或电机前，应先断电检查极性，并从较低占空比开始测试。PWM 数值与实际输出电压不一定完全线性。

详见 [TTL Node (A) 产品 Wiki](../../bus-devices/ttl-node-a/index.md)。

## 关闭与恢复扭矩

检修或重新摆放机械臂时，可以关闭舵机扭矩：

```bash
python linkarm.py torque-off-all
python linkarm.py torque-on-all
```

也可对单个关节执行：

```bash
python linkarm.py torque-off --help
python linkarm.py torque-on --help
```

!!! danger "关闭扭矩后机械臂会失去支撑"
    先用手托住机械臂，再关闭扭矩。垂直安装或末端带负载时，关节可能立即下落。

## 扭矩限制

```bash
python linkarm.py torque-limit --help
```

扭矩限制不是碰撞检测，也不能代替机械限位或急停。设置过低可能导致无法到位，设置过高则会增加夹伤、堵转和结构损伤风险。

## 中位维护

更换舵机或机械结构后可能需要重新记录中位：

```bash
python linkarm.py torque-off-all
python linkarm.py set-middle
python linkarm.py save-middle
```

具体步骤和风险见[配置与中位校准](configuration-and-calibration.md)。正常使用时，应优先采用机身贴纸上的出厂数据。

## 日常检查

- 检查底座和各连接件是否松动
- 检查线缆是否磨损、拉紧或卷入关节
- 检查电源接口是否发热
- 确认舵机 ID 和 TTL Node ID 没有冲突
- 备份经过验证的 `arm_config.json`
- 升级 SDK 后先执行 `status` 和小幅动作测试

## 安全停机

1. 停止发送新动作。
2. 等待当前动作完成，或通过上层程序执行停止流程。
3. 托住机械臂后按需要关闭扭矩。
4. 关闭动力电源。
5. 最后断开 USB。

不要通过直接拔 USB 代替动力侧停机；USB 主要承担通信，机械臂可能仍处于上电状态。
