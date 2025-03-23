incomes = [
{"amount": 1000, "description": "Salary"},
{"amount": 200, "description": "Freelance work"}
]

expenses = [
{"amount": 500, "description": "Rent"},
{"amount": 100, "description": "Utilities"}
]


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