# This section is for declaring variables
name = "Timothy Ting"
age = 22
height = 5.7
student = True
legal = True

# Where I format, and add calculations
introduction = "Welcome to Python Programming!"
introduction2 = "Python is widely used in data science, web development, AI, and more."
fullName = f"My name is {name}, I am {age} years old."
convertedHeight = f"My height is {height * 0.3048:.2f} meters."
amIaStudent = f"Am I a student? {student}"

# Printing each formatted line
print(introduction)
print(introduction2)

print()

print(fullName)
print(convertedHeight)
print(amIaStudent)

print()

print("Data Types: ")
print(type(name))
print(type(age))
print(type(height))
print(type(student))

print()

# 2nd part of activity
afterFiveYears = f"After 5 years, I will be {age + 5} years old."
convertedHeightCM = f"My height in centimeters is {height * 30.48:.1f} cm."
greeting = f"Hello, {name}! Nice to meet you." 
legal = f"Is student, and over 18? {legal}"

print(afterFiveYears)
print(convertedHeightCM)
print(greeting)
print(legal)

print()

# Just the same as the first two, but added together
number = input("Enter your favorite number: ")
doubleNum = int(number) * 2
print("Double your favorite number is: ", int(doubleNum))
favoriteWord = input("Enter your favorite word: ")
print(favoriteWord * 3)