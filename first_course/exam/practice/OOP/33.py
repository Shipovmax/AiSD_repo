'''
Создайте класс ПРОГРАММНОЕ_ОБЕСПЕЧЕНИЕ (информация, проверка возможности использования на текущую дату).
Дочерние классы: СВОБОДНОЕ, УСЛОВНО_БЕСПЛАТНОЕ, КОММЕРЧЕСКОЕ
'''

from datetime import datetime


class Software:
    def __init__(self, name: str, developer: str):
        self.name = name
        self.developer = developer

    def is_usable(self, current_date_str: str) -> bool:
        return True

    def __str__(self):
        return f"ПО: {self.name} | Разработчик: {self.developer}"


class FreeSoftware(Software):
    def __init__(self, name: str, developer: str, license_type: str):
        super().__init__(name, developer)
        self.license_type = license_type

    def __str__(self):
        return f"Свободное ПО: {self.name} | Лицензия: {self.license_type}"


class Shareware(Software):
    def __init__(self, name: str, developer: str, install_date: str, trial_days: int):
        super().__init__(name, developer)
        self.install_date = datetime.strptime(install_date, "%d.%m.%Y")
        self.trial_days = trial_days

    def is_usable(self, current_date_str: str) -> bool:
        current_date = datetime.strptime(current_date_str, "%d.%m.%Y")
        days_passed = (current_date - self.install_date).days
        return 0 <= days_passed <= self.trial_days

    def __str__(self):
        return f"Условно-бесплатное ПО: {self.name} | Установлено: {self.install_date.strftime('%d.%m.%Y')} | Пробный период: {self.trial_days} дней"


class CommercialSoftware(Software):
    def __init__(self, name: str, developer: str, expiration_date: str):
        super().__init__(name, developer)
        self.expiration_date = datetime.strptime(expiration_date, "%d.%m.%Y")

    def is_usable(self, current_date_str: str) -> bool:
        current_date = datetime.strptime(current_date_str, "%d.%m.%Y")
        return current_date <= self.expiration_date

    def __str__(self):
        return f"Коммерческое ПО: {self.name} | Лицензия активна до: {self.expiration_date.strftime('%d.%m.%Y')}"


software_list = [
    FreeSoftware("Linux Ubuntu", "Canonical", "GPL"),
    Shareware("WinRAR", "RARLab", "15.05.2026", 40),
    CommercialSoftware("MS Office 365", "Microsoft", "31.12.2026"),
    Shareware("Photoshop Trial", "Adobe", "01.01.2026", 30),
    CommercialSoftware("Касперский Антивирус", "Лаборатория Касперского", "01.05.2026")
]

today = "08.06.2026"
print(f"=== ПРОВЕРКА ДОСТУПНОСТИ ПО НА ДАТУ {today} ===\n")

for sw in software_list:
    print(sw)
    status = "Доступно для использования" if sw.is_usable(today) else "Срок использования истек / Требуется покупка"
    print(f"Статус: {status}")
    print("-" * 60)
