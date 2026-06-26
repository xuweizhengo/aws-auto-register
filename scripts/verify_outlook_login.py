from outlook_service import get_access_token
from outlook_accounts import OUTLOOK_ACCOUNTS
import re

def test_oauth_login():
    print("🚀 开始测试 Outlook OAuth 登录...")
    
    # 取第一个账号测试
    account = OUTLOOK_ACCOUNTS[0]
    email = account['email']
    raw_token_url = account['api_url']
    
    print(f"📧 测试邮箱: {email}")
    
    # 提取 Token
    token = raw_token_url
    if "token=" in raw_token_url:
        match = re.search(r'token=([^&]+)', raw_token_url)
        if match:
            token = match.group(1)
            
    print(f"🔑 提取到的 Token: {token}")
    print(f"📏 Token 长度: {len(token)}")
    
    if len(token) < 50:
        print("⚠️ 警告: Token 长度似乎过短 (通常微软 Refresh Token 很长)")
        print("   如果请求失败，这可能只是平台的一个 key，而不是真正的 refresh_token")
    
    # 尝试获取 Access Token
    print("\n🔄 正在请求 Microsoft OAuth...")
    access_token = get_access_token(token)
    
    if access_token:
        print("\n✅ 成功获取 Access Token!")
        print(f"🎫 Access Token (前20位): {access_token[:20]}...")
        print("🎉 邮箱验证逻辑通过！可以开始批量注册。")
    else:
        print("\n❌ 获取 Access Token 失败。")
        print("💡 原因可能是: 提供的 token 不是有效的 Microsoft Refresh Token。")
        
        print("\n🕵️‍♀️ 尝试直接访问该 Token URL，看看里面有什么...")
        import requests
        try:
            # 尝试访问原始 URL (nineemail) 和新 URL (appleemail)
            urls_to_try = [
                f"https://api.nineemail.com/index.php?token={token}",
                f"https://www.appleemail.top/index.php?token={token}",
                f"http://api.nineemail.com/token={token}" # 不带 index.php
            ]
            
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            }
            for url in urls_to_try:
                print(f"👉 尝试GET请求: {url}")
                try:
                    r = requests.get(url, timeout=10, headers=headers, proxies={"http": None, "https": None}, verify=False)
                    print(f"   状态码: {r.status_code}")
                    print(f"   内容(前200字): {r.text[:200]}")
                    if "refresh_token" in r.text or "access_token" in r.text:
                        print("   ✨ 发现关键词！也许真正的 token 在这里面！")
                except Exception as e:
                    print(f"   请求出错: {e}")
                    
        except Exception as e:
            print(f"探测出错: {e}")

if __name__ == "__main__":
    test_oauth_login()
