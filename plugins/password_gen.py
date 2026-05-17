#!/usr/bin/env python3
# password_gen.py - 随机密码生成器
import random
import string

def run(args, lang, lang_code, current_user):
    length = 16
    if args and args[0].isdigit():
        length = int(args[0])
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = ''.join(random.choices(chars, k=length))
    print(f"生成的密码: {password}")
    print(f"长度: {length}")
