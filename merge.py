# -*- coding: utf-8 -*-
"""merge.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mgyKiS_qEom9jdVZxvxwzxWbunpNwuuk
"""

import pandas as pd
import os
import glob

# Folder containing all CSV files
folder_path = "/content/drive/My Drive/TW/Dataset/"  # Update this with the actual folder path

# Get a list of all CSV files in the folder
csv_files = glob.glob(os.path.join(folder_path, "*.csv"))

# Create an empty list to store DataFrames
dfs = []

# Read each CSV file and append to the list
for file in csv_files:
    df = pd.read_csv(file)
    dfs.append(df)

# Concatenate all DataFrames into a single DataFrame
merged_df = pd.concat(dfs, ignore_index=True)

# Save the merged DataFrame to a new CSV file
merged_df.to_csv("/content/drive/My Drive/TW/Dataset/merged_tweets.csv", index=False)

print(f"Merged {len(csv_files)} CSV files into 'merged_tweets.csv' successfully!")

import pandas as pd

# Load datasets
file1_path = "/content/drive/My Drive/TW/Dataset/merged_tweets.csv"
file2_path = "/content/drive/My Drive/TW/Dataset/Tweets.csv"

df1 = pd.read_csv(file1_path)  # Already structured dataset
df2 = pd.read_csv(file2_path, header=None, names=["Tweet ID", "Text"])  # Fix column names

# Remove invalid Tweet IDs (entries where Tweet ID is 0)
df2 = df2[df2["Tweet ID"] != 0]

# Add missing columns with placeholder values
df2["Author ID"] = "Unknown"  # Placeholder for missing Author IDs
df2["Time"] = "Unknown"       # Placeholder for missing timestamps

# Reorder columns to match df1
df2 = df2[["Tweet ID", "Author ID", "Time", "Text"]]

# Merge both datasets
merged_df = pd.concat([df1, df2], ignore_index=True, sort=False)

# Save the final merged dataset
merged_df.to_csv("final_merged_tweets.csv", index=False)

print("Datasets merged successfully! ✅")