import time
from datetime import datetime

import input_generator
import log
import util
from input_generator import ArrayOrder

LOGGER = log.get_logger(__name__)


class AlgorithmType:
    BASE = "base"
    SEARCH = "search"
    SORT = "sort"


def recording(function_list, algorithm_type, input_control, *args, **kwargs):
    record = {}
    returned_values = []

    # Recording running times & storing returned values
    for func in function_list:
        start = time.time()
        returned_value = func(*args, **kwargs)
        stop = time.time()
        record[func.__name__] = stop - start
        returned_values.append(returned_value)

    # Check if all returned values are the same
    try:
        util.assert_all_elements_equal(returned_values)
    except AssertionError as e:
        print(e)

    # Record input control note
    if algorithm_type == AlgorithmType.SEARCH:
        record["found"] = input_control
    elif algorithm_type == AlgorithmType.SORT:
        record["input_control"] = input_control

    # Store param lengths and/or values
    for i, param in enumerate(args):
        param_info = util.get_param_info(param)
        record[f"param_{i + 1}_{param_info[0]}"] = param_info[1]
    return record


def measure_sorting_algorithms(function_list, input_lengths, number_of_runs, sorted_input):
    result = []
    start = datetime.now()
    for length in input_lengths:
        for n in range(number_of_runs):
            if n % 3 == 1:
                input_order = ArrayOrder.SORTED
            elif n % 3 == 2:
                input_order = ArrayOrder.REVERSE
            else:
                input_order = ArrayOrder.RANDOM
            input_list = input_generator.generate_numeric_array(length, input_order)
            record = recording(function_list, AlgorithmType.SORT, input_order, input_list)
            result.append(record)
    LOGGER.info(log.get_elapsed_time_log_string(function_list, datetime.now(), start))
    return result


def measure_search_algorithms(function_list, input_lengths, number_of_runs, sorted_input):
    data = []
    start = datetime.now()
    for length in input_lengths:
        LOGGER.info(f"Input length: {length}; starting {number_of_runs} runs")
        for n in range(number_of_runs):
            find_it = n % 2 == 0
            input_array, input_number = input_generator.generate_search_input(length, sorted_input, find_it)
            record = recording(function_list, AlgorithmType.SEARCH, find_it, input_array, input_number)
            data.append(record)
    LOGGER.info(log.get_elapsed_time_log_string(function_list, datetime.now(), start))
    return data


def measure_base_algorithms(function_list, input_lengths, number_of_runs, sorted_input):
    result = []
    input_order = ArrayOrder.SORTED if sorted_input else ArrayOrder.RANDOM
    start = datetime.now()
    for i, length_1 in enumerate(input_lengths):
        for length_2 in input_lengths[i:]:
            LOGGER.info(f"Input 1 length: {length_1}, input 2 length: {length_2}")
            LOGGER.info(f"Starting {number_of_runs} runs")
            for n in range(number_of_runs):
                input_1 = input_generator.generate_numeric_array(length_1, input_order)
                input_2 = input_generator.generate_numeric_array(length_2, input_order)
                record = recording(function_list, AlgorithmType.BASE, None, input_1, input_2)
                result.append(record)
            LOGGER.info(log.get_elapsed_time_log_string(function_list, datetime.now(), start))
    return result
