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
import seaborn as sns

#----------------------------------------------------------------------------------------

# The following code loads the iris file into a pandas dataframe and adds column headers to it.

df = pd.read_csv('iris.data', header = None)

df.columns = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Iris Class"]


#-------------------------------------------------------------------------------
# The following data gives a summary description of the entire iris table
# it transposes the headings into nice side column and uses the describe function
# to give the main statistics of the data set ----------

summary = df.describe()
summary = summary.transpose()
summary.head()


# The following code loads each class of iris into its own dataframe to perform analysis on it and
# then uses the describe() function of pandas dataframes to output the statistical information needed
# and assigns the information to variables which will be output to a text file further down the code.
#------------------------------------------------------------------------------------------

# Iris Setosa

iris_setosa = df[df['Iris Class'] == "Iris-setosa"]    
setosa_summary = iris_setosa.describe()
setosa_summary = setosa_summary.transpose()


#--------------------------------------------------------

# Iris Vericolor

iris_versicolor = df[df['Iris Class'] == "Iris-versicolor"]    
versicolor_summary = iris_versicolor.describe()
versicolor_summary = versicolor_summary.transpose()

#---------------------------------------------------------

# Iris Virginica

iris_virginica = df[df['Iris Class'] == "Iris-virginica"]    
virginica_summary = iris_virginica.describe()
virginica_summary = virginica_summary.transpose()


#---------------------------------------------------------

# The following code reveals the correlations between the different variables

correlations = df.groupby("Iris Class").corr()


#------------------------------------------------------------------------



# The following code creates a histogram of the sepal lengths for all the classes

x = df["Sepal Length"] 
plt.hist(x, bins = 10, color = "blue", edgecolor='black', linewidth=1)
plt.title("Sepal Length in cm")
plt.xlabel("Sepal_Length_cm")
plt.ylabel("Count") 
plt.savefig("Sepal_Length.png")
plt.clf()




# The following code creates a histogram of the sepal widths for all the classes

y = df["Sepal Width"] 
plt.hist(y, bins = 10, color = "green", edgecolor='black', linewidth=1)
plt.title("Sepal Width in cm")
plt.xlabel("Sepal_Width_cm")
plt.ylabel("Count")
plt.savefig("Sepal_Width.png")
plt.clf()



# The following code creates a histogram of the petal length of all the iris classes.

z = df["Petal Length"] 
plt.hist(z, bins = 10, color = "yellow", edgecolor='black', linewidth=1)
plt.title("Petal Length in cm")
plt.xlabel("Petal_Length_cm")
plt.ylabel("Count")
plt.savefig("Petal_Length.png")
plt.clf()


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
# In the code below, the variables declared earlier in the program are output to a text file.
#----Sepal Length analysis written to file.---------------------------------

f = open("datafile.txt", "a")
f.write("Analysis of Fishers Iris Data Set\n\n")
f.write("Below is an overall statistical description of the complete iris data set\n\n")
f.write(str(summary.head()) + '\n\n')

f.write("Below is a statistical description of the iris setosa species\n\n")
f.write(str(setosa_summary.head()) + '\n\n')

f.write("Below is a statistical description of the iris versicolor species\n\n")
f.write(str(versicolor_summary.head()) + '\n\n')

f.write("Below is a statistical description of the iris virginica species\n\n")
f.write(str(virginica_summary.head()) + '\n\n')

f.write("Observations\n\n")
f.write("Iris Setosa  has on average significantly shorter sepals than the other two species\n")
f.write("but they are on average a bit wider.\n")
f.write("Iris Setosa seems to have far smaller petals, both width and lengthwise, than the other classes.\n")
f.write("Iris Versicolor has longer but thinner sepals than Iris Setosa\n")
f.write("but overall they are smaller than Iris Virginica, so this species seems to lie in the middle\n")
f.write("of the three.  Its petal size, both length and width are again larger than Iris Setosa but smaller\n")
f.write("than Iris Virginica, which in terms of both its petals and sepals dimensions is on average the largest\n")
f.write("of the three species.\n\n\n")

f.write("The following code shows the correlation coefficients between different pairs of variables\n\n")
f.write(str(correlations) + '\n\n')
f.write("Observations\n\n")
f.write("With Iris Setosa, there is a strong correlation between the sepal width and length at about 0.704\n")
f.write("but a weaker correction between the petal width and length at 0.306\n")
f.write("With Iris Verisicolr there is a strong correlation between petal and sepal length 0.754\n")
f.write("and also between petal width and length 0.786.\n")
f.write("With Iris Virginica there is a definite strong correlation between sepal and petal length 0.864\n")




f.close()




#-----------------scatterplot-------------------------
# The following code generates a scatter plot for the widths and heights of the iris petals
# and for the widths and lengths of the iris sepals. The information is taken from the original dataframe 
# df declared at the beginning of the program.

e = df["Sepal Length"] 
f = df["Sepal Width"] 
g = df["Petal Length"]
h = df["Petal Width"]



sns.scatterplot(data=df, x="Sepal Length", y="Sepal Width", hue="Iris Class")
plt.savefig("Scatterplot_Sepal.png")
plt.clf()

sns.scatterplot(data=df, x="Petal Length", y="Petal Width", hue="Iris Class")
plt.savefig("Scatterplot_Petal.png")
plt.clf()




