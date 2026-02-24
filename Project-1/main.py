# Expense Tracker Project

Expenses = []  #empty expenses dictionary
print("Welcome to Expense Tracker!!!")
while True:
    print("====MENU====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")
    c = int(input("Enter your choice[1 to 4]:"))
    if c == 1:
        name = input("Enter expense name:")
        de = input("Enter expense description:")
        cat = input("Enter expense category:")
        amt = float(input("Enter expense amount:"))
        exp ={
            'Name' : name,
            'Description' : de,
            'Category' : cat,
            'Amount' : amt
        }
        Expenses.append(exp)
        print("Expense added successfully!!!")
    elif c == 4:
        break
    elif c == 3:
        total = 0
        for exp in Expenses:
            total += exp['Amount']
        print("Total Expense:",total)
    elif c == 2:
        print("\n====Expenses====")
        for exp in Expenses:
            print("Name:",exp['Name'])
            print("Description:",exp['Description'])
            print("Category:",exp['Category'])
            print("Amount:",exp['Amount'])
            print("-------------------------")
    else:
        print("Invalid choice!!!")