from playwright.sync_api import sync_playwright
import time

def probe():
    with sync_playwright() as p:
        # 使用非无头模式（如果支持）或者是无头
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        url = "https://api.nineemail.com"
        print(f"正在打开: {url}")
        
        try:
            page.goto(url, timeout=30000)
            page.wait_for_load_state("networkidle")
            print(f"页面标题: {page.title()}")
            
            # 打印页面上的输入框和按钮
            print("--- 页面元素分析 ---")
            inputs = page.locator("input").all()
            for i, inp in enumerate(inputs):
                print(f"Input {i}: name='{inp.get_attribute('name')}', placeholder='{inp.get_attribute('placeholder')}', id='{inp.get_attribute('id')}'")
            
            buttons = page.locator("button").all()
            for i, btn in enumerate(buttons):
                print(f"Button {i}: text='{str(btn.text_content()).strip()}', type='{btn.get_attribute('type')}'")
                
            # 同时也找找 links，有时候按钮是 a 标签
            links = page.locator("a").all()
            for i, link in enumerate(links):
                text = str(link.text_content()).strip()
                if "反查" in text or "查询" in text:
                    print(f"Link {i}: text='{text}', href='{link.get_attribute('href')}'")
            
        except Exception as e:
            print(f"出错: {e}")
        
        browser.close()
        
        browser.close()

if __name__ == "__main__":
    probe()
