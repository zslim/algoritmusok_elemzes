import math


def linear_unsorted(array, checked):
    search_result = {"found": False, "index": -1}
    for i, element in enumerate(array):
        if element == checked:
            _set_search_result(search_result, i)
            break
    return search_result


def strazsas_unsorted(array_param, checked):
    search_result = {"found": False, "index": -1}
    array = array_param[:]
    array.append(checked)
    i = 0
    while array[i] != checked:
        i += 1
    if i < len(array) - 1:  # need the length of the original array here
        _set_search_result(search_result, i)
    return search_result


def linear_sorted(array, checked):
    search_result = {"found": False, "index": -1}
    for i, element in enumerate(array):
        if element == checked:
            _set_search_result(search_result, i)
            break
        if element > checked:
            break
    return search_result


def binary_sorted(array, checked):
    search_result = {"found": False, "index": -1}
    if checked < array[0] or checked > array[-1]:
        return search_result
    low = 0
    high = len(array) - 1
    while low <= high:
        center = (low + high) // 2
        if checked < array[center]:
            high = center - 1
        elif checked == array[center]:
            _set_search_result(search_result, center)
            break
        else:
            low = center + 1
    return search_result


def jump_sorted(array, checked):
    search_result = {"found": False, "index": -1}
    if checked < array[0] or checked > array[-1]:
        return search_result

    n = len(array)
    block_length = math.floor(math.sqrt(n))
    low = 0
    high = block_length

    while array[min(n, high) - 1] < checked:
        low = high
        high = low + block_length
        if low >= n:
            return search_result

    block = array[low:high]
    for i, element in enumerate(block):
        if element == checked:
            _set_search_result(search_result, i + low)
            break
        if element > checked:
            break
    return search_result


def _set_search_result(result_dict, index):
    result_dict["found"] = True
    result_dict["index"] = index
