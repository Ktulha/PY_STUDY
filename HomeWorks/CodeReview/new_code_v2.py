import math
import random

class Customer:
    """
    Represents a customer with a name and address.

    Attributes:
        name (str): The name of the customer.
        address (str): The address of the customer.
    """
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address

class BalanceManager:
    """
    Manages the balance of an account, allowing deposits and withdrawals.

    Attributes:
        _balance (float): The current balance of the account.
    """
    def __init__(self):
        self._balance: float = 0

    @staticmethod
    def _validate_amount(amount: float):
        """
        Validates that the given amount is non-negative.

        Args:
            amount (float): The amount to validate.

        Raises:
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount must be non-negative")

    def deposit(self, amount: float):
        """
        Deposits a specified amount into the account.

        Args:
            amount (float): The amount to deposit.

        Raises:
            ValueError: If the amount is negative.
        """
        self._validate_amount(amount)
        self._balance += amount

    def withdraw(self, amount: float):
        """
        Withdraws a specified amount from the account.

        Args:
            amount (float): The amount to withdraw.

        Raises:
            ValueError: If the amount is negative or exceeds the current balance.
        """
        self._validate_amount(amount)
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    def get_balance(self) -> float:
        """
        Returns the current balance of the account.

        Returns:
            float: The current balance.
        """
        return self._balance

class Account:
    """
    Represents a bank account belonging to a customer.

    Attributes:
        customer (Customer): The customer who owns the account.
        account_number (int): The unique account number.
        _balance (BalanceManager): The balance manager for the account.
    """
    def __init__(self, customer: Customer, account_number: int, initial_balance: float = 0):
        self.customer = customer
        self.account_number = account_number
        self._balance = BalanceManager()
        self._balance.deposit(initial_balance)

    def deposit(self, amount: float):
        """
        Deposits a specified amount into the account.

        Args:
            amount (float): The amount to deposit.
        """
        try:
            self._balance.deposit(amount)
        except ValueError as e:
            print(e)

    def withdraw(self, amount: float):
        """
        Withdraws a specified amount from the account.

        Args:
            amount (float): The amount to withdraw.
        """
        try:
            self._balance.withdraw(amount)
        except ValueError as e:
            print(e)

    def get_balance(self) -> float:
        """
        Returns the current balance of the account.

        Returns:
            float: The current balance.
        """
        return self._balance.get_balance()

class AccountNumberGenerator:
    """
    Generates unique account numbers for bank accounts.

    Attributes:
        _used_numbers (set): A set of account numbers that have already been used.
        _salt (int): A multiplier for generating account numbers.
    """
    def __init__(self):
        self._used_numbers = set()
        self._salt: int = 1000000

    def generate(self) -> int:
        """
        Generates a unique account number.

        Returns:
            int: A unique account number.
        """
        if len(self._used_numbers) >= self._salt:
            self._salt *= 10
        acc_num = math.floor(random.random() * self._salt)
        while acc_num in self._used_numbers:
            acc_num = math.floor(random.random() * self._salt)
        self._used_numbers.add(acc_num)
        return acc_num

    def remove_account_number(self, account_number: int):
        """
        Removes an account number from the set of used numbers.

        Args:
            account_number (int): The account number to remove.
        """
        self._used_numbers.discard(account_number)

class Bank:
    """
    Represents a bank that manages customer accounts.

    Attributes:
        _accounts (dict): A dictionary of accounts indexed by account number.
        _account_number_generator (AccountNumberGenerator): An instance for generating unique account numbers.
    """
    def __init__(self):
        self._accounts: dict = {}
        self._account_number_generator = AccountNumberGenerator()

    def create_account(self, customer: Customer, initial_balance: float = 0 ) -> int:
        """
        Creates a new account for a customer.

        Args:
            customer (Customer): The customer who owns the account.
            initial_balance (float, optional): The initial balance of the account. Defaults to 0.

        Returns:
            int: The unique account number of the new account.
        """
        account_number = self._account_number_generator.generate()
        self._accounts[account_number] = Account(customer, account_number, initial_balance)
        return account_number

    def get_account(self, account_number: int) -> Account:
        """
        Retrieves an account by its account number.

        Args:
            account_number (int): The account number of the account to retrieve.

        Returns:
            Account: The account associated with the given account number.
        """
        return self._accounts.get(account_number)

    def close_account(self, account_number: int):
        """
        Closes an account and removes it from the bank's records.

        Args:
            account_number (int): The account number of the account to close.
        """
        if account_number in self._accounts:
            self._account_number_generator.remove_account_number(account_number)
            del self._accounts[account_number]

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