def linear_unsorted(array, checked):
    search_result = {"found": False, "index": -1}
    for i, element in enumerate(array):
        if element == checked:
            search_result["found"] = True
            search_result["index"] = i
            break
    return search_result
