# pands-project
GMIT Programming and scripting - Final project

 The following project concerns the public Fishers Iris data set.
 The dataset must be researched and documentented and all code written in Python.
 Information relating to this data set can be found online at 
 http://archive.ics.uci.edu/ml/datasets/iris
 This dataset contains data relating to three classes of Iris plant of which there are 50 instances of 
 of each in the dataset.
 the atributes in the dataset relating to each instance are as follows
 sepal length in cm, sepal width in cm, petal length in cm, petal length in cm
 class: Iris Setosa, Iris Setosa, Iris Setosa
 
 The main objectives of the project are: 
 output a summary of each variable to a single text file
 save a histogram of each variable to png files
 output a scatter plot of each pair of variables
 perform any other analysis that I feel is relevant.

Objectives of code:

The code for this program starts out by importing pandas for data analysis and matplotlib and Seaborn to help visualise my analysis. 
I used pandas dataframes for all lot of the analysis and matplotlib for creating and displaying the histograms and Seaborn for the scatterplots.

The first step was to read in the iris data set to the program and assigned it to a dataframe.
I created headers for the iris dataframe to make it easier to navigate and analyse.
Then I passed the data file in as an argument to the pandas dataframe to create a dataframe containing the entire file.
I created smaller data frames from this original dataframe with just the iris class and the variable I was trying to analysis
e.g df_sepallength = df[["Sepal Length", "Iris Class"]]
and achieved this by passing the column names in as an argument to the dataframe and creating a new dataframe from that.
then I used the mean, max, min and median functions to created variables from these dataframes to hold my analysis.

Doing all of the above was great practise in working with variables but the coding was quite laborious with way to many
write() functions. I felt that this was a good place to start and get some basic analysis pinned down.
I decided to revise the above and use the describe() method to output the information I needed,
(min, max, mean std dev etc)  with way less code than previously used and a much tidier output.  


The groupby() and corr() functions were very useful in outputting the correlation coeficcients in an organised table type format.

I used matplotlib and Seaborn to help visualise the data in the form of histograms for the individual variables (width, height..)
and the scatterplot for each pair of variables (sepal width & height, and petal width and height.

Finally I wrote my analysis and observations to a text file called datafile.txt using using the open() function to create the file
and the write() to write my data analysis to it.


Findings:



Iris Setosa  has on average significantly shorter sepals than the other two species
but they are on average a bit wider.
Iris Setosa seems to have far smaller petals, both width and lengthwise, than the other classes.
Iris Versicolor has longer but thinner sepals than Iris Setosa
but overall they are smaller than Iris Virginica, so this species seems to lie in the middle
of the three.  Its petal size, both length and width are again larger than Iris Setosa but smaller
than Iris Virginica, which in terms of both its petals and sepals dimensions is on average the largest
of the three species.

With Iris Setosa, there is a strong corelation between the sepal width and length at about 0.704
but a weaker correction between the petal width and length at 0.306
With Iris Verisicolr there is a strong correlation between petal and sepal length 0.754
and also between petal width and length 0.786.
With Iris Virginica there is a definite strong correlation between sepal and petal length 0.864




Resources:
https://www.w3schools.com/python/
I found this website terrific for general learning of python syntax to supplement my GMIT lectures.
https://www.w3schools.com/python/python_file_write.asp
This section of w3schools helped a lot with the syntax of how to write to a file. 
https://www.w3schools.com/python/pandas/default.asp
This module in W3 schools was a very helpful resource on how to use pandas, read and write to text files and manipulate dataframes.
The extra pandas lecture on the GMIT course was a great help trying to get to grips with pandas and its features.
to be continued......
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html
https://seaborn.pydata.org/introduction.html
https://python-graph-gallery.com/20-basic-histogram-seaborn
https://seaborn.pydata.org/generated/seaborn.scatterplot.html
https://www.adamsmith.haus/python/answers/how-to-display-a-seaborn-plot-in-python




 
