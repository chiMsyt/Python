# Part 1: Basic Function Arguments
# I'm defining the function here with two required arguments.
def describe_pet(animal_type, pet_name):
    """
    Prints a sentence describing a pet's type and name.
    Arguments:
        animal_type (str): The kind of animal.
        pet_name (str): The name of the pet.
    """
    print(f"I have a {animal_type} and its name is {pet_name}.")

# Now I'm calling the function three times with different values.
describe_pet("hamster", "Harry")
describe_pet("lizard", "Lizzy")
describe_pet("turtle", "Speedy")


# Part 2: Positional vs Keyword Arguments
# I'm using the same function from Part 1 but calling it differently.
print("\n--- Testing Positional vs Keyword ---")

# Positional arguments (order matters)
describe_pet("dog", "Chanel")

# Keyword arguments (I can swap the order here)
describe_pet(pet_name="Milo", animal_type="cat")


# Part 3: Default Arguments
# I need to redefine the function to include a default value for animal_type.
# Note: I had to move animal_type to the end because default args must come last.
def describe_pet(pet_name, animal_type="dog"):
    """
    Prints a pet description.
    Defaults to 'dog' if no animal_type is provided.
    """
    print(f"I have a {animal_type} and its name is {pet_name}.")

print("\n--- Testing Default Arguments ---")
describe_pet("Brownie")  # Using the default "dog"
describe_pet("Nugget", "chicken")  # Overriding the default


# Part 4: Create Your Own Function
def order_drink(drink, size="medium", iced=False):
    """
    Creates a drink order string.
    Arguments:
        drink (str): The name of the beverage.
        size (str): Default is 'medium'.
        iced (bool): Default is False.
    Returns:
        str: The formatted order sentence.
    """
    # I added this logic to decide if I should print 'hot' or 'iced'
    if iced:
        temp = "iced"
    else:
        temp = "hot"
        
    return f"Your order: {size} {temp} {drink}"

print("\n--- My Drink Orders ---")
# 1. Default order
print(order_drink("coffee"))

# 2. Large hot chocolate (iced is False by default)
print(order_drink("chocolate", size="large"))

# 3. Small iced milk tea
print(order_drink("milk tea", size="small", iced=True))


# Part 5: Mini Challenge (Calculator)
def compute(operation, num1, num2=1):
    """
    Performs basic math based on the operation string.
    If 'subtract' is used without a second number, it subtracts 1.
    """
    if operation == "add":
        return num1 + num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "subtract":
        return num1 - num2
    else:
        return "Invalid operation"

print("\n--- Calculator Results ---")
# Testing the add function
print(compute("add", 5, 10))

# Testing multiply with keywords
print(compute("multiply", num1=3, num2=4))

# Testing subtract using the default value for num2
print(compute("subtract", 20))

# Testing an operation that doesn't exist
print(compute("divide", 10, 5))