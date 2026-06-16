# 安装开发环境

需要安装 VS Code 和 PlatformIO IDE。Git 与 GitHub 不是编译固件的必需条件，但强烈建议安装 Git。

## 安装 VS Code

=== "Windows"

    1. 安装 VS Code。
    2. 建议启用“添加到 PATH”和“在资源管理器中打开”。
    3. 安装后重新打开终端。
    4. 验证：

    ```powershell
    code --version
    ```

=== "macOS"

    1. 安装 VS Code 并移动到 Applications。
    2. 在 VS Code 命令面板运行 `Shell Command: Install 'code' command in PATH`。
    3. 重新打开终端并验证：

    ```bash
    code --version
    ```

=== "Linux"

    使用发行版软件中心或适合系统的 `.deb`、`.rpm` 安装包，然后验证：

    ```bash
    code --version
    ```

## 安装 PlatformIO IDE

1. 打开 VS Code 的扩展视图。
2. 搜索 `PlatformIO IDE`。
3. 确认发布者后安装。
4. 重启 VS Code。
5. 等待 PlatformIO Core 初始化结束。
6. 左侧出现 PlatformIO 图标、底部出现编译和上传按钮后，说明扩展已启动。

首次安装和首次构建会下载 Python 环境、编译器、开发平台和依赖库，可能耗时较长。

!!! tip "Core 初始化卡住时"
    完全退出 VS Code 后重新打开，再等待初始化。不要连续安装多个同类 PlatformIO 扩展。

## 安装 Git

=== "Windows"

    安装 Git for Windows。建议：

    - 允许命令行和第三方程序使用 Git
    - 默认分支使用 `main`
    - 默认编辑器选择 VS Code
    - 保留 Git Credential Manager

    验证：

    ```powershell
    git --version
    ```

=== "macOS"

    系统提示安装 Command Line Tools 时按引导完成，或使用 Homebrew：

    ```bash
    brew install git
    git --version
    ```

=== "Linux"

    Ubuntu / Debian：

    ```bash
    sudo apt update
    sudo apt install git
    git --version
    ```

    其他发行版使用对应包管理器安装。

首次提交前设置作者信息：

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

## 推荐扩展

| 扩展 | 用途 |
| --- | --- |
| PlatformIO IDE | 构建、上传和监视 |
| C/C++ Extension Pack | C/C++ 导航与补全 |
| GitHub Pull Requests | 可选，管理 GitHub PR |
| HTML CSS Support | 项目包含 Web 前端时使用 |

AI 编程扩展是可选项。生成的代码仍需由开发者检查引脚、边界条件、实时性和硬件安全。

## 验证 PlatformIO Core

从 PlatformIO 的 `New Terminal` 打开终端：

=== "Windows"

    ```powershell
    pio --version
    ```

=== "macOS"

    ```bash
    pio --version
    ```

=== "Linux"

    ```bash
    pio --version
    ```

如果系统普通终端找不到 `pio`，不代表扩展损坏。先使用 PlatformIO 提供的终端，或直接使用 VS Code 状态栏按钮。
