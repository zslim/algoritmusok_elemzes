from datetime import datetime


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
    for element in list_of_results:
        if element != first:
            raise AssertionError(f"Unequal values: {first}, {element}")


def concat_function_names(function_list):
    return ", ".join([func.__name__ for func in function_list])


def swap_elements(array, index1, index2):  # In place; lists are passed by reference by default
    array[index1], array[index2] = array[index2], array[index1]
