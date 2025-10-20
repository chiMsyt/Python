'''
Loops in Python

Automatic Repetition

for Loop - iterating over known sequences
while Loop - repeating while a condition is true
Loop Control - taking charge with break, continue, and pass
Nested Loops - patterns within patterns

'''

'''
for Loop : Your Iteration Workhorse
used when you know how many times you want to loop, or you want to iterate over each item in a collection
it iterates over any iterable: lists, strings, tuples, dictionaries, and range()

'''

# iterating over a list
from doctest import NORMALIZE_WHITESPACE


fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
  print(fruit)
  
# iterating over a string
for char in "Hello":
  print(char)
  
# using range() to loop a specific number of times
for i in range(5): # Loops 0, 1, 2, 3, 4
  print(f"Loop iteration {i}")
  
'''
range() Function : Your Loop Counter
range() generates a sequence of numbers, perfect for controlling your loops
range(stop) : 0 to stop-1
range(start, stop) : start to stop-1
range(start, stop, step) : start to stop-1, incrementing by step

'''

# counting from 0 to 4
for m in range(5):
  print(m) # 0, 1, 2, 3, 4
  
# counting from 2 to 6
for s in range(2, 7):
  print(s) # 2, 3, 4, 5, 6
  
# counting even numbers from 0 to 10
for y in range(0, 11, 2):
  print(y) # 0, 2, 4, 6, 8, 10
  
'''
while Lopp : Repeat While True
used when you don't know how many times you need to loop, but you know under what condition it should stop
the loop continues as long as the condition is True

'''

# a simple counter
count = 5
while count > 0:
  print(f"Countdown: {count}")
  count -= 1 # decrement count, CRUCIAL to avoid an infinite loop!
print("Blast off!")

# user input validation
user_input = ""
while user_input != "quit":
  user_input = input("Enter a command (type 'quit' to exit): ")
  print(f"You entered: {user_input}")
  
'''
for vs while : Which One to Use?

                  for Loop                                                            while Loop
use when: iterating over a known sequence (list, string, range)                    waiting for a specific condition to become False.
          you KNOW the number of iterations (or defined by data)                   you DON'T KNOW the number of iterations in advance

rule of thumb: 
iterating over items? -> use a [for] loop
looping until something happens? -> use a [while] loop
'''

'''
Loop Control : The Emergency Exit
the break statement immediately terminates the entire loop it is in
program execution jumps to the first line after the loop

'''

# searching for an item
numbers = [1, 3, 5, 7, 9, 11]
search_for = 7

for num in numbers:
  print(f"Checking {num}")
  if num == search_for:
    print("Item found!")
    break # stop the loop immediately
# code continues here after the break

'''
Loop Control : continue - The Skip Button
the continue statement skips the rest of the current iteration and jumps to the top of the loop for the next one

'''

# printing only odd numbers
for num in range(10):
  if num % 2==0: # if the number is even...
    continue # ...skip the print statement
  print(num) # output : 1, 3, 5, 7, 9
  
'''
Loop Control : pass - The Placeholder
the pass statement does absolutely nothing. it's a null operation
why? as a placeholder, when syntax requires a statement but you don't want to execute and code

'''

# placeholder for future code
my_list = []
for item in my_list:
  # TODO : Implement this logic later
  pass # without 'pass' this would be a syntax error!
# this is valid and runs without error

'''
Nested Loops : Patterns within Patterns
you can put loop inside another loop, essential for working with multi-dimensional data
inner loop : runs completely for every single iteration of the outer loop

'''

# creating a pattern
for s in range(3): # outer loop
  for o in range(3): # inner loop
    print(f"s = {s}, o = {o}")
    
# Common Use Case:
# iterating over a 2D list (a grid)
matrix = [[1,2,3], [4,5,6], [7,8,9]]
for row in matrix:
  for cell in row:
    print(cell, end='')
  print() # new line after each row


# putting it all together:
while True: # Main program loop
    print("\n--- Calculator ---")
    print("1. Add")
    print("2. Multiply")
    print("3. Quit")
    choice = input("Enter your choice (1-3): ")
    if choice == '3':
        print("Goodbye!")
        break # BREAK out of the main loop to exit
    if choice not in ('1', '2'):
        print("Invalid choice. Please try again.")
        continue # CONTINUE to skip the rest and show the menu again
    # This part only runs for valid choices 1 or 2
    numbers = input("Enter two numbers separated by a space: ").split()
    num1 = int(numbers[0])
    num2 = int(numbers[1])
    if choice == '1':
        print(f"Result: {num1 + num2}")
    elif choice == '2':
        print(f"Result: {num1 * num2}")

'''
Summary & Key Takeaways

for - iterating over sequences (lists, strings, range)
while - run as long as a condition is True
break - exits the loop immediately
continue - skips to the next iteration
pass - placeholder, does nothing
nested loops - powerful for complex patterns and multi-dimensional data

choose the right tool : [for] - known iterations, [while] - conditonal repetition
'''