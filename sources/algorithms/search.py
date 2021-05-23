def linear_unsorted(array, checked):
    search_result = {"found": False, "index": -1}
    for i, element in enumerate(array):
        if element == checked:
            _set_search_result(search_result, i)
            break
    return search_result


def strazsas_unsorted(array, checked):
    search_result = {"found": False, "index": -1}
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
    low = 0
    high = len(array) - 1
    while low < high:
        center = (low + high) // 2
        if checked < array[center]:
            high = center
        elif checked == array[center]:
            _set_search_result(search_result, center)
            break
        else:
            low = center
    return search_result


def _set_search_result(result_dict, index):
    result_dict["found"] = True
    result_dict["index"] = index
