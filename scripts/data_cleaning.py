import pandas as pd
import numpy as np
#loading data
data = pd.read_csv("Data/netflix_titles.csv")
print("Columns in dataset:", data.columns.tolist())

print("Initial Database information:")
print(data.info())

#handling missing values 
# in director, country with unknown
columns_to_fill = [col for col in ['director', 'country'] if col in data.columns]
data[columns_to_fill] = data[columns_to_fill].fillna("Unknown")

data['rating'] = data['rating'].fillna("Not Rated")

#date added to datetime
data['date_added'] = pd.to_datetime(data['date_added'])
data['date_added'] = data['date_added'].fillna(data['date_added'].mode()[0])

#removing duplicates
data.drop_duplicates(inplace=True)

#dropping unncessary columns like show_id
data.drop(columns= ['show_id'],inplace=True)

#feature Engineering
#extracting Y, M, D from 'date_added'
data['year_added']=data['date_added'].dt.year
data['month_added']=data['date_added'].dt.month
data['day_added']=data['date_added'].dt.day

 #converting 'duration' to numerical format
data['duration'] = data['duration'].str.replace(' min', '').str.replace(' Season', '').str.replace(' Seasons', '')
data['duration'] = pd.to_numeric(data['duration'],errors='coerce')

#splitting genres from listed_in column
data['genres'] = data['listed_in'].apply(lambda x: x.split(',') if isinstance(x, str) else [] )

#saving the cleaned dataset
cleaned_file_path="Data/netflix_titles_cleaned.csv"
data.to_csv(cleaned_file_path, index= False)
print(f"Cleaned dataset is saved as {cleaned_file_path}")

# final dataset display
print("Cleaned Dataset information:")
print(data.info())
