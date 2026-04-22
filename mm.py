#create a class bank acc
#rivateno
#balance
#owner name
class Bankaccount:
    def __init__(self, account_number, owner_name, balance):
        self.__account_number = account_number
        self.__owner_name = owner_name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited successfully")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount > self.__balance:
            print("Transaction failed, insufficient balance")
        else:
            self.__balance -= amount
            print(f"{amount} withdrawn successfully")

    def display_details(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Owner Name: {self.__owner_name}")
        print(f"Balance: {self.__balance}")



account = Bankaccount(10101, "Mr. Singh", 1000)


account.display_details()
account.deposit(500)
account.withdraw(200)
account.display_details()
