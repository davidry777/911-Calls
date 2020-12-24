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

# Creating a groupby object called byMonth, and creating a plot indicating the count of calls per month
byMonth = df.groupby('Month').count()
print(byMonth.head())
byMonth['twp'].plot()
plt.show()

# Creating a lmplot on the number of calls per month
sns.lmplot(x='Month', y='twp', data=byMonth.reset_index())
plt.show()

# Creating Date column and making a plot on 911 calls based on Date
df['Date'] = df['timeStamp'].apply(lambda c: c.date())
df.groupby('Date').count()['twp'].plot()
plt.tight_layout()
plt.show()

# Creating three separate plots based on Reason
df[df['Reason'] == 'EMS'].groupby('Date').count()['twp'].plot()
plt.title('EMS')
plt.tight_layout()
plt.show()

df[df['Reason'] == 'Traffic'].groupby('Date').count()['twp'].plot()
plt.title('Traffic')
plt.tight_layout()
plt.show()

df[df['Reason'] == 'Fire'].groupby('Date').count()['twp'].plot()
plt.title('Fire')
plt.tight_layout()
plt.show()

# Creating a heatmap plot using the new hourPerDay DataFrame
hourPerDay = df.groupby(by=['Day of Week','Hour']).count()['Reason'].unstack()
hourPerDay.head()
plt.figure(figsize=(12,6))
sns.heatmap(data=hourPerDay, cmap='coolwarm')
plt.show()
