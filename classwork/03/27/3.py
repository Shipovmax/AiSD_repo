'''
Шипов Максим Кириллович 

Вариант 2
Задание 3

Создать класс Деньги для работы с денежными суммами.
Число должно быть представлено списком, состоящим из
рублей и копеек. Работу с рублями и копейками организовать
как с закрытыми атрибутами. Реализовать сложение, вычитание,
умножение сумм, деление денежных сумм, используя магические методы.

'''

class Money:
    def __init__(self, rubles: int = 0, kopecks: int = 0):
        self.__rubles = rubles
        self.__kopecks = kopecks
        self.__normalize()

    def __normalize(self):
        '''Закрытая функция '''
        self.__rubles += self.__kopecks // 100
        self.__kopecks = self.__kopecks % 100

    def __add__(self, other):
        '''Магический метод сложения'''
        return Money(self.__rubles + other.__rubles, self.__kopecks + other.__kopecks)

    def __sub__(self, other):
        '''Магический метод вычитания'''
        total_kopecks = (self.__rubles * 100 + self.__kopecks) - (other.__rubles * 100 + other.__kopecks)
        return Money(0, total_kopecks)

    def __mul__(self, factor):
        '''Магический метод'''
        total_kopecks = int((self.__rubles * 100 + self.__kopecks) * factor)
        return Money(0, total_kopecks)

    def __truediv__(self, divisor):
        '''Магический метод деления'''
        total_kopecks = int((self.__rubles * 100 + self.__kopecks) / divisor)
        return Money(0, total_kopecks)

    def __eq__(self, other):
        '''Магический метод сравнения'''
        return self.__rubles == other.__rubles and self.__kopecks == other.__kopecks

    def __lt__(self, other):
        '''Магический метод сравнения <'''
        return (self.__rubles * 100 + self.__kopecks) < (other.__rubles * 100 + other.__kopecks)

    def __le__(self, other):
        '''Магический метод сравнения <='''
        return (self.__rubles * 100 + self.__kopecks) <= (other.__rubles * 100 + other.__kopecks)

    def __str__(self):
        '''Магический метод вывода'''
        return f"{self.__rubles} руб. {self.__kopecks:02d} коп."

    def __repr__(self):
        '''Магический метод вывода в терминал'''
        return f"Money({self.__rubles}, {self.__kopecks})"

    def get_rubles(self):
        return self.__rubles

    def get_kopecks(self):
        return self.__kopecks

    def to_list(self):
        return [self.__rubles, self.__kopecks]


if __name__ == "__main__":
    m1 = Money(100, 50)
    m2 = Money(50, 75)

    print(f"m1 = {m1}")
    print(f"m2 = {m2}")

    print(f"\nm1 + m2 = {m1 + m2}")
    print(f"m1 - m2 = {m1 - m2}")
    print(f"m1 * 2 = {m1 * 2}")
    print(f"m1 / 2 = {m1 / 2}")

    print(f"\nm1 == m2: {m1 == m2}")
    print(f"m1 < m2: {m1 < m2}")

    print(f"\nm1 в виде списка: {m1.to_list()}")
