import math

import util


def insertion_sort(array):
    out = []
    for element in array:
        if len(out) == 0:
            out.append(element)
        else:
            i = 0
            while i <= len(out) - 1 and element > out[i]:
                i += 1
            out.insert(i, element)
    return out


def bubble_sort(array):
    out = array[:]
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if out[j] > out[j + 1]:
                util.swap_elements(out, j, j + 1)
    return out


def selection_sort(array):
    out = array[:]
    for i in range(len(out)):
        index_of_minimal_element = i
        for j in range(i + 1, len(out)):
            if out[j] < out[index_of_minimal_element]:
                index_of_minimal_element = j
        util.swap_elements(out, i, index_of_minimal_element)
    return out


def comb_sort(array):
    shrink = 1.3
    out = array[:]
    gap = len(out)
    is_sorted = False

    while not is_sorted:  # More than one iteration may be needed with gap = 1
        gap = math.floor(gap / shrink)
        if gap <= 1:
            gap = 1
            is_sorted = True
        for i in range(len(out) - gap):
            if out[i] > out[i + gap]:
                util.swap_elements(out, i, i + gap)
                is_sorted = False
    return out


def enhanced_cocktail_sort(array):
    out = array[:]
    low = 0
    high = len(out) - 1

    while low < high:
        swapped = False
        for i in range(low, high):
            if out[i] > out[i + 1]:
                util.swap_elements(out, i, i + 1)
                swapped = True

        if not swapped:
            break

        swapped = False
        high -= 1

        for i in range(high, low, -1):
            if out[i] < out[i - 1]:
                util.swap_elements(out, i, i - 1)
                swapped = True

        if not swapped:
            break
        low += 1

    return out


def quicksort_partition(array, low, high):
    # array[high] will be our pivot value
    pivot_position = low
    for i in range(low, high):
        if array[i] <= array[high]:
            util.swap_elements(array, i, pivot_position)
            pivot_position += 1
    util.swap_elements(array, pivot_position, high)
    return pivot_position


def quicksort_in_place(array, low=0, high=-1):
    if high == -1:
        high = len(array) - 1
    if low < high:
        pivot_index = quicksort_partition(array, low, high)
        quicksort_in_place(array, low, pivot_index - 1)
        quicksort_in_place(array, pivot_index + 1, high)


def quicksort(array):
    if array == []:
        return array
    out = array[:]
    pivot = out[0]
    lesser = quicksort([e for e in out[1:] if e < pivot])
    greater = quicksort([e for e in out[1:] if e >= pivot])
    return lesser + [pivot] + greater
