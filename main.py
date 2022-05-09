import random
import time

from sorters import Sorters


array_lengths = (100, 1_000, 2_500, 5_000, 10_000)  # Длины генерируемых списков | 100 - холостой прогон


def main():
    for length in array_lengths:
        print(f'- - - {length:_d} элементов - - -')
        array = [random.randint(0, length) for i in range(length)]  # Заполнение случайными числами от 0 до длины списка

        print('Шелла:\t\t\t', end='')
        Sorters.shell(array.copy())

        print('Голубиная:\t\t', end='')
        Sorters.pigeon(array.copy())

        print('Поразрядная:\t', end='')
        Sorters.radix(array.copy())

        print('Блочная:\t\t', end='')
        Sorters.bucket(array.copy())

        print()


if __name__ == '__main__':
    main()
