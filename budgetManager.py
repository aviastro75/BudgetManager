incomes = []

expenses = []


balance = sum(item["amount"] for item in incomes) - sum(item["amount"] for item in
expenses)

def addIncome():
    amount = int(input("Enter new income: "))
    description = input("Enter new income description: ")

    # Append the new income to the incomes list
    incomes.append({"amount": amount, "description": description})

    # Print the updated incomes list
    print(incomes)


def addExpense():
    amount = int(input("Enter new expense: "))
    description = input("Enter new expense description: ")

    expenses.append({"amount": amount, "description": description})

    print(expenses)


def showBalance():
    balance = sum(item["amount"] for item in incomes) - sum(item["amount"] for item in expenses)
    print(f"Your balance: ${balance}")
    

def showTranHistory():

    print("Income history\n")

    for item in range(len(incomes)):

        print(incomes[item]["description"]+" "+ str(incomes[item]["amount"]))

    print("\n")

    print("Expenses history\n")
    for item in range(len(expenses)):

        print(expenses[item]["description"]+" "+ str(expenses[item]["amount"]))
