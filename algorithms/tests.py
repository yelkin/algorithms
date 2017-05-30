import random
from unittest import TestCase

from . import sort


class TestSort(TestCase):
    def bench(self, sort_func):
        for _ in range(10):
            data = [random.randint(-100, 100) for _ in range(random.randint(0, 10))]
            self.assertEqual(sort_func(data), sorted(data))

    def test_insertion_sort(self):
        self.bench(sort.insertion_sort)

    def test_bubble_sort(self):
        self.bench(sort.bubble_sort)

    def test_quick_sort(self):
        self.bench(sort.quick_sort)

    def test_merge_sort(self):
        self.bench(sort.merge_sort)