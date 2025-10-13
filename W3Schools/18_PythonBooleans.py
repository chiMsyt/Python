# Python Booleans

# Booleans are just True/False
# In programming, we often need to know if an expression is True or False
# Every expression can be evaluated to get one of two answers; True or False
# Comparing two values, the expression is evaluated and Python returns the Boolean answer
print(10 > 9)
print(10 == 9)
print(10 < 9)

# When we run into a condition in an [if statement], Python returns True or False
# Print a message based on whether the condition is True or False:
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  
# Evaluate Values and Variables
# bool() allows you to evaluate any value, and give you True or False in return
# evaluate a string and a number:
print(bool("Hello"))
print(bool(15))

# evaluate two variables
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

# Most Values are True
# Almost any value is evaluated to True if it has some sort of content
# Any string is True, except empty strings
# Any number is True, except [0]
# Any list, tuple, set, and dictionary are True, except empty ones
# These will all return True
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

# Some Values are False
# There are not many values that evaluate to False, except empty values such as:
# (), [], {}, "", the number [0], and the value [None], and the value [False]
# These will return False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# one more value, or object in this case, evaluates to false, and that is if you have an object that is made from a class with a __len__ function that returns [0] or [False]
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

# Functions can Return a Boolean
# We can create functions that return a Boolean Value
def myFunction() :
  return True

print(myFunction())

# We can execute code based on the Boolean answer of a function
# Print "YES!" if the function returns True, otherwise print "NO!":
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
  
# Python also has many built-in functions that return a boolean value:
# isinstance() -> used to determine if an object is of a certain data type
# check if an object is an integer or not
x = 200
print(isinstance(x, int))