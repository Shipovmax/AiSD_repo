'''
Создайте двусвязный список для хранения и
управления информацией о студентах в университете.

Каждый элемент списка должен содержать имя, фамилию, номер
студенческого билета и список курсов, на которые студент записан.
'''

class StudentNode:
    __slots__ = ('first_name', 'last_name', 'student_id', 'courses', 'prev', 'next')

    def __init__(self, first_name, last_name, student_id, courses=None):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.courses = courses if courses is not None else []
        self.prev = None
        self.next = None

    def __repr__(self):
        return (f"Student({self.first_name} {self.last_name}, id={self.student_id}, "
                f"courses={self.courses})")


class StudentDLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, node):
        if not self.head:
            self.head = self.tail = node
            return
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def find(self, student_id):
        curr = self.head
        while curr:
            if curr.student_id == student_id:
                return curr
            curr = curr.next
        return None

    def delete(self, student_id):
        node = self.find(student_id)
        if not node:
            return False

        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        node.prev = node.next = None
        return True

    def display(self):
        if not self.head:
            print("Список студентов пуст.")
            return
        curr = self.head
        while curr:
            print(curr)
            curr = curr.next

    def display_reverse(self):
        if not self.tail:
            print("Список студентов пуст.")
            return
        curr = self.tail
        while curr:
            print(curr)
            curr = curr.prev



students_list = StudentDLL()

s1 = StudentNode("Maxim", "Shipov", "253585", ["Математика", "Физика"])
s2 = StudentNode("Anna", "Ivanova", "123456", ["Программирование", "Английский"])
s3 = StudentNode("Igor", "Petrov", "987654", ["История", "Химия"])

students_list.append(s1)
students_list.append(s2)
students_list.append(s3)

print("-" * 100)
print("")

students_list.display()

print("")
print("-" * 100)
print("")

students_list.display_reverse()

print("")
print("-" * 100)
print("")

found = students_list.find("123456")
print(found if found else "Не найден")

print("")
print("-" * 100)
print("")

students_list.delete("987654")
students_list.display()

print("")
print("-" * 100)
print("")