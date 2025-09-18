# Pandas

# What is it used for?
# It's a Python library, built on top of NumPy
# Widely used in Data Analysis, Data Science, Machine Learning
# Comes from the term: "Panel Data"
# Using Pandas, we typically work with Series vs Dataframes

# Series
# Like a one-dimensional labeled column

# Data Frame
# Like a two-dimensional labeled grid/table

# With this library, we can Import, Display, Manipulate, Export tabulated data
# Python's version of Microsoft Excel, but on steroids

import pandas as pd # we have to declare pandas, in order to get started the (pd) is the alias -> used in calling constructor, etc, later on
# to check if we have pandas installed, we can do the following print statement
# print(pd.__version__) # output: 2.3.2, uncomment to run

# Lesson 1:

# Series = A Pandas 1-dimensional labeled array that can hold any data type
# think of it like a single column in a spreadsheet
data = [100, 102, 104]

series = pd.Series(data, index=["a", "b", "c"])

print(series)
# this will print 0 100 | 1 102 | 2 104 with 0,1,2 as indexes, and 100,102,104 as the data (one column each)
# index renames the initial [0, 1, 2] names of the first column to a,b,c respectively

print(series.loc["a"]) # output: 100 , this is the locate function