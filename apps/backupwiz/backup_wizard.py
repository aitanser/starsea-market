#!/usr/bin/env python3
# backup_wizard.py
# 作者: 鸿渚 | 蓝域星河
# 版权: © 2026 鸿渚 - 蓝域星河. All rights reserved.

import os
import shutil
from system.restore_points import create_restore_point, list_restore_points, restore_to_point
from system.backup_versioning import create_versioned_backup, list_versioned_backups

def backup_wizard_menu():
    while True:
        print("\n===== 备份还原向导 =====")
        print("1. 创建还原点")
        print("2. 查看还原点")
        print("3. 恢复到还原点")
        print("4. 创建版本化备份")
        print("5. 查看版本化备份")
        print("6. 从版本化备份恢复")
        print("0. 退出")
        choice = input("请选择: ").strip()
        if choice == '1':
            desc = input("还原点描述: ").strip()
            create_restore_point(desc)
        elif choice == '2':
            points = list_restore_points()
            if points:
                for i, (name, desc) in enumerate(points, 1):
                    print(f"{i}. {name} - {desc}")
            else:
                print("暂无还原点。")
        elif choice == '3':
            points = list_restore_points()
            if not points:
                print("无还原点可恢复。")
                continue
            idx = int(input("输入还原点编号: ").strip())
            if 1 <= idx <= len(points):
                restore_to_point(points[idx-1][0])
            else:
                print("无效编号。")
        elif choice == '4':
            desc = input("备份描述: ").strip()
            create_versioned_backup(desc)
        elif choice == '5':
            backups = list_versioned_backups()
            if backups:
                for i, (ts, desc) in enumerate(backups, 1):
                    print(f"{i}. {ts} - {desc}")
            else:
                print("暂无版本化备份。")
        elif choice == '6':
            backups = list_versioned_backups()
            if not backups:
                print("无备份可恢复。")
                continue
            idx = int(input("输入备份编号: ").strip())
            if 1 <= idx <= len(backups):
                folder = os.path.join("backup_archive", backups[idx-1][0])
                if os.path.exists(folder):
                    for f in os.listdir(folder):
                        if f.endswith('.lyxh.enc'):
                            shutil.copy2(os.path.join(folder, f), '.')
                    print("已恢复，请重启系统。")
                else:
                    print("备份文件夹不存在。")
            else:
                print("无效编号。")
        elif choice == '0':
            break
        else:
            print("无效选择。")
