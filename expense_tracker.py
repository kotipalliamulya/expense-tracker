import csv
from collections import defaultdict
import matplotlib.pyplot as plt

FILE = "expenses.csv"

def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category (Food/Travel/Shopping): ").lower()
    amount = float(input("Enter amount: "))

    with open(FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

    print("Expense added!")

def view_expenses():
    try:
        with open(FILE, "r") as file:
            reader = csv.reader(file)
            total = 0
            print("\n All Expenses:")
            for row in reader:
                print(row)
                total += float(row[2])
            print("Total Expense:", total)
    except:
        print(" No data found!")

def category_analysis():
    data = defaultdict(float)

    try:
        with open(FILE, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                category = row[1]
                amount = float(row[2])
                data[category] += amount

        print("\nCategory Analysis:")
        for k, v in data.items():
            print(k, ":", v)

        # Graph
        plt.bar(data.keys(), data.values())
        plt.title("Expense by Category")
        plt.xlabel("Category")
        plt.ylabel("Amount")
        plt.show()

    except:
        print(" No data found!")

def monthly_report():
    month = input("Enter month (MM): ")
    total = 0

    try:
        with open(FILE, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0].split("-")[1] == month:
                    total += float(row[2])

        print(f"Total expense for month {month}: {total}")
    except:
        print(" No data found!")

while True:
    print("\n==== Smart Expense Tracker ====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Category Analysis")
    print("4. Monthly Report")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        category_analysis()
    elif choice == "4":
        monthly_report()
    elif choice == "5":
        break
    else:
        print(" Invalid choice")