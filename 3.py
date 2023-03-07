class Node:
    """ Это узел """
    def __init__(self, data, next_node=None):
        self.data = data  # тут данные
        self.next_node = next_node # тут ссылка на следующий

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        """ Тут добавление элемента """
        new_node = Node(data)
        new_node.next_node = self.top
        self.top = new_node

    def pop(self):
        """ Тут удаление элемента """
        if self.top is None:
            return None
        else:
            data = self.top.data
            self.top = self.top.next_node
            return data