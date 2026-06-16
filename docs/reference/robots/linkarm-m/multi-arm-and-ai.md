# 多机械臂与 AI 集成

## 多台机械臂

每台 LinkArm-M 都应有独立的串口和配置文件：

```text
configs/
├─ arm_left.json
└─ arm_right.json
```

两个配置文件至少应分别填写：

- 对应的串口设备
- 当前机械臂贴纸上的 `servo_middle`
- 与实际硬件一致的 ID 和波特率

```python
from linkarm import RobotController


left = RobotController(
    config_file="configs/arm_left.json",
    port="COM7",
)
right = RobotController(
    config_file="configs/arm_right.json",
    port="COM8",
)

left.set_joints_angle([0.0, -0.2, 0.4, 0.0], reliable=True)
right.set_joints_angle([0.0, -0.2, 0.4, 0.0], reliable=True)
```

Linux 和 macOS 请将端口替换为实际设备路径。

!!! warning "不要复制同一份中位参数"
    即使两台机械臂型号相同，`servo_middle` 也不应共用。配置串错可能造成明显姿态偏移。

## 稳定识别串口

=== "Windows"

    在设备管理器中确认 COM 号。若插入不同 USB 口后编号变化，应同步修改对应配置。

=== "macOS"

    使用 `python3 -m serial.tools.list_ports`，优先选择 `/dev/cu.*` 设备。

=== "Linux / Raspberry Pi / Jetson"

    可检查 `/dev/serial/by-id/`，在可用时它通常比 `/dev/ttyUSB0` 更适合长期部署：

    ```bash
    ls -l /dev/serial/by-id/
    ```

## CLI 作为上层工具

JSON 输出适合被 Node.js、Shell、工作流服务或 AI Agent 调用：

```bash
python linkarm.py --json status
python linkarm.py --json fk
python linkarm.py --json cmd "joint 3 -0.5 --reliable"
```

批量动作可使用：

```bash
python linkarm.py --json batch \
  "status" \
  "joint 3 -0.5 --reliable" \
  "gripper -1"
```

上层程序应根据退出码和 JSON 中的成功状态判断结果，不要只检查是否产生了输出。

## AI Agent 工具设计

建议只向模型暴露有限、可验证的高层工具：

```json
{
  "name": "move_linkarm_joint",
  "description": "在允许范围内移动 LinkArm-M 的一个关节",
  "parameters": {
    "type": "object",
    "properties": {
      "joint": {"type": "integer", "minimum": 0, "maximum": 3},
      "angle_rad": {"type": "number"}
    },
    "required": ["joint", "angle_rad"]
  }
}
```

工具执行层应负责：

- 校验关节索引和角度范围
- 限制单次移动幅度和速度
- 动作前确认设备在线
- 设置超时并处理串口异常
- 记录请求、结果和操作者
- 为用户保留物理急停或断电能力

不要把任意 Shell 命令执行权直接交给模型，也不要让模型绕过 `joint_limit`。

## 并发控制

同一个串口不应被多个进程同时打开。推荐让一个常驻控制服务独占串口，其他程序通过队列、HTTP 或本地 IPC 提交动作。

多机械臂同时动作时还要考虑：

- 两台机械臂的共享工作空间
- 供电总功率
- 动作开始时间与执行顺序
- 单台失败时其他机械臂的停止策略
- 恢复运行前的姿态重新确认
