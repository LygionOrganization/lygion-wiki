# CLI 命令控制

`linkarm.py` 提供一次性命令和交互式 Shell，适合安装验证、手动调试、自动化脚本和上层程序调用。

!!! danger "动作前检查"
    确认机械臂已固定、工作空间已清空，并已填写当前设备专属的 `servo_middle`。首次测试应从读取状态和小幅关节运动开始。

## 查看帮助与状态

=== "Windows"

    ```powershell
    python linkarm.py --help
    python linkarm.py status
    ```

=== "macOS / Linux"

    ```bash
    python3 linkarm.py --help
    python3 linkarm.py status
    ```

若当前目录没有配置文件，可通过 `--config` 指定：

```bash
python linkarm.py --config arm_config.json status
```

SDK 通常依次查找命令行指定的配置、当前目录的 `arm_config.json` 和 SDK 目录中的配置文件。

## 控制夹爪与关节

CLI 的关节角度使用**弧度**。

```bash
# 设置夹爪角度
python linkarm.py gripper -1

# 设置第 3 个关节
python linkarm.py joint 3 -1

# 等待运动到位后再退出
python linkarm.py joint 3 -1 --reliable

# 同时设置 4 个关节
python linkarm.py joints 0 -0.3 0.5 0
python linkarm.py joints 0 -0.3 0.5 0 --reliable
```

`--reliable` 会阻塞当前命令，直到控制器判断已到达目标或发生超时。需要严格按顺序执行动作时建议启用。

## IK 与 FK

笛卡尔坐标的单位统一为毫米（mm）。

```bash
# 计算目标坐标的逆运动学
python linkarm.py ik 250 0 60

# 求解后立即控制机械臂
python linkarm.py ik-now 250 0 60

# 读取当前姿态的正运动学结果
python linkarm.py fk
```

上述 `250 0 60` 表示目标坐标 `[250 mm, 0 mm, 60 mm]`。如果返回 `IK_FAILED`，通常表示目标不可达或机械臂配置不正确。

## 交互式 Shell

```bash
python linkarm.py shell
```

进入 Shell 后可连续输入命令，减少重复初始化串口的开销。输入帮助命令查看当前版本支持的完整列表。

## 一次执行多条命令

```bash
python linkarm.py batch "status" "gripper -1" "joint 3 -1 --reliable"
```

也可把完整命令字符串交给 `cmd`：

```bash
python linkarm.py cmd "joints 0 -0.3 0.5 0 --reliable"
```

## JSON 输出

上层程序或 AI Agent 不应解析面向人的终端文本，建议使用 JSON：

```bash
python linkarm.py --json status
python linkarm.py --json fk
```

需要同时回显输入命令时，可按当前版本帮助信息使用 `--echo`。

## 常用命令

| 命令 | 用途 |
| --- | --- |
| `status` | 读取连接与机械臂状态 |
| `gripper` | 控制夹爪 |
| `joint` / `joints` | 控制单个或全部关节 |
| `ik` / `ik-now` | 计算逆解或计算后执行 |
| `fk` | 读取当前末端位置 |
| `led` / `led-off` | 控制 TTL Node (A) RGB 灯 |
| `pwm` | 控制 TTL Node (A) PWM 输出 |
| `torque-off` / `torque-on` | 设置单个舵机扭矩状态 |
| `torque-off-all` / `torque-on-all` | 设置全部舵机扭矩状态 |
| `torque-limit` | 设置扭矩限制 |
| `set-middle` / `save-middle` | 记录并保存关节中位 |
| `shell` | 进入交互式控制 |

外设和校准命令涉及供电与机械零位，请先阅读[外设与维护](peripherals-and-maintenance.md)。
