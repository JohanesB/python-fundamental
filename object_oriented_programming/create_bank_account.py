class Account():
    def __init__(self, owner, balance) -> None:
        self.owner = owner
        self.balance = balance

    def __str__(self) -> str:
        return (f"Account owner: {self.owner} \nAccount balance: {self.balance}")
    
    def deposit(self, depo):
            self.balance += depo
            print("Deposit Successfully")

    def withdrow(self, withdraw):
        if withdraw < self.balance:
            self.balance -= withdraw
        else:
             print("Insufficient amount to withdraw")

acct1 = Account(owner="Jose", balance=5000)
print(acct1.balance)
