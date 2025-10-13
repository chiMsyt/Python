'''
Task 4: The Movie Ticket Price Decider
Write a program that determines the price of a movie ticket based on the following rules:
*   Base price is $12.
*   Children (age <= 12) get a $3 discount.
*   Seniors (age >= 65) get a $4 discount.
*   Students (check with a variable is_student) get a $2 discount.

Instructions:
1.  Create variables for age and is_student (a boolean).
2.  Use logical operators (and, or) and comparison operators (<=, >=) to create the discount rules.
    *   *Note: A person can only qualify for one best discount. A 70-year-old student should get the senior discount, not both.*
3.  Calculate the final price and print it.

Example Output:

Age: 20
Is student? (True/False): True
Your ticket price is $10.
'''

# Get user input
age = int(input("Age: "))
is_student_input = input("Is student? (True/False): ")
is_student = is_student_input.lower() == "true"
# Determine the best discount (only one applies, prioritizing highest discount)
discount = 0
if age >= 65:
    discount = 4
elif age <= 12:
    discount = 3
elif is_student:
    discount = 2
# Calculate final price
price = 12 - discount
# Output the result
print(f"Your ticket price is ${price}.")