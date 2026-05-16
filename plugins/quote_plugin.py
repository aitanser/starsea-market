#!/usr/bin/env python3
# quote_plugin.py
# 作者: 鸿渚 | 蓝域星河
# 版权: © 2026 鸿渚 - 蓝域星河. All rights reserved.

import random

QUOTES = [
    ("Stay hungry, stay foolish.", "Steve Jobs"),
    ("The only way to do great work is to love what you do.", "Steve Jobs"),
    ("In the middle of difficulty lies opportunity.", "Albert Einstein"),
    ("Imagination is more important than knowledge.", "Albert Einstein"),
    ("Code is like humor. When you have to explain it, it's bad.", "Cory House"),
    ("First, solve the problem. Then, write the code.", "John Johnson"),
    ("Talk is cheap. Show me the code.", "Linus Torvalds"),
    ("The best error message is the one that never shows up.", "Thomas Fuchs"),
    ("Any fool can write code that a computer can understand. Good programmers write code that humans can understand.", "Martin Fowler"),
    ("Experience is the name everyone gives to their mistakes.", "Oscar Wilde"),
]

def run(args, lang, lang_code, current_user):
    quote, author = random.choice(QUOTES)
    print(f'"{quote}"')
    print(f"  —— {author}")
