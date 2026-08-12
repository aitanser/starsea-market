#!/usr/bin/env python3
# calendar.py
# 作者: 鸿渚 | 蓝域星河
# 版权: © 2026 鸿渚 - 蓝域星河. All rights reserved.

from datetime import datetime
import calendar as cal_module
from starsea_sdk.errors import ConfigError

EVENTS_KEY = "calendar_events"

def calendar_menu(client, config_path):
    while True:
        print("\n===== 日历与提醒 =====")
        print("1. 查看日历 (当月)")
        print("2. 添加事件")
        print("3. 查看所有事件")
        print("4. 删除事件")
        print("5. 今日提醒")
        print("0. 退出")
        choice = input("请选择: ").strip()
        try:
            config = client.load_config(config_path)
            events = config.get(EVENTS_KEY, [])
            if choice == '1':
                now = datetime.now()
                print(f"\n{now.year}年 {now.month}月")
                cal = cal_module.month(now.year, now.month)
                print(cal)
            elif choice == '2':
                date_str = input("日期 (YYYY-MM-DD): ").strip()
                datetime.strptime(date_str, "%Y-%m-%d")
                title = input("事件标题: ").strip()
                events.append({"date": date_str, "title": title})
                config[EVENTS_KEY] = events
                client.save_config(config_path, config)
                print("事件已添加。")
            elif choice == '3':
                if events:
                    for i, e in enumerate(events, 1):
                        print(f"{i}. [{e['date']}] {e['title']}")
                else:
                    print("无事件。")
            elif choice == '4':
                if not events:
                    print("无事件可删除。")
                    continue
                idx = int(input("输入事件编号: ").strip())
                if 1 <= idx <= len(events):
                    del events[idx - 1]
                    config[EVENTS_KEY] = events
                    client.save_config(config_path, config)
                    print("已删除。")
            elif choice == '5':
                today = datetime.now().strftime("%Y-%m-%d")
                today_events = [e for e in events if e['date'] == today]
                if today_events:
                    print(f"今日提醒 ({today}):")
                    for e in today_events:
                        print(f"  - {e['title']}")
                else:
                    print("今日无事件。")
            elif choice == '0':
                break
        except ConfigError as e:
            print(f"错误: {e}")
