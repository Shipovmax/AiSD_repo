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
        self.courses = courses or []
        self.prev = None
        self.next = None

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


student = StudentNode("Maxim","Shipov", "253585", "1")