import pandas as pd
import matplotlib
matplotlib.use("Agg")  # Use TkAgg backend to prevent macOS issues
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("output", exist_ok=True)


data= pd.read_csv("Data/netflix_titles_cleaned.csv")

sns.set_style("darkgrid")

# 1. Content Type Distribution - piechart

plt.figure(figsize=(6, 6))
data["type"].value_counts().plot(kind="pie", autopct="%1.1f%%", colors=["#66b3ff", "#ff9999"], startangle=90)
plt.title("Distribution of Content by Type")
plt.ylabel("")  # Hide y-label
plt.savefig("output/content_type_pie_chart.png", bbox_inches="tight")
plt.close()


# 2. Top 10 Countries with Most Content
plt.figure(figsize=(10, 5))
top_countries = data["country"].value_counts().head(10)
sns.barplot(x=top_countries.values, y=top_countries.index, hue=top_countries.index, palette="viridis", legend=False)
plt.title("Top 10 Countries with Most Netflix Content", fontsize=14)
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.savefig("output/top_ten_countries.png", bbox_inches='tight')
plt.close()


# 3. Content Trend Over the Years - linegraph

plt.figure(figsize=(10, 5))
yearly_counts = data["year_added"].value_counts().sort_index()
sns.lineplot(x=yearly_counts.index, y=yearly_counts.values, marker="o", color="blue")
plt.title("Trend of Netflix Content Over the Years", fontsize=14)
plt.xlabel("Year Added")
plt.ylabel("Number of Titles")
plt.grid(True)
plt.savefig("output/content_trend_line.png", bbox_inches="tight")
plt.close()

#  4. Most Common Genres

plt.figure(figsize=(10, 5))
all_genres = data["listed_in"].str.split(", ").explode()
top_genres = all_genres.value_counts().head(10)
sns.barplot(x=top_genres.values, y=top_genres.index, hue=top_genres.index, palette="coolwarm", legend=False)
plt.title("Top 10 Most Common Genres", fontsize=14)
plt.xlabel("Number of Titles")
plt.ylabel("Genre")
plt.savefig("output/most_common_genres.png", bbox_inches='tight')
plt.close()

#  5. Top 10 Directors with Most Titles

plt.figure(figsize=(10, 5))
top_directors = data["director"].value_counts().head(10)
sns.barplot(x=top_directors.values, y=top_directors.index, hue=top_directors.index, palette="Blues_r", legend=False)
plt.title("Top 10 Directors with Most Titles", fontsize=14)
plt.xlabel("Number of Titles")
plt.ylabel("Director")
plt.savefig("output/top_ten_directors.png", bbox_inches='tight')
plt.close()

#  6. Monthly Content Releases - heatmap

plt.figure(figsize=(10, 5))
monthly_releases = data.groupby(["year_added", "month_added"]).size().unstack(fill_value=0)
sns.heatmap(monthly_releases, cmap="Blues", linewidths=0.5)
plt.title("Monthly Netflix Releases Heatmap")
plt.xlabel("Month")
plt.ylabel("Year")
plt.savefig("output/monthly_releases_heatmap.png", bbox_inches="tight")
plt.close()

# 7. Duration Distribution - Box plot
plt.figure(figsize=(8, 5))
sns.boxplot(x=data["duration"].dropna(), color="purple")
plt.title("Distribution of Content Duration")
plt.xlabel("Duration (in minutes/seasons)")
plt.savefig("output/duration_boxplot.png", bbox_inches="tight")
plt.close()

# 8. Year Added vs Duration - Scatter plot
plt.figure(figsize=(10, 5))
sns.scatterplot(x=data["year_added"], y=data["duration"], alpha=0.5, color="red")
plt.title("Year Added vs. Content Duration", fontsize=14)
plt.xlabel("Year Added")
plt.ylabel("Duration")
plt.savefig("output/year_vs_duration_scatter.png", bbox_inches="tight")
plt.close()

# 9 Netflix Ratings Distribution-Bar Chart

plt.figure(figsize=(10, 5))
rating_counts = data["rating"].value_counts()
sns.barplot(x=rating_counts.index, y=rating_counts.values, palette="coolwarm")
plt.title("Distribution of Ratings on Netflix", fontsize=14)
plt.xlabel("Rating")
plt.ylabel("Count")
plt.xticks(rotation=45)  # Rotated labels for better visibility
plt.savefig("output/netflix_ratings_bar.png", bbox_inches="tight")
plt.close()

# 2. Ratings Percentage Share-Pie Chart

plt.figure(figsize=(7, 7))
rating_counts.plot(kind="pie", autopct="%1.1f%%", cmap="Set2", startangle=90)
plt.title("Percentage Share of Each Rating")
plt.ylabel("")  #  y-label Hidden
plt.savefig("output/netflix_ratings_pie.png", bbox_inches="tight")
plt.close()

print("Exploratory Analysis Completed! New graphs saved in 'output/' folder.")
