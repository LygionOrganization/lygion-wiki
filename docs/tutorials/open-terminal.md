# 如何打开终端 / CMD / PowerShell

在 Wiki 教程中，经常会看到需要输入命令的步骤，例如：

```bash
python3 --version
```

这些命令需要在系统的命令行工具中输入。不同系统的工具名称不同：

| 系统 | 常见命令行工具 |
| --- | --- |
| Linux | Terminal / 终端 |
| macOS | Terminal / 终端 |
| Windows | Windows Terminal / PowerShell / CMD |

## Linux

### 方法一：快捷键打开

大多数 Linux 桌面系统可以按：

```text
Ctrl + Alt + T
```

打开终端。

### 方法二：从应用菜单打开

在应用菜单中搜索：

```text
Terminal
```

或：

```text
终端
```

打开后通常会看到类似提示符：

```bash
user@computer:~$
```

你可以在 `$` 后面输入命令。

## macOS

### 方法一：Spotlight 搜索

1. 按 `Command + Space`。
2. 输入 `Terminal` 或 `终端`。
3. 按回车打开。

打开后通常会看到类似提示符：

```bash
user@MacBook ~ %
```

你可以在 `%` 后面输入命令。

### 方法二：从应用程序打开

路径通常为：

```text
应用程序 → 实用工具 → 终端
```

## Windows

Windows 下常用 PowerShell 或 CMD。推荐优先使用 PowerShell。

### 方法一：右键开始菜单

1. 右键点击 Windows 开始菜单。
2. 选择 `终端`、`Windows PowerShell` 或 `Terminal`。

### 方法二：使用运行窗口打开 CMD

1. 按 `Win + R`。
2. 输入：

```text
cmd
```

3. 按回车。

### 方法三：从文件夹中打开终端

进入某个文件夹后，可以在文件夹空白处右键，选择：

```text
在终端中打开
```

这样打开的终端会直接位于当前文件夹，适合运行当前目录中的 Python 脚本或工程命令。

## 如何判断命令输入位置是否正确

命令应该输入在终端提示符后面，例如：

=== "Linux / macOS"

    ```bash
    python3 --version
    ```

=== "Windows PowerShell"

    ```powershell
    py -3 --version
    ```

不要把命令输入到浏览器地址栏、Python 交互窗口或代码文件里。

## 常见问题

### Q1：为什么我的命令前面有 `$`，我要不要输入 `$`？

不用。

文档中的 `$`、`%`、`>` 通常只是提示符，不属于命令本身。你只需要输入后面的命令内容。

### Q2：PowerShell 和 CMD 有什么区别？

二者都可以运行基础命令。本文档 Windows 示例默认使用 PowerShell，因为它在新版本 Windows 中更常见。

如果某条命令在 PowerShell 中无法运行，文档会单独说明 CMD 写法。

### Q3：终端打开后应该先进入哪个目录？

需要进入 SDK 或工程所在目录。

例如 SDK 解压在桌面：

=== "Linux / macOS"

    ```bash
    cd ~/Desktop/lygion_devs_py
    ```

=== "Windows"

    ```powershell
    cd $env:USERPROFILE\Desktop\lygion_devs_py
    ```

进入目录后再运行示例脚本。
