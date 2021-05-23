from datetime import datetime
import random
import time

import log

LOGGER = log.get_logger(__name__)


def recording(function, returns_list, *args, **kwargs):
    start = time.time()
    returned_value = function(*args, **kwargs)
    stop = time.time()
    record = {"function": function.__name__, "parameter lengths": [len(e) for e in args],
              "seconds": stop - start, "length of returned": len(returned_value)}
    if returns_list:
        record["length of returned"] = len(returned_value)
    else:
        record["returned"] = returned_value
    return record


def generate_numeric_input(list_length, do_sort):
    array = [random.randint(0, 10000) for _ in range(list_length)]
    if do_sort:
        array.sort()
    return array


def measure_single_arg_function(function, input_lengths, number_of_runs, sorted_input, returns_list):
    result = []
    for length in input_lengths:
        for n in range(number_of_runs):
            input_list = generate_numeric_input(length, sorted_input)
            record = recording(function, returns_list, input_list)
            result.append(record)
    return result


def measure_double_arg_function(function, input_lengths, number_of_runs, sorted_input, returns_list):
    result = []
    start = datetime.now()
    for i, length_1 in enumerate(input_lengths):
        LOGGER.info(f"Running <{function.__name__}>")
        for length_2 in input_lengths[i:]:
            LOGGER.info(f"input 1 length: {length_1}, input 2 length: {length_2}")
            LOGGER.info(f"Starting {number_of_runs} runs")
            for n in range(number_of_runs):
                input_1 = generate_numeric_input(length_1, sorted_input)
                input_2 = generate_numeric_input(length_2, sorted_input)
                record = recording(function, returns_list, input_1, input_2)
                result.append(record)
            LOGGER.info(f"Elapsed time: {datetime.now() - start}")
    return result
