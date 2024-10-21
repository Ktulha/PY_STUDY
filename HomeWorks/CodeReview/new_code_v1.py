import math
import random

class Customer:
    """
    Represents a customer with a name and address.

    Attributes:
        name (str): The name of the customer.
        address (str): The address of the customer.
    """

    def __init__(self, name, address):
        """
        Initializes a new Customer instance.

        Args:
            name (str): The name of the customer.
            address (str): The address of the customer.
        """
        self.name = name
        self.address = address

    def __repr__(self) -> str:
        """
        Returns:
            str: A string representation of the Customer.
        """
        return f"{self.name} ({self.address})"


class Account:
    """
    Represents a bank account for a customer.

    Attributes:
        customer (Customer): The customer who owns the account.
        account_number (int): The unique account number.
        _balance (float): The current balance of the account.
    """

    _balance: float = 0

    def __init__(self, customer: Customer, account_number: int):
        """
        Initializes a new Account instance.

        Args:
            customer (Customer): The customer who owns the account.
            account_number (int): The unique account number.
        """
        self.customer = customer
        self.account_number = account_number

    def deposit(self, amount: float):
        """
        Deposits a specified amount into the account.

        Args:
            amount (float): The amount to deposit.

        Raises:
            ValueError: If the deposit amount is negative.
        """
        if amount >= 0:
            self._balance += amount
        else:
            print("Deposit amount must be non-negative")

    def withdraw(self, amount: float):
        """
        Withdraws a specified amount from the account.

        Args:
            amount (float): The amount to withdraw.

        Raises:
            ValueError: If the withdrawal amount is negative or exceeds the current balance.
        """
        if amount < 0:
            print("Withdrawal amount must be non-negative")
        elif amount > self._balance:
            print("Insufficient funds")
        else:
            self._balance -= amount

    def get_balance(self):
        """
        Returns the current balance of the account.

        Returns:
            float: The current balance of the account.
        """
        return self._balance

    def __repr__(self) -> str:
        """
        Returns:
            str: A string representation of the Account.
        """
        return f"Account {self.account_number} by {self.customer}"


class Bank:
    """
    Represents a bank that manages customer accounts.

    Attributes:
        _accounts (dict): A dictionary of accounts indexed by account number.
    """

    def __init__(self):
        """
        Initializes a new Bank instance with an empty account dictionary.
        """
        self._accounts = {}

    def _get_account_number(self) -> int:
        """
        Generates a unique account number that is not already in use.

        Returns:
            int: A unique account number.
        """
        acc_num = math.floor(random.random() * 1000000)
        while acc_num in self._accounts:
            acc_num = math.floor(random.random() * 1000000)
        return acc_num

    def create_account(self, customer: Customer, initial_balance: float = 0) -> Account:
        """
        Creates a new account for a customer with an optional initial balance.

        Args:
            customer (Customer): The customer for whom to create the account.
            initial_balance (float): The initial balance to deposit into the account.

        Returns:
            Account: The newly created Account instance.
        """
        acc_num = self._get_account_number()
        account = Account(customer, acc_num)
        account.deposit(initial_balance)
        self._accounts[acc_num] = account
        return account

    def get_account(self, account_number: int)->Account:
        """
        Retrieves the account associated with the given account number.

        Args:
            account_number (int): The account number to look up.

        Returns:
            Account: The Account instance associated with the account number.

        Raises:
            ValueError: If the account number is not found.
        """
        if account_number in self._accounts:
            return self._accounts[account_number]
        raise ValueError("Account not found")

    def get_account_info(self, account_number: int) -> str:
        """
        Retrieves the information of the account associated with the given account number.

        Args:
            account_number (int): The account number to look up.

        Returns:
            str: A string containing the account information and balance.
        """
        account = self.get_account(account_number)
        return f"{account}, balance {account.get_balance()}"

# Example
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
  
  print(bank.get_account_info(alice_account.account_number)) # Account XXXXXX by Alice (Moscow, Stremyannyi per, 1), balance 300.0




banking_scenario()   

