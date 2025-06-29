![Netflix Dashboard](/netflix_logo.jpg)

# Netflix Data Cleaning, Analysis & Visualization

## Project Story

Imagine this: You open Netflix, hoping to start your next binge session. Instead, you end up scrolling endlessly, drowning in options. What if that chaos could be transformed into clear, meaningful insights?

Welcome to **Netflix & Analyze** — a data-driven deep dive where we clean, explore, and visualize Netflix data to uncover the stories behind the screen. Think of this as the backstage pass to your favorite streaming platform. We take a messy dataset, refine it, and build an interactive Tableau dashboard so you can explore viewing trends instead of just shows.

## Project Overview

This project focuses on cleaning, analyzing, and visualizing Netflix data to understand trends, content distribution, and ratings. The final output is a Tableau dashboard for interactive exploration.

## Project Structure

```
📁 Netflix Data- Cleaning, Analysis and Visualization/
│── 📂 Data/
│   ├── netflix_titles.csv             # Raw dataset
│   ├── netflix_titles_cleaned.csv     # Cleaned dataset
│   ├── netflix_tableau_ready.csv      # Ready for Tableau
│── 📂 scripts/
│   ├── data_cleaning.py
│   ├── exploratory_analysis.py
│   ├── dashboard_visualization.py
│── 📂 output/                         # Visualizations and plots
│── README.md
```

## Dataset Information

* **Source**: Netflix Kaggle Dataset
* **Columns**: `show_id`, `type`, `title`, `director`, `country`, `date_added`, `release_year`, `rating`, `duration`, `listed_in`
* **Analysis Goals**:

  * Movies vs TV Shows distribution
  * Trends of content added over the years
  * Top genres and ratings
  * Monthly release patterns
  * Country-wise content distribution

## Installation & Setup

### 1. Clone the Repository

```bash
git clone <repo-url>
cd Netflix Data- Cleaning, Analysis and Visualization
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Data Cleaning Script

```bash
python scripts/data_cleaning.py
```

### 4. Run Exploratory Data Analysis

```bash
python scripts/exploratory_analysis.py
```

* Output visualizations will be saved in the `output/` folder.

### 5. Prepare Data for Tableau

```bash
python scripts/dashboard_visualization.py
```

## Exploratory Data Analysis (EDA)

Key visuals include:

* Content type distribution (Movies vs TV Shows)
* Top genres and ratings
* Monthly release trends (heatmap)
* Duration and rating trends
* Geographic distribution

## Tableau Dashboard

### Loading Data in Tableau

1. Open Tableau Desktop or Tableau Public
2. Click "Connect to a Text File"
3. Select `Data/netflix_tableau_ready.csv`
4. Start building your visualizations

### Suggested Dashboard Elements

* Movies vs TV Shows (area chart)
* Content trends over the years (line graph)
* Monthly releases (Gantt or heatmap)
* Top genres and ratings
* Countries producing most content

## Future Improvements

* Predictive analytics on content trends
* Sentiment analysis of reviews
* Streamlit app for interactive web-based exploration

## Contact

Questions or ideas? Feel free to reach out and connect.
