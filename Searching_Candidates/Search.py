# Search a query in google and return de obtained links and main info
import random
import urllib

import requests
from requests_html import HTMLSession  # type: ignore

HEADERS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124'
    ' Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212'
    ' Safari/537.36',
]


class SearchGoogle:
    """SearchGoogle is responsible of obtaining the links of the candidates linkedin"""

    def __init__(self, query):
        self.query = query
        self.pages_per_query = 5  # Upgrade when there is a strategy for avoiding google banned ip
        self.start_num = 0
        self.output = []

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

    def parse_results(self):
        css_identifier_result = ".tF2Cxc"
        css_identifier_title = "h3"
        css_identifier_link = ".yuRUbf a"
        css_identifier_text = ".VwiC3b"

        self.results = self.response.html.find(css_identifier_result)

        for result in self.results:
            item = {
                'title': result.find(css_identifier_title, first=True).text,
                'link': result.find(css_identifier_link, first=True).attrs['href'],
                'text': result.find(css_identifier_text, first=True).text,
            }

            self.output.append(item)

    def google_search(self):
        self.get_results()
        self.parse_results()
        return self.output

    def get_results(self):
        query = urllib.parse.quote_plus(self.query)
        self.response = self.get_source(
            "https://www.google.com.ar/search?q="
            + query
            + '&num='
            + str(self.pages_per_query)
            + '&start='
            + str(self.start_num)
        )
