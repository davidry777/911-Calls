import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

# Reading 911.csv file and storing into df (data file)
df = pd.read_csv('911.csv')
# Checking info
print(df.info())
# Checking the head of the data file
print(df.head())

# Analyzing the top 5 zipcodes for 911 calls
print(df['zip'].value_counts().head(5))
# Analyzing the top 5 townships for 911 calls
print(df['twp'].value_counts().head(5))
# Analyzing the amount of unique title codes
print(df['title'].nunique())

# Creating a new column called Reason using lambda
df['Reason'] = df['title'].apply(lambda title: title.split(':')[0])
# Analyzing most common reasons for 911 call
print(df['Reason'].value_counts())
