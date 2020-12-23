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

# Creating a countplot of 911 calls by Reason
sns.countplot(x='Reason', data=df)
plt.show()

# Converting timeStamp column to DateTime objects
df['timeStamp'] = pd.to_datetime(df['timeStamp'])

# Creating new columns Hour, Month, and Day of  Week
df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)
df['Month'] = df['timeStamp'].apply(lambda time: time.month)
df['Day of Week'] = df['timeStamp'].apply(lambda time: time.dayofweek)

# Mapping actual string days to Day of Week column
dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
df['Day of Week'] = df['Day of Week'].map(dmap)

# Creating a countplot for the Day of Week column with hue based on Reason
sns.countplot(x='Day of Week', data=df, hue='Reason')
plt.show()

# Creating a countplot for the Month column with hue based on Reason
sns.countplot(x='Month', data=df, hue='Reason')
plt.show()
