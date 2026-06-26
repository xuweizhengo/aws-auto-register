"""
代理白名单管理工具
自动添加当前IP到代理白名单
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import requests
import hashlib
from config import REGION_PROXY_API


def get_public_ip():
    """获取当前公网IP"""
    try:
        # 尝试多个IP查询服务
        services = [
            'https://api.ipify.org',
            'https://ifconfig.me/ip',
            'http://icanhazip.com',
            'https://ident.me'
        ]
        
        for service in services:
            try:
                response = requests.get(service, timeout=5)
                if response.status_code == 200:
                    ip = response.text.strip()
                    print(f"✅ 获取到当前公网IP: {ip}")
                    return ip
            except:
                continue
        
        print("⚠️  无法获取公网IP")
        return None
    except Exception as e:
        print(f"⚠️  获取公网IP失败: {e}")
        return None


def generate_sign(key, brand, ip):
    """
    生成签名
    根据API文档，可能需要特定的签名算法
    如果不需要sign参数，这个函数可以返回空字符串
    """
    # 如果API文档有说明签名算法，在这里实现
    # 暂时返回空，如果需要可以补充
    return ""


def add_to_whitelist(key, ip=None, brand=2):
    """
    添加IP到白名单
    
    Args:
        key: API密钥
        ip: 要添加的IP，如果为None则自动获取当前公网IP
        brand: 品牌标识 (默认2)
    
    Returns:
        bool: 成功返回True，失败返回False
    """
    if ip is None:
        ip = get_public_ip()
        if not ip:
            return False
    
    # 生成签名（如果需要）
    sign = generate_sign(key, brand, ip)
    
    # 构建API URL
    if sign:
        url = f"http://your-proxy-api.com/white/add?key={key}&brand={brand}&sign={sign}&ip={ip}"
    else:
        # 尝试不使用sign参数
        url = f"http://your-proxy-api.com/white/add?key={key}&brand={brand}&ip={ip}"
    
    try:
        print(f"🔄 正在添加IP到白名单...")
        print(f"   IP: {ip}")
        
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            result = response.text.strip()
            print(f"📝 API响应: {result}")
            
            # 判断是否成功（根据API返回格式调整）
            if "成功" in result or "success" in result.lower() or "ok" in result.lower():
                print(f"✅ IP已成功添加到白名单！")
                return True
            else:
                print(f"⚠️  添加白名单可能失败，请检查响应")
                return False
        else:
            print(f"⚠️  API请求失败: HTTP {response.status_code}")
            return False
            
    except Exception as e:
        print(f"⚠️  添加白名单失败: {e}")
        return False


def delete_from_whitelist(key, ip=None, brand=2):
    """从白名单删除IP"""
    if ip is None:
        ip = get_public_ip()
        if not ip:
            return False
    
    sign = generate_sign(key, brand, ip)
    
    if sign:
        url = f"http://your-proxy-api.com/white/delete?key={key}&brand={brand}&sign={sign}&ip={ip}"
    else:
        url = f"http://your-proxy-api.com/white/delete?key={key}&brand={brand}&ip={ip}"
    
    try:
        print(f"🔄 正在从白名单删除IP...")
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            print(f"✅ IP已从白名单删除")
            print(f"📝 响应: {response.text}")
            return True
        else:
            print(f"⚠️  删除失败: HTTP {response.status_code}")
            return False
            
    except Exception as e:
        print(f"⚠️  删除白名单失败: {e}")
        return False


def fetch_whitelist(key, brand=2):
    """查看白名单"""
    sign = generate_sign(key, brand, "")
    
    if sign:
        url = f"http://your-proxy-api.com/white/fetch?key={key}&brand={brand}&sign={sign}"
    else:
        url = f"http://your-proxy-api.com/white/fetch?key={key}&brand={brand}"
    
    try:
        print(f"🔄 正在查询白名单...")
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            print(f"📋 当前白名单:")
            print(response.text)
            return True
        else:
            print(f"⚠️  查询失败: HTTP {response.status_code}")
            return False
            
    except Exception as e:
        print(f"⚠️  查询白名单失败: {e}")
        return False


def extract_key_from_url(api_url):
    """从API URL中提取key参数"""
    try:
        # 从 URL 中提取 key 参数
        if 'key=' in api_url:
            key = api_url.split('key=')[1].split('&')[0]
            return key
        return None
    except:
        return None


def auto_add_whitelist():
    """自动添加当前IP到白名单"""
    print("=" * 60)
    print("自动添加IP到代理白名单")
    print("=" * 60)
    
    # 从配置中获取API信息
    api_url = REGION_PROXY_API.get('url', '')
    
    if not api_url:
        print("⚠️  未找到代理API配置")
        return False
    
    # 提取key
    key = extract_key_from_url(api_url)
    
    if not key:
        print("⚠️  无法从API URL中提取key")
        print(f"   URL: {api_url}")
        return False
    
    print(f"🔑 API Key: {key}")
    print("-" * 60)
    
    # 添加到白名单
    success = add_to_whitelist(key)
    
    if success:
        print("-" * 60)
        print("🎉 白名单配置完成！")
        print("💡 提示: 现在可以运行 python check_proxy.py 测试代理")
    
    return success


if __name__ == "__main__":
    auto_add_whitelist()
