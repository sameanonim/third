import unittest
from third import Node, Stack
from custom_queue import Queue
from linked_list import LinkedList

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
    def setUp(self):
        self.queue = Queue()
    
    def test_enqueue(self):
        self.queue.enqueue(1)
        self.assertEqual(self.queue.head.data, 1)
        self.assertEqual(self.queue.tail.data, 1)
        self.assertEqual(self.queue.size, 1)
        
        self.queue.enqueue(2)
        self.assertEqual(self.queue.head.data, 1)
        self.assertEqual(self.queue.tail.data, 2)
        self.assertEqual(self.queue.size, 2)
        
        self.queue.enqueue(3)
        self.assertEqual(self.queue.head.data, 1)
        self.assertEqual(self.queue.tail.data, 3)
        self.assertEqual(self.queue.size, 3)
        
    def test_dequeue(self):
        self.assertIsNone(self.queue.dequeue())
        
        self.queue.enqueue(1)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertIsNone(self.queue.head)
        self.assertIsNone(self.queue.tail)
        self.assertEqual(self.queue.size, 0)
        
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.head.data, 2)
        self.assertEqual(self.queue.tail.data, 2)
        self.assertEqual(self.queue.size, 1)
        
        self.queue.enqueue(3)
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.head.data, 3)
        self.assertEqual(self.queue.tail.data, 3)
        self.assertEqual(self.queue.size, 1)

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()

    def test_insert_beginning(self):
        self.ll.insert_beginning(1)
        self.assertEqual(self.ll.head.data, 1)
        self.assertEqual(self.ll.tail.data, 1)

        self.ll.insert_beginning(2)
        self.assertEqual(self.ll.head.data, 2)
        self.assertEqual(self.ll.tail.data, 1)

        self.ll.insert_beginning(3)
        self.assertEqual(self.ll.head.data, 3)
        self.assertEqual(self.ll.tail.data, 1)

    def test_insert_at_end(self):
        self.ll.insert_at_end(1)
        self.assertEqual(self.ll.head.data, 1)
        self.assertEqual(self.ll.tail.data, 1)

        self.ll.insert_at_end(2)
        self.assertEqual(self.ll.head.data, 1)
        self.assertEqual(self.ll.tail.data, 2)

        self.ll.insert_at_end(3)
        self.assertEqual(self.ll.head.data, 1)
        self.assertEqual(self.ll.tail.data, 3)

    def test_print_ll(self):
        self.ll.insert_beginning(1)
        self.ll.insert_beginning(2)
        self.ll.insert_beginning(3)

if __name__ == "__main__":
    unittest.main()