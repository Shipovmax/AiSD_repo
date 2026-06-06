"""
Создай класс BankAccount.

В методе __init__ инициализируй
приватный атрибут __balance (баланс), равный нулю.

Добавь два публичных метода:
deposit(amount) для пополнения счета (сумма должна быть больше нуля)
и
get_balance(), который просто возвращает текущий баланс.

Изменить баланс напрямую извне класса должно быть невозможно.
"""


class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return print(f"\n--- Ваш депозит в {amount} зачислен")
        else:
            return print(f"\n-- Ваша сумма {amount} меньше нуля")

    def get_balance(self):
        return print(f"\n--- Ваш баланс {self.__balance}\n")


maksim = BankAccount()
maksim.deposit(100)
maksim.get_balance()
