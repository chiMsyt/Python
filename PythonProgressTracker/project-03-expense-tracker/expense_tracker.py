import csv
import os

FILE_NAME = "expenses.csv"

# Ensure CSV file exists with headers
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Description", "Amount"])


def add_expense():
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (Food, Transport, Bills, Entertainment, Other): ")
    if category not in ["Food", "Transport", "Bills", "Entertainment", "Other"]:
        print("Invalid category. Please try again.")
        return
    description = input("Enter the description: ")
    amount = input("Enter the amount: ")

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])
    
    print("Expense added successfully!\n")


def view_expenses():
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            print(f"{i}. {row}")
    print()


def search_expenses():
    keyword = input("Enter a keyword to search: ").lower()
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        results = [row for row in reader if keyword in " ".join(row).lower()]
        
    if len(results) <= 0:
        print("No matching expenses found.\n")
    else:
        print("\n--- Search Results ---")
        for row in results:
            print(row)
        print()


def total_by_category():
    totals = {}
    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])
            totals[category] = totals.get(category, 0) + amount
            
    print("\n--- Total Expenses by Category ---")
    for category, total in totals.items():
        print(f"{category}: ${total:.2f}")
    print()


def delete_expense():
    with open(FILE_NAME, mode='r') as file:
        reader = list(csv.reader(file))

    if len(reader) <= 1:
        print("No expenses to delete.\n")
        return

    for i, row in enumerate(reader):
        print(f"{i}. {row}")

    try:
        index = int(input("Enter the number of the expense to delete: "))
        if index == 0:
            print("You cannot delete the header row!\n")
            return
        deleted = reader.pop(index)
    except (ValueError, IndexError):
        print("Invalid selection.\n")
        return

    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(reader)

    print(f"Deleted expense: {deleted}\n")


def edit_expense():
    with open(FILE_NAME, mode='r') as file:
        reader = list(csv.reader(file))

    if len(reader) <= 1:
        print("No expenses to edit.\n")
        return

    for i, row in enumerate(reader):
        print(f"{i}. {row}")

    try:
        index = int(input("Enter the number of the expense to edit: "))
        if index == 0:
            print("You cannot edit the header row!\n")
            return
        expense = reader[index]
    except (ValueError, IndexError):
        print("Invalid selection.\n")
        return

    print("\nLeave blank to keep current value.")
    new_date = input(f"Enter new date (current: {expense[0]}): ") or expense[0]
    new_category = input(f"Enter new category (current: {expense[1]}): ") or expense[1]
    new_description = input(f"Enter new description (current: {expense[2]}): ") or expense[2]
    new_amount = input(f"Enter new amount (current: {expense[3]}): ") or expense[3]

    reader[index] = [new_date, new_category, new_description, new_amount]

    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(reader)

    print("Expense updated successfully!\n")


def main():
    while True:
        print("===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expenses")
        print("4. Total Expenses by Category")
        print("5. Delete Expense")
        print("6. Edit Expense")
        print("7. Exit")
        
        choice = input("Choose an option (1-7): ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            search_expenses()
        elif choice == '4':
            total_by_category()
        elif choice == '5':
            delete_expense()
        elif choice == '6':
            edit_expense()
        elif choice == '7':
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
