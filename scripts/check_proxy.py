#!/usr/bin/env python3
"""
代理API测试工具
测试代理API是否正常工作
"""

from proxy_manager import proxy_manager

print("=" * 60)
print("代理API测试")
print("=" * 60)

# 显示当前配置
print("\n📋 当前配置:")
print(f"   代理启用: {proxy_manager.use_proxy}")
print(f"   代理模式: {proxy_manager.proxy_mode}")

if proxy_manager.use_proxy:
    print("\n" + "-" * 60)
    
    # 获取代理
    proxy_url = proxy_manager.get_proxy()
    
    if proxy_url:
        print(f"\n✅ 代理获取成功!")
        print(f"   完整URL: {proxy_url}")
        
        # 测试代理
        print("\n" + "-" * 60)
        is_working = proxy_manager.test_proxy()
        
        if is_working:
            print("\n🎉 代理测试通过，可以正常使用！")
        else:
            print("\n❌ 代理测试失败，请检查代理设置")
    else:
        print("\n❌ 代理获取失败")
        print("   请检查:")
        print("   1. API URL 是否正确")
        print("   2. API密钥是否有效")
        print("   3. 网络连接是否正常")
else:
    print("\n⚠️  代理未启用")
    print("   如需启用，请修改 config.yaml 中的 use_proxy 为 true")

print("\n" + "=" * 60)
