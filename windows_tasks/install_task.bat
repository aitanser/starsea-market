@echo off
:: ============================================================
:: 安装星海市场自动更新计划任务
:: 以管理员身份运行
:: ============================================================

echo ============================================================
echo  星海市场 · 安装自动更新计划任务
echo ============================================================

:: 获取当前目录
set TASK_DIR=%~dp0..
set TASK_SCRIPT=%TASK_DIR%\windows_tasks\update.bat

echo 任务目录: %TASK_DIR%
echo 任务脚本: %TASK_SCRIPT%

:: 创建计划任务（每6小时运行）
schtasks /create /tn "StarseaMarketUpdate" ^
    /tr "%TASK_SCRIPT%" ^
    /sc hourly /mo 6 ^
    /ru SYSTEM ^
    /rl HIGHEST ^
    /f

if errorlevel 1 (
    echo [错误] 任务创建失败
    pause
    exit /b 1
)

echo [成功] 计划任务创建成功
echo    任务名称: StarseaMarketUpdate
echo    运行频率: 每6小时
echo    运行用户: SYSTEM
echo.
echo 手动触发:
echo   schtasks /run /tn "StarseaMarketUpdate"
echo.
echo 查看任务:
echo   schtasks /query /tn "StarseaMarketUpdate" /v
pause
