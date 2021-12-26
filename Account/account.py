import datetime
import pytz


class Account:

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance, currency):
        self._name = name
        self.__balance = balance
        self._currency = currency
        self._transaction_list = [(self._current_time(), balance)]

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self._transaction_list.append((self._current_time(), amount))
        else:
            print("Invalid amount for deposit")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            self._transaction_list.append((self._current_time(), -amount))
        else:
            print("Invalid amount for withdrawal")

    def show_balance(self):
        print(f"Balance: {self.__balance} {self._currency}")

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount >= 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print(f"{amount} {tran_type} on {date} (local time was {date.astimezone()})")

    def __str__(self):
        return f"Name: {self._name}\nBalance: {self.__balance} {self._currency}"


acc = Account("Oleksii", 800, "$")
acc.__balance = 200
acc.deposit(100)
acc.withdraw(200)
acc.show_transactions()
acc.show_balance()
print(acc.__dict__)