class BankAccount:
    def __init__(self, account_number: int, balance: (int, float), date_of_opening: str, customer_name: str):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount: (int, float)):
        self.balance += amount

    def withdraw(self, amount: (int, float)):
        if amount < self.balance:
            self.balance -= amount
        else:
            print("Niewystarczająca ilość pieniędzy na koncie\n")

    def check_balance(self):
        return self.balance


account_1 = BankAccount(1753, 2784.1, "24.03.2017", "Jan Kowalski")
account_2 = BankAccount(1354, 1984.78, "28.09.2023", "Grzegorz Nowak")

print(account_1.check_balance())
account_1.deposit(800)

print(account_2.check_balance())
account_2.withdraw(2000)
