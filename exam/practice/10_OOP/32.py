'''
Создайте класс КЛИЕНТ (информация, поиск по критерию).
Дочерние классы: ВКЛАДЧИК, КРЕДИТОР, ОРГАНИЗАЦИЯ.
Организуйте поиск по дате сотрудничества.
'''

from datetime import datetime


class Client:
    def __init__(self, name: str, start_date: str):
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d.%m.%Y")

    def match_date(self, target_date_str: str) -> bool:
        target_date = datetime.strptime(target_date_str, "%d.%m.%Y")
        return self.start_date == target_date

    def __str__(self):
        return f"Клиент: {self.name} | Дата сотрудничества: {self.start_date.strftime('%d.%m.%Y')}"


class Depositor(Client):
    def __init__(self, name: str, start_date: str, deposit_amount: float, interest_rate: float):
        super().__init__(name, start_date)
        self.deposit_amount = deposit_amount
        self.interest_rate = interest_rate

    def __str__(self):
        return f"Вкладчик: {self.name} | Дата договора: {self.start_date.strftime('%d.%m.%Y')} | Депозит: {self.deposit_amount} руб. под {self.interest_rate}%"


class Creditor(Client):
    def __init__(self, name: str, start_date: str, loan_amount: float, monthly_payment: float):
        super().__init__(name, start_date)
        self.loan_amount = loan_amount
        self.monthly_payment = monthly_payment

    def __str__(self):
        return f"Кредитор: {self.name} | Дата выдачи: {self.start_date.strftime('%d.%m.%Y')} | Кредит: {self.loan_amount} руб. | Платеж: {self.monthly_payment} руб./мес."


class Organization(Client):
    def __init__(self, name: str, start_date: str, inn: str, account_type: str):
        super().__init__(name, start_date)
        self.inn = inn
        self.account_type = account_type

    def __str__(self):
        return f"Организация: '{self.name}' | Дата открытия: {self.start_date.strftime('%d.%m.%Y')} | ИНН: {self.inn} | Счет: {self.account_type}"


def search_by_date(client_list: list[Client], date_str: str) -> list[Client]:
    return [client for client in client_list if client.match_date(date_str)]


database = [
    Depositor("Иван Петров", "12.04.2023", 500000.0, 14.5),
    Creditor("Елена Сидорова", "15.08.2024", 1200000.0, 35000.0),
    Organization("ООО ТехноРешения", "12.04.2023", "7701234567", "Расчетный"),
    Depositor("Алексей Смирнов", "01.06.2025", 100000.0, 16.0),
    Organization("АО МеталлПром", "10.11.2022", "7809876543", "Корпоративный")
]

print("=== ВСЕ КЛИЕНТЫ БАНКА ===")
for client in database:
    print(client)

print("\n" + "=" * 70 + "\n")

search_date = "12.04.2023"
print(f"=== ПОИСК КЛИЕНТОВ ПО ДАТЕ СОТРУДНИЧЕСТВА ({search_date}) ===")
results = search_by_date(database, search_date)

if results:
    for client in results:
        print(client)
else:
    print("Клиенты с такой датой не найдены")
