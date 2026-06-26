#!/usr/bin/env python3
"""
指纹检测测试
访问指纹检测网站，验证随机化效果
"""

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from fingerprint import fingerprint_randomizer
import time

def test_fingerprint():
    """测试指纹随机化效果"""
    
    print("=" * 70)
    print("🎭 浏览器指纹随机化测试")
    print("=" * 70)
    
    # 配置浏览器
    options = uc.ChromeOptions()
    options.add_argument('--window-size=1920,1080')
    
    # 启动浏览器
    print("\n🚀 启动浏览器...")
    driver = uc.Chrome(options=options)
    
    # 注入指纹随机化
    print("🎭 注入指纹随机化脚本...")
    fingerprint_randomizer.inject_to_driver(driver)
    
    # 测试网站列表
    test_sites = [
        {
            'name': 'BrowserLeaks - Canvas',
            'url': 'https://browserleaks.com/canvas',
            'desc': '测试Canvas指纹'
        },
        {
            'name': 'BrowserLeaks - WebGL',
            'url': 'https://browserleaks.com/webgl',
            'desc': '测试WebGL指纹'
        },
        {
            'name': 'CreepJS',
            'url': 'https://abrahamjuliot.github.io/creepjs/',
            'desc': '综合指纹检测'
        }
    ]
    
    print("\n📊 将访问以下指纹检测网站:")
    for i, site in enumerate(test_sites, 1):
        print(f"   {i}. {site['name']} - {site['desc']}")
    
    choice = input("\n选择要访问的网站 (1-3, 或按Enter访问第1个): ").strip() or "1"
    
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(test_sites):
            site = test_sites[idx]
            print(f"\n🔗 正在打开: {site['name']}")
            print(f"   URL: {site['url']}")
            
            driver.get(site['url'])
            print("\n✅ 页面已加载")
            print("📝 请在浏览器中查看指纹检测结果")
            print("   注意：每次运行都会生成不同的指纹！")
            
            input("\n按Enter键关闭浏览器...")
        else:
            print("❌ 无效选择")
    except ValueError:
        print("❌ 无效输入")
    except Exception as e:
        print(f"❌ 发生错误: {e}")
    finally:
        driver.quit()
        print("\n✅ 测试完成")


if __name__ == "__main__":
    test_fingerprint()
