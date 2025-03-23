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
