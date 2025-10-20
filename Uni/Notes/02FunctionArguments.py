'''
What are Function Arguments?

Arguments are like information you give to a function so it can do its job

examples:
a coffee machine needs coffee beans and water (arguments) to make coffee (function)
you need ingredients (arguments) to bake a cake (function)

'''
def say_hello(name):
  print(f"Hello, {name}!")
  
say_hello("Marsella") # "Marsella" is the argument

'''
a. Basic Function Arguments

What it means : functions can accept information through arguments

'''
# function that adds two numbers
def add_numbers(a,b):
  result = a + b
  return result

# using the function
sum = add_numbers(5,3)
print(sum) # output : 8
# key point; arguments make functions flexible and reusable!

'''
b. Positional vs. Keyword Arguments

positional arguments:
values are matched by position
order matters!

keyword arguments:
values are matched by name
order doesn't matter
clearer to read

'''
def introduce(name, age):
  print(f"My name is {name}, I'm {age} years old")

# correct order
introduce("Sol", 24) # works fine
# wrong order
introduce(24, "Sol") # doesn't make sense!

# KA:
def introduce(name, age):
  print(f"My name is {name}, I'm {age} years old")
  
# using keyword arguments
introduce(age = 24, name = "Sol") # perfectly fine
introduce(name = "Sol", age = 24) # also works
# benefit : easier to understand what each value means

'''
c. Default Argument Values

what are defaults?
pre-set values for arguments
makes arguments optional

'''
def greet(name, message = "Hello"):
  print(f"{message}, {name}!")

# using defaults
greet("Sella") # uses default "Hello"
greet("Sella", "Hi") # uses "Hi" instead
greet("Sella", "Good morning") # uses "Good morning" instead
# why? no need to repeat common values

# practical example:
def order_food(item, quantity=1, spicy=False):
    order = f"{quantity} {item}"
    if spicy:
        order += " (spicy)"
    return order

# Different ways to order:
print(order_food("pizza"))           # 1 pizza
print(order_food("burger", 2))       # 2 burgers  
print(order_food("noodles", 1, True)) # 1 noodles (spicy)
# note : required arguments must come first

# function with Multiple Arguments:
def calculator(operation, num1, num2):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    else:
        return "Unknown operation"
# Different ways to call it:

# Positional arguments
result1 = calculator("add", 10, 5)        # 15

# Keyword arguments  
result2 = calculator(num2=8, num1=4, operation="subtract")  # -4

# Mixed style
result3 = calculator("multiply", num1=3, num2=7)  # 21
# Flexibility: Choose the style that's clearest for your code!
print(f"result1 = {result1}, result2 = {result2}, result3 = {result3}")

# actual example : student report
# Practical Function:
def create_student_report(name, grade, subjects=["Math", "Science"]):
    report = {
        "student_name": name,
        "grade_level": grade,
        "subjects": subjects
    }
    return report
# Usage:
# Basic report
report1 = create_student_report("Alice", 10)

# Custom subjects
report2 = create_student_report("Bob", 11, ["Art", "Music", "History"])

# Using keywords
report3 = create_student_report(name="Carol", grade=12)


# common mistakes to avoid:
# 1. wrong order
def person_info(name, age):
    print(f"{name} is {age} years old")

person_info(24, "Sol")  # Wrong! Output: "25 is John years old"

# 2. forgetting required arguments
def person_info(name, age):
    print(f"{name} is {age} years old")

person_info("Sol")  # Error! Missing age argument

# quick tips
# 1. use descriptive argument names
# Good
def calculate_rectangle_area(width, height):
  pass

# Not so good  
def calculate_rectangle_area(a, b):
  pass

# 2. put required arguments first
# Correct
def function(required1, required2, optional1="default"):
  pass

# Wrong
def function(optional1="default", required1, required2): # type: ignore
  pass

'''
Simple Rules to Remember

1. Arguments = information for functions
2. Positional = order matters
3. Keyword = use names, order doesn't matter
4. Default values = make arguments optional
5. Required first = put required arguments before optional ones

Why?
benefits of using arguments:
reusable code - same function works with different data
flexible - can customize how functions work
organized - clear what information functions need
maintainable - easy to understand and modify

Key Points:
arguments let you pass information to functions
positional - simple, but order matters
keyword - clearer, order doesn't matter
defaults - make arguments optional
mix and match - use different styles as needed
remember; practice with small examples to build understanding!

'''