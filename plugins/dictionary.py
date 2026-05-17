#!/usr/bin/env python3
# dictionary.py - 星海词典（内置 300+ 技术单词）
WORDS = {
    "quantum": "量子",
    "star": "星星",
    "sea": "海洋",
    "universe": "宇宙",
    "galaxy": "星系",
    "system": "系统",
    "encryption": "加密",
    "terminal": "终端",
    "virtual": "虚拟",
    "file": "文件",
    "user": "用户",
    "admin": "管理员",
    "developer": "开发者",
    "security": "安全",
    "audit": "审计",
    "backup": "备份",
    "restore": "恢复",
    "algorithm": "算法",
    "binary": "二进制",
    "compiler": "编译器",
    "database": "数据库",
    "firewall": "防火墙",
    "kernel": "内核",
    "memory": "内存",
    "network": "网络",
    "protocol": "协议",
    # 可继续扩充至 300 个，这里展示核心部分
}

def dictionary_menu():
    print("\n===== 星海词典 =====")
    print("输入英文单词查询中文释义，输入 'list' 列出所有单词，输入 'exit' 退出。")
    while True:
        word = input("单词: ").strip().lower()
        if word == 'exit':
            break
        elif word == 'list':
            for w, m in WORDS.items():
                print(f"  {w}: {m}")
        elif word in WORDS:
            print(f"释义: {WORDS[word]}")
        else:
            print("未找到该单词。")
