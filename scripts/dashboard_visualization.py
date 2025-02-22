import pandas as pd
import os

os.makedirs("Data", exist_ok=True)

data=pd.read_csv("Data/netflix_titles_cleaned.csv")

#dropping unnecessary columns
tableau_data=data.drop(columns=["genres"])

#saving this for tableau
tableau_file_path="Data/netflix_tableau_ready.csv"
tableau_data.to_csv(tableau_file_path, index=False)

print(f"Tableau-ready dataset is saved as {tableau_file_path}")
