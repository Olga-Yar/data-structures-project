"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Stack, Node


class TestStack(unittest.TestCase):
    def test_push(self):
        stack = Stack()
        self.assertEqual(None, stack.top)
        n1 = Node(5, None)
        self.assertEqual(5, n1.data)
        self.assertEqual(None, n1.next_node)

    def test_pop(self):
        stack = Stack()
        stack.push('data1')
        data = stack.pop().data
        self.assertEqual(stack.top, None)
        self.assertEqual(data, 'data1')


