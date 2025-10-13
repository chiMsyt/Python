'''
Task 3: Unit Conversion Challenge
Write a program that solves the challenge from the presentation.
*   Prompt the user to enter a number of inches.
*   Convert the input to an integer.
*   Calculate how many feet and remaining inches that represents.
    *   *Hint: Use // for feet and % for inches.*
*   Print the result in a user-friendly format.

Example Output:

Enter the number of inches: 47
47 inches is equal to 3 feet and 11 inches.

'''

# Prompt user for input
total_inches = int(input("Enter the number of inches: "))

# Calculate feet and remaining inches
feet = total_inches // 12
remaining_inches = total_inches % 12

# Print the result
print(f"{total_inches} inches is equal to {feet} feet and {remaining_inches} inches.")