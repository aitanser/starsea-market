#!/usr/bin/env python3
# sysinfo_plus.py
# 作者: 鸿渚 | 蓝域星河
# 版权: © 2026 鸿渚 - 蓝域星河. All rights reserved.

import platform
import os
import sys
import socket

def run(args, lang, lang_code, current_user):
    print("\n===== 增强系统信息 =====")
    print(f"操作系统: {platform.system()} {platform.release()}")
    print(f"架构: {platform.machine()}")
    print(f"处理器: {platform.processor() or '未知'}")
    print(f"主机名: {socket.gethostname()}")
    print(f"Python版本: {sys.version.split()[0]}")
    print(f"当前目录: {os.getcwd()}")
    print(f"用户: {current_user.get('username', '未知')}")
    print(f"角色: {current_user.get('role', '未知')}")
