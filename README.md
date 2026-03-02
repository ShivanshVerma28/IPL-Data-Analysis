# 🏏 IPL Data Analysis

Exploratory Data Analysis (EDA) on Indian Premier League (IPL) match data from 2008 to 2023 using Python.

## 📌 Project Overview

This project analyzes IPL match and delivery-level data to uncover trends in team performance, player statistics, and match outcomes. The goal is to derive meaningful business intelligence insights from raw cricket data using data wrangling, statistical analysis, and data visualization techniques.

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| Python | Core programming language |
| Pandas | Data cleaning, wrangling & ETL |
| Matplotlib | Data visualization |
| Google Colab | Development platform |

## 📂 Dataset

| File | Description |
|------|-------------|
| `matches.csv` | Match-level data — teams, venue, toss, winner, result |
| `deliveries.csv` | Ball-by-ball delivery data — batsman, bowler, runs, wickets |

**Source:** [Kaggle - IPL Dataset](https://www.kaggle.com/datasets/patrickb1912/ipl-complete-dataset-20082020)

> Download the dataset from Kaggle and place `matches.csv` and `deliveries.csv` in the project folder before running.

## 📊 Analysis Performed

- Data Cleaning — Handled missing values, standardized team names, converted date formats
- Data Wrangling — Grouped, aggregated, and derived new columns for analysis
- Statistical Analysis — Win counts, toss impact percentage, run/wicket totals
- ETL Pipeline — Extracted raw CSV data, transformed it, loaded insights into visualizations
- Data Visualization — 6 charts covering teams, players, venues, and seasons
- Business Intelligence — Key insights summarized for decision-making

## 📈 Key Insights

1. Most Successful Team — Mumbai Indians lead in total wins across all seasons
2. Top Run Scorer — Virat Kohli holds the record for most IPL runs
3. Top Wicket Taker — Lasith Malinga leads in wickets
4. Toss Advantage — Toss winner wins approximately 50-52% of matches
5. Peak Season — IPL saw highest match count in 2013 and 2022 seasons
6. Top Venue — Wankhede Stadium and Eden Gardens host the most matches

## How to Run

### Option 1: Google Colab (Recommended)
1. Upload `ipl_analysis.py`, `matches.csv`, and `deliveries.csv` to Colab
2. Run all cells

### Option 2: Local Machine
```
git clone https://github.com/shivanshverma28/ipl-data-analysis.git
cd ipl-data-analysis
pip install pandas matplotlib
python ipl_analysis.py
```

## Project Structure

```
ipl-data-analysis/
├── ipl_analysis.py
├── matches.csv
├── deliveries.csv
├── ipl_analysis_results.png
└── README.md
```

## Author

**Shivansh Verma**
- LinkedIn: linkedin.com/in/shivanshverma28

---
If you found this project helpful, please give it a star!
