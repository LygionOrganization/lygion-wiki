# Git 开发工作流

Git 记录每次可验证修改，让固件出现问题时可以比较或回退。GitHub、GitLab 等远程平台是可选的，所有版本管理都可以先在本地完成。

## 初始化项目

已有仓库无需再次执行 `git init`。

```bash
git init
git add .
git commit -m "Initial working firmware"
```

提交前确认 `.gitignore` 至少排除：

```gitignore
.pio/
.vscode/.browse.c_cpp.db*
```

团队需要共享的 `.vscode` 设置可以保留，不要一概忽略整个目录。

## 推荐分支流程

```bash
git switch -c feature/add-distance-sensor
```

开发过程中保持小提交：

```bash
git add src include platformio.ini
git commit -m "Add distance sensor initialization"
```

完成验证后再合并到主分支。

## 每次修改的闭环

1. 拉取或确认当前基线。
2. 新建功能分支。
3. 做一个小范围修改。
4. 编译。
5. 安全上传并验证。
6. 查看 `git diff`。
7. 提交。

不要把“格式化全部文件”“升级所有依赖”和“新增功能”混在同一个提交中。

## 常用命令

```bash
git status
git diff
git add <文件>
git commit -m "Describe the verified change"
git log --oneline --decorate -10
```

添加远程仓库：

```bash
git remote add origin <仓库地址>
git branch -M main
git push -u origin main
```

## 不同操作系统

=== "Windows"

    可在 VS Code 源代码管理面板操作，也可使用 PowerShell 或 Git Bash：

    ```powershell
    git status
    git pull
    git push
    ```

=== "macOS"

    ```bash
    git status
    git pull
    git push
    ```

=== "Linux"

    ```bash
    git status
    git pull
    git push
    ```

## 处理冲突

出现冲突时不要直接选择“全部保留本地”或“全部保留远程”：

1. 阅读冲突两侧代码。
2. 明确各自意图。
3. 手动组合正确结果。
4. 重新编译。
5. 在硬件上验证。
6. 再提交冲突解决。

VS Code 的选项含义：

| 选项 | 含义 |
| --- | --- |
| Accept Current | 保留当前本地分支 |
| Accept Incoming | 保留正在合入的版本 |
| Accept Both | 两侧都保留，仍需人工整理 |
| Compare | 对比两侧差异 |

## 与远程协作

推荐使用功能分支和 Pull Request：

1. 推送功能分支。
2. 在 PR 中说明硬件、环境和测试方法。
3. 由其他开发者审查。
4. 合并后在主分支再构建一次。

PR 描述至少包含：

- 修改目的
- 影响的硬件和接口
- `platformio.ini` 环境名
- 测试步骤和结果
- 是否修改分区、配置或协议

## 回退思路

先查看历史：

```bash
git log --oneline
```

若只想临时验证旧版本，可创建临时分支，不要用破坏性命令覆盖当前修改：

```bash
git switch -c test-old-version <提交号>
```

确认问题后切回原分支继续修复。
