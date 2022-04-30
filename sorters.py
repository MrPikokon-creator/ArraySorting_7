import math
import time


# Декоратор, засекающий время сортировки
def stopwatch(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result_array = func(*args, **kwargs)
        end_time = time.time()
        time_result = int((end_time - start_time) * 1_000_000)
        print(time_result)
        return result_array

    return wrapper


class Sorters:
    # Шелла
    @staticmethod
    @stopwatch
    def shell(array: list) -> list:
        n = len(array)
        k = int(math.log2(n))
        interval = 2 ** k - 1

        while interval > 0:
            for i in range(interval, n):
                temp = array[i]
                j = i
                while j >= interval and array[j - interval] > temp:
                    array[j] = array[j - interval]
                    j -= interval
                array[j] = temp
            k -= 1
            interval = 2 ** k - 1

        return array

    # Голубиная
    @staticmethod
    @stopwatch
    def pigeon(array: list) -> list:
        mi = min(array)
        size = max(array) - mi + 1
        holes = [0] * size

        for x in array:
            holes[x - mi] += 1

        i = 0
        for count in range(size):
            while holes[count] > 0:
                holes[count] -= 1
                array[i] = count + mi
                i += 1

        return array

    # Поразрядная
    @staticmethod
    @stopwatch
    def radix(array: list) -> list:
        radix = 10
        max_length = False
        tmp, placement = -1, 1

        while not max_length:
            max_length = True
            buckets = [list() for _ in range(radix)]
            for i in array:
                tmp = i // placement
                buckets[tmp % radix].append(i)
                if max_length and tmp > 0:
                    max_length = False

            a = 0
            for b in range(radix):
                buck = buckets[b]
                for i in buck:
                    array[a] = i
                    a += 1

            placement *= radix

        return array

    # Блочная
    @staticmethod
    @stopwatch
    def bucket(array: list) -> list:
        largest = max(array)
        length = len(array)
        size = largest / length

        buckets = [[] for _ in range(length)]

        for i in range(length):
            index = int(array[i] / size)
            if index != length:
                buckets[index].append(array[i])
            else:
                buckets[length - 1].append(array[i])

        for i in range(len(array)):
            buckets[i] = sorted(buckets[i])

        result = []
        for i in range(length):
            result = result + buckets[i]

        return result
