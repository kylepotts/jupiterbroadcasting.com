from playwright.sync_api import Page
from urllib.parse import urlparse

def base_url(page: Page):
    parsed_url = urlparse(page.url)
    return "{}://{}".format(parsed_url.scheme, parsed_url.netloc)
