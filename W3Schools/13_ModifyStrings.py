# Modify Strings

# Python has a set of built-in methods that you can use on strings

# Upper Case
# upper() returns the string in upper case
a = "Hello, World!"
print(a.upper())

# Lower Case
# lower() returns the string in lower case
a = "Hello, World!"
print(a.lower())

# Remove Whitespace
# Whitespace is the space before and/or after the actual text, and very often you want to remove this space
# strip() removes any whitespace from beginning or the end
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# Replace String
# replace() replaces a string with another string
a = "Hello, World!"
print(a.replace("H", "J"))

# Split String
# split() returns a list where the text between the specified separator becomes the list items
# split() splits the string into substrings if it finds instances of the separator
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']