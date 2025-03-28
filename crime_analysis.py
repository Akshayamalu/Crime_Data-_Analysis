import pandas as pd
import numpy as np

df = pd.read_csv(r"c:\Users\Home\OneDrive\Desktop\MY PROJECT\new datasets small\crime_dataset_india.csv")

df.info()
print(df.head())  
print(df.isnull().sum())
df.dropna(axis=1, inplace=True)

print(df.isnull().sum())  # Check missing values in each column

print(df.columns)  # This will show all column names in the dataset

print(df.describe())  # Summary statistics of numerical columns

print(df["Crime Domain"].value_counts())  # Count of crimes per category

print(df["City"].value_counts().head(10))  # Top 10 cities with most crimes

df.to_csv("cleaned_crime_data.csv", index=False)
df_cleaned = pd.read_csv("cleaned_crime_data.csv")  
print(df_cleaned.info())  
print(df_cleaned.head())  

