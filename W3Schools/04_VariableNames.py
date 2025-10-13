# Variable Names

# Variables can have short names, or more descriptive ones
# Rules for variables:
# 1. Must start with a letter or the underscore character
# 2. Cannot start with a number
# 3. Can only contain alpha-numeric characters and underscores
# 4. Case-sensitive
# 5. Cannot be any of the Python keywords

myvar = "Tim"
my_var = "Tim"
_my_var = "Tim"
myVar = "Tim"
MYVAR = "Tim"
myvar2 = "Tim"

# Illegal variable names:

2myvar = "Tim" # type: ignore
my-var = "Tim" # type: ignore
my var = "Tim" # type: ignore

# Multi Words Variable Names
# Variable names with more than one word can be difficult to read
# There are several techniques you can use to make them more readable

# Camel Case
# Each word, except the first, starts with a capital letter
myVariableName = "Tim"

# Pascal Case
# Each word starts with a capital letter
MyVariableName = "Tim"

# Snake Case
# Each word is separated by an underscore
my_variable_name = "Tim"