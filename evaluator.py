from crewai import Agent
from pydantic import PrivateAttr
import re

class Tokenizer:
    def tokenize(self, text: str) -> list:
        return re.findall(r"\w+", text.lower())

class CategoryScorer:
    def score(self, tokens: list, guideline: dict) -> float:
        keywords = re.findall(r"\w+", guideline['text'].lower())
        overlap = set(tokens) & set(keywords)
        return min(100.0, len(overlap) / max(1, len(keywords)) * 100)

class DynamicRiskEvaluationAgent(Agent):
    _tokenizer: Tokenizer = PrivateAttr(default_factory=Tokenizer)
    _scorer: CategoryScorer = PrivateAttr(default_factory=CategoryScorer)

    def __init__(self):
        super().__init__(
            name="DynamicRiskEvaluationAgent",
            role="Analyze tweet content against legal data",
            goal="Compute risk percentages per legal category and overall risk",
            backstory="You are a risk analytics bot that reads tweets and scores them against legal guidelines."
        )

    def run(self, inputs: dict) -> dict:
        tweet = inputs.get('tweet', '')
        legal_data = inputs.get('legal_data', {})
        tokens = self._tokenizer.tokenize(tweet)

        scores = {cat: self._scorer.score(tokens, info)
                  for cat, info in legal_data.items()}
        overall = sum(scores.values()) / max(1, len(scores))
        return {'per_category': scores, 'overall_risk': overall}
