"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Node, Queue


class TestQueue(unittest.TestCase):
    def test_dequeue(self):
        queue = Queue()
        queue.enqueue('data1')
        data = queue.dequeue()
        self.assertEqual(data, 'data1')
