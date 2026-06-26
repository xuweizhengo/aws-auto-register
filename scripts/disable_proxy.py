#!/usr/bin/env python3
"""
临时配置切换工具 - 禁用代理
"""

import yaml
from pathlib import Path

config_path = Path(__file__).parent / "config.yaml"

# 读取配置
with open(config_path, 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

# 禁用代理
config['region']['use_proxy'] = False

# 保存配置
with open(config_path, 'w', encoding='utf-8') as f:
    yaml.dump(config, f, allow_unicode=True, sort_keys=False)

print("✅ 代理已临时禁用")
print("   如需重新启用，手动修改 config.yaml 中的 use_proxy: true")
