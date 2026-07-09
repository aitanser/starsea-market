#!/usr/bin/env python3
# text_editor.py
# 作者: 鸿渚 | 蓝域星河
# 版权: © 2026 鸿渚 - 蓝域星河. All rights reserved.

from starsea_sdk.errors import ConfigError

def text_editor_menu(client, config_path):
    current_file = None
    current_buffer = []
    while True:
        print(f"\n===== 文本编辑器 =====")
        print(f"当前文件: {current_file or '无'}")
        print(f"缓冲区行数: {len(current_buffer)}")
        print("1. 打开文件 (虚拟)  2. 查看内容  3. 添加行")
        print("4. 插入行           5. 删除行   6. 替换行")
        print("7. 保存             8. 另存为   0. 退出")
        choice = input("请选择: ").strip()
        try:
            if choice == '1':
                path = input("虚拟文件路径（绝对）: ").strip()
                content = client.vfs_read(config_path, path)
                current_buffer = content.split('\n') if content else ['']
                current_file = path
                print(f"已打开: {path}")
            elif choice == '2':
                for i, line in enumerate(current_buffer, 1):
                    print(f"{i:4d}: {line}")
            elif choice == '3':
                line = input("新行内容: ")
                current_buffer.append(line)
            elif choice == '4':
                num = int(input("插入行号: ").strip())
                text = input("内容: ")
                if 1 <= num <= len(current_buffer) + 1:
                    current_buffer.insert(num - 1, text)
            elif choice == '5':
                num = int(input("删除行号: ").strip())
                if 1 <= num <= len(current_buffer):
                    current_buffer.pop(num - 1)
            elif choice == '6':
                num = int(input("替换行号: ").strip())
                text = input("新内容: ")
                if 1 <= num <= len(current_buffer):
                    current_buffer[num - 1] = text
            elif choice == '7':
                if not current_file:
                    print("请先打开文件。")
                    continue
                client.vfs_write(config_path, current_file, '\n'.join(current_buffer))
                print("文件已保存。")
            elif choice == '8':
                new_path = input("另存为路径: ").strip()
                client.vfs_write(config_path, new_path, '\n'.join(current_buffer))
                print("已另存为。")
            elif choice == '0':
                break
        except ConfigError as e:
            print(f"错误: {e}")
