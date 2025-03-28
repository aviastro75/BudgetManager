import budgetManager

incomes = []

expenses = []

balance = sum(item["amount"] for item in incomes) - sum(item["amount"] for item in
expenses)

while True:

  print("Welcome to Budget Manager v1.0\n")

  print("1. add new income")
  print("2. add new expense")
  print("3. show balance")
  print("4. show transaction history")
  print("5. exit")


  userChoise = input("Enter your chiose: ")

  match userChoise:

    case "1":
        
        transactions.addIncome()


    case "2":

        transactions.addExpense()

    case "3":

        transactions.showBalance()

    case "4":
      
        transactions.showTranHistory()

    case "5":

        break

    case _:
            print("Invalid option, return to main menu\n")
            continue

