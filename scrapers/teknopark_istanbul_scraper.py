from playwright.sync_api import sync_playwright

from config import COMPANY_LIST_URL, HEADLESS, PAGE_TIMEOUT_MS


def scrape_teknopark():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=HEADLESS)

        try:
            page = browser.new_page()

            page.goto(
                COMPANY_LIST_URL,
                wait_until="domcontentloaded",
                timeout=PAGE_TIMEOUT_MS,
            )

            return page.title()

        finally:
            browser.close()