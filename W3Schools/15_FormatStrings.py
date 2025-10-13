# String Format

# We cannot combine strings and numbers like this:
age = 22
# This will produce an error:
txt = "My name is Tim, I am " + age
print(txt)
# but we can combine strings and numbers using the f-strings or by using the function format()

# F-Strings
# Preferred way of formatting strings
# to specify a string as an f-string, put [f] in front of the string literal, and add {} as placeholders for variables and other operations
age = 22
txt = f"My name is Tim, I am {age}"
print(txt)

# Placeholders and Modifiers
# placeholders can contain variables, operations, functions, and modifiers to format the value
# add a placeholder for the [price] variable
price = 59
txt = f"The price is {price} dollars"
print(txt)

# a placeholder can include a modifier to format the value
# a modifier is included by adding a colon [:] followed by a legal formatting type, like .2f which means fixed point number with 2 decimals
# display the price with 2 decimals
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

# a placeholder can contain Python code, like math operations
txt = f"The price is {20 * 59} dollars"
print(txt)