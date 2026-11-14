
import json

from lightpanda import Browser

from app.llm.planner import generate_plan


def scrape_website(url: str, instruction: str):

    with Browser(args=["--obey-robots"]) as browser:

        page = browser.new_session()

        try:
            # 1. Navigate to the website
            result = page.goto(url=url)

            if result.http_status and result.http_status >= 400:
                raise RuntimeError(
                    f"HTTP error: {result.http_status}"
                )

            # 2. Get limited HTML for the LLM
            html = page.html(
                max_bytes=12000,
                strip={"js": True, "css": True}
            )

            # 3. Ask LLM to identify selectors
            plan = generate_plan(
                instruction=instruction,
                page_info=str(html)
            )

            container = plan["container_selector"]
            fields = plan["fields"]

            if not fields:
                raise ValueError("No extraction fields generated")

            # 4. Validate selectors against the actual DOM
            selectors = [container, *fields.values()]

            for selector in selectors:
                count = page.evaluate(
                    script=(
                        "document.querySelectorAll("
                        + json.dumps(selector)
                        + ").length"
                    )
                )

                if not count:
                    raise ValueError(
                        f"Invalid or unmatched selector: {selector}"
                    )

            # 5. Construct Lightpanda extraction schema
            schema = {
                "records": [
                    {
                        "selector": container,
                        "fields": fields
                    }
                ]
            }

            # 6. Extract structured records
            records = page.extract(schema=schema)

            return records

        finally:
            page.close()
