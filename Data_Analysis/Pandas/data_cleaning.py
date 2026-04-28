import numpy as np
import pandas as pd

df = pd.read_csv('Data_Analysis\Pandas\data.csv')

print(df.info())
print(df.isnull().sum())
print(df.describe())

#Missing Values Handling

df1 = df.dropna() #Drop rows with missing values
print(df1.info())
print(df1.isnull().sum())

numeric_cols = df.select_dtypes(include=[np.number]).columns #Select only numeric columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean()) #Fill missing values in numeric columns with mean
print(df.info())

categorical_cols = df.select_dtypes(include=['object']).columns #Select only categorical columns
df[categorical_cols] = df[categorical_cols].fillna(df[categorical_cols].mode().iloc[0]) #Fill missing values in categorical columns with mode
print(df.info())

df3 = df.fillna(0) #Fill missing values with 0
print(df3.info())

# Removing Duplicate Rows
df = df.drop_duplicates() #Drop duplicate rows

# Removing Leading and Trailing Whitespace from Column Names
df.columns = df.columns.str.strip() #Remove leading and trailing whitespace from column names
print(df.columns)

#Verify Cleaning
print(df.isnull().sum()) 

df.to_csv('Data_Analysis\Pandas\cleaned_data.csv', index=False) #Save cleaned data to a new CSV file
