# Output Variables

# The Python print() function is often used to output variables

x = "Marsella"

# In the print() function, you output multiple variables, separated by a comma

x = "Marsella"
y = "is"
z = "the best"
print(x, y, z)

# You can also use the + operator to output multiple variables

t = "Tim "
a = "is "
g = "good "
print(t + a + g)
# Note that without the space, it would be "Timisgood"

# In the print() function, when you try to combine a string and a number, Python will give you an error

c = 5
y = "Gabriel"
print(c + y)
# TypeError: can only concatenate str (not "int") to str

# The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types