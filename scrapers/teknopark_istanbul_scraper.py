from playwright.sync_api import sync_playwright


def scrape_teknopark():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        page.goto(
            "https://www.teknoparkistanbul.com.tr/firma-listesi"
        )

        page.wait_for_timeout(3000)

        print(page.title())

        browser.close()