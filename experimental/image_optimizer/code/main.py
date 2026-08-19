#!/usr/bin/env python3
# main.py
# 作者: 鸿渚 | 蓝域星河
# 版权: © 2026 鸿渚 - 蓝域星河. All rights reserved.

"""
图片压缩器 - 实验性功能
"""

import os
from pathlib import Path


def run():
    print("\n" + "=" * 50)
    print("  🖼️ 图片压缩器 (实验性功能)")
    print("=" * 50)
    print("警告: 此功能需要安装 Pillow 库")
    print("      pip install Pillow")
    print()

    try:
        from PIL import Image
    except ImportError:
        print("❌ Pillow 未安装，请执行: pip install Pillow")
        return

    path = input("请输入图片目录路径: ").strip()
    if not path or not os.path.exists(path):
        print("路径不存在")
        return

    quality = input("压缩质量 (1-100, 默认 75): ").strip()
    quality = int(quality) if quality.isdigit() else 75
    quality = max(1, min(100, quality))

    count = 0
    for f in Path(path).glob("*"):
        if f.suffix.lower() in ['.jpg', '.jpeg', '.png']:
            try:
                img = Image.open(f)
                out_path = f.parent / f"{f.stem}_compressed{f.suffix}"
                img.save(out_path, quality=quality, optimize=True)
                count += 1
                print(f"  ✅ {f.name} -> {out_path.name}")
            except Exception as e:
                print(f"  ❌ {f.name}: {e}")

    print(f"\n✅ 压缩完成，共处理 {count} 张图片")


if __name__ == "__main__":
    run()
