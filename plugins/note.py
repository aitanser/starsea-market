#!/usr/bin/env python3
# note.py
# 作者: 鸿渚 | 蓝域星河
# 版权: © 2026 鸿渚 - 蓝域星河. All rights reserved.

from starsea_sdk.errors import ConfigError

def note_menu(client, config_path):
    print("\n===== 星海便签 =====")
    notes_file = "/notes.txt"
    try:
        content = client.vfs_read(config_path, notes_file)
    except ConfigError:
        content = ""
    notes = content.split('\n') if content else []

    while True:
        print(f"\n当前便签数: {len(notes)}")
        print("1. 查看所有便签")
        print("2. 添加便签")
        print("3. 删除便签")
        print("4. 清空便签")
        print("0. 退出")
        choice = input("请选择: ").strip()
        if choice == '1':
            if notes:
                for i, note in enumerate(notes, 1):
                    print(f"{i}. {note}")
            else:
                print("暂无便签。")
        elif choice == '2':
            text = input("输入新便签: ").strip()
            if text:
                notes.append(text)
                _save(client, config_path, notes_file, notes)
                print("已添加。")
        elif choice == '3':
            idx = int(input("输入要删除的便签编号: ").strip())
            if 1 <= idx <= len(notes):
                del notes[idx-1]
                _save(client, config_path, notes_file, notes)
                print("已删除。")
            else:
                print("无效编号。")
        elif choice == '4':
            notes = []
            _save(client, config_path, notes_file, notes)
            print("已清空。")
        elif choice == '0':
            break
        else:
            print("无效选择。")

def _save(client, config_path, path, notes_list):
    content = '\n'.join(notes_list)
    client.vfs_write(config_path, path, content)
