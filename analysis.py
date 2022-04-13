# The following project concerns the public Fishers Iris data set.
# The dataset must be researched and documentented and all code written in Python.
# Information relating to this data set can be found online at 
# http://archive.ics.uci.edu/ml/datasets/iris
# This dataset contains data relating to three classes of Iris plant of which there are 50 instances of 
# of each in the dataset.
# the atributes in the dataset relating to each instance are as follows
# 1. sepal length in cm
# 2. sepal width in cm
# 3. petal length in cm
# 4. petal width in cm
# 5. class:
# -- Iris Setosa
# --Iris Versicolour
# --Iris Virginica
# This program will output a summary of each variable to a single text file
# it will save a histogram of each variable to png files
# It will output a scatter plot of each pair of variables
# It will perform some other relevant analysis.

# reading in the file for testing purposes

# f = open("iris.data", "r")
# print(f.readline())

# irisfile = open("iris.data", "r")
# for x in irisfile:
  # print(x)

# The following code loads the iris file into a pandas datafile and adds column headers to it.

import pandas as pd

df = pd.read_csv('iris.data', header = None)

df.columns = ["Sepal Length", "Sepal width", "Petal Length", "Petal width", "Iris Class"]

# code to check dataframe ok and load first 3 rows
# print(df.head(3))

# this code  finds the average length in cm of the iris data.

# meanVal = df["Sepal Length"].mean()
# print(meanVal)

# this code  finds the mode length of the iris data.

# modeVal = df["Sepal Length"].mode()
# print(modeVal)

# this code  finds the shortest length of the iris data.

# minVal = df["Sepal Length"].min()
# print(minVal)

# this code  finds the maxium length of the iris data.

# maxVal = df["Sepal Length"].max()
# print(maxVal)


# This code separates the sepal length and the class of iris into a separate dataframe
# calculates the mean/average for each class of iris.

df_sepallength = df[["Sepal Length", "Iris Class"]]
#print(df_sepallength)

meanvalue = df_sepallength.groupby("Iris Class").mean()
print(meanvalue)












# Iris Setosa

# print(df["Sepal Length"])
# print(df.loc[df['Iris Class'] == "Iris-setosa"])
# this code separates the Iris Setosa data into its own dataframe

# df_iris_setosa = df.loc[df['Iris Class'] == "Iris-setosa"]

# print(df_iris_setosa)








