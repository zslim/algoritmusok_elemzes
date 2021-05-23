def _does_include(array, element):
    i = 0
    while i < len(array) and element != array[i]:
        i += 1
    return i < len(array)


def intersection(a, b):
    result = []
    for a_element in a:
        if _does_include(b, a_element):
            result.append(a_element)
    return result


def union(a: list, b: list):
    result = a[:]
    for b_element in b:
        if not _does_include(a, b_element):
            result.append(b_element)
    return result


def merge_sorted(a, b):
    result = []
    n = len(a)
    m = len(b)
    i = 0
    j = 0
    while i < n and j < m:
        a_current = a[i]
        b_current = b[j]
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
        result += b[j:]
    else:
        result += a[i:]
    return result
