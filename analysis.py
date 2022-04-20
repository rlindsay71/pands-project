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


# The following code loads the iris file into a pandas datafile and adds column headers to it.

#from isort import file
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('iris.data', header = None)

df.columns = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Iris Class"]

# code to check dataframe ok and load first 3 rows
# print(df.head(3))




# This code separates the sepal length and the class of iris into a separate dataframe
# calculates the mean/average sepal length for each class of iris.

#df_sepallength = df[["Sepal Length", "Iris Class"]]
#print(df_sepallength)

# meanvalue = df_sepallength.groupby("Iris Class").mean()
#print(meanvalue)

# Below calculates the maximum length within each class of iris.

# maxvalue = df_sepallength.groupby("Iris Class").max() 
# print(maxvalue)

# The code below determines the minimum irish length within each Iris class.

# minvalue = df_sepallength.groupby("Iris Class").min() 
# print(minvalue)

# The code below calculates the median(half way value) sepal length within each iris class

#medianvalue = df_sepallength.groupby("Iris Class").median()
#print(medianvalue)

# The following code creates a histogram of the sepal lengths for all the classes

x = df["Sepal Length"] 
plt.hist(x, bins = 20)
plt.title("Sepal Length in cm")
plt.xlabel("Sepal_Length_cm")
plt.ylabel("Count") 
plt.savefig("Sepal_Length.jpg")
#plt.show()



#----------------------------------------------------------------------------------------------

# The following code separates the sepal width and class into its own dataframe to perform analysis on it
# df_sepalwidth = df[["Sepal Width", "Iris Class"]]
# print(df_sepalwidth)


# calculating the mean sepal width within each iris group
#meanvalsw = df_sepalwidth.groupby("Iris Class").mean()
#print(meanvalsw)

# calculating the minimum sepal width within each iris group
#minvalsw = df_sepalwidth.groupby("Iris Class").min()
#print(minvalsw)

# calculating the maximum sepal width within each iris group

#maxvalsw = df_sepalwidth.groupby("Iris Class").max()
#print(maxvalsw)

# calculating the median sepal width within each iris group

# medianvalsw = df_sepalwidth.groupby("Iris Class").median()
# print(medianvalsw)

# The following code creates a histogram of the sepal widths for all the classes

y = df["Sepal Width"] 
plt.hist(y, bins = 20, color = "green")
plt.title("Sepal Width in cm")
plt.xlabel("Sepal_Width_cm")
plt.ylabel("Count")
plt.savefig("Sepal_Width.jpg")
#plt.show()

#------------------------------------------------------------------------------------------

# This code separates the petal length and the class of iris into a separate dataframe
# calculates the mean/average petal length for each class of iris.

# df_petallength = df[["Petal Length", "Iris Class"]]
# print(df_petallength)

# meanvaluepl = df_petallength.groupby("Iris Class").mean()
#print(meanvaluepl)

# Below calculates the maximum petal length within each class of iris.

# maxvaluepl = df_petallength.groupby("Iris Class").max() 
# print(maxvaluepl)

# The code below determines the minimum petal length within each Iris class.

# minvaluepl = df_petallength.groupby("Iris Class").min() 
# print(minvaluepl)

# The code below calculates the median(half way value) sepal length within each iris class

# medianvaluepl = df_petallength.groupby("Iris Class").median()
# print(medianvaluepl)



z = df["Petal Length"] 
plt.hist(z, bins = 20, color = "yellow")
plt.title("Petal Length in cm")
plt.xlabel("Petal_Length_cm")
plt.ylabel("Count")
plt.savefig("Petal_Length.jpg")
#plt.show()

#------------------------------------------------------------------------

# The following code separates the Petal width and class into its own dataframe to perform analysis on it
# df_petalwidth = df[["Petal Width", "Iris Class"]]
#print(df_petalwidth)


# calculating the mean petal width within each iris group
#meanvalpw = df_petalwidth.groupby("Iris Class").mean()
#print(meanvalpw)

# calculating the minimum petal width within each iris group
#minvalpw = df_petalwidth.groupby("Iris Class").min()
#print(minvalpw)

# calculating the maximum petal width within each iris group

#maxvalpw = df_petalwidth.groupby("Iris Class").max()
#print(maxvalpw)

# calculating the median petal width within each iris group

#medianvalpw = df_petalwidth.groupby("Iris Class").median()
# print(medianvalpw)

w = df["Petal Width"] 
plt.hist(w, bins = 20, color = "red")
plt.title("Petal width in cm")
plt.xlabel("Petal_width_cm")
plt.ylabel("Count")
plt.savefig("Petal_Width.jpg")
#plt.show()




#-----------------------------------------------------------------------------

# -------Testing exporting analysis to a new text file-----------

#f = open("myfile.txt", "a")
#f.write("This is where I will be putting the results of my analysis!\n")
#f.write(str(medianvalpw))
#f.close()

#------------------------------------------------------------------------------




