'''
Реализация базового класса StackList: 

Используя принципы ООП из Блока 1, создай 
собственный класс стека на основе стандартного 
списка Python. 

Тебе нужно реализовать методы: 

push(item) (добавление),
pop() (удаление с возвратом),
peek() (возврат верхнего элемента без удаления) 
is_empty() (проверка на пустоту).
'''

class StackList:
    def __init__(self):
        self._items = []

    def push(self, item):
        """Добавляет элемент в конец (на вершину стека)."""
        self._items.append(item)
    
    def pop(self):
        """Удаляет и возвращает верхний элемент. Обрабатывает пустой стек."""
        if self.is_empty():
            return None
        return self._items.pop()

    def peek(self):
        """Возвращает верхний элемент без удаления."""
        if self.is_empty():
            return None
        return self._items[-1]

    def is_empty(self):
        """Возвращает True, если стек пуст."""
        return len(self._items) == 0