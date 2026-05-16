#!/usr/bin/env python3
# app_store.py
# 作者: 鸿渚 | 蓝域星河
# 版权: © 2026 鸿渚 - 蓝域星河. All rights reserved.

import os
from system.plugin_manager import list_plugins, PLUGIN_DIR

MOCK_STORE = {
    "hello": {"name": "Hello World", "desc": "问候插件", "version": "1.0"},
    "disk_check": {"name": "磁盘检查", "desc": "查看磁盘使用", "version": "1.2"},
    "show_config": {"name": "配置查看", "desc": "查看系统配置（需权限）", "version": "1.0"},
}

def app_store_menu():
    while True:
        print("\n===== 应用商店 =====")
        print("1. 浏览已安装  2. 浏览远程商店  3. 安装插件")
        print("4. 卸载插件    5. 更新插件      0. 退出")
        choice = input("请选择: ").strip()
        if choice == '1':
            plugins = list_plugins()
            if plugins:
                print("已安装插件:")
                for p in plugins:
                    info = MOCK_STORE.get(p, {})
                    name = info.get('name', p)
                    ver = info.get('version', '?')
                    print(f"  📦 {name} ({p}) v{ver}")
            else:
                print("暂无已安装插件。")
        elif choice == '2':
            print("远程商店可用插件:")
            for key, info in MOCK_STORE.items():
                installed = key in list_plugins()
                print(f"  {'✅' if installed else '⬇️'} {info['name']} - {info['desc']} (v{info['version']})")
        elif choice == '3':
            name = input("输入插件名（英文ID）: ").strip()
            if name in MOCK_STORE:
                plugin_content = f"""# 插件: {name}
def run(args, lang, lang_code, current_user):
    print("插件 {name} 已运行。")
"""
                dest = os.path.join(PLUGIN_DIR, name + '.py')
                with open(dest, 'w', encoding='utf-8') as f:
                    f.write(plugin_content)
                print(f"插件 {name} 安装成功。")
            else:
                print("插件不存在于远程商店。")
        elif choice == '4':
            name = input("要卸载的插件名（英文ID）: ").strip()
            plugin_path = os.path.join(PLUGIN_DIR, name + '.py')
            if os.path.exists(plugin_path):
                os.remove(plugin_path)
                print(f"插件 {name} 已卸载。")
            else:
                print("插件不存在。")
        elif choice == '5':
            name = input("要更新的插件名: ").strip()
            if name in list_plugins() and name in MOCK_STORE:
                dest = os.path.join(PLUGIN_DIR, name + '.py')
                with open(dest, 'w', encoding='utf-8') as f:
                    f.write(f"# 插件: {name}\ndef run(args, lang, lang_code, current_user):\n    print('插件 {name} 已更新运行。')\n")
                print(f"插件 {name} 已更新。")
            else:
                print("无法更新。")
        elif choice == '0':
            break
        else:
            print("无效选择。")
