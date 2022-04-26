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
 
 The main tasks of the project are: 
 output a summary of each variable to a single text file
 save a histogram of each variable to png files
 output a scatter plot of each pair of variables
 perform any other analysis you feel is relevant.

Objectives of code:

The code for this program starts out by importing pandas and matplotlib, 
I used pandas dataframes for all lot of the analysis and matplotlib for creating and displaying the histograms and scatterplots
I created headers for the iris data file to make it easier to navigate and analyse.
Then I passed the data file in as an argument to the pandas dataframe to create a dataframe containing the entire file.
I created smaller data frames from this original dataframe with just the iris class and the variable I was trying to analysis
e.g df_sepallength = df[["Sepal Length", "Iris Class"]]
and achieved this by passing the column names in as an argument to the dataframe and creating a new dataframe from that.
then I used the mean, max, min and median functions to created variables from these dataframes to hold my analysis.
to be continued....
 
