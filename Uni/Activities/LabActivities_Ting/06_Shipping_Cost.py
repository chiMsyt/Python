'''
Challenge Problem (Bonus)

The Shipping Cost Calculator with Rules
Write a program that calculates shipping costs based on the following complex rules:
*   The base shipping cost is $10.
*   If the order total weight is over 20 pounds, add $5.
*   If the shipping destination is "international", double the total cost.
*   However, if the customer is a "premium" member, they get a 20% discount on the final cost and are exempt from the international surcharge.

Instructions:
1.  Create variables for weight, destination ("domestic" or "international"), and membership ("standard" or "premium").
2.  Use arithmetic operators to calculate the costs.
3.  Use logical operators (and, or, not) to check the conditions for the premium member exemption and other rules.
4.  Print a detailed breakdown of the final shipping cost.

Example Output:

Weight (lbs): 25
Destination (domestic/international): international
Membership (standard/premium): premium
Final Shipping Cost: $12.00
(Details: Base $10 + Overweight $5, Premium 20% discount applied, International fee waived.)

'''

# Prompt for inputs
weight = int(input("Weight (lbs): "))
destination = input("Destination (domestic/international): ")
membership = input("Membership (standard/premium): ")

# Calculate base and overweight
overweight_fee = 5 if weight > 20 else 0
total = 10 + overweight_fee

# Normalize inputs
is_premium = membership.lower().strip() == "premium"
dest_lower = destination.lower().strip()

# Build details string starting with base
details = "Base $10"
if overweight_fee > 0:
    details += " + Overweight $5"

# Apply rules based on membership
if is_premium:
    final_cost = total * 0.8
    details += ", Premium 20% discount applied"
    if dest_lower == "international":
        details += ", International fee waived."
else:
    if dest_lower == "international":
        total *= 2
        final_cost = total
        details += ", International doubling applied"
    else:
        final_cost = total

# Output the result
print(f"Final Shipping Cost: ${final_cost:.2f}")
print(f"(Details: {details})")
