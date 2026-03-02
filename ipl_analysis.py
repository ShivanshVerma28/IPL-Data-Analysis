# ============================================================
# IPL Data Analysis - Exploratory Data Analysis (EDA)
# Author: Shivansh Verma
# Tools: Python, Pandas, Matplotlib
# Platform: Google Colab / Jupyter Notebook
# Dataset: IPL Matches & Deliveries (2008-2023)
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import warnings
warnings.filterwarnings('ignore')

# ── 1. LOAD DATA ─────────────────────────────────────────────
print("Loading IPL dataset...")
matches = pd.read_csv('matches.csv')
deliveries = pd.read_csv('deliveries.csv')

print(f"Matches dataset: {matches.shape[0]} rows, {matches.shape[1]} columns")
print(f"Deliveries dataset: {deliveries.shape[0]} rows, {deliveries.shape[1]} columns")

# ── 2. DATA CLEANING & WRANGLING ─────────────────────────────
print("\n--- Data Cleaning ---")

# Check missing values
print("Missing values in matches:\n", matches.isnull().sum()[matches.isnull().sum() > 0])

# Drop rows where result is missing
matches.dropna(subset=['winner'], inplace=True)

# Standardize team names (some teams have renamed)
team_rename = {
    'Delhi Daredevils': 'Delhi Capitals',
    'Deccan Chargers': 'Sunrisers Hyderabad',
    'Rising Pune Supergiants': 'Rising Pune Supergiant',
}
matches['winner'] = matches['winner'].replace(team_rename)
matches['team1'] = matches['team1'].replace(team_rename)
matches['team2'] = matches['team2'].replace(team_rename)

# Convert date column
matches['date'] = pd.to_datetime(matches['date'])
matches['season'] = matches['date'].dt.year

print("Data cleaning complete.")

# ── 3. STATISTICAL ANALYSIS ──────────────────────────────────

# 3.1 Most Successful Teams (Win Count)
team_wins = matches['winner'].value_counts().head(10)

# 3.2 Toss Impact Analysis
matches['toss_won_match'] = matches['toss_winner'] == matches['winner']
toss_win_pct = matches['toss_won_match'].mean() * 100
print(f"\nToss winner wins the match: {toss_win_pct:.1f}% of the time")

# 3.3 Top Run Scorers
top_batsmen = (deliveries.groupby('batter')['batsman_runs']
               .sum()
               .sort_values(ascending=False)
               .head(10))

# 3.4 Top Wicket Takers
wicket_deliveries = deliveries[deliveries['dismissal_kind'].notna() &
                               ~deliveries['dismissal_kind'].isin(['run out', 'retired hurt', 'obstructing the field'])]
top_bowlers = (wicket_deliveries.groupby('bowler')['dismissal_kind']
               .count()
               .sort_values(ascending=False)
               .head(10))

# 3.5 Win Rate by Venue
venue_stats = matches.groupby('venue').agg(
    total_matches=('id', 'count'),
).sort_values('total_matches', ascending=False).head(10)

# 3.6 Seasons Analysis
season_matches = matches.groupby('season')['id'].count()

# ── 4. DATA VISUALIZATION ────────────────────────────────────
fig, axes = plt.subplots(3, 2, figsize=(16, 18))
fig.suptitle('IPL Data Analysis (2008-2023)', fontsize=20, fontweight='bold', y=1.01)

# Plot 1: Most Successful Teams
axes[0, 0].barh(team_wins.index[::-1], team_wins.values[::-1], color='#1f77b4', edgecolor='black')
axes[0, 0].set_title('Top 10 Most Successful Teams', fontsize=13, fontweight='bold')
axes[0, 0].set_xlabel('Number of Wins')
for i, v in enumerate(team_wins.values[::-1]):
    axes[0, 0].text(v + 0.5, i, str(v), va='center', fontsize=9)

# Plot 2: Top Run Scorers
axes[0, 1].barh(top_batsmen.index[::-1], top_batsmen.values[::-1], color='#ff7f0e', edgecolor='black')
axes[0, 1].set_title('Top 10 Run Scorers (All Time)', fontsize=13, fontweight='bold')
axes[0, 1].set_xlabel('Total Runs')
for i, v in enumerate(top_batsmen.values[::-1]):
    axes[0, 1].text(v + 10, i, str(v), va='center', fontsize=9)

# Plot 3: Top Wicket Takers
axes[1, 0].barh(top_bowlers.index[::-1], top_bowlers.values[::-1], color='#2ca02c', edgecolor='black')
axes[1, 0].set_title('Top 10 Wicket Takers (All Time)', fontsize=13, fontweight='bold')
axes[1, 0].set_xlabel('Total Wickets')
for i, v in enumerate(top_bowlers.values[::-1]):
    axes[1, 0].text(v + 0.3, i, str(v), va='center', fontsize=9)

# Plot 4: Toss Impact
toss_labels = ['Toss Winner\nWon Match', 'Toss Winner\nLost Match']
toss_values = [toss_win_pct, 100 - toss_win_pct]
axes[1, 1].pie(toss_values, labels=toss_labels, autopct='%1.1f%%',
               colors=['#2ca02c', '#d62728'], startangle=90,
               wedgeprops={'edgecolor': 'black'})
axes[1, 1].set_title('Toss Impact on Match Result', fontsize=13, fontweight='bold')

# Plot 5: Matches per Season
axes[2, 0].plot(season_matches.index, season_matches.values, marker='o',
                color='#9467bd', linewidth=2, markersize=7)
axes[2, 0].fill_between(season_matches.index, season_matches.values, alpha=0.3, color='#9467bd')
axes[2, 0].set_title('Number of Matches Per Season', fontsize=13, fontweight='bold')
axes[2, 0].set_xlabel('Season')
axes[2, 0].set_ylabel('Matches')
axes[2, 0].xaxis.set_major_locator(ticker.MaxNLocator(integer=True))

# Plot 6: Top Venues
axes[2, 1].barh(venue_stats.index[::-1], venue_stats['total_matches'][::-1],
                color='#8c564b', edgecolor='black')
axes[2, 1].set_title('Top 10 Venues by Matches Hosted', fontsize=13, fontweight='bold')
axes[2, 1].set_xlabel('Total Matches')
axes[2, 1].tick_params(axis='y', labelsize=8)

plt.tight_layout()
plt.savefig('ipl_analysis_results.png', dpi=150, bbox_inches='tight')
plt.show()
print("\nAnalysis complete! Chart saved as ipl_analysis_results.png")

# ── 5. BUSINESS INTELLIGENCE SUMMARY ─────────────────────────
print("\n========== KEY INSIGHTS ==========")
print(f"1. Most successful team: {team_wins.index[0]} with {team_wins.values[0]} wins")
print(f"2. Top run scorer: {top_batsmen.index[0]} with {top_batsmen.values[0]} runs")
print(f"3. Top wicket taker: {top_bowlers.index[0]} with {top_bowlers.values[0]} wickets")
print(f"4. Toss advantage: Toss winner wins {toss_win_pct:.1f}% of matches")
print(f"5. Total seasons analyzed: {matches['season'].nunique()}")
print(f"6. Total matches analyzed: {len(matches)}")
print("===================================")
