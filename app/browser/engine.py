
from lightpanda import Browser


class LightpandaEngine:

    def __init__(self):
        self.browser = Browser(
            args=["--obey-robots"]
        )

    def extract_page(self, url: str, schema: dict):

        page = self.browser.new_session()

        try:
            result = page.goto(url=url)

            if result.http_status and result.http_status >= 400:
                raise RuntimeError(
                    f"Website returned HTTP {result.http_status}"
                )

            return page.extract(schema=schema)

        finally:
            page.close()

    def close(self):
        self.browser.close()
