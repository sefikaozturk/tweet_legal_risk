from crewai import Agent
from pydantic import PrivateAttr
import requests
from bs4 import BeautifulSoup

class PortalScraper:
    def fetch(self, url: str) -> str:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        return resp.text

    def parse(self, html: str, url: str) -> dict:
        soup = BeautifulSoup(html, 'html.parser')
        paragraphs = soup.find_all('p')
        text = ' '.join(p.get_text(strip=True) for p in paragraphs[:5])
        return {'text': text, 'url': url}

class CountryLegalDataCollector(Agent):
    _portal: PortalScraper = PrivateAttr(default_factory=PortalScraper)

    def __init__(self):
        super().__init__(
            name="CountryLegalDataCollector",
            role="Retrieve legal guidelines and documents from official sources",
            goal="Gather and validate current legal data for the selected country",
            backstory="You are a legal researcher bot that scrapes official sites for the latest laws."
        )

    def run(self, inputs: dict) -> dict:
        country = inputs.get('country', '').lower()
        if country in ('US', 'USA', 'United-States'):
            urls = {
                'defamation': 'https://www.law.cornell.edu/wex/defamation',
                'incitement': 'https://www.law.cornell.edu/wex/incitement',
                'hate_speech': 'https://en.wikipedia.org/wiki/Hate_speech_in_the_United_States'
            }
        else:
            raise NotImplementedError(f"Scraping logic not defined for country: {country}")

        rules = {}
        for category, url in urls.items():
            html = self._portal.fetch(url)
            rules[category] = self._portal.parse(html, url)
        return rules
