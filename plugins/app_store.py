# app_store.py - 星海量子应用商店（仅管理本地已安装应用）
import os
from system.plugin_manager import PLUGIN_DIR
from system.app_registry import get_all_apps, unregister_app

def app_store_menu():
    while True:
        print("\n===== 星海量子应用商店 =====")
        print("1. 查看已安装应用")
        print("2. 卸载应用")
        print("0. 退出")
        choice = input("请选择: ").strip()
        if choice == '1':
            list_installed_apps()
        elif choice == '2':
            uninstall_app()
        elif choice == '0':
            break
        else:
            print("无效选择。")

def list_installed_apps():
    registry = get_all_apps()
    if not registry:
        print("暂无已安装的应用。")
        return
    print("\n已安装应用列表：")
    for cmd, info in registry.items():
        print(f"  {cmd} - {info['name']} [{info.get('type', 'unknown')}]")
        if info.get('desc'):
            print(f"      描述: {info['desc']}")

def uninstall_app():
    registry = get_all_apps()
    if not registry:
        print("没有可卸载的应用。")
        return
    print("\n可卸载的应用：")
    for cmd, info in registry.items():
        print(f"  {cmd} - {info['name']}")
    cmd = input("\n请输入要卸载的应用命令名: ").strip()
    if cmd not in registry:
        print("未找到该应用。")
        return
    if unregister_app(cmd):
        plugin_file = os.path.join(PLUGIN_DIR, cmd + '.py')
        if os.path.exists(plugin_file):
            os.remove(plugin_file)
        print(f"应用 '{cmd}' 已成功卸载。")
    else:
        print("卸载失败，请检查权限或应用状态。")
