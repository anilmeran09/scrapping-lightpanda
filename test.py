
from lightpanda import Browser

URL = "https://quotes.toscrape.com/js/"

SCHEMA = {
    "title": "title",
    "quotes": [
        {
            "selector": ".quote",
            "fields": {
                "text": ".text",
                "author": ".author",
            },
        }
    ],
}


def main():
    with Browser() as browser:
        with browser.new_session() as page:
            result = page.goto(url=URL)

            print("Page status:", result.http_status)

            data = page.extract(schema=SCHEMA)

            print(data)


if __name__ == "__main__":
    main()
