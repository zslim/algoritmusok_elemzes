import random

RANDOM_LOW = 0
RANDOM_HIGH = 100000


class ArrayOrder:
    SORTED = "sorted"
    REVERSE = "reverse"
    RANDOM = "random"


def generate_numeric_array(list_length, array_order):
    array = [random.randint(RANDOM_LOW, RANDOM_HIGH) for _ in range(list_length)]
    if array_order == ArrayOrder.SORTED:
        array.sort()
    elif array_order == ArrayOrder.REVERSE:
        array.sort(reverse=True)
    return array


def generate_search_input(length, sorted_input, contains: bool):
    array_order = ArrayOrder.SORTED if sorted_input else ArrayOrder.RANDOM
    array = generate_numeric_array(length, array_order)
    if contains:
        index = random.randint(0, length - 1)
        number = array[index]
    else:
        number = random.randint(RANDOM_LOW, RANDOM_HIGH)
    return array, number
