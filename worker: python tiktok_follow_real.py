
import time, random, string
from playwright.sync_api import sync_playwright

def generate_username():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

def follow_tiktok(target_username):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        try:
            page.goto(f"https://www.tiktok.com/@{target_username}", timeout=60000)
            page.wait_for_selector("button", timeout=10000)
            follow_buttons = page.query_selector_all("button")
            for button in follow_buttons:
                text = button.inner_text().lower()
                if "follow" in text:
                    button.click()
                    print(f"[✓] Akun berhasil follow @{target_username}")
                    break
            else:
                print(f"[✗] Tombol follow tidak ditemukan untuk @{target_username}")
        except Exception as e:
            print(f"[✗] Error saat mencoba follow: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    target = "cx39294"
    for _ in range(5):
        username = generate_username()
        print(f"[+] Simulasi login akun @{username}")
        follow_tiktok(target)
        time.sleep(2)
