import math
import random

class BankAccount:

    # Constructor to initialize account details
    def __init__ (self, holder, account_number, balance=0):
        self.holder = holder
        self.account_number = account_number
        self.__balance = balance  # Private attribute

    def __str__ (self):
        return f"Account Holder: {self.holder}, Account Number: {self.account_number}, Balance: ${self.__balance:.2f}"
    
    def deposit (self, amount):
        #minimum deposit amount of $20
        if amount < 20:
            print("Deposit amount must be at least $20.00")
            return 0
        
        else:
            self.__balance += amount
            print(f"Deposited ${amount:.2f}. New balance is ${self.__balance:.2f}")
            return 1
        

    def withdraw (self, amount):

        if amount > self.__balance:
            print(f"Insufficient funds. Current balance is ${self.__balance:.2f}")
            return 0 
        
        else: 
            self.__balance -= amount
            return f"Withdrew ${amount:.2f}. New balance is ${self.__balance:.2f}"
        

#Create Account
input_holder = input("To open an account, please enter your name: ")
account_number = random.randint(100000, 999999)
account1 = BankAccount(input_holder, account_number)
print(f"Account created successfully! Your account number is {account_number}")

choice = input("Would you like to deposit or withdraw? (d/w):").lower()

if choice == "d":
    amount = float(input("Enter amount to deposit: "))
    success = account1.deposit(amount)

    while success == 0:
        amount = float(input("Enter amount to deposit: "))
        success = account1.deposit(amount)

    
elif choice == "w":
    amount = float(input("Enter amount to withdraw: "))
    success = account1.withdraw(amount)

    if success == 0:
        amount = float(input("Enter amount to withdraw: "))
        account1.withdraw(amount)



        
        
