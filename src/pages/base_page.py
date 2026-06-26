class BasePage:
    def __init__(self, page):
        self.page = page

    def goto(self, url):
        self.page.goto(url)

    def click(self, selector):
        self.page.click(selector)

    def fill(self, selector, text):
        self.page.fill(selector, text)

    def get_text(self, selector):
        return self.page.text_content(selector)

    def wait_for(self, selector, timeout=30000):
        self.page.wait_for_selector(selector, timeout=timeout)

    def screenshot(self, path):
        self.page.screenshot(path=path)
