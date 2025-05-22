import csv
import os
from datetime import datetime

FILENAME = "expenses.csv"

def add_expense():
    category = input("Enter category (e.g., Food, Transport): ")
    amount = input("Enter amount: $")

    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(FILENAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

    print("✅ Expense recorded!")

def view_expenses():
    if not os.path.exists(FILENAME):
        print("No expenses recorded yet.")
        return

    total = 0.0
    print("\n📋 Expenses:")
    print("-" * 30)
    with open(FILENAME, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"{row[0]} | {row[1]} | ${row[2]}")
            total += float(row[2])
    print("-" * 30)
    print(f"💰 Total spent: ${total:.2f}\n")

def main():
    while True:
        print("=== Daily Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
