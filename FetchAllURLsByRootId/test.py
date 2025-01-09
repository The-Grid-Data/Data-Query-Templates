import json
import logging
import requests
import unittest

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def pretty_print(data):
    """Helper function to pretty-print JSON data."""
    try:
        return json.dumps(data, indent=2)
    except (TypeError, ValueError) as e:
        return f"Error marshaling data: {e}"

def fetch_urls_for_root_id(graphql_url, root_id):
    """
    Fetch URLs for a given root ID from the specified GraphQL endpoint.

    :param graphql_url: URL of the GraphQL endpoint.
    :param root_id: Root ID for the query.
    :return: List of URLs.
    :raises: Exception if the request fails or the data is invalid.
    """
    query = """
    query FetchUrls($id: ID!) {
      root(id: $id) {
        urls {
          url
        }
      }
    }
    """

    variables = {"id": root_id}

    response = requests.post(
        graphql_url,
        json={"query": query, "variables": variables},
        headers={"Content-Type": "application/json"}
    )

    if response.status_code != 200:
        raise Exception(f"GraphQL query failed with status code {response.status_code}: {response.text}")

    data = response.json()
    if "errors" in data:
        raise Exception(f"GraphQL query returned errors: {data['errors']}")

    urls = [url_entry["url"] for url_entry in data.get("data", {}).get("root", {}).get("urls", [])]
    return urls

class TestFetchUrlsForRootID(unittest.TestCase):

    def setUp(self):
        self.endpoints = [
            {"name": "Development", "url": "https://thegriddev.node.thegrid.id/graphql"},
            {"name": "Beta", "url": "https://beta.node.thegrid.id/graphql"},
        ]

    def test_fetch_urls_for_root_id(self):
        root_id = "1"  # Replace with a valid root ID for your test

        for endpoint in self.endpoints:
            with self.subTest(endpoint=endpoint):
                logger.info(f"Testing endpoint: {endpoint['url']} with rootID: {root_id}")
                try:
                    result = fetch_urls_for_root_id(endpoint['url'], root_id)
                    self.assertGreater(len(result), 0, f"No URLs found for endpoint {endpoint['url']} with rootID {root_id}")

                    logger.info(f"Successfully fetched {len(result)} URLs for endpoint {endpoint['url']} with rootID {root_id}")
                    logger.info("\nParsed Response:\n%s", pretty_print(result))

                except Exception as e:
                    self.fail(f"FetchUrlsForRootID failed for endpoint {endpoint['url']} with rootID {root_id}: {e}")

if __name__ == "__main__":
    unittest.main()
