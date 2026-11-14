
from app.services.scraper import scrape_website
from app.storage.json_storage import save_json


def main():

    url = "https://quotes.toscrape.com/js/"

    instruction = """
    Extract all quotes, author names and tags.
    """

    records = scrape_website(
        url=url,
        instruction=instruction
    )

    file_path = save_json(records)

    print("Scraping completed!")
    print(f"Saved at: {file_path}")
    print(records)


if __name__ == "__main__":
    main()
