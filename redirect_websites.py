from playwright.sync_api import sync_playwright

def detect_default_url():
    with sync_playwright() as p:
        # Launch the browser with headless mode disabled and maximized window
        browser = p.chromium.launch(headless=False, args=["--start-maximized"])
        context = browser.new_context()

        # Open a new page
        page = context.new_page()

        # Navigate to Instagram with a timeout
        default_url = "https://instagram.com"
        timeout_seconds = 30000  # 30 seconds timeout in milliseconds
        try:
            page.goto(default_url, timeout=timeout_seconds)
            print(f"Default URL detected: {page.url}")
        except Exception as e:
            print(f"Navigation to {default_url} failed: {e}")

        # Keep the browser open for 10 seconds to observe it before closing
        import time
        time.sleep(10)

        # Close the browser
        browser.close()

if __name__ == "__main__":
    detect_default_url()
