import csv
import datetime


# Function to add an expense
def add_expense():
    amount = float(input("Enter the amount spent: "))
    category = input("Enter the category (e.g., Food, Entertainment): ")
    description = input("Enter a description (optional): ")
    date = input("Enter the date of the expense (YYYY-MM-DD, leave empty for today): ")

    if not date:
        date = datetime.date.today().strftime("%Y-%m-%d")

    # Save expense to file
    with open("expenses.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([amount, category, description, date])

    print("Expense added successfully!")


# Function to view all expenses
def view_expenses():
    try:
        with open("expenses.csv", mode='r') as file:
            reader = csv.reader(file)
            print("Expenses:")
            for row in reader:
                print(f"Amount: {row[0]} | Category: {row[1]} | Description: {row[2]} | Date: {row[3]}")
    except FileNotFoundError:
        print("No expenses recorded yet.")


# Function to view a summary of expenses
def summary_expenses():
    try:
        with open("expenses.csv", mode='r') as file:
            reader = csv.reader(file)
            total = 0
            categories = {}
            for row in reader:
                amount = float(row[0])
                total += amount
                category = row[1]
                if category not in categories:
                    categories[category] = 0
                categories[category] += amount

            print(f"Total Expenses: {total}")
            for category, amount in categories.items():
                print(f"Total spent on {category}: {amount}")
    except FileNotFoundError:
        print("No expenses recorded yet.")


# Main menu to interact with the app
def main():
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Summary")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            summary_expenses()
        elif choice == '4':
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()