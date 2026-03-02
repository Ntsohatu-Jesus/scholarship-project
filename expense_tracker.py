expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    expenses.append((name, amount))
    print("Expense added successfully!\n")

def view_expenses():
    if not expenses:
        print("No expenses recorded.\n")
        return

    print("\nExpenses:")
    for name, amount in expenses:
        print(f"{name}: ${amount}")
    print()

def view_total():
    total = 0
    for _, amount in expenses:
        total += amount
    print(f"\nTotal spending: ${total}\n")

def main():
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_total()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")

main()