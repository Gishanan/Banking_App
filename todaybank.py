import random
import os
from getpass import getpass

accounts = {}

ACCOUNT_FILE= "account.txt"

#load accounts from file
def creates_account():
      if not os.path.exists(ACCOUNT_FILE):
            return
      with open(ACCOUNT_FILE,"r") as f:
            for line in f:
                  parts = line.strip().split(",")
                  if len(parts) >= 6:
                        user_id,acc_no,balance,password,tx_str = parts
                        transactions = tx_str.split("|") if tx_str else[]
                        account[acc_no] = {
                              "user_id" : user_id,
                              "name" : name,
                              "balance" : float(balance),
                              "password" : password,
                              "transactions" : transactions
                        }

# save account to file
def save_account():
      with open(ACCOUNT_FILE, "w") as f:
            for acc_no, acc in accounts.item():
                  tx_str = "|" .join(acc["transactions"])
                  f.write(f"{acc["user_id"]},{acc_no},{acc["name"]},{acc["balance"]},{acc["password"]},{tx_str}\n")

#generats user id
def create_account_id():
      if not os.path.exists(ACCOUNT_FILE) or os.path.getsize(ACCOUNT_FILE) == 0:
            return "g001"
            with open(ACCOUNT_FILE, "r") as f:
                  last_line = f.readlines()[-1:])
                  last_id = int(last_line.split(",")[0][1:])
                  return f"g{last_id + 1:03}"
                  
                        
            
      #Generate account number starts with 77(unique bank code)
def generate_account_number():
      while True:
        random_part = random.randint(1000000, 9999999) 
        account_number = "77" + str(random_part)

        if account_number not in userAccounts:
            return account_number


def create_account():
    name = input("Enter account holder name: ").strip()
    while not account_holder_name:
        print("Name cannot be empty.")
        name = input("Enter account holder name: ").strip()

    while True:
      try:
            balace = float(input("enter initial balance:"))
            if balance < 0:
                  print("balance must be non-negative.")
                  continue
            break
      except ValueError:
            print("please enter a valid number.")
   while True:
         password = getpass("set a pasword:")
         confirm = getpass("confirm password:")
         if password == confirm:
               break
         else:
               print("password do not match.")
               



  
def deposit_money():
    #Deposits money into an existing account.
    account_number = input("Enter account number: ")
    if account_number not in userAccounts:
        print("Account not found.")
        return

    while True:
        try:
            deposit_amount_str = input("Enter deposit amount: ")
            deposit_amount = float(deposit_amount_str)
            if deposit_amount > 0:
                break
            else:
                print("Deposit amount must be positive.")
        except ValueError:
            print("Invalid input. Please enter a valid number for the deposit amount.")

    name, balance, transactions = userAccounts[account_number]
    new_balance = balance + deposit_amount
    updated_transactions = transactions + [f"Deposit: +{deposit_amount}"]
    userAccounts[account_number] = (name, new_balance, updated_transactions)
    print("Deposit successful.")
    print(f"New balance: {new_balance}")

def withdraw_money():
    #Withdraw money
    account_number = input("Enter account number: ")
    if account_number not in userAccounts:
        print("Account not found.")
        return

    while True:
        try:
            withdrawal_amount_str = input("Enter withdrawal amount: ")
            withdrawal_amount = float(withdrawal_amount_str)
            if withdrawal_amount > 0:
                break
            else:
                print("Withdrawal amount must be positive.")
        except ValueError:
            print("Invalid input. Please enter a valid number for the withdrawal amount.")

    name, balance, transactions = userAccounts[account_number]
    if withdrawal_amount > balance:
        print("Insufficient balance.")
        return

    new_balance = balance - withdrawal_amount
    updated_transactions = transactions + [f"Withdrawal: -{withdrawal_amount}"]
    userAccounts[account_number] = (name, new_balance, updated_transactions)
    print("Withdrawal successful.")
    print(f"New balance: {new_balance}")

def check_balance():
    #Check the current balance
    account_number = input("Enter account number: ")
    if account_number not in userAccounts:
        print("Account not found.")
        return

    name, balance, _ = userAccounts[account_number]
    print(f"Account Holder: {name}")
    print(f"Current Balance: Rs.{balance}")

def view_transaction_history():
    #transaction history
    account_number = input("Enter account number: ")
    if account_number not in userAccounts:
        print("Account not found.")
        return

    name, _, transactions = userAccounts[account_number]
    print(f"Transaction History for Account: {account_number} ({name})")
    if not transactions:
        print("No transactions yet.")
    else:
        for transaction in transactions:
            print(f"-- {transaction}")

def main():
    #Main function
    while True:
        print("\nMini Banking Application")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_account()
        elif choice == '2':
            deposit_money()
        elif choice == '3':
            withdraw_money()
        elif choice == '4':
            check_balance()
        elif choice == '5':
            view_transaction_history()
        elif choice == '6':
            print("Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


