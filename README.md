# Tweet Legal Risk Analyzer

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

