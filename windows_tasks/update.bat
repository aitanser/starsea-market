@echo off
:: ============================================================
:: 星海市场 · 自动更新 Windows 计划任务脚本
:: ============================================================

:: 切换到 UTF-8 代码页（处理日志中的中文）
chcp 65001 >nul

setlocal enabledelayedexpansion

set SCRIPT_DIR=%~dp0..
set LOG_DIR=%SCRIPT_DIR%\logs
set LOG_FILE=%LOG_DIR%\windows_update.log

:: 获取当前时间
for /f "tokens=1-3 delims=/: " %%a in ("%TIME%") do set HOUR=%%a&set MIN=%%b&set SEC=%%c
for /f "tokens=1-3 delims=/- " %%a in ("%DATE%") do set YEAR=%%a&set MONTH=%%b&set DAY=%%c
set DATE_STR=%YEAR%-%MONTH%-%DAY% %HOUR%:%MIN%:%SEC%

if not exist "%LOG_DIR%" mkdir "%LOG_DIR%"

echo [!DATE_STR!] 开始自动更新... >> "%LOG_FILE%"

cd /d "%SCRIPT_DIR%"

:: 拉取最新代码
git pull origin main >> "%LOG_FILE%" 2>&1

:: 运行更新
python update_market.py --skip-automation >> "%LOG_FILE%" 2>&1

:: 提交更改
git add index.json plugins.json apps/ plugins/ experimental/
git diff --staged --quiet
if errorlevel 1 (
    git commit -m "chore: 市场仓库自动更新 [skip ci]" >> "%LOG_FILE%" 2>&1
    git push origin main >> "%LOG_FILE%" 2>&1
    echo [!DATE_STR!] 更新完成并已推送 >> "%LOG_FILE%"
) else (
    echo [!DATE_STR!] 无变化 >> "%LOG_FILE%"
)

echo [!DATE_STR!] 执行完成 >> "%LOG_FILE%"
