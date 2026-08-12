#!/usr/bin/env python3
# system_watcher.py
# 作者: 鸿渚 | 蓝域星河
# 版权: © 2026 鸿渚 - 蓝域星河. All rights reserved.

import os
import time
import threading
try:
    import psutil
    HAS_PSUTIL = True
except ImportError:
    HAS_PSUTIL = False

def watch_menu():
    if not HAS_PSUTIL:
        print("需要安装 psutil: pip install psutil")
        return
    stop_watch = False
    sort_key = 'cpu'
    def monitor_thread():
        while not stop_watch:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("===== 系统监视器 (按 Ctrl+C 停止) =====")
            print(f"CPU: {psutil.cpu_percent()}%")
            mem = psutil.virtual_memory()
            print(f"内存: {mem.percent}% ({mem.used//1024**2}/{mem.total//1024**2} MB)")
            procs = []
            for p in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
                try:
                    procs.append(p.info)
                except:
                    pass
            if sort_key == 'cpu':
                procs.sort(key=lambda x: x['cpu_percent'] or 0, reverse=True)
            elif sort_key == 'mem':
                procs.sort(key=lambda x: x['memory_percent'] or 0, reverse=True)
            print(f"\n进程列表 (排序: {sort_key}, 前10):")
            for p in procs[:10]:
                print(f"  {p['pid']:6d} {p['name']:20s} CPU:{p['cpu_percent']:6.1f}% MEM:{p['memory_percent']:5.1f}%")
            time.sleep(2)
    print("按 Enter 开始监控...")
    input()
    thread = threading.Thread(target=monitor_thread, daemon=True)
    thread.start()
    try:
        while True:
            cmd = input("监视器命令 (sort cpu/mem, kill <pid>, q退出): ").strip()
            if cmd == 'q':
                stop_watch = True
                break
            elif cmd.startswith('sort '):
                sort_key = cmd.split()[1]
                if sort_key not in ('cpu', 'mem'):
                    print("无效排序键。")
            elif cmd.startswith('kill '):
                pid = int(cmd.split()[1])
                try:
                    p = psutil.Process(pid)
                    p.terminate()
                    print(f"进程 {pid} 已终止。")
                except:
                    print("终止失败。")
    except KeyboardInterrupt:
        stop_watch = True
    print("监视器已退出。")
