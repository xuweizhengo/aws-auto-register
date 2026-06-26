#!/usr/bin/env python3
"""
设备类型切换工具
快速在桌面和移动设备之间切换
"""

import yaml
import sys
from pathlib import Path


def switch_device(device_type: str):
    """切换设备类型"""
    valid_devices = ['desktop', 'mobile']
    
    if device_type not in valid_devices:
        print(f"❌ 无效的设备类型: {device_type}")
        print(f"✅ 可用类型: {', '.join(valid_devices)}")
        return False
    
    config_path = Path(__file__).parent / "config.yaml"
    
    # 读取配置
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    
    # 更新设备类型
    old_device = config['region'].get('device_type', 'desktop')
    config['region']['device_type'] = device_type
    
    # 保存配置
    with open(config_path, 'w', encoding='utf-8') as f:
        yaml.dump(config, f, allow_unicode=True, sort_keys=False)
    
    emoji = "📱" if device_type == "mobile" else "💻"
    print(f"{emoji} 设备类型已切换: {old_device} -> {device_type}")
    
    # 显示当前配置
    region = config['region']['current']
    profile = config['region']['profiles'][region]
    
    ua_key = f"{device_type}_user_agents"
    user_agents = profile.get(ua_key, [])
    
    print(f"\n📱 当前配置:")
    print(f"  设备类型: {device_type.upper()}")
    print(f"  地区: {region.upper()}")
    print(f"  User-Agent 数量: {len(user_agents)}")
    if user_agents:
        print(f"  示例 UA: {user_agents[0][:80]}...")
    
    return True


def show_current():
    """显示当前设备配置"""
    config_path = Path(__file__).parent / "config.yaml"
    
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    
    device_type = config['region'].get('device_type', 'desktop')
    region = config['region']['current']
    profile = config['region']['profiles'][region]
    
    emoji = "📱" if device_type == "mobile" else "💻"
    print(f"{emoji} 当前设备类型: {device_type.upper()}")
    print(f"📍 地区: {region.upper()}")
    
    ua_key = f"{device_type}_user_agents"
    user_agents = profile.get(ua_key, [])
    print(f"🔧 User-Agent 数量: {len(user_agents)}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法:")
        print("  查看当前配置: python switch_device.py show")
        print("  切换设备类型: python switch_device.py [desktop|mobile]")
        print()
        show_current()
    elif sys.argv[1] == "show":
        show_current()
    else:
        switch_device(sys.argv[1].lower())
