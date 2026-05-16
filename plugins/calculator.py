#!/usr/bin/env python3
# calculator.py
# 作者: 鸿渚 | 蓝域星河
# 版权: © 2026 鸿渚 - 蓝域星河. All rights reserved.

import math

HISTORY = []

def calculator_menu():
    print("\n===== 星海量子科学计算器 =====")
    print("支持：+ - * / ** sqrt sin cos tan log ln 单位转换")
    print("示例：2+3, sqrt(16), sin(30), unit 10 km to mile")
    while True:
        expr = input("计算表达式 (输入 'history' 查看历史, 'exit' 退出): ").strip()
        if expr.lower() == 'exit':
            break
        elif expr.lower() == 'history':
            if HISTORY:
                for i, h in enumerate(HISTORY, 1):
                    print(f"{i}: {h}")
            else:
                print("暂无历史记录。")
            continue
        elif expr.lower().startswith('unit '):
            parts = expr.split()
            if len(parts) == 5 and parts[3] == 'to':
                try:
                    value = float(parts[1])
                    unit_from = parts[2]
                    unit_to = parts[4]
                    result = convert_unit(value, unit_from, unit_to)
                    print(f"{value} {unit_from} = {result} {unit_to}")
                    HISTORY.append(f"{expr} = {result}")
                except Exception as e:
                    print(f"转换错误: {e}")
            else:
                print("格式: unit <数值> <原单位> to <目标单位>")
            continue
        else:
            safe_expr = expr.replace('^', '**')
            try:
                result = eval(safe_expr, {"__builtins__": {}}, {
                    "sqrt": math.sqrt, "sin": math.sin, "cos": math.cos,
                    "tan": math.tan, "log": math.log10, "ln": math.log,
                    "pi": math.pi, "e": math.e, "radians": math.radians
                })
                print(f"结果: {result}")
                HISTORY.append(f"{expr} = {result}")
            except Exception as e:
                print(f"计算错误: {e}")

def convert_unit(value, unit_from, unit_to):
    conversions = {
        'km_to_mile': 0.621371,
        'mile_to_km': 1.60934,
        'kg_to_lb': 2.20462,
        'lb_to_kg': 0.453592,
        'c_to_f': lambda v: v * 9/5 + 32,
        'f_to_c': lambda v: (v - 32) * 5/9,
    }
    key = f"{unit_from}_to_{unit_to}"
    if key in conversions:
        conv = conversions[key]
        return conv(value) if callable(conv) else value * conv
    else:
        raise ValueError("不支持的单位转换")
