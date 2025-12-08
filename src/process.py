from load import load_mpx_research_data, load_celiac_data, load_infant_breastfeeding_data
import pandas as pd
import numpy as np


def process_mpx_research_data(mpx_df: pd.DataFrame) -> pd.DataFrame:
    """Cleans and processes Monkeypox research data from healthdata.gov"""
    if mpx_df is None or mpx_df.empty:
        return pd.DataFrame()

    print("\nMonkeypox Research Data Head:")
    print(mpx_df.head())

    # Cleans key columns for analysis
    processed_df = mpx_df.copy()

    # Cleans 'Topic' column
    processed_df['Topic'] = processed_df['Topic'].str.strip()

    # Extracts agency from 'Agency and Office Name'
    processed_df['Agency'] = processed_df['Agency and Office Name'].str.split('/').str[0].str.strip()

    # Cleans 'Status' column
    processed_df['Status'] = processed_df['Status'].str.strip()

    # Creates a summary by Topic and Status
    summary_df = processed_df.groupby(['Topic', 'Status', 'Agency']).size().reset_index(name='Count')

    print("\nMPX Research Summary by Topic/Status:")
    print(summary_df.head())

    return summary_df


def process_celiac_data(celiac_df: pd.DataFrame) -> pd.DataFrame:
    """Cleans and processes Celiac disease data from Kaggle"""
    if celiac_df is None or celiac_df.empty:
        return pd.DataFrame()

    print("\nCeliac Disease Data Head:")
    print(celiac_df.head())

    # Common cleaning for typical celiac datasets
    processed_df = celiac_df.copy()

    # Cleans numeric columns
    numeric_cols = processed_df.select_dtypes(include=['object']).columns
    for col in processed_df.columns:
        if processed_df[col].dtype == 'object':
            processed_df[col] = processed_df[col].astype(str).str.strip()

    # Handles missing values
    processed_df = processed_df.dropna()

    print(f"\nCeliac data shape after cleaning: {processed_df.shape}")
    return processed_df


def process_infant_data(infant_df: pd.DataFrame) -> pd.DataFrame:
    """Cleans and processes infant breastfeeding/weight data from Kaggle"""
    if infant_df is None or infant_df.empty:
        return pd.DataFrame()

    print("\nInfant Breastfeeding Data Head:")
    print(infant_df.head())

    processed_df = infant_df.copy()

    # Cleans weight/height columns
    weight_cols = [col for col in processed_df.columns if 'weight' in col.lower() or 'wt' in col.lower()]
    height_cols = [col for col in processed_df.columns if 'height' in col.lower() or 'length' in col.lower()]
    breast_cols = [col for col in processed_df.columns if 'breast' in col.lower() or 'feed' in col.lower()]

    # Converts numeric columns
    for col in processed_df.select_dtypes(include=['object']).columns:
        processed_df[col] = pd.to_numeric(processed_df[col], errors='coerce')

    # Handles missing values
    processed_df = processed_df.dropna()

    print(f"\nInfant data shape after cleaning: {processed_df.shape}")
    print("Weight columns found:", weight_cols)
    print("Breastfeeding columns found:", breast_cols)

    return processed_df


# --- MAIN PROCESSING FUNCTIONS ---

def load_and_process_all_data():
    """Loads and processes all three datasets for the project"""
    print("=== Loading and Processing All Datasets ===\n")

    # Loads raw data
    mpx_df = load_mpx_research_data()
    celiac_df = load_celiac_data()
    infant_df = load_infant_breastfeeding_data()

    # Processes each dataset
    mpx_processed = process_mpx_research_data(mpx_df)
    celiac_processed = process_celiac_data(celiac_df)
    infant_processed = process_infant_data(infant_df)

    return {
        'mpx_research': mpx_processed,
        'celiac': celiac_processed,
        'infant_breastfeeding': infant_processed}
