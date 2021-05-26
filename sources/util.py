from datetime import datetime

import log

LOGGER = log.get_logger(__name__)


def create_file_name(name):
    now = datetime.now()
    timestamp = f"{now.year}{now.month:02}{now.day:02}_{now.hour:02}{now.minute:02}{now.second:02}"
    file_name = f"{name}_{timestamp}.csv"
    return file_name


def get_param_info(param):
    if isinstance(param, list):
        return "length", len(param)
    else:
        return "value", param


def parse_search_result(dict_string):
    content = dict_string[1:-1]
    cut = [d.split(":") for d in content.split(",")]
    result = {"found": cut[0][1] == " True", "index": int(cut[1][1])}
    return result


def assert_all_elements_equal(list_of_results):
    first = list_of_results[0]
    # printed_results = "\n".join([str(result) for result in list_of_results])
    for element in list_of_results:
        comparisons = [a == b for a, b in zip(first, element)]
        if not all(comparisons):
            if list_of_results[-1] != "recursion error":
                fails = [numbers for numbers, match in zip(zip(first, element), comparisons) if not match]
                LOGGER.info(f"Fails: {fails}")
            raise AssertionError(f"Unequal values:\n{first}\n{element}")


def swap_elements(array, index1, index2):  # In place; lists are passed by reference by default
    array[index1], array[index2] = array[index2], array[index1]
