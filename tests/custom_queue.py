class Node:
    """ Это узел """
    def __init__(self, data, next_node=None):
        self.data = data  # тут данные
        self.next_node = next_node # тут ссылка на следующий

class Queue:
    """ Это список """
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def enqueue(self, data):
        """ Добавление в конец списка """
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        """ Удаление из списка """
        if self.is_empty():
            raise Exception("Список пуст")
        data = self.head.data