# 依赖与资源文件

PlatformIO 的核心优势之一，是让项目依赖和资源构建随仓库一起复现。

## 使用 lib_deps

```ini
lib_deps =
  bblanchon/ArduinoJson@7.2.1
  https://github.com/example/vendor-library.git#v1.3.0
```

优先使用库注册表中的明确版本。Git 依赖应指定 tag 或 commit，避免默认分支变化导致构建结果漂移。

## 本地库

只服务于当前项目的代码放在 `lib/`：

```text
lib/
  robot_bus/
    src/
      robot_bus.cpp
      robot_bus.h
```

多个项目共享且独立维护的库，更适合单独仓库或 PlatformIO 包。

## 不要修改 .pio/libdeps

`.pio/libdeps` 是自动下载的缓存。直接修改会导致：

- 清理后丢失
- 换电脑后无法复现
- 同事拿不到修改

需要临时修补第三方库时，将其复制到 `lib/`，并记录来源和修改原因。

## 解决依赖冲突

出现重复定义、API 不兼容或头文件选错时：

1. 查看构建日志实际选中了哪个库。
2. 检查 `lib_deps` 是否同时引入多个同类库。
3. 固定已验证版本。
4. 清理后重建：

```bash
pio run -t clean
pio run
```

必要时删除 `.pio` 重新下载，但这会增加后续构建时间。

## data 目录

Web 页面、JSON 模板、任务和默认配置可放在 `data/`：

```text
data/
  index.html
  app.js
  style.css
  default-config.json
```

上传文件系统：

```bash
pio run -t uploadfs
```

!!! warning "上传程序不等于上传文件系统"
    `upload` 通常只写程序分区；网页或配置变更后还需要 `uploadfs`。反过来，上传文件系统也不会更新程序代码。

## 文件系统初始化

```cpp
#include <LittleFS.h>

void setup() {
  Serial.begin(115200);

  if (!LittleFS.begin(false)) {
    Serial.println("LittleFS mount failed");
    return;
  }
}
```

生产固件不建议默认使用自动格式化参数，否则一次挂载异常可能清空用户数据。应明确设计恢复流程。

## 配置兼容

配置文件增加字段时：

- 为新字段提供默认值
- 忽略未知字段
- 增加配置版本号
- 必要时编写迁移逻辑

```json
{
  "version": 2,
  "device_name": "robot",
  "max_speed": 0.5
}
```

## 秘密信息

Wi-Fi 密码、Token 和私钥不要直接提交到公开仓库。

可采用：

- 不提交 Git 的本地头文件
- 首次启动配置
- NVS
- CI 的 Secret

并提供不含真实秘密的示例文件，例如 `secrets.example.h`。

## 升级依赖的流程

1. 建立单独分支。
2. 每次只升级平台或少量依赖。
3. 清理并完整构建。
4. 验证启动、文件系统、网络和硬件。
5. 记录版本变化。
6. 提交锁定后的配置。
