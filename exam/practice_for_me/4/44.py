"""
Реализуйте функцию вставки нового узла в однонаправленный связный список.

Функция должна поддерживать два режима работы:

вставка после узла с заданным порядковым номером (индексом)
или
вставка после узла с определенным целевым значением.
"""


class Node:
    def __init__(self, value, link=None):
        self.value = value
        self.link = link


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        """Добавление в начало списка"""
        new_node = Node(value, link=self.head)
        self.head = new_node

    def insert_after(self, new_value, target_index=None, target_value=None):
        """
        Вставляет новый узел со значением new_value ПОСЛЕ определенного узла.
        Можно передать либо target_index (индексация с 0), либо target_value.
        """
        if self.head is None:
            print("Список пуст! Вставка невозможна.")
            return False

        current = self.head

        if target_index is not None:
            current_index = 0
            while current is not None and current_index < target_index:
                current = current.link
                current_index += 1

        elif target_value is not None:
            while current is not None and current.value != target_value:
                current = current.link

        else:
            print("Ошибка: укажите target_index или target_value.")
            return False

        if current is None:
            print("Целевой узел не найден в списке.")
            return False

        new_node = Node(new_value)
        new_node.link = current.link
        current.link = new_node
        return True

    def display(self):
        """Вспомогательный метод для вывода списка в консоль"""
        current = self.head
        elements = []
        while current is not None:
            elements.append(str(current.value))
            current = current.link
        print(" -> ".join(elements) + " -> None")
