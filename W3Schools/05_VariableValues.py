# Variable Values

# Many values to Multiple Variables
# Python allows you to assign many values to multiple variables

x, y, z = "Orange", "Banana", "Cherry"
print(x, y, z)

# One Value to Multiple Variables
# And you can assign the same value to multiple variables in one line

x = y = z = "Orange"
print(x, y, z)

# Unpack a Collection
# If you have a collection of values in a list, tuple etc., Python allows you to extract the values into variables

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x, y, z)

