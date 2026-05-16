#!/usr/bin/env python3
# file_manager.py
# 作者: 鸿渚 | 蓝域星河
# 版权: © 2026 鸿渚 - 蓝域星河. All rights reserved.

from starsea_sdk.errors import ConfigError

def file_manager_menu(client, config_path):
    print("\n===== 星海量子文件管理器 =====")
    cwd = "/"
    while True:
        print(f"\n当前目录: {cwd}")
        print("1. 列出内容   2. 创建目录   3. 创建文件")
        print("4. 删除       5. 读取文件   6. 写入文件")
        print("7. 搜索       8. 复制/移动  9. 批量删除")
        print("0. 退出")
        choice = input("请选择: ").strip()
        try:
            if choice == '1':
                items = client.vfs_list(config_path, cwd)
                for name, kind in items:
                    print(f"  {'📁' if kind == 'dir' else '📄'} {name}")
            elif choice == '2':
                name = input("新目录名: ").strip()
                new_path = (cwd + '/' + name) if cwd != '/' else '/' + name
                client.vfs_mkdir(config_path, new_path)
                print("目录已创建。")
            elif choice == '3':
                name = input("新文件名: ").strip()
                new_path = (cwd + '/' + name) if cwd != '/' else '/' + name
                client.vfs_touch(config_path, new_path)
                print("文件已创建。")
            elif choice == '4':
                target = input("删除目标（相对路径）: ").strip()
                del_path = (cwd + '/' + target) if cwd != '/' else '/' + target
                client.vfs_delete(config_path, del_path)
                print("已删除。")
            elif choice == '5':
                name = input("文件名: ").strip()
                read_path = (cwd + '/' + name) if cwd != '/' else '/' + name
                content = client.vfs_read(config_path, read_path)
                print(content if content else "(空文件)")
            elif choice == '6':
                name = input("文件名: ").strip()
                write_path = (cwd + '/' + name) if cwd != '/' else '/' + name
                content = input("内容: ")
                client.vfs_write(config_path, write_path, content)
                print("写入成功。")
            elif choice == '7':
                keyword = input("搜索关键词: ").strip()
                results = client.vfs_search(config_path, keyword)
                if results:
                    print("搜索结果:")
                    for r in results:
                        print(f"  ✨ {r}")
                else:
                    print("未找到。")
            elif choice == '8':
                sub = input("1.复制 2.移动: ").strip()
                src = input("源路径（相对当前目录）: ").strip()
                dst = input("目标路径（绝对或相对）: ").strip()
                src_path = (cwd + '/' + src) if cwd != '/' else '/' + src
                dst_path = dst if dst.startswith('/') else (cwd + '/' + dst) if cwd != '/' else '/' + dst
                content = client.vfs_read(config_path, src_path)
                client.vfs_write(config_path, dst_path, content)
                if sub == '2':
                    client.vfs_delete(config_path, src_path)
                print("操作完成。")
            elif choice == '9':
                targets = input("输入要删除的文件/目录（空格分隔）: ").strip().split()
                for t in targets:
                    del_path = (cwd + '/' + t) if cwd != '/' else '/' + t
                    client.vfs_delete(config_path, del_path)
                print("批量删除完成。")
            elif choice == '0':
                break
            else:
                print("无效选择。")
        except ConfigError as e:
            print(f"操作失败: {e}")
