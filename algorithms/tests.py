import random
from unittest import TestCase
from . import sort


class TestSort(TestCase):
    def test_sort(self):
        for _ in range(10):
            data = [random.randint(-100, 100) for _ in range(random.randint(0, 10))]
            self.assertEqual(sort.bubble_sort(data), sorted(data))