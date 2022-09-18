"""
Домашнее задание №1
Функции и структуры данных
"""

def power_numbers(*nums):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    """
    return [i ** 2 for i in nums]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(n):
    """
    функция, которая на вход принимает целое число,
    и возвращает его, только если оно является простым
    """
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return None
        else:
            return n
    else:
        return None


def filter_numbers(lst, type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)
    """
    if type == "even":
        return list(filter(lambda x: x % 2 == 0, lst))
    elif type == "odd":
        return list(filter(lambda x: x % 2 != 0, lst))
    elif type == "prime":
        return list(filter(is_prime, lst))

print(filter_numbers([2, 3, 4, 5, 17, 15], ODD))
print(filter_numbers([2, 3, 4, 5, 17, 15], EVEN))
print(filter_numbers([2, 3, 4, 5, 17, 15], PRIME))

