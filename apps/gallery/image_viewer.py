#!/usr/bin/env python3
# image_viewer.py
# 作者: 鸿渚 | 蓝域星河
# 版权: © 2026 鸿渚 - 蓝域星河. All rights reserved.

import os
import time
try:
    from PIL import Image
    HAS_PIL = True
except ImportError:
    HAS_PIL = False

def display_ascii(path, width=80):
    if not HAS_PIL:
        print("请安装 Pillow: pip install Pillow")
        return
    try:
        img = Image.open(path)
        aspect = img.height / img.width / 2
        height = int(aspect * width)
        img = img.resize((width, height)).convert('L')
        chars = "@%#*+=-:. "
        result = []
        for y in range(height):
            row = []
            for x in range(width):
                row.append(chars[img.getpixel((x, y)) * len(chars) // 256])
            result.append(''.join(row))
        print('\n'.join(result))
    except Exception as e:
        print(f"无法显示: {e}")

def gallery_menu():
    current_dir = '.'
    while True:
        print("\n===== 图库 =====")
        print(f"当前目录: {current_dir}")
        print("1. 浏览图片列表  2. 查看图片  3. 幻灯片播放")
        print("4. 更改目录      0. 退出")
        choice = input("请选择: ").strip()
        exts = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')
        if choice == '1':
            files = [f for f in os.listdir(current_dir) if f.lower().endswith(exts)]
            if files:
                print("图片列表:")
                for i, f in enumerate(files, 1):
                    print(f"  {i}. {f}")
            else:
                print("该目录下没有图片文件。")
        elif choice == '2':
            idx = input("输入图片序号（或直接输入文件名）: ").strip()
            if idx.isdigit():
                files = [f for f in os.listdir(current_dir) if f.lower().endswith(exts)]
                if 0 < int(idx) <= len(files):
                    path = os.path.join(current_dir, files[int(idx)-1])
                    width = input("宽度（默认80）: ").strip() or '80'
                    display_ascii(path, int(width))
                else:
                    print("序号无效。")
            else:
                path = os.path.join(current_dir, idx)
                if os.path.exists(path):
                    display_ascii(path)
                else:
                    print("文件不存在。")
        elif choice == '3':
            files = [f for f in os.listdir(current_dir) if f.lower().endswith(exts)]
            if not files:
                print("无图片。")
                continue
            try:
                interval = input("间隔秒数（默认2）: ").strip() or '2'
                print("开始幻灯片播放，按 Ctrl+C 停止。")
                for f in files:
                    path = os.path.join(current_dir, f)
                    display_ascii(path, 80)
                    time.sleep(int(interval))
            except KeyboardInterrupt:
                print("停止播放。")
        elif choice == '4':
            new_dir = input("输入目录路径: ").strip()
            if os.path.isdir(new_dir):
                current_dir = new_dir
            else:
                print("目录无效。")
        elif choice == '0':
            break
        else:
            print("无效选择。")
