from pathlib import Path
from dotenv import load_dotenv
import os

# project configuration from .env (secret part)
env_path = Path(__file__).resolve().parent / '.env'
load_dotenv(dotenv_path=env_path)  # loads into os.environ

# project directories from .env
DATA_DIR = os.getenv("DATA_DIR", "data")
RESULTS_DIR = os.getenv("RESULTS_DIR", "results")
DOC_DIR = os.getenv("DOC_DIR", "doc")

# data sources configuration
MPX_RESEARCH_URL = 'https://healthdata.gov/api/views/x7kq-cyv4/rows.csv'
CELIAC_DATASET_SLUG = 'jackwin07/celiac-disease-coeliac-disease'
INFANT_DATASET_SLUG = 'chidirolex/weightheight-and-breastfeeding-pattern-of-infants'
