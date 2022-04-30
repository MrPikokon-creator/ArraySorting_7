import unittest

from sorters import Sorters


already_sorted = list(range(10))                  # От 0 до 9
all_the_same = [1] * 10                           # Все 1
reversed_sorted = list(reversed(already_sorted))  # От 9 до 0


class BucketTests(unittest.TestCase):
    # Сортировка уже отсортированного списка
    def test_already_sorted(self):
        result = Sorters.bucket(already_sorted.copy())
        self.assertListEqual(result, already_sorted)

    # Сортировка списка, где все значения одинаковые
    def test_all_the_same(self):
        result = Sorters.bucket(all_the_same.copy())
        self.assertListEqual(result, all_the_same)

    # Сортировка списка от 9 до 0
    def test_reversed_sorted(self):
        result = Sorters.bucket(reversed_sorted.copy())
        self.assertListEqual(result, already_sorted)


if __name__ == '__main__':
    unittest.main()
