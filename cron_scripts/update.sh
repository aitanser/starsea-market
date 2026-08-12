#!/bin/bash
# 星海市场 · 自动更新 Cron 脚本
# 安装: crontab -e
# 添加: 0 */6 * * * cd /path/to/starsea-market && ./cron_scripts/update.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")"/.. && pwd)"
LOG_DIR="$SCRIPT_DIR/logs"
LOG_FILE="$LOG_DIR/cron_update.log"
DATE=$(date '+%Y-%m-%d %H:%M:%S')

mkdir -p "$LOG_DIR"

echo "[$DATE] 开始自动更新..." >> "$LOG_FILE"

cd "$SCRIPT_DIR"

# 拉取最新代码
git pull origin main >> "$LOG_FILE" 2>&1

# 运行更新
python update_market.py --skip-automation >> "$LOG_FILE" 2>&1

# 提交更改
git add index.json plugins.json apps/ plugins/ experimental/
if ! git diff --staged --quiet; then
    git commit -m "chore: 市场仓库自动更新 [skip ci]" >> "$LOG_FILE" 2>&1
    git push origin main >> "$LOG_FILE" 2>&1
    echo "[$DATE] 更新完成并已推送" >> "$LOG_FILE"
else
    echo "[$DATE] 无变化" >> "$LOG_FILE"
fi

# 清理旧日志（保留30天）
find "$LOG_DIR" -name "*.log" -mtime +30 -delete

echo "[$DATE] 执行完成" >> "$LOG_FILE"
