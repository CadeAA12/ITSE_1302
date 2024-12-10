import locale

locale.setlocale(locale.LC_ALL, "us")

def main():
    
    print("Welcome to the budget tracker app!")
    print("===================================")

    while True:
        try:
            income = float(input("Enter your monthly income: "))
            income = round(income, 2)
            if income < 0:
                raise ValueError("Income must be greater than 0. Please try again")
            else:
                break
        except ValueError as e:
            print(f"There was a value error. Please enter a number. Error was: {e}")

    expense_list = []
    
    while True:
        try:
            expenses = float(input("Enter your expenses. Press 0 to finish: "))
            expenses = round(expenses, 2)
            if expenses < 0:
                raise ValueError("Expenses must be greater than 0. Please try again")
            elif expenses == 0:
                break
            else:
                expense_list.append(expenses)
        except ValueError as e:
            print(f"There was a value error. Please enter a number. Error was: {e}")

    total_expense = sum(expense_list)
    budget = income - total_expense

    print("Budget information")
    print("===================================")
    print(f"Total income: ${locale.currency(income, grouping=True)}")
    print(f"Total expenses: ${locale.currency(total_expense, grouping=True)}")
    print(f"Remaining budget: ${locale.currency(budget, grouping=True)}")

    print("===================================")
    print("Individual Expenses")
    print("===================================")
    for i, expense in enumerate(expense_list, 1):
        print(f"Expense {i}: {locale.currency(expense, grouping=True)}")


        
if __name__ == "__main__":
    main()