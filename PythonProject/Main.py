class Account:
    acc_no = 0
    name = ''
    deposit=0
    type = ''

def create_account(self):
    self.acc_no= int(input("\tEnter the account no : "))
    self.name = input("\tEnter the account holder name : ")
    self.type = input("\tEnte the type of account [C/S] : ")
    self.deposit = int(input("\tEnter The Initial amount :"))
    print("\n\tAccount Created")

def show_account(self):
    print("\tAccount Number : ",self.acc_no)
    print("\tAccount Holder Name : ", self.name)
    print("\tType of Account",self.type)
    print("\tBalance : ",self.deposit)

def modify_account(self):
    print("\tAccount Number : ",self.acc_no)
    self.name = input("\tModify Account Holder Name :")
    self.type = input("\tModify type of Account :")
    self.deposit = int(input("\tModify Balance :"))
    
def deposit_amount(self,amount):
    self.deposit += amount

def withdraw_amount(self,amount):
    self.deposit -= amount

# def report(self):
#     print(self.accNo, " ",self.name ," ",self.type," ", self.deposit)

def getAccountNo(self):
    return self.acc_no
def getAcccountHolderName(self):
    return self.name
def getAccountType(self):
    return self.type
def getDeposit(self):
    return self.deposit