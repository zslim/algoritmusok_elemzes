import math


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
                temp = out[j]
                out[j] = out[j + 1]
                out[j + 1] = temp
    return out


def selection_sort(array):
    out = array[:]
    for i in range(len(out)):
        index_of_minimal_element = i
        for j in range(i + 1, len(out)):
            if out[j] < out[index_of_minimal_element]:
                index_of_minimal_element = j
        temp = out[index_of_minimal_element]
        out[index_of_minimal_element] = out[i]
        out[i] = temp
    return out


def comb_sort(array):
    shrink = 1.3
    out = array[:]
    gap = len(out)

    while gap > 1:
        gap = math.floor(gap / shrink)
        if gap <= 1:
            gap = 1
        for i in range(len(out) - gap):
            if out[i] > out[i + gap]:
                out[i], out[i + gap] = out[i + gap], out[i]
    return out


def enhanced_cocktail_sort(array):
    out = array[:]
    low = 0
    high = len(out) - 1

    while low < high:
        swapped = False
        for i in range(low, high):
            if out[i] > out[i + 1]:
                out[i], out[i + 1] = out[i + 1], out[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        high -= 1

        for i in range(high, low, -1):
            if out[i] < out[i - 1]:
                out[i - 1], out[i] = out[i], out[i - 1]
                swapped = True

        if not swapped:
            break
        low += 1

    return out
