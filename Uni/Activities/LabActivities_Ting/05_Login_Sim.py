'''
Task 5: Secure System Login Simulator
Create a simple login system that checks multiple conditions.
1.  Set the correct username, password, and a boolean is_2fa_enabled (Two-Factor Authentication) to True.
2.  Prompt the user to enter their input_username, input_password, and input_2fa_code.
3.  Assume the correct 2FA code is "123456".
4.  The login is successful only if:
    *   The username is correct, AND
    *   The password is correct, AND
    *   (Either the user does not have 2FA enabled OR the entered 2FA code is correct).

Instructions:
*   Use and and or operators to combine these conditions in a single if statement.
*   Print "Login successful!" or "Login failed!" accordingly.

Example Output:

Enter username: Marsellugh
Enter password: 1202
Is 2FA enabled? (y/n): y
Enter 2FA code: 123456
Login successful!

'''

# Set correct credentials
correct_username = "Marsellugh"
correct_password = "1202"
correct_2fa_code = "123456"

# Prompt for inputs
input_username = input("Enter username: ")
input_password = input("Enter password: ")
enabled_str = input("Is 2FA enabled? (y/n): ")
is_2fa_enabled = enabled_str.lower() == "y"

# Prompt for 2FA code only if enabled
if is_2fa_enabled:
    input_2fa_code = input("Enter 2FA code: ")
else:
    input_2fa_code = correct_2fa_code  # Treat as correct if not enabled

# Check login conditions in a single if statement
if input_username == correct_username and input_password == correct_password and (not is_2fa_enabled or input_2fa_code == correct_2fa_code):
    print("Login successful!")
else:
    print("Login failed!")
