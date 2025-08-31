# Variables are containers for storing data values
# A variable is created the moment you first assign a value to it

x = 2
y = "Marsella"

print(x, y)

# Variables don't need to be declared with any particular type, and can even change type after they have been set

x = 2 # x is of type int
x = "Tim" # x is now of type str

print(x)

# Casting
# To specify the data type of a variable, this can be done with casting

x = str(3) # x will be '3'
y = int(3) # y will be 3
z = float(3) # z will be 3.0

# Get the Type
# To get the data type of a variable, use type() function

x = 2
y = "Marsella"

print(type(x))
print(type(y))

# Single or Double Quotes?
# String variables can be declared either by using single or double quotes

x = 'Tim'
# is the same as,
x = "Tim"

# Case-Sensitive
a = 1
A = "one"
# A will not overwrite a