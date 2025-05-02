from crewai import Agent
from pydantic import PrivateAttr

class CategoryParser:
    def split_into_categories(self, data: dict) -> dict:
        return data

class CitationManager:
    def attach_citations(self, categorized: dict) -> dict:
        return {
            category: {
                'text': info['text'],
                'citation': info['url']
            }
            for category, info in categorized.items()
        }

class LegalDataAggregator(Agent):
    _parser: CategoryParser = PrivateAttr(default_factory=CategoryParser)
    _citer: CitationManager = PrivateAttr(default_factory=CitationManager)

    def __init__(self):
        super().__init__(
            name="LegalDataAggregator",
            role="Process and structure the collected legal data",
            goal="Organize legal guidelines into searchable categories with citations",
            backstory="You are an expert in parsing and citing legal rules by topic."
        )

    def run(self, inputs: dict) -> dict:
        categorized = self._parser.split_into_categories(inputs)
        return self._citer.attach_citations(categorized)
