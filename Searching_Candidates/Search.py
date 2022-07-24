# Search a query in google and return de obtained links and main info
import random
import urllib

import requests
from requests_html import HTMLSession #type: ignore

HEADERS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124'
    ' Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212'
    ' Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Mozilla/5.0 (Linux; Android 11; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile'
    ' Safari/537.36',
]


class SearchGoogle:
    def __init__(self, query):
        self.query = query
        self.pages_per_query = 5
        self.start_num = 0

    def print_query(self):
        print(self.query)

    def get_source(self, url):
        """Return the source code for the provided URL.

        Args:
            url (string): URL of the page to scrape.

        Returns:
            response (object): HTTP response object from requests_html.
        """
        self.select_new_header()
        try:
            session = HTMLSession()
            response = session.get(url, headers=self.headers)
            return response

        except requests.exceptions.RequestException as e:
            print(e)

    def select_new_header(self):
        self.headers = {'User-Agent': random.choice(HEADERS)}

    def scrape_google(self):
        query = urllib.parse.quote_plus(self.query)
        response = self.get_source(
            "https://www.google.com.ar/search?q="
            + query
            + '&num='
            + str(self.pages_per_query)
            + '&start='
            + str(self.start_num)
        )

        links = list(response.html.absolute_links)
        google_domains = (
            'https://www.google.',
            'https://google.',
            'https://webcache.googleusercontent.',
            'http://webcache.googleusercontent.',
            'https://policies.google.',
            'https://support.google.',
            'https://maps.google.',
        )

        for url in links[:]:
            if url.startswith(google_domains):
                links.remove(url)

        return links
