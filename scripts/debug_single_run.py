from main import run
from outlook_accounts import OUTLOOK_ACCOUNTS
import time

def debug_one():
    # 取第一个账号
    account = OUTLOOK_ACCOUNTS[0]
    print(f"🐞 开始单线程 Debug 运行: {account['email']}")
    print("👀 请观察浏览器行为...")
    
    # 运行
    try:
        run(fixed_account=account)
    except Exception as e:
        print(f"❌ 运行出错: {e}")

if __name__ == "__main__":
    debug_one()
