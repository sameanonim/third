import unittest

# код программы

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

# код тестирования
class TestNode(unittest.TestCase):
    def test_init(self):
        node = Node("Test Data")
        self.assertEqual(node.data, "Test Data")
        self.assertIsNone(node.next_node)

class TestStack(unittest.TestCase):
    def test_init(self):
        stack = Stack()
        self.assertIsNone(stack.top)

    def test_push(self):
        stack = Stack()
        stack.push("Data 1")
        self.assertEqual(stack.top.data, "Data 1")
        stack.push("Data 2")
        self.assertEqual(stack.top.data, "Data 2")

if __name__ == '__main__':
    unittest.main()