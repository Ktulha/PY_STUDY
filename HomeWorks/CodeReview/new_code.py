import math
import random

class Customer:
  def __init__(self, name, address):
    self.name = name
    self.address = address

  def __repr__(self) -> str:
    return f"{self.name} ({self.address})"

class Account:
  _balance:float=0
  def __init__(self, customer:Customer,account_number:int):
    self.customer = customer
    self.account_number = account_number

  def deposit(self, amount:float):
    self._balance += amount
  
  def withdraw(self,amount:float):
    if amount > self._balance:
      raise ValueError("Insufficient funds")  
    self._balance -= amount

  def get_balance(self):
    return self._balance

  def __repr__(self) -> str:
    return  f"Account {self.account_number} by {self.customer}"

class Bank:
  def  __init__(self):
    self._accounts={}

  def _get_account_number(self)->int:
    acc_num=math.floor(random.random() * 1000000)
    while  acc_num in self._accounts:
      #  if the account number is already in use, generate a new one
      acc_num=math.floor(random.random() * 1000000)
    return acc_num
  
  def create_account(self,customer:Customer,innitial_balance:float=0)->Account:
    # create a new account for the customer
    acc_num=self._get_account_number()
    account=Account(customer,acc_num)
    account.deposit(innitial_balance)
    self._accounts[acc_num] = account
    return account
    
  def get_account(self,account_number:int):
    #  return the account with the given account number
    if account_number  in self._accounts:
      return self._accounts[account_number]
    raise  ValueError("Account not found")

bank=Bank()
test=Customer('John Doe','NY,1453-233, 13 av')
print(test)
# acc_test=Account(test)
# print (acc_test) 
b_test=bank.create_account(test,500)
print (b_test,b_test.get_balance()) 
b_test.deposit(1200)
t=bank.get_account(b_test.account_number)
print(f"{t}, balance {t.get_balance()}")
try:
  b_test.withdraw(1750)
except ValueError as e:
  print(e)
    


  
  