from crewai import Agent
from pydantic import PrivateAttr

class SummaryFormatter:
    def format_summary(self, overall: float) -> str:
        return f"**Overall risk:** {overall:.1f}%"

class DetailsFormatter:
    def format_details(self, scores: dict) -> str:
        return "\n".join(f"- {cat.replace('_',' ').title()}: {pct:.1f}%"
                         for cat, pct in scores.items())

class ReportGenerator(Agent):
    _summary_formatter: SummaryFormatter = PrivateAttr(default_factory=SummaryFormatter)
    _details_formatter: DetailsFormatter = PrivateAttr(default_factory=DetailsFormatter)

    def __init__(self):
        super().__init__(
            name="ReportGenerator",
            role="Compile summary and detailed reports",
            goal="Produce structured output with risk scores and explanations",
            backstory="You are a report writer bot that formats risk assessments into human-readable summaries."
        )

    def run(self, inputs: dict) -> dict:
        ev = inputs.get('evaluation', {})
        summary = self._summary_formatter.format_summary(ev.get('overall_risk', 0.0))
        details = self._details_formatter.format_details(ev.get('per_category', {}))
        return {'summary': summary, 'details': details, 'full_report': f"{summary}\n\n{details}"}
