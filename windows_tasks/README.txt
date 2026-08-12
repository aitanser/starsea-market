============================================================
  星海市场 · Windows 自动更新
============================================================

【安装】
  以管理员身份运行: install_task.bat

【手动触发】
  schtasks /run /tn "StarseaMarketUpdate"

【查看状态】
  schtasks /query /tn "StarseaMarketUpdate" /v

【卸载任务】
  schtasks /delete /tn "StarseaMarketUpdate" /f

【日志位置】
  logs/windows_update.log

【问题排查】
  1. 确保 git 和 python 在系统 PATH 中
  2. 确保 starsea-market 目录已初始化 Git
  3. 检查 logs/windows_update.log 查看详细错误
