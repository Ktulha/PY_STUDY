

import math
import random


class Customer:
  """ Customer class """

  def __init__(self, name:str, address:str):
    self.name=name
    self.address=address
    
class BalanceManager:
  def  __init__(self):
    self._balance:float=0
  
  @staticmethod
  def _validate_amount(amount:float):
    if amount<0:
      raise ValueError("Amount must be non-negative")
  
  def  deposit(self, amount:float):
    self._validate_amount(amount)
    self._balance+=amount
  
  def withdraw(self,amount:float):
    self._validate_amount(amount)
    if  amount>self._balance:
      raise  ValueError("Insufficient funds")
    self._balance-=amount
    
  def get_balance(self)->float:
    return self._balance

class Account:
  def __init__(self, customer:Customer, account_number:int,initial_balance:float=0):
    self.customer=customer
    self.account_number=account_number
    self._balance=BalanceManager()
    self._balance.deposit(initial_balance)

  def deposit(self,amount:float):
    try:
      self._balance.deposit(amount)
    except  ValueError as e:
      print(e)

  def  withdraw(self,amount:float):
    try:
      self._balance.withdraw(amount)
    except ValueError as e:
      print(e)
  
  def get_balance(self)->float:
    return self._balance.get_balance()

class AccountNumberGenerator:
  def __init__(self):
    self._used_numbers=set()
    self._salt:int=1000000
  
  def generate(self)->int:
    if len(self._used_numbers)>=self._salt:
      self._salt*=10
    acc_num = math.floor(random.random() * self._salt)
    while acc_num in self._used_numbers:
      acc_num = math.floor(random.random() * self._salt)
    self._used_numbers.add(acc_num)
    return acc_num
  
  def remove_account_number(self, account_number: int):
    #  Remove the account number from the set of used numbers (not in use on this example)
    self._used_numbers.discard(account_number)
  
class Bank:
  def __init__(self):
    self._accounts:dict={}
    self._account_number_generator=AccountNumberGenerator()
    
  def create_account(self, customer:Customer,initial_balance:float=0)->Account:
    BalanceManager._validate_amount(initial_balance)
    # if initial_balance<0:
    #   raise ValueError("Initial balance cannot be negative")
    
    acc_num=self._account_number_generator.generate()
    account=Account(customer,acc_num,initial_balance)
    self._accounts[acc_num]=account
    return account
    
  def get_account(self,account_number:int)->Account:
      if  account_number in self._accounts:
        return self._accounts[account_number]
      raise ValueError("Account not found")

def banking_scenario():
  bank=Bank()
  customer1 = Customer("Alice", "Moscow, Stremyannyi per, 1")
  customer2 = Customer("Bob", "Vorkuta, ul. Lenina, 5")

  # Alice opens an account and deposits some money
  alice_account = bank.create_account(customer1,500.0)
  alice_account.deposit(100.0)
  print(f"Alice's balance: {alice_account.get_balance()}")  # Alice's balance: 600.0  
  
    # Bob opens an account and deposits some money
  bob_account = bank.create_account(customer2,1000.0)
  bob_account.deposit(500.0)
  print(f"Bob's balance: {bob_account.get_balance()}")  # Bob's balance: 1500.0
   
  # Alice withdraws some money from her account
  alice_account.withdraw(300.0)
  print(f"Alice's balance: {alice_account.get_balance()}")  # Alice's balance: 300.0
  
  alice_account.withdraw(500.0)# Insufficient funds
  bob_account.deposit(-500.0) #Amount must be non-negative

  # Bank retrieves Alice's account using the account number
  retrieved_account = bank.get_account(alice_account.account_number)
  print(f"Account {retrieved_account.account_number} by {retrieved_account.customer.name} ({retrieved_account.customer.address}), balance {retrieved_account.get_balance()}") # Account XXXXXX by Alice (Moscow, Stremyannyi per, 1), balance 300.0




banking_scenario()    