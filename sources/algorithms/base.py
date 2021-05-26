import sort


def _does_include(array, element):
    i = 0
    while i < len(array) and element != array[i]:
        i += 1
    return i < len(array)


def intersection(array1, array2):
    result = []
    for element in array1:
        if _does_include(array2, element):
            result.append(element)
    return result


def union(array1: list, array2: list):
    result = array1[:]
    for element in array2:
        if not _does_include(array1, element):
            result.append(element)
    return result


def merge_sorted(array1, array2):
    result = []
    n = len(array1)
    m = len(array2)
    i = 0
    j = 0
    while i < n and j < m:
        a_current = array1[i]
        b_current = array2[j]
        if a_current < b_current:
            result.append(a_current)
            i += 1
        elif a_current == b_current:
            result.append(a_current)
            i += 1
            j += 1
        else:
            result.append(b_current)
            j += 1
    if i >= n:
        result += array2[j:]
    else:
        result += array1[i:]
    return result


def merge_unsorted(array1, array2):
    sort.quicksort(array1)
    sort.quicksort(array2)
    return merge_sorted(array1, array2)
