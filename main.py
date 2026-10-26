from playwright.sync_api import Error as PlaywrightError

from config import TEKNOPARK_NAME
from scrapers.teknopark_istanbul_scraper import scrape_teknopark


def main():
    print("JOB HUNTER başlatıldı.")
    print(f"Teknopark: {TEKNOPARK_NAME}")

    try:
        page_title = scrape_teknopark()

    except PlaywrightError as error:
        print("Sayfaya erişirken bir hata oluştu.")
        print(f"Hata ayrıntısı: {error}")
        return

    print(f"Sayfa başlığı: {page_title}")
    print("Sayfa kontrolü tamamlandı.")


if __name__ == "__main__":
    main()