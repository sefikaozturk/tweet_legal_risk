import json
from collector import CountryLegalDataCollector
from aggregator import LegalDataAggregator
from evaluator import DynamicRiskEvaluationAgent
from reporter import ReportGenerator
from crewai import Task, Crew, Process

if __name__ == "__main__":
    # Task 1: Collect legal data
    collect_task = Task(
        name="collect_legal_data",
        agent=CountryLegalDataCollector(),
        params={"country": "{country}"}
    )

    # Task 2: Aggregate and structure legal data
    aggregate_task = Task(
        name="aggregate_legal_data",
        agent=LegalDataAggregator(),
        params={"legal_data": "{collect_legal_data}"}
    )

    # Task 3: Evaluate the tweet content against legal data
    evaluate_task = Task(
        name="evaluate_tweet",
        agent=DynamicRiskEvaluationAgent(),
        params={
            "tweet": "{tweet}",
            "legal_data": "{aggregate_legal_data}"
        }
    )

    # Task 4: Generate the final report
    report_task = Task(
        name="generate_report",
        agent=ReportGenerator(),
        params={"evaluation": "{evaluate_tweet}"}
    )

    # Orchestrate the crew sequentially
    crew = Crew(
        name="TweetLegalRiskCrew",
        tasks=[collect_task, aggregate_task, evaluate_task, report_task],
        process=Process.sequential,
        verbose=True
    )

    # Run the crew with dynamic inputs
    # Replace placeholders with actual values when invoking
    result = crew.run()
    print(json.dumps(result, indent=2))
