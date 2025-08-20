# project-02-calculator/calculator.py

def add(x, y):
    """Return the sum of x and y."""
    return x + y
def subtract(x, y):
    """Return the difference of x and y."""
    return x - y
def multiply(x, y):
    """Return the product of x and y."""
    return x * y
def divide(x, y):
    """Return the quotient of x and y."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def calculator():
    print("=== Project 02: Calculator ===")
    print("Available operations: add, subtract, multiply, divide")
    print("Type 'exit' to quit the calculator.")
    
    while True:
        op = input("\nEnter operation: ").strip().lower()
        
        if op == 'exit':
            print("Exiting the calculator. Goodbye!")
            break
        
        if op not in ['add', 'subtract', 'multiply', 'divide']:
            print("Invalid operation. Please try again.")
            continue
        
        try:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
        # Using type: ignore to suppress type checking for dynamic operations
        # This is a workaround for type checking since the operation is dynamic
        
        if op == "add":
            print(f"Result: {add(x, y)}") # type: ignore
        elif op == "subtract":
            print(f"Result: {subtract(x, y)}")
        elif op == "multiply":
            print(f"Result: {multiply(x, y)}")
        elif op == "divide":
            print(f"Result: {divide(x, y)}")
            
if __name__ == "__main__":
    calculator()