incomes = []

expenses = []


balance = sum(item["amount"] for item in incomes) - sum(item["amount"] for item in
expenses)

def addIncome():

    incomes = []

    expenses = []


    balance = sum(item["amount"] for item in incomes) - sum(item["amount"] for item in
    expenses)



    amount = int(input("Enter new income: "))
    description = input("Enter new income description: ")

    incomes.append({"amount": amount, "description": description})

    print(incomes)