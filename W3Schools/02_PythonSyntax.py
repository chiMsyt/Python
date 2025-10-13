# Python Indentation

# Refers to the spaces at the beginning of a code line
# Compared to other languages, indentation is not only for readability
# Python uses indentation to indicate a block of code

if 5 > 2:
    print("Five is greater than two!")
    
# Python will give you an error if you skip the indentation

if 6 > 3:
print("Six is greater than three!") # type: ignore

# The number of spaces is up to you, most common is four, but it has to at least be one

if 6 > 3:
 print("Six is greater than three!")

if 6 > 3:
                print("Six is greater than three!")
                
# You have to use the same number of spaces in the same block of code, otherwise Python will give you an error

if 5 > 2:
    print("Five is greater than two!")
        print("Five is greater than two!") # type: ignore
        
# Python Variables
# Variables are created when you assign a value to it

x = 5
y = "Hello, World!"

# Python has no command for declaring a variable

# Comments
# These lines are called comments, often used for documentation-describing what a block of code does, etc.

# Suppressing Problems
# To suppress problems, use -> # type: ignore
# This will suppress the annoying red things on files