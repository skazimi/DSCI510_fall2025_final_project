import pytest
import pandas as pd
from load import load_mpx_research_data, load_celiac_data, load_infant_breastfeeding_data
from config import MPX_RESEARCH_URL, CELIAC_DATASET_SLUG, INFANT_DATASET_SLUG

def test_load_mpx_research_data():
    """Tests loading Monkeypox research data from healthdata.gov"""
    df = load_mpx_research_data()
    assert df is not None, "MPX research data failed to load"
    assert isinstance(df, pd.DataFrame), "MPX data is not a DataFrame"
    assert len(df) > 0, "MPX research data is empty"
    assert 'Research Activity' in df.columns, "Expected 'Research Activity' column"
    print(f"MPX research data loaded: {len(df)} rows, {len(df.columns)} columns")

def test_load_celiac_data():
    """Tests loading Celiac disease data from Kaggle"""
    df = load_celiac_data()
    if df is not None:
        assert isinstance(df, pd.DataFrame), "Celiac data is not a DataFrame"
        assert len(df) > 0, "Celiac data is empty"
        print(f"Celiac data loaded: {len(df)} rows")
    else:
        print("Celiac data skipped (Kaggle auth required)")

def test_load_infant_breastfeeding_data():
    """Tests loading infant breastfeeding data from Kaggle"""
    df = load_infant_breastfeeding_data()
    if df is not None:
        assert isinstance(df, pd.DataFrame), "Infant data is not a DataFrame"
        assert len(df) > 0, "Infant data is empty"
        print(f"Infant breastfeeding data loaded: {len(df)} rows")
    else:
        print("Infant data skipped (Kaggle auth required)")

def test_config_urls():
    """Tests that config URLs/slugs are properly defined"""
    assert MPX_RESEARCH_URL == 'https://healthdata.gov/api/views/x7kq-cyv4/rows.csv'
    assert CELIAC_DATASET_SLUG == 'jackwin07/celiac-disease-coeliac-disease'
    assert INFANT_DATASET_SLUG == 'chidirolex/weightheight-and-breastfeeding-pattern-of-infants'
    print("Config URLs and Kaggle slugs are correct")

# Runs all tests
if __name__ == "__main__":
    pytest.main([__file__, "-v"])
