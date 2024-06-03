
class Account:
    def __init__(self,number,pin ):
        self.number=number
        self.__pin=pin
        self.__balance=0
    def check_balance(self,pin):
        if pin==self.__pin:
            return self.__balance
        else:
            return "Wrong pin"
    def __init__(self, number, pin, owner=None):
        self.number = number
        self.__pin = pin
        self.owner = owner if owner else "Unknown"
        self.__balance = 0
        self.overdraft_limit = 0 
        self.is_frozen = False
        self.minimum_balance = 0  
        self.transactions: list[float] = []
        self.history: list[str] = []  
    def check_balance(self, pin):
        if pin == self.__pin:
            return self.__balance
        else:
            return "Wrong pin"
    def deposit(self, amount: float) -> None:
        self.__balance += amount
        self.transactions.append(f"Deposit: {amount}")
        self.history.append(f"Deposit: {amount}")
    def withdraw(self, amount: float) -> bool:
        if amount > (self.__balance + self.overdraft_limit):
            return False
        self.__balance -= amount
        self.transactions.append(f"Withdrawal: {-amount}")
        self.history.append(f"Withdrawal: {-amount}")
        return True
    def get_balance(self) -> float:
        return self.__balance
    def get_transactions(self) -> list[str]:
        return self.transactions
    def get_history(self) -> list[str]:
        return self.history
    def change_owner(self, new_owner):
        self.owner = new_owner
    def generate_statement(self):
        statement = f"Account Number: {self.number}\nOwner: {self.owner}\nBalance: {self.__balance}\nTransactions:\n{self.get_transactions()}"
        return statement
    def set_overdraft_limit(self, limit):
        self.overdraft_limit = limit
    def calculate_interest(self, rate):
        interest = self.__balance * rate / 100
        self.__balance += interest
        self.transactions.append(f"Interest Earned: {interest:.2f}")
        self.history.append(f"Interest Earned: {interest:.2f}")
    def freeze_account(self):
        self.is_frozen = True
    def unfreeze_account(self):
        self.is_frozen = False
    def set_minimum_balance(self, min_balance):
        self.minimum_balance = min_balance
    def transfer_funds(self, target_account, amount):
        if not self.withdraw(amount):
            return False
        if target_account.withdraw(amount):  # Assuming target_account has enough balance
            self.transactions.append(f"Transfer to {target_account.number}: {amount}")
            target_account.transactions.append(f"Received from {self.number}: {amount}")
            return True
        return False
    def close_account(self):
        self.__balance = 0
        self.transactions.append("Account Closed")
        self.history.append("Account Closed")

account = Account(12345667, 7898, "Haiba")
account.deposit(43567)
print(account.check_balance(7898))
result = account.withdraw(50.0)
print(result)
print(account.get_balance())
result = account.withdraw(234.0)
print(result)
print(account.get_transactions())

account.change_owner("Nairat")
print(account.generate_statement())
account.set_overdraft_limit(500)
account.calculate_interest(5)
account.freeze_account()
print(account.is_frozen)

account.set_minimum_balance(100)
account.transfer_funds(Account(87654321, 4321), 200)
print(account.get_transactions())
account.close_account()
print(account.get_balance())










