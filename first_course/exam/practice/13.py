'''
Создайте класс Банк (название, список счетов).
Счет представлен классом Счет (номер, баланс).

Реализуйте методы добавления/удаления счетов и вычисления общего баланса.
Используйте __len__ для количества счетов
'''


class Account:
    def __init__(self, number: int, balance: int):
        self.number = number
        self.balance = balance

    def __str__(self):
        return f"Счет №{self.number} (Баланс: {self.balance} руб.)"


class Bank:
    def __init__(self, name: str):
        self.name = name
        self.accounts = []

    def add_account(self, account: Account):
        self.accounts.append(account)

    def remove_account(self, number: int):
        for account in self.accounts:
            if account.number == number:
                self.accounts.remove(account)
                return True
        return False

    def get_total_balance(self):
        total = 0
        for account in self.accounts:
            total += account.balance
        return total

    def __len__(self):
        return len(self.accounts)

    def __str__(self):
        info = f"Банк: {self.name}\nСписок счетов:\n"
        if not self.accounts:
            info += "Нет открытых счетов"
        for account in self.accounts:
            info += f"- {account}\n"
        return info


bank = Bank("Сбер")

acc1 = Account(1001, 50000)
acc2 = Account(1002, 150000)
acc3 = Account(1003, 3500)

bank.add_account(acc1)
bank.add_account(acc2)
bank.add_account(acc3)

print(bank)
print(f"Количество счетов в банке: {len(bank)}")
print(f"Общий баланс всех счетов: {bank.get_total_balance()} руб.\n")

bank.remove_account(1003)

print("=== ПОСЛЕ УДАЛЕНИЯ СЧЕТА ===")
print(bank)
print(f"Количество счетов в банке: {len(bank)}")
print(f"Общий баланс всех счетов: {bank.get_total_balance()} руб.")
