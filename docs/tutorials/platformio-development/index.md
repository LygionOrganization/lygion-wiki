# VS Code + PlatformIO 复杂项目开发

这套教程面向需要修改机器人下位机完整固件的用户。你将学习如何在 VS Code 中打开一个已有 PlatformIO 工程，理解代码和配置，安全地编译上传，并用 Git 管理长期开发。

PlatformIO 适合多文件、多依赖、多开发板或需要持续维护的项目。简单的单文件示例仍可使用 Arduino IDE。

## 你将完成什么

完成教程后，你应该能够：

- 安装并验证 VS Code、PlatformIO 和 Git
- 正确打开已有工程，而不是误建空项目
- 阅读 `src`、`include`、`lib`、`data` 和 `platformio.ini`
- 管理库版本、构建宏、上传端口、分区和文件系统
- 使用 GUI 或终端编译、上传、监视日志
- 区分程序固件与文件系统镜像
- 拆分复杂业务模块，避免入口文件无限膨胀
- 使用分支和提交保存可回退的修改
- 根据第一条真实错误定位构建与上传故障

## 推荐学习顺序

1. [安装开发环境](setup.md)
2. [获取并打开项目](open-project.md)
3. [理解工程结构](project-structure.md)
4. [配置 platformio.ini](configuration.md)
5. [编译、上传与调试](build-upload-debug.md)
6. [依赖与资源文件](dependencies-and-data.md)
7. [Git 开发工作流](git-workflow.md)
8. [常见问题](troubleshooting.md)

## 开发路线

```text
获取项目
  ↓
首次原样编译
  ↓
记录可工作的配置
  ↓
小范围修改 → 再次编译
  ↓
断开执行器后上传
  ↓
查看日志与板载反馈
  ↓
连接真实硬件测试
  ↓
提交 Git
```

!!! tip "先复现，再修改"
    打开项目后的第一件事应是原样编译。只有确认原始工程能成功构建，后续错误才可以明确归因于自己的改动。

!!! danger "机器人固件不是普通程序"
    固件上传后可能立即驱动电机、舵机或电磁机构。首次上传和修改初始化逻辑时，应断开外部动力和执行器。

## PlatformIO 与 Arduino IDE

| 能力 | Arduino IDE | PlatformIO |
| --- | --- | --- |
| 单文件示例 | 简单直观 | 可以 |
| 多文件工程 | 管理能力有限 | 原生支持 |
| 依赖版本 | 常依赖人工安装 | 可写入 `lib_deps` |
| 多套构建配置 | 不方便 | 多环境 `[env:...]` |
| 自动化构建 | 较弱 | CLI 和 CI 友好 |
| 代码导航 | 基础 | VS Code 补全、跳转和重构 |
| 团队协作 | 容易出现环境差异 | 配置可随仓库提交 |

教程默认使用 Arduino 框架，但项目组织、依赖管理和 Git 工作流也适用于其他 PlatformIO 框架。
