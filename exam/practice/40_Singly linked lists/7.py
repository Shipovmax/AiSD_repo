"""
Реализуйте функцию подсчета суммы всех элементов, кратных 3.
"""


class Node:
    def __init__(self, value):
        self.value = value  # Хранит данные узла
        self.next = None  # Ссылка на следующий узел (по умолчанию пустая)


class LinkedList:
    def __init__(self):
        self.head = None  # Инициализация пустого списка (голова указывает на None)

    def append(self, value):
        """Добавление нового элемента в конец списка"""
        new_node = Node(value)

        # Если список пуст, делаем новый узел головой списка
        if not self.head:
            self.head = new_node
            return

        # Иначе доходим до последнего узла (у которого next равен None)
        current = self.head
        while current.next:
            current = current.next

        # Привязываем новый узел к следующему за последним
        current.next = new_node

    def prepend(self, value):
        """Добавление нового элемента в начало списка (в голову)"""
        new_node = Node(value)

        # Направляем указатель нового узла на текущую голову
        new_node.next = self.head

        # Делаем новый узел новой головой списка
        self.head = new_node

    def delete(self, value):
        """Удаление первого узла с указанным значением"""
        # Если список пуст, удалять нечего
        if not self.head:
            return

        # Если нужно удалить саму голову, просто перенаправляем head на следующий узел
        if self.head.value == value:
            self.head = self.head.next
            return

        # Ищем узел, КОТОРЫЙ СТОИТ ПЕРЕД удаляемым узлом
        current = self.head
        while current.next and current.next.value != value:
            current = current.next

        # Если нашли нужный узел, меняем его указатель, "перешагивая" через удаляемый элемент
        if current.next:
            current.next = current.next.next

    def find(self, value):
        """Поиск узла по его значению"""
        current = self.head

        # Перебираем все узлы по очереди
        while current:
            if current.value == value:
                return current  # Возвращаем найденный узел
            current = current.next

        return None  # Если ничего не нашли, возвращаем None

    def display(self):
        """Вывод всех элементов списка в удобочитаемом виде"""
        elements = []
        current = self.head

        # Собираем значения всех узлов в список
        while current:
            elements.append(str(current.value))
            current = current.next

        # Красиво соединяем стрелочками для визуализации связи
        print(" -> ".join(elements) + " -> None")

    def sum_multiples_of_three(self):
        """Подсчет суммы всех элементов, кратных 3"""
        total_sum = 0
        current = self.head

        # Обходим список с начала до конца
        while current:
            # Проверяем делимость на 3 без остатка
            if current.value % 3 == 0:
                total_sum += current.value
            current = current.next

        return total_sum
