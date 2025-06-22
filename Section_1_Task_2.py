'''
2. Expense Tracker (Console)

Features:
Add daily expenses
Total calculator
Show summary

'''

expenses = []

def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    description = input("Enter description: ")
    try:
        amount = float(input("Enter expense amount: "))
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return
    expense = {"date": date, "description": description, "amount": amount}
    expenses.append(expense)
    print("Expense added successfully!")

def calc_total():
    return sum(expense["amount"] for expense in expenses)

def show_summary():
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\nExpense Summary:")
    print("-" * 40)
    for expense in expenses:
        print(f"Date: {expense['date']} | Description: {expense['description']} | Amount: ${expense['amount']:.2f}")
    print("-" * 40)
    print(f"Total Expenses: ${calc_total():.2f}\n")


while True:
        print("\nExpense Tracker")
        print("1. Add Daily Expense")
        print("2. Show Total Expense")
        print("3. Show Expense Summary")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            print(f"Total Expenses: ${calc_total():.2f}")
        elif choice == "3":
            show_summary()
        elif choice == "4":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

