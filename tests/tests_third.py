import unittest
from third import Node, Stack
from custom_queue import Queue

# код тестирования
class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.stack.push(1)
        self.assertEqual(self.stack.top.data, 1)

    def test_pop_empty_stack(self):
        self.assertEqual(self.stack.pop(), None)

    def test_pop_non_empty_stack(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.top.data, 1)

    def test_pop_until_empty(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.pop()
        self.stack.pop()
        self.assertEqual(self.stack.pop(), None)

class TestQueue(unittest.TestCase):
    def test_enqueue(self):
        queue = Queue()
        queue.enqueue(1)
        self.assertEqual(queue.head.data, 1)
        self.assertEqual(queue.tail.data, 1)
        queue.enqueue(2)
        self.assertEqual(queue.tail.data, 2)

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        with self.assertRaises(Exception):
            queue.dequeue()

if __name__ == "__main__":
    unittest.main()