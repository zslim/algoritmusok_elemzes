import random
import time
from datetime import datetime

import log
import util

LOGGER = log.get_logger(__name__)
RANDOM_LOW = 0
RANDOM_HIGH = 100000


class AlgorithmType:
    BASE = "base"
    SEARCH = "search"
    SORT = "sort"


def recording(function_list, algorithm_type, *args, **kwargs):
    record = {}
    returned_values = []

    # Recording running times & storing returned values
    for func in function_list:
        start = time.time()
        returned_values.append(func(*args, **kwargs))
        stop = time.time()
        record[func.__name__] = stop - start

    # If all returned values are the same, record it (or the length)
    util.assert_all_elements_equal(returned_values)
    if algorithm_type == AlgorithmType.SEARCH:
        record["returned"] = returned_values[0]["found"]
    else:
        record["lengthOfReturned"] = len(returned_values[0])

    # Store param lengths and/or values
    for i, param in enumerate(args):
        param_info = util.get_param_info(param)
        record[f"param_{i + 1}_{param_info[0]}"] = param_info[1]
    return record


def generate_numeric_array(list_length, do_sort):
    array = [random.randint(RANDOM_LOW, RANDOM_HIGH) for _ in range(list_length)]
    if do_sort:
        array.sort()
    return array


def measure_sorting_algorithms(function_list, input_lengths, number_of_runs, sorted_input):
    result = []
    start = datetime.now()
    for length in input_lengths:
        for n in range(number_of_runs):
            input_list = generate_numeric_array(length, sorted_input)
            record = recording(function_list, AlgorithmType.SORT, input_list)
            result.append(record)
    LOGGER.info(log.get_elapsed_time_log_string(function_list, datetime.now(), start))
    return result


def measure_search_algorithms(function_list, input_lengths, number_of_runs, sorted_input):
    data = []
    start = datetime.now()
    for length in input_lengths:
        LOGGER.info(f"Input length: {length}; starting {number_of_runs} runs")
        for n in range(number_of_runs):
            input_array = generate_numeric_array(length, sorted_input)
            input_number = random.randint(RANDOM_LOW, RANDOM_HIGH)
            record = recording(function_list, AlgorithmType.SEARCH, input_array, input_number)
            data.append(record)
    LOGGER.info(log.get_elapsed_time_log_string(function_list, datetime.now(), start))
    return data


def measure_base_algorithms(function_list, input_lengths, number_of_runs, sorted_input):
    result = []
    start = datetime.now()
    for i, length_1 in enumerate(input_lengths):
        for length_2 in input_lengths[i:]:
            LOGGER.info(f"Input 1 length: {length_1}, input 2 length: {length_2}")
            LOGGER.info(f"Starting {number_of_runs} runs")
            for n in range(number_of_runs):
                input_1 = generate_numeric_array(length_1, sorted_input)
                input_2 = generate_numeric_array(length_2, sorted_input)
                record = recording(function_list, AlgorithmType.BASE, input_1, input_2)
                result.append(record)
            LOGGER.info(log.get_elapsed_time_log_string(function_list, datetime.now(), start))
    return result
