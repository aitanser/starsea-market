#!/usr/bin/env python3
# sysinfo_plus.py
# 作者: 鸿渚 | 蓝域星河
# 版权: © 2026 鸿渚 - 蓝域星河. All rights reserved.

import platform
import sys
import os

try:
    import psutil
    HAS_PSUTIL = True
except ImportError:
    HAS_PSUTIL = False

def run(args, lang, lang_code, current_user):
    print("=== 系统信息 (增强) ===")
    print(f"操作系统: {platform.platform()}")
    print(f"Python版本: {sys.version}")
    print(f"当前用户: {current_user['username']} ({current_user['role']})")
    print(f"工作目录: {os.getcwd()}")
    if HAS_PSUTIL:
        mem = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        print(f"内存: {mem.percent}% ({mem.used//1024**2}/{mem.total//1024**2} MB)")
        print(f"磁盘: {disk.percent}% ({disk.free//1024**2}/{disk.total//1024**2} MB)")
        net = psutil.net_io_counters()
        print(f"网络: 发送 {net.bytes_sent//1024} KB, 接收 {net.bytes_recv//1024} KB")
    else:
        print("psutil未安装，无法显示资源信息。")
