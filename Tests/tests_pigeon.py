import unittest

from sorters import Sorters


already_sorted = list(range(10))                  # От 0 до 9
all_the_same = [1] * 10                           # Все 0
reversed_sorted = list(reversed(already_sorted))  # От 9 до 0


class PigeonTests(unittest.TestCase):
    # Сортировка уже отсортированного списка
    def test_already_sorted(self):
        result = Sorters.pigeon(already_sorted.copy())
        self.assertListEqual(result, already_sorted)

    # Сортировка списка, где все значения одинаковые
    def test_all_the_same(self):
        result = Sorters.pigeon(all_the_same.copy())
        self.assertListEqual(result, all_the_same)

    # Сортировка списка от 9 до 0
    def test_reversed_sorted(self):
        result = Sorters.pigeon(reversed_sorted.copy())
        self.assertListEqual(result, already_sorted)


if __name__ == '__main__':
    unittest.main()
