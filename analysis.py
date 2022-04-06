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

#print(df.to_string())

df.columns = ["Sepal Length", "Sepal width", "Petal Length", "Petal width", "Iris Class"]

# print(df.head(3))

# this code performs some analysis on each class of Irish
# Iris Setosa

# print(df["Sepal Length"])
# print(df.loc[df['Iris Class'] == "Iris-setosa"])
# this code separates the Iris Setosa data into its own dataframe

df_iris_setosa = df.loc[df['Iris Class'] == "Iris-setosa"]

# print(df_iris_setosa)

# The code calculates the mean of the Irish setosa sepal Lengths.

# mean_length_sepal_setosa = df_iris_setosa["Sepal Length"].mean()
# print(mean_length_sepal_setosa)
# max_length_sepal_setosa = df_iris_setosa["Sepal Length"].max()
# print(max_length_sepal_setosa)
min_length_sepal_setosa = df_iris_setosa["Sepal Length"].min()
print(min_length_sepal_setosa)






