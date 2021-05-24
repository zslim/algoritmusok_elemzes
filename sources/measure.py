from datetime import datetime
import random
import time

import log
import util

LOGGER = log.get_logger(__name__)


def recording(function, returns_list, *args, **kwargs):
    start = time.time()
    returned_value = function(*args, **kwargs)
    stop = time.time()
    record = {"function": function.__name__, "parameterLengths": [util.get_size(e) for e in args],
              "seconds": stop - start}
    if returns_list:
        record["lengthOfReturned"] = len(returned_value)
    else:
        record["returned"] = returned_value
    return record


def generate_numeric_array(list_length, do_sort):
    array = [random.randint(0, 10000) for _ in range(list_length)]
    if do_sort:
        array.sort()
    return array


def measure_function_one_array(function, input_lengths, number_of_runs, sorted_input, returns_list):
    result = []
    start = datetime.now()
    for length in input_lengths:
        for n in range(number_of_runs):
            input_list = generate_numeric_array(length, sorted_input)
            record = recording(function, returns_list, input_list)
            result.append(record)
    LOGGER.info(f"Ran {function.__name__} for this long: {datetime.now() - start}")
    return result


def measure_function_one_array_one_number(function, input_lengths, number_of_runs, sorted_input, returns_list):
    data = []
    start = datetime.now()
    for length in input_lengths:
        LOGGER.info(f"Input length: {length}; starting {number_of_runs} runs")
        for n in range(number_of_runs):
            input_array = generate_numeric_array(length, sorted_input)
            input_number = random.randint(0, 10000)
            record = recording(function, returns_list, input_array, input_number)
            data.append(record)
    LOGGER.info(f"Ran {function.__name__} for this long: {datetime.now() - start}")
    return data


def measure_function_two_arrays(function, input_lengths, number_of_runs, sorted_input, returns_list):
    result = []
    start = datetime.now()
    for i, length_1 in enumerate(input_lengths):
        for length_2 in input_lengths[i:]:
            LOGGER.info(f"Input 1 length: {length_1}, input 2 length: {length_2}")
            LOGGER.info(f"Starting {number_of_runs} runs")
            for n in range(number_of_runs):
                input_1 = generate_numeric_array(length_1, sorted_input)
                input_2 = generate_numeric_array(length_2, sorted_input)
                record = recording(function, returns_list, input_1, input_2)
                result.append(record)
            LOGGER.info(f"Been running {function.__name__} for this long: {datetime.now() - start}")
    return result


class InputType:
    ONE_ARRAY = "one array"
    ARRAY_AND_NUMBER = "array and number"
    TWO_ARRAYS = "two arrays"
