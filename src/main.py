import os
from config import DATA_DIR, RESULTS_DIR, MPX_RESEARCH_URL, CELIAC_DATASET_SLUG, INFANT_DATASET_SLUG
from load import load_mpx_research_data, load_celiac_data, load_infant_breastfeeding_data
from analyze import plot_statistics

if __name__ == "__main__":
    # Creates directories
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(RESULTS_DIR, exist_ok=True)

    print("Starting Breastfeeding & Gluten Sensitivity Data Analysis Pipeline\n")

    # --- 1. MPX Research Data (healthdata.gov) ---
    print("Loading MPX Research Data...")
    mpx_df = load_mpx_research_data()
    if mpx_df is not None:
        print(f"MPX Research Data Shape: {mpx_df.shape}")
        print(mpx_df.head())
        plot_statistics(mpx_df, 'MPX_Research', result_dir=RESULTS_DIR)
    print("\n" + "=" * 60 + "\n")

    # --- 2. Celiac Disease Data (Kaggle) ---
    print("Loading Celiac Disease Data...")
    celiac_df = load_celiac_data()
    if celiac_df is not None:
        print(f"Celiac Disease Data Shape: {celiac_df.shape}")
        print(celiac_df.head())
        plot_statistics(celiac_df, 'Celiac_Disease', result_dir=RESULTS_DIR)
    print("\n" + "=" * 60 + "\n")

    # --- 3. Infant Breastfeeding & Weight Data (Kaggle) ---
    print("Loading Infant Breastfeeding Data...")
    infant_df = load_infant_breastfeeding_data()
    if infant_df is not None:
        print(f"Infant Breastfeeding Data Shape: {infant_df.shape}")
        print(infant_df.head())
        plot_statistics(infant_df, 'Infant_Breastfeeding', result_dir=RESULTS_DIR)
    print("\n" + "=" * 60 + "\n")

    print("--- Breastfeeding & Gluten Sensitivity Analysis Complete! ---")
    print(f"Check '{RESULTS_DIR}' directory for plots and visualizations.")
