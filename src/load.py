import os
from pathlib import Path
import kaggle
import pandas as pd
import requests

# Loads config from .env
from config import DATA_DIR, MPX_RESEARCH_URL, CELIAC_DATASET_SLUG, INFANT_DATASET_SLUG

# Ensures data directory exists
data_path = Path(DATA_DIR)
data_path.mkdir(parents=True, exist_ok=True)


# --- 1. DOWNLOADS DATA FROM KAGGLE ---

def get_kaggle_data(dataset_slug, extract_dir=None):
    """
    Downloads a specific file from a Kaggle dataset, extracts it,
    and loads it into a pandas DataFrame.

    :param dataset_slug: The slug of the dataset (e.g., 'jackwin07/celiac-disease-coeliac-disease')
    :param extract_dir: Directory to extract files into (defaults to DATA_DIR/kaggle/{slug})
    :return: pandas DataFrame or None
    """
    if extract_dir is None:
        extract_dir = data_path / 'kaggle' / dataset_slug.replace('/', '_')

    print(f"--- Loading data from Kaggle: {dataset_slug} ---")
    try:
        # Ensures extraction directory exists
        extract_dir.mkdir(parents=True, exist_ok=True)

        print(f"Downloading {dataset_slug}...")
        kaggle.api.dataset_download_files(dataset_slug, path=extract_dir, unzip=True)

        csv_file_path = [f for f in extract_dir.iterdir() if f.suffix == '.csv'][0]

        # Loads the extracted CSV into a DataFrame
        print(f"Loading {csv_file_path} into DataFrame...")
        df = pd.read_csv(csv_file_path)
        print("Kaggle data loaded successfully.")
        return df

    except Exception as e:
        print(f"Error loading data from Kaggle: {e}")
        return None


# --- 2. DOWNLOADS FILE FROM WEB ---

def get_web_csv_data(url):
    """
    Downloads a CSV file directly from a URL into a pandas DataFrame.

    :param url: The direct URL to the .csv file
    :return: pandas DataFrame or None
    """
    print(f"--- Loading data from Web URL: {url[:50]}... ---")
    try:
        # pandas can read a CSV directly from a URL
        df = pd.read_csv(url)
        print("Web CSV data loaded successfully.")
        return df
    except Exception as e:
        print(f"Error loading data from URL: {e}")
        return None


# --- MAIN LOADER FUNCTIONS FOR THE PROJECT ---

def load_mpx_research_data():
    """Load Monkeypox research data from healthdata.gov"""
    return get_web_csv_data(MPX_RESEARCH_URL)


def load_celiac_data():
    """Load Celiac disease data from Kaggle"""
    return get_kaggle_data(CELIAC_DATASET_SLUG)


def load_infant_breastfeeding_data():
    """Load infant breastfeeding/weight data from Kaggle"""
    return get_kaggle_data(INFANT_DATASET_SLUG)
