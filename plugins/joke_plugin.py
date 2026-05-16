#!/usr/bin/env python3
# joke_plugin.py
# 作者: 鸿渚 | 蓝域星河
# 版权: © 2026 鸿渚 - 蓝域星河. All rights reserved.

import random

JOKES = [
    "我问我的狗：'你会汪吗？' 它说：'喵。'",
    "为什么程序员总是搞混圣诞节和万圣节？因为 Oct 31 == Dec 25。",
    "为什么Python程序员不使用Java？因为他们有自己的咖啡（coffee）。",
    "敲代码的都知道：世界上有两种错误，一种是错误，另一种是你还在寻找。",
    "如果你想精通Python，就试着用列表推导式写一封情书。",
    "程序员最讨厌的数字是：1024。因为加班太多了。",
    "从前有个程序员，他从来不写注释，后来没有人知道他是怎么死的。",
    "为什么程序员不喜欢森林？因为太多分支了。",
    "我是一个简单的程序员，我的需求是：能跑就行。",
    "你的代码就像一首诗：没人看得懂。",
]

def run(args, lang, lang_code, current_user):
    print(random.choice(JOKES))
