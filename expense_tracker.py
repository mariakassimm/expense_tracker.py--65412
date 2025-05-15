import datetime
expenses = []


def add_expense():
    print("\n--- Add New Expense ---")
    try:
        date_str = input("Enter date (YYYY-MM-DD): ")
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        category = input("Enter category (e.g., Food, Transport, Shopping): ")
        amount = float(input("Enter amount: "))
        description = input("Enter description: ")

        entry = {
            "date": date,
            "category": category,
            "amount": amount,
            "description": description
        }
        expenses.append(entry)
        print("Expense added successfully!\n")
    except ValueError:
        print("Invalid input! Please try again.\n")


def view_expenses():
    print("\n--- All Expenses ---")
    if not expenses:
        print("No expenses recorded yet.\n")
    else:
        for idx, exp in enumerate(expenses, start=1):
            print(
                f"{idx}. Date: {exp['date']}, Category: {exp['category']}, Amount: ${exp['amount']:.2f}, Description: {exp['description']}")
        print()


def total_by_category():
    print("\n--- Total Expenses by Category ---")
    cat = input("Enter category name: ")
    total = sum(exp['amount'] for exp in expenses if exp['category'].lower() == cat.lower())
    print(f"Total spent on '{cat}': ${total:.2f}\n")


def delete_expense():
    view_expenses()
    try:
        idx = int(input("Enter expense number to delete: "))
        if 1 <= idx <= len(expenses):
            removed = expenses.pop(idx - 1)
            print(f"Removed expense: {removed['description']} (${removed['amount']:.2f})\n")
        else:
            print("Invalid entry number.\n")
    except ValueError:
        print("Invalid input! Please enter a number.\n")


def main():
    while True:
        print("==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total by Category")
        print("4. Delete an Expense")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_by_category()
        elif choice == '4':
            delete_expense()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
