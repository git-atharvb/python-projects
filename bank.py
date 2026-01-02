import os
from time import sleep
class Bank:
    def __init__(self):

        self.users = {}
        self.last_transaction = {}
        self.type={}

    def create_user(self):
        name = input("\tEnter user name: ")
        initial_balance = float(input("\tEnter initial balance: "))
        account_number = input("\tEnter account number: ")
        self.users[account_number] = {
            'name': name,
            'balance': initial_balance
        }
        print("\tUser created successfully.")
        sleep(5)
        os.system('cls')

    def withdraw(self):
        account_number = input("\tEnter account number: ")
        if account_number in self.users:
            amount = float(input("\tEnter amount to withdraw: "))
            if amount <= self.users[account_number]['balance']:
                self.users[account_number]['balance'] -= amount
                self.last_transaction[account_number] = f"Withdrawn {amount}"
                print("\tAmount withdrawn successfully.")
            else:
                print("\tInsufficient balance.")
        else:
            print("\tAccount number not found.")
        sleep(5)
        os.system('cls')

    def deposit(self):
        account_number = input("\tEnter account number: ")
        if account_number in self.users:
            amount = float(input("\tEnter amount to deposit: "))
            self.users[account_number]['balance'] += amount
            self.last_transaction[account_number] = f"Deposited {amount}"
            print("\tAmount deposited successfully.")
        else:
            print("\tAccount number not found.")
        sleep(5)
        os.system('cls')

    def last_transaction_info(self):
        account_number = input("Enter account number: ")
        if account_number in self.last_transaction:
            print("\tLast transaction:", self.last_transaction[account_number])
        else:
            print("\tNo transaction found for the account number.")
        sleep(5)
        os.system('cls')

    def user_information(self):
        account_number = input("\tEnter account number: ")
        if account_number in self.users:
            user = self.users[account_number]
            print("\tName:", user['name'])
            print("\tBalance:", user['balance'])
        else:
            print("\tAccount number not found.")
        sleep(5)
        os.system('cls')

    def menu(self):
        while True:
            print("\t---***---***---***---***---")
            print("\t    Static Bank System")
            print("\t---------------------------")
            print("\t(1) Create User")
            print("\t(2) Withdraw")
            print("\t(3) Deposit")
            print("\t(4) Last Transaction")
            print("\t(5) User Information")
            print("\t(6) Exit")
            print("\t---***---***---***---***---")

            #accept choice from user to perform particular task
            choice = input("\tEnter your choice (1-6): ")
            if choice == '1':
                self.create_user()
            elif choice == '2':
                self.withdraw()
            elif choice == '3':
                self.deposit()
            elif choice == '4':
                self.last_transaction_info()
            elif choice == '5':
                self.user_information()
            elif choice == '6':
                print("\tExiting the system... Wait for few seconds...")
                break
            else:
                print("\t---Incorrect Task Option (Enter between 1 to 6)---")
        sleep(5)
        os.system('cls')


#calling the menu function to start the program
bank = Bank()
bank.menu()