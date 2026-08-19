#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# webhook_server.py
# 作者: 鸿渚 | 蓝域星河
# 版权: © 2026 鸿渚 - 蓝域星河. All rights reserved.

"""
星海市场 · Webhook 服务
自动响应 GitHub Webhook 触发更新

启动: python webhook_server.py
"""

import os
import sys
import json
import subprocess
import threading
from pathlib import Path
from flask import Flask, request, jsonify

SCRIPT_DIR = Path(__file__).parent.resolve()
CONFIG_FILE = SCRIPT_DIR / ".automation" / "webhook_config.json"

DEFAULT_CONFIG = {
    "port": 8080,
    "secret": "",
    "allowed_events": ["push", "workflow_dispatch"],
    "log_file": "logs/webhook.log"
}


def load_config():
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)
    else:
        config = DEFAULT_CONFIG
        CONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(CONFIG_FILE, 'w') as f:
            json.dump(config, f, indent=2)
    return config


def run_update():
    try:
        result = subprocess.run(
            [sys.executable, "update_market.py", "--skip-automation"],
            cwd=SCRIPT_DIR,
            capture_output=True,
            text=True,
            timeout=300
        )
        subprocess.run(
            ["git", "add", "index.json", "plugins.json", "apps/", "plugins/", "experimental/"],
            cwd=SCRIPT_DIR
        )
        subprocess.run(
            ["git", "commit", "-m", "chore: Webhook 触发更新 [skip ci]"],
            cwd=SCRIPT_DIR,
            capture_output=True
        )
        subprocess.run(["git", "push"], cwd=SCRIPT_DIR, capture_output=True)
        return result.returncode == 0
    except Exception as e:
        print(f"更新失败: {e}")
        return False


app = Flask(__name__)
config = load_config()


@app.route('/webhook', methods=['POST'])
def webhook():
    event = request.headers.get('X-GitHub-Event', '')
    secret = request.headers.get('X-Webhook-Secret', '')

    webhook_secret = os.environ.get('WEBHOOK_SECRET', config.get('secret', ''))
    if webhook_secret and secret != webhook_secret:
        return jsonify({"error": "Invalid secret"}), 401

    if event == 'ping':
        return jsonify({"status": "ok", "message": "ping received"})

    if event not in config.get('allowed_events', ['push']):
        return jsonify({"status": "ignored", "event": event})

    def do_update():
        success = run_update()
        print(f"[Webhook] 更新 {'成功' if success else '失败'}")

    threading.Thread(target=do_update, daemon=True).start()
    return jsonify({"status": "started", "event": event})


@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})


if __name__ == '__main__':
    port = int(os.environ.get('PORT', config.get('port', 8080)))
    print(f"星海市场 Webhook 服务启动: http://0.0.0.0:{port}")
    app.run(host='0.0.0.0', port=port, debug=False)
