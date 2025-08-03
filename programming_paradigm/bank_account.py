class BankAccount:
    """
    A simple bank account class that demonstrates OOP principles.
    
    This class encapsulates banking operations including deposits,
    withdrawals, and balance display functionality.
    """
    
    def __init__(self, initial_balance=0):
        """
        Initialize a bank account with an optional starting balance.
        
        Args:
            initial_balance (float): Starting balance for the account (default: 0)
        """
        self.account_balance = initial_balance
    
    def deposit(self, amount):
        """
        Add money to the account balance.
        
        Args:
            amount (float): Amount to deposit (must be positive)
        """
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        """
        Withdraw money from the account if sufficient funds are available.
        
        Args:
            amount (float): Amount to withdraw
            
        Returns:
            bool: True if withdrawal successful, False if insufficient funds
        """
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False
    
    def display_balance(self):
        """
        Display the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.account_balance:.2f}")
    
    def get_balance(self):
        """
        Get the current account balance.
        
        Returns:
            float: Current account balance
        """
        return self.account_balance
