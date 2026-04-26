import pandas as pd

df = pd.read_csv("Data_Analysis\Pandas\Iris.csv")
print(df.head())

# Basic statistics
print(df.describe())
print(df.info())
print(df.columns)
print(df.dtypes)
print(df.shape)

#Filtering Data

# Show only flowers where:
# SepalLengthCm > 5
print(df[df["SepalLengthCm"]>5.0])

# Show only flowers where: species is "Iris-setosa"
print(df[df["Species"]=="Iris-setosa"])

# Show flowers where:
# PetalLengthCm > 4
# AND
# Species = virginica

print(df[(df["PetalLengthCm"]>4.0) & (df["Species"]=="Iris-virginica")])

# Sorting Data

# flowers with highest petal length
print(df.sort_values(by="PetalLengthCm", ascending=False))

# flowers with smallest sepal width
print(df.sort_values(by="SepalWidthCm", ascending=True))

# Value counts

# How many flowers of each species are there?
print(df["Species"].value_counts())

# GroupBy

# Average sepal length for each species
print(df.groupby("Species")["SepalLengthCm"].mean())

# Average petal length for each species
print(df.groupby("Species")["PetalLengthCm"].mean())

#Basic Insights

# Setosa average sepal length = __
# Versicolor average petal length = __
df1 = df[df["Species"] == "Iris-setosa"]
print("Setosa Average sepal length: ", df1["SepalLengthCm"].mean())

df2 = df[df["Species"] == "Iris-versicolor"]
print("Versicolor Average petal length: ", df2["PetalLengthCm"].mean())

# Mini Analyst Challenge

# Which species has longest petals on average?
df3 = df.groupby("Species")["PetalLengthCm"].mean()
print("Species with longest average petals: ", df3.idxmax())

# Which species has smallest sepal width?
df4 = df.groupby("Species")["SepalWidthCm"].mean()
print("Species with smallest sepal width: ", df4.idxmin())

# Which species appears most frequently?
df5 = df.value_counts("Species")
print("Species with most flowers: ", df5.idxmax())


