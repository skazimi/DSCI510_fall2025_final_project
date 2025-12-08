# Breastfeeding, Celiac Disease, and Mpox Research Data
## Introduction
This project explores relationships between infant feeding patterns, early growth, and later gluten-related outcomes using publicly available health data. The focus is on summarizing patterns in breastfeeding and infant anthropometrics, characterizing celiac disease records, and contextualizing these findings within broader infectious disease and vaccine research on mpox. The codebase implements a small data pipeline: fetching data from APIs and Kaggle, cleaning and transforming it, and producing descriptive analyses and visualizations in a reproducible way.

## Data sources
All raw data are fetched automatically by the code and are not stored in this repository. The table below summarizes the datasets used.

| Dataset                 | Source / Type               | Description                                                                            |
|-------------------------|-----------------------------|----------------------------------------------------------------------------------------|
| Mpox research projects  | HealthData.gov CSV API      | Research and development activities related to mpox (topic, agency, milestones, etc.)  |
| Celiac disease records  | Kaggle dataset (jackwin07)  | 2206 records with clinical and demographic variables related to celiac disease         |
| Infant feeding patterns | Kaggle dataset (chidirolex) | Infant weight, height, and breastfeeding pattern variables                             |


These sources together support descriptive statistics, basic exploratory analysis, and derived features for examining patterns related to breastfeeding and gluten sensitivity.

## Analysis
The analysis pipeline is organized into modular Python files in src/ and a final notebook results.ipynb that orchestrates the main steps. The pipeline:
    Loads mpox research data from the healthdata.gov CSV API, then filters and summarizes projects by topic, agency, geography, and timeline to provide context on vaccine and epidemiology research.​

    Downloads and loads the celiac disease dataset from Kaggle to explore distributions of key clinical fields and potential associations with demographic factors.

    Downloads and loads the infant weight/height and breastfeeding dataset from Kaggle to summarize breastfeeding patterns, growth indicators, and their variation across subgroups.

Core analyses include data quality checks, column selection and renaming, feature engineering for categorical variables, and visualizations such as histograms, bar charts, and grouped summaries to compare patterns across datasets.

## Summary of results
The notebook results.ipynb includes the current descriptive results and plots produced by the pipeline. As of this version, the project focuses on:​

Summary tables and figures for mpox research projects by topic and sponsoring agency.

Initial descriptive statistics for the celiac dataset (e.g., counts by outcome or demographic categories).

Descriptive summaries of infant breastfeeding patterns and growth measures.

This section can be expanded as additional models, hypothesis tests, or more advanced statistical analyses are added.

## How to run
1. Clone the repository
git clone <https://github.com/skazimi/DSCI510_fall2025_final_project/>
cd breastfeeding_and_gluten_sensitivity_data
2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate    # macOS / Linux
# or
venv\Scripts\activate       # Windows
3. Install dependencies
pip install -r requirements.txt
4. Configure environment variables
Create a file src/.env (do not commit this file) with entries matching .env.example:​
5. Run the full pipeline from Python
From the project root:
python src/main.py
6. Reproduce analysis in the notebook
7. Run tests
python src/tests.py

