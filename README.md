# Legal Risk Analyzer for Tweets

🛡️ **Not Legal Advice** — This Streamlit app estimates the legal risk of a tweet for a given country, using a multi-agent CrewAI workflow. It collects statutes, codes and regulations, evaluates your tweet against hate-speech, defamation, incitement, and other categories, then surfaces a risk score and detailed breakdown.

---

## 🚀 Features

- **Multi-Agent Architecture**  
  - **CountryLegalDataCollector**: Scrapes official legal sources for a given country  
  - **LegalDataAggregator**: Parses and structures statutes by category with citations  
  - **DynamicRiskEvaluationAgent**: Scores your tweet against each legal category  
  - **ReportGenerator**: Compiles a human-friendly summary, per-category details, and full JSON  

- **Interactive Streamlit UI**  
  - Enter your **Country** (e.g. `US`, `UK`, `Germany`)  
  - Paste your **Tweet** text  
  - Get an **Overall Risk** percentage, a clickable breakdown panel, and raw JSON  

- **Polished UX**  
  - Full-screen prison-bars background  
  - Semi-transparent content container for legibility  
  - Centered layout for any screen size  

- **Deployment-Ready**  
  - 📦 Dockerfile for containerized builds  
  - ☁️ Streamlit Community Cloud instructions  

---

## 🔧 Project Structure

  tweet_legal_risk/
    ├── app.py                  # Streamlit front-end & Crew kickoff
    ├── collector.py            # CountryLegalDataCollector agent
    ├── aggregator.py           # LegalDataAggregator agent
    ├── evaluator.py            # DynamicRiskEvaluationAgent
    ├── reporter.py             # ReportGenerator
    ├── requirements.txt        # Python dependencies
    ├── Dockerfile              # Container build instructions
    ├── .dockerignore
    └── background.png          # Jail-bars background image

---

## 💻 Local Setup

1. **Clone & cd**  

```bash
   git clone https://github.com/<your-username>/tweet-legal-risk.git
   cd tweet-legal-risk
```
Create & activate venv
```
python3.11 -m venv .venv
source .venv/bin/activate       # macOS/Linux
.\.venv\Scripts\Activate.ps1    # Windows PowerShell
```
Install dependencies
```
pip install --upgrade pip
pip install -r requirements.txt
```
Set your OpenAI key
```
export OPENAI_API_KEY="sk-..."
```
Run the app
```
python -m streamlit run app.py
```
Visit http://localhost:8501 in your browser.

## 🐳 Docker

Build and run in a container:
```
docker build -t tweet-legal-risk:latest .
docker run -d -p 8501:8501 --name tweet-risk-app tweet-legal-risk:latest
```

Open http://localhost:8501.

## ☁️ Deploy to Streamlit Community Cloud

Push your code to GitHub (public or private).
Go to https://share.streamlit.io → New app → select your repo, branch main, and app.py.
Under Settings → Secrets, add OPENAI_API_KEY.
Click Deploy and share your public URL.

## 🎯 Usage

Enter a country code (e.g. US, germany).
Paste any tweet text.
Click Analyze Tweet.
View your overall risk, expand categories for details, or inspect raw JSON.

## ⚖️ Disclaimer

This tool is not legal advice. It’s a demonstration of AI-driven risk estimation based on publicly available statutes. Always consult a qualified attorney for real legal guidance.

## 📄 License

This project is released under the MIT License.
