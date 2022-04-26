# The following project concerns the public Fishers Iris data set.
# The dataset must be researched and documentented and all code written in Python.
# Information relating to this data set can be found online at 
# http://archive.ics.uci.edu/ml/datasets/iris
# This dataset contains data relating to three classes of Iris plant of which there are 50 instances of 
# of each in the dataset.
# the atributes in the dataset relating to each instance are as follows
# sepal length in cm, sepal width in cm, petal length in cm, petal length in cm
# class: Iris Setosa, Iris Setosa, Iris Setosa
# output a summary of each variable to a single text file
# it will save a histogram of each variable to png files
# It will output a scatter plot of each pair of variables
# It will perform some other relevant analysis.
# For more information on this project including the resources used please
# refer to the read me file.


import pandas as pd
import matplotlib.pyplot as plt
#----------------------------------------------------------------------------------------

# The following code loads the iris file into a pandas dataframe and adds column headers to it.

df = pd.read_csv('iris.data', header = None)

df.columns = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Iris Class"]

#------------------------------------------------------------------------------------

# This code separates the sepal length and the class of iris into a separate dataframe

df_sepallength = df[["Sepal Length", "Iris Class"]]

# calculates the mean, maximum, minimum and median sepal length value for each class of iris.

meanvalue = df_sepallength.groupby("Iris Class").mean()
maxvalue = df_sepallength.groupby("Iris Class").max() 
minvalue = df_sepallength.groupby("Iris Class").min() 
medianvalue = df_sepallength.groupby("Iris Class").median()


#-------------------------------------------------------------------------------------------

# The following code creates a histogram of the sepal lengths for all the classes

x = df["Sepal Length"] 
plt.hist(x, bins = 10, color = "blue", edgecolor='black', linewidth=1)
plt.title("Sepal Length in cm")
plt.xlabel("Sepal_Length_cm")
plt.ylabel("Count") 
plt.savefig("Sepal_Length.png")
plt.clf()

#----------------------------------------------------------------------------------------------

# The following code separates the sepal width and class into its own dataframe to perform analysis on it
 df_sepalwidth = df[["Sepal Width", "Iris Class"]]

# calculating the mean, maximum, minimum and median sepal width within each iris group
meanvalsw = df_sepalwidth.groupby("Iris Class").mean()
minvalsw = df_sepalwidth.groupby("Iris Class").min()
maxvalsw = df_sepalwidth.groupby("Iris Class").max()
medianvalsw = df_sepalwidth.groupby("Iris Class").median()

 #---------------------------------------------------------------------------------------


# The following code creates a histogram of the sepal widths for all the classes

y = df["Sepal Width"] 
plt.hist(y, bins = 10, color = "green", edgecolor='black', linewidth=1)
plt.title("Sepal Width in cm")
plt.xlabel("Sepal_Width_cm")
plt.ylabel("Count")
plt.savefig("Sepal_Width.png")
plt.clf()

#------------------------------------------------------------------------------------------

# This code separates the petal length and the class of iris into a separate dataframe


 df_petallength = df[["Petal Length", "Iris Class"]]

# calculates the mean, maximum, minimum and median petal length for each class of iris.

 meanvaluepl = df_petallength.groupby("Iris Class").mean()
 maxvaluepl = df_petallength.groupby("Iris Class").max() 
 minvaluepl = df_petallength.groupby("Iris Class").min() 
medianvaluepl = df_petallength.groupby("Iris Class").median()


#-------------------------------------------------------------------------------------------
# The following code creates a histogram of the petal length of all the iris classes.

z = df["Petal Length"] 
plt.hist(z, bins = 10, color = "yellow", edgecolor='black', linewidth=1)
plt.title("Petal Length in cm")
plt.xlabel("Petal_Length_cm")
plt.ylabel("Count")
plt.savefig("Petal_Length.png")
plt.clf()

#------------------------------------------------------------------------

# The following code separates the Petal width and class into its own dataframe to perform analysis on it
 df_petalwidth = df[["Petal Width", "Iris Class"]]


# calculating the mean, maximum, minimum and median petal width within each iris group
meanvalpw = df_petalwidth.groupby("Iris Class").mean()
minvalpw = df_petalwidth.groupby("Iris Class").min()
maxvalpw = df_petalwidth.groupby("Iris Class").max()
medianvalpw = df_petalwidth.groupby("Iris Class").median()

#---------------------------------------------------------------------
# The following code creates a histogram of the petal widths of all the iris plants.


w = df["Petal Width"] 
plt.hist(w, bins = 10, color = "red", edgecolor='black', linewidth=1)
plt.title("Petal width in cm")
plt.xlabel("Petal_width_cm")
plt.ylabel("Count")
plt.savefig("Petal_Width.png")
plt.clf()


#-----------------------------------------------------------------------------

# -------Writing results to a text file-----------

f = open("myfile.txt", "a")
f.write("Analysis of the Iris Fisher Data Set!\n")
f.write("Below are the min, max, mean and median values of the Sepal Length grouped by Iris class\n\n")
f.write("Maximum sepal length Value per class\n")
f.write(str(maxvalue) + '\n\n')
f.write("Median sepal length per class\n")
f.write(str(medianvalue) + '\n\n')
f.write("Minimum sepal length  per class\n")
f.write(str(minvalue) + '\n\n')
f.write("Mean sepal length  per class\n")
f.write(str(meanvalue) + '\n\n')
f.write("It can be seen by the above analysis that the Iris-virginica class of iris tend to have the\n")
f.write("the longest sepals, followed by Iris-versicolor with Iris-setosa being the shortest. \n")
f.close()




#-----------------scatterplot-------------------------
# The following code generates a scatter plot for the widths and heights of the iris petals
# and for the widths and lengths of the iris sepals.

e = df["Sepal Length"] 
f = df["Sepal Width"] 
g = df["Petal Length"]
h = df["Petal Width"]


plt.scatter(e, f)
plt.savefig("Scatterplot_Sepal.png")
plt.clf()
#plt.show()

plt.scatter(g, h)
plt.savefig("Scatterplot_Petal.png")
plt.clf()
#plt.show()



