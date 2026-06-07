class BankAccount:
    def __init__(self,account_number,balance,owner_name,date_opened):
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name
        self.date_opened = date_opened

    def deposit(self, dep_amount):
        self.balance += dep_amount
        print(f"Ksh {dep_amount} deposited into account {self.account_number}.")

    def withdraw(self, withd_amount):
        if withd_amount <= self.balance:
            self.balance -= withd_amount
            print(f"Ksh {withd_amount} withdrawn from account {self.account_number}.")
        else:
            print("Insufficient funds.")

    def check_balance(self):
        print(f"Current balance: Ksh {self.balance}")

    def display_info(self):
        print("Account information:")
        print(f"Account Number: {self.account_number}")
        print(f"Owner Name: {self.owner_name}")
        print(f"Date Opened: {self.date_opened}")
        print(f"Balance: Ksh {self.balance}")
            
    def close_account(self):
        print(f"Account {self.account_number} has been closed.")
        print("________________________________________")

# Object 1:
owner1=BankAccount("B10001",50000,"Sophia Janet","12/05/2014")
print(type(owner1))

deposit_amount = float(input("Enter deposit amount: "))
owner1.deposit(deposit_amount)

withdraw_amount = float(input("Enter withdrawal amount: "))
owner1.withdraw(withdraw_amount)

owner1.check_balance()
owner1.display_info()
owner1.close_account()

# Object 2:
owner2=BankAccount("B10002",135000,"Evaline Kate","09/03/2018")
print(type(owner2))

deposit_amount = float(input("Enter deposit amount: "))
owner2.deposit(deposit_amount)

withdraw_amount = float(input("Enter withdrawal amount: "))
owner2.withdraw(withdraw_amount)

owner2.check_balance()
owner2.display_info()
owner2.close_account()