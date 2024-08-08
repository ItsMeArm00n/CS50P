import sys

def main():
    global expenses
    expenses=[]
    while True:
        print("Expense Tracker")
        print("1. Add an expense")
        print("2. List all expenses")
        print("3. Show Total expenses")
        print("4. Filter expenses by category")
        print("5. Exit")
        n=input("Enter Your Choice: ")

        if n=="1" or n.lower()=="add an expense"  or n.lower=="1. add an expense":
            category=input("Enter Category: ")
            amt=float(input("Enter Amount in ($): "))
            add_expense(expenses, amt, category)

        elif n=="2" or n.lower()=="list all expenses"  or n.lower=="2. list all expenses":
            print("All Expenses: ")
            print_expense(expenses)

        elif n=="3" or n.lower()=="show total expenses"  or n.lower=="3. show total expenses":
            print(f"Total Expenses ---> ${total_expense(expenses)}")

        elif n=="4" or n.lower()=="filter expenses by category"  or n.lower=="4. filter expenses by category":
            category=input("Enter category: ")
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses(expenses, category)
            print_expense(expenses_from_category)

        elif n=="5" or n.lower()=="exit" or n.lower()=="5. exit":
            sys.exit("Exiting !")

        else :
            print("! Invalid Input !")

def add_expense(expenses, amt, category):
    expenses.append({"Amount":amt, "Category":category})

def print_expense(expenses):
    for expense in expenses:
        print(f"Amount: ${expense['Amount']}, Category: {expense['Category']}")

def total_expense(expenses):
    return sum(expense["Amount"] for expense in expenses)

def filter_expenses(expenses,category):
    return [expense for expense in expenses if expense["Category"] == category]

if __name__ == "__main__":
    main()
