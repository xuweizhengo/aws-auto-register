#!/usr/bin/env python3
"""调试脚本 - 查看页面元素"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time

def debug_page():
    print("🔍 启动调试浏览器...")
    
    options = uc.ChromeOptions()
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--disable-blink-features=AutomationControlled')
    
    driver = uc.Chrome(options=options)
    
    try:
        print("📄 打开 AWS Builder 页面...")
        driver.get("https://builder.aws.com/start")
        time.sleep(5)
        
        print(f"\n页面标题: {driver.title}")
        print(f"页面URL: {driver.current_url}")
        
        # 查找所有按钮
        print("\n=== 所有按钮 ===")
        buttons = driver.find_elements(By.TAG_NAME, "button")
        for i, btn in enumerate(buttons[:10]):
            text = btn.text.strip()[:50] if btn.text else "(无文本)"
            print(f"  [{i}] {text}")
        
        # 查找所有链接
        print("\n=== 所有链接 ===")
        links = driver.find_elements(By.TAG_NAME, "a")
        for i, link in enumerate(links[:15]):
            text = link.text.strip()[:50] if link.text else "(无文本)"
            href = link.get_attribute("href") or ""
            print(f"  [{i}] {text} -> {href[:60]}")
        
        # 查找包含 sign/register/builder 的元素
        print("\n=== 关键词元素 ===")
        keywords = ["sign", "register", "builder", "create", "start"]
        for kw in keywords:
            els = driver.find_elements(By.XPATH, f"//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{kw}')]")
            if els:
                print(f"  '{kw}': 找到 {len(els)} 个")
                for el in els[:3]:
                    print(f"    - <{el.tag_name}> {el.text[:40]}")
        
        print("\n⏸️  浏览器保持打开，按 Ctrl+C 关闭...")
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n关闭浏览器...")
    finally:
        driver.quit()

if __name__ == "__main__":
    debug_page()
