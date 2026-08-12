# 星海市场 · 自动化部署指南

## 文件说明

| 文件 | 用途 |
|------|------|
| `.github/workflows/update-market.yml` | GitHub Actions 工作流 |
| `cron_scripts/update.sh` | Linux Cron 定时脚本 |
| `windows_tasks/update.bat` | Windows 批处理脚本 (GBK) |
| `windows_tasks/install_task.bat` | Windows 计划任务安装 (GBK) |
| `webhook_server.py` | Webhook 服务 |
| `.automation/systemd/starsea-market.service` | Linux systemd 服务 |

## Windows 安装

```cmd
# 以管理员身份运行
cd windows_tasks
install_task.bat
```

## Linux Cron

```bash
crontab -e
# 添加: 0 */6 * * * cd /path/to/starsea-market && ./cron_scripts/update.sh
```

## GitHub Actions

推送代码到 GitHub 仓库后自动运行。
