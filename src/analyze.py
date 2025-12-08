import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

RESULTS_DIR = "results"
os.makedirs(RESULTS_DIR, exist_ok=True)

sns.set_style("whitegrid")


# ---------- Infant dataset ----------

def plot_infant_growth(infant_df):
    """
    Plot average infant weight by month and breastfeeding pattern.
    Assumes columns: Month, Weight, Breastfeeding Partern.
    """
    df = infant_df.copy()
    df["Month_num"] = df["Month"].str.extract(r"(\d+)").astype(int)

    avg_weight = (
        df.groupby(["Month_num", "Breastfeeding Partern"])["Weight"]
        .mean()
        .reset_index())

    plt.figure(figsize=(6, 4))
    for method, group in avg_weight.groupby("Breastfeeding Partern"):
        plt.plot(
            group["Month_num"],
            group["Weight"],
            marker="o",
            linewidth=2.5,
            label=method,)

    plt.title("Average Infant Weight Trajectory by Feeding Method")
    plt.xlabel("Month")
    plt.ylabel("Average Weight")
    plt.legend()
    plt.grid(alpha=0.3, linestyle="--")
    plt.tight_layout()
    plt.savefig(f"{RESULTS_DIR}/infant_weight_trajectory_linechart.png", dpi=150)
    plt.close()


# ---------- Celiac dataset ----------

def plot_celiac(celiac_df):
    """
    Make: age histogram, IgA boxplot by cd_type with medians,
    and correlation heatmap for Age, IgA, IgG, IgM.
    """
    df = celiac_df.copy()

    # ensures numeric
    for col in ["Age", "IgA", "IgG", "IgM"]:
        df[col] = df[col].apply(
            lambda x: float(x) if str(x).strip() not in ("", "NaN", "nan") else np.nan)

    # 1) Age histogram
    plt.figure(figsize=(6, 5))
    df["Age"].hist(bins=15, color="green", edgecolor="black")
    plt.title("Distribution of Ages - Celiac Dataset (Histogram)")
    plt.xlabel("Age")
    plt.ylabel("Number of Patients")
    plt.tight_layout()
    plt.savefig(f"{RESULTS_DIR}/celiac_age_histogram.png", dpi=150)
    plt.close()

    # 2) IgA boxplot by cd_type + medians
    plt.figure(figsize=(6, 4))
    ax = sns.boxplot(data=df, x="cd_type", y="IgA")
    medians = df.groupby("cd_type")["IgA"].median()
    for i, (group, median) in enumerate(medians.items()):
        ax.text(
            i,
            median,
            f"{median:.2f}",
            ha="center",
            va="center",
            fontsize=9,
            color="black",
            fontweight="bold",)
    plt.title("IgA Levels by Celiac Disease Type (boxplot)")
    plt.xlabel("Celiac Disease Type")
    plt.ylabel("IgA Level")
    plt.tight_layout()
    plt.savefig(f"{RESULTS_DIR}/celiac_immuno_boxplot.png", dpi=150)
    plt.close()

    # 3) Correlation heatmap
    num_cols = ["Age", "IgA", "IgG", "IgM"]
    corr = df[num_cols].corr()

    plt.figure(figsize=(6, 5))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", vmin=-1, vmax=1)
    plt.title("Correlation: Age & Immunoglobulins (Heatmap)")
    plt.tight_layout()
    plt.savefig(f"{RESULTS_DIR}/celiac_corr_heatmap.png", dpi=150)
    plt.close()


# ---------- Monkeypox dataset ----------

def plot_monkeypox(monkeypox_df):
    """
    Make: region pie chart, completion bar chart, and
    description-length boxplot by Topic.
    Assumes columns: Region, Completion, Topic, Brief Description.
    """
    df = monkeypox_df.copy()

    # 1) Region pie chart with percentages outside and legend
    region_counts = df["Region"].value_counts()
    plt.figure(figsize=(6, 6))
    wedges, _ = plt.pie(
        region_counts,
        labels=None,
        startangle=90,
        counterclock=False,)

    total = region_counts.sum()
    for w, value in zip(wedges, region_counts):
        angle = (w.theta2 + w.theta1) / 2.0
        x = 1.1 * np.cos(np.deg2rad(angle))
        y = 1.1 * np.sin(np.deg2rad(angle))
        pct = 100 * value / total
        plt.text(x, y, f"{pct:.1f}%", ha="center", va="center")

    plt.legend(
        wedges,
        region_counts.index,
        title="Region",
        loc="center left",
        bbox_to_anchor=(1, 0.5),)
    plt.title("Monkeypox Research Projects by Region")
    plt.tight_layout()
    plt.savefig(f"{RESULTS_DIR}/monkeypox_proj_byregion_piechart.png", dpi=150)
    plt.close()

    # 2) Completion bar chart (short labels)
    comp_counts = df["Completion"].value_counts()
    comp_counts = comp_counts[comp_counts.index.str.len() <= 15]

    plt.figure(figsize=(10, 5))
    comp_counts.sort_index().plot(kind="bar", color="#16a34a", edgecolor="black")
    plt.title("Monkeypox Projects by Anticipated Completion")
    plt.xlabel("Anticipated Completion")
    plt.ylabel("Number of Projects")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(f"{RESULTS_DIR}/monkeypox_proj_comp_barchart.png", dpi=150)
    plt.close()

    # 3) Description length boxplot by Topic + medians
    df["Desc_len"] = df["Brief Description"].str.len()

    plt.figure(figsize=(9, 5))
    ax = sns.boxplot(data=df, x="Topic", y="Desc_len")
    medians = df.groupby("Topic")["Desc_len"].median()
    for i, (group, median) in enumerate(medians.items()):
        ax.text(
            i,
            median,
            f"{median:.2f}",
            ha="center",
            va="center",
            fontsize=9,
            color="black",
            fontweight="bold",)
    plt.title("Description Length by Topic - Monkeypox Projects")
    plt.xlabel("Monkeypox research topic")
    plt.ylabel("Description length (characters)")
    plt.xticks(rotation=20, ha="right")
    plt.tight_layout()
    plt.savefig(f"{RESULTS_DIR}/monkeypox_desclen_boxplot.png", dpi=150)
    plt.close()
