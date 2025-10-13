'''

Task 1: The Basic Calculator
Write a program that does the following:
1.  Assigns two different numbers to two variables, a and b.
2.  Calculates and prints the result of:
    *   Addition (a + b)
    *   Subtraction (a - b)
    *   Multiplication (a * b)
    *   Floating-Point Division (a / b)
    *   Integer Division (a // b)
    *   Modulus (a % b)
    *   Exponentiation (a  b)

Example Output:
a = 15, b = 4
Addition: 19
Subtraction: 11
Multiplication: 60
Floating-Point Division: 3.75
Integer Division: 3
Modulus: 3
Exponentiation: 50625

'''

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print(f"The sum of {a} and {b} is {a + b}")
print(f"The difference of {a} and {b} is {a - b}")
print(f"The product of {a} and {b} is {a * b}")
print(f"The floating point quotient of {a} and {b} is {a / b}")
print(f"The integer quotient of {a} and {b} is {a // b}")
print(f"The remainder of {a} and {b} is {a % b}")
print(f"The power of {a} to {b} is {a ** b}")