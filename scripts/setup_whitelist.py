#!/usr/bin/env python3
"""
代理白名单手动配置工具
用于测试和配置白名单参数
"""

import requests
import sys


def test_whitelist_api():
    """测试白名单API的不同参数组合"""
    
    print("=" * 70)
    print("代理白名单API测试工具")
    print("=" * 70)
    
    # 获取当前IP
    print("\n1️⃣  获取当前公网IP...")
    try:
        ip = requests.get('https://api.ipify.org', timeout=5).text.strip()
        print(f"   ✅ 当前IP: {ip}")
    except:
        print("   ⚠️  获取IP失败")
        ip = input("   请手动输入你的公网IP: ").strip()
    
    # 输入API Key
    print("\n2️⃣  输入API配置:")
    key = input("   API Key: ").strip()
    if not key:
        print("   ❌ API Key 不能为空")
        return False
    brand = input("   Brand (默认: 2): ").strip() or "2"
    
    # 测试不同的API调用方式
    print("\n3️⃣  开始测试API...")
    print("-" * 70)
    
    # 测试1: 不使用sign
    print("\n📝 测试1: 不使用sign参数")
    url1 = f"http://your-proxy-api.com/white/add?key={key}&brand={brand}&ip={ip}"
    print(f"   URL: {url1}")
    try:
        resp = requests.get(url1, timeout=10)
        print(f"   状态码: {resp.status_code}")
        print(f"   响应: {resp.text[:200]}")
        if resp.status_code == 200:
            print("   ✅ 成功!")
            return True
    except Exception as e:
        print(f"   ❌ 失败: {e}")
    
    # 测试2: 使用空sign
    print("\n📝 测试2: 使用空sign参数")
    url2 = f"http://your-proxy-api.com/white/add?key={key}&brand={brand}&sign=&ip={ip}"
    print(f"   URL: {url2}")
    try:
        resp = requests.get(url2, timeout=10)
        print(f"   状态码: {resp.status_code}")
        print(f"   响应: {resp.text[:200]}")
        if resp.status_code == 200:
            print("   ✅ 成功!")
            return True
    except Exception as e:
        print(f"   ❌ 失败: {e}")
    
    # 测试3: 查看白名单（不需要IP参数）
    print("\n📝 测试3: 查看当前白名单")
    url3 = f"http://your-proxy-api.com/white/fetch?key={key}&brand={brand}"
    print(f"   URL: {url3}")
    try:
        resp = requests.get(url3, timeout=10)
        print(f"   状态码: {resp.status_code}")
        print(f"   响应: {resp.text[:200]}")
    except Exception as e:
        print(f"   ❌ 失败: {e}")
    
    # 测试4: 不同的brand值
    print("\n📝 测试4: 尝试brand=1")
    url4 = f"http://your-proxy-api.com/white/add?key={key}&brand=1&ip={ip}"
    print(f"   URL: {url4}")
    try:
        resp = requests.get(url4, timeout=10)
        print(f"   状态码: {resp.status_code}")
        print(f"   响应: {resp.text[:200]}")
        if resp.status_code == 200:
            print("   ✅ 成功!")
            return True
    except Exception as e:
        print(f"   ❌ 失败: {e}")
    
    print("\n" + "=" * 70)
    print("💡 建议:")
    print("   1. 检查API文档中的正确参数")
    print("   2. 确认key是否正确")
    print("   3. 联系代理服务商客服确认白名单API的使用方法")
    print("=" * 70)
    
    return False


def manual_add():
    """手动添加IP到白名单"""
    print("\n" + "=" * 70)
    print("手动添加IP到白名单")
    print("=" * 70)
    
    url = input("\n请输入完整的API URL: ").strip()
    
    if not url:
        print("❌ URL不能为空")
        return
    
    try:
        print(f"\n🔄 正在调用API...")
        print(f"   URL: {url}")
        
        resp = requests.get(url, timeout=10)
        print(f"\n📊 结果:")
        print(f"   状态码: {resp.status_code}")
        print(f"   响应内容:")
        print(f"   {resp.text}")
        
        if resp.status_code == 200:
            print("\n✅ 请求成功！检查上面的响应内容确认是否添加成功")
        else:
            print(f"\n⚠️  请求返回状态码 {resp.status_code}")
    
    except Exception as e:
        print(f"\n❌ 请求失败: {e}")


if __name__ == "__main__":
    print("\n选择操作:")
    print("1. 自动测试白名单API")
    print("2. 手动输入完整URL测试")
    
    choice = input("\n请选择 (1/2, 默认1): ").strip() or "1"
    
    if choice == "1":
        test_whitelist_api()
    elif choice == "2":
        manual_add()
    else:
        print("无效选择")
