#pandas is a powerful data manipulation library in Python that provides data structures and functions needed to work with structured data seamlessly. 
#It is built on top of NumPy and is widely used for data analysis, cleaning, and visualization.
# Data Structures in Pandas:
# Series: A one-dimensional labeled array that can hold any data type (integers, strings, floating-point numbers, etc.). It is similar to a column in a spreadsheet or a database table.
# DataFrame: A two-dimensional labeled data structure with columns of potentially different types. It is similar to a table in a relational database or an Excel spreadsheet.
import pandas as pd

# s = pd.Series([10, 20, 30, 40, 50]) #creates a Series with the given list of values
# print(s) #prints the Series

# s1 = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e']) #creates a Series with the given list of values and custom index
# print(s1) #prints the Series with custom index

# df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
#                    'Age': [25, 30, 35, 40, 45],})
# print(df) #prints the DataFrame

# to read excel or csv file
df = pd.read_csv("C:\\Users\\priya\\Desktop\\DataScience_Roadmap\\Data_Analysis\\Pandas\\Iris.csv") #reads a CSV file into a DataFrame
print(df) #prints the DataFrame read from the CSV file

print(df.head()) #prints the first 5 rows of the DataFrame
print(df.tail()) #prints the last 5 rows of the DataFrame
print(df.describe()) #provides summary statistics of the DataFrame
print(df.info()) #provides information about the DataFrame, including data types and non-null counts

#Data Selection and Filtering:

print(df['SepalLengthCm']) #selects the 'SepalLengthCm' column from the DataFrame
print(type(df['Id'])) #prints the type of the 'Id' column, which is a Series
print(df[['SepalLengthCm', 'SepalWidthCm']]) #selects multiple columns from the DataFrame

print(df.iloc[0]) #selects the first row of the DataFrame using integer-location based indexing

df2 = pd.read_csv("C:\\Users\\priya\\Desktop\\DataScience_Roadmap\\Data_Analysis\\Pandas\\data.csv") #reads a CSV file into a DataFrame
print(df2) #prints the DataFrame read from the CSV file

print(df2.dropna()) #drops rows with missing values from the DataFrame
print(df2.fillna(0)) #fills missing values in the DataFrame with 0

#if we write df2.fillna(inplace=True) then it will fill the missing values in the original DataFrame df2 itself without creating a new DataFrame.
# therefore dont ue inplace=True if you want to keep the original DataFrame unchanged and create a new DataFrame with filled values.

print(df2.rename(columns={'SepalLengthCm': 'SL', 'SepalWidthCm': 'SW'})) #renames columns in the DataFrame
#print(df2) #prints the original DataFrame to show that it remains unchanged after renaming columns

#to convert the data type of a column in a DataFrame, we can use the astype() method. For example, if we want to convert the 'SL' column to integer data type, we can do it as follows:

#df2['SepalLengthCm'] = df2['SepalLengthCm'].astype(int) #converts the 'SepalLengthCm' column to integer data type
#print(df2.info()) #prints the 'SepalLengthCm' column after converting it to integer data type

print(df2["SepalLengthCm"][0]) #accesses the first value of the 'SepalLengthCm' column in the DataFrame

print(len(df2)) #prints the number of rows in the DataFrame

#adding new column to the DataFrame
df2["zeros"] = [0 for i in range(len(df2))] #adds a new column named 'zeros' to the DataFrame with all values set to 0
print(df2) #prints the DataFrame with the new 'zeros' column added

df2["zeros+1"] = df2["zeros"] + 1 #adds a new column named 'zeros+1' to the DataFrame by adding 1 to the 'zeros' column
print(df2) #prints the DataFrame with the new 'zeros+1' column added

#alternate option to add 1 to the 'zeros' column and create a new column 'zeros+1'
def fx(x):
    return x + 1
df2["zeros+1"] = df2["zeros"].apply(fx) #adds a new column named 'zeros+1' to the DataFrame by applying a lambda function to the 'zeros' column
print(df2) #prints the DataFrame with the new 'zeros+1' column added

#save df to csv file
df2.to_csv("C:\\Users\\priya\\Desktop\\DataScience_Roadmap\\Data_Analysis\\Pandas\\export.csv", index=False) #saves the DataFrame to a CSV file without including the index

#concatenate two DataFrames 
df3 = pd.DataFrame({"Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
                    "Marks": [25, 30, 35, 40, 45]})
print(df3) #prints the first DataFrame
df4 = pd.DataFrame({"Name": ["Harry", "John", "Tim", "Max", "Stubbs"],
                    "Marks ": [65, 23, 78, 99, 67]})
print(df4) #prints the second DataFrame
df5 = pd.concat([df3, df4]) #concatenates two DataFrames 
print(df5) #prints the merged DataFrame

#merging two DataFrames based on a common column
df6 = pd.DataFrame({"Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
                    "Marks": [65, 89, 60, 77, 59]}) 
print(df6) #prints the first DataFrame
df7 = pd.DataFrame({"Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
                    "Age": [25, 30, 35, 40, 45]})
print(df7) #prints the second DataFrame
df8 = pd.merge(df6, df7) #merges two DataFrames based on the common column 'Name'
print(df8) #prints the merged DataFrame with columns 'Name', 'Marks', and 'Age'