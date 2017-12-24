import unittest
from main import select_sort

class MainTest(unittest.TestCase):
    def test_unordered_list(self):
        result = select_sort([1,5,3,4,1])
        self.assertEqual([1,1,3,4,5], result)

    def test_empty_list(self):
        result = select_sort([])
        self.assertEqual([], result)

    def test_short_list(self):
        result = select_sort([10,1])
        self.assertEqual([1,10], result)
        