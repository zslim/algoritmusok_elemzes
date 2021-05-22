import random
import time
import log

LOGGER = log.get_logger(__name__)


def recording(function, *args, **kwargs):
    start = time.time()
    returned_value = function(*args, **kwargs)
    stop = time.time()
    record = {"function": function.__name__, "parameter lengths": [len(e) for e in args],
              "seconds": stop - start, "length of returned": len(returned_value)}
    return record


def generate_numeric_input(list_length):
    return [random.randint(0, 10000) for _ in range(list_length)]


def measure_single_arg_function(function, input_lengths, number_of_runs):
    result = []
    for length in input_lengths:
        input_list = generate_numeric_input(length)
        for n in range(number_of_runs):
            record = recording(function, input_list)
            result.append(record)
    return result


def measure_double_arg_function(function, input_lengths, number_of_runs):
    result = []
    for i, length_1 in enumerate(input_lengths):
        input_1 = generate_numeric_input(length_1)
        for length_2 in input_lengths[i:]:
            input_2 = generate_numeric_input(length_2)
            LOGGER.info(f"input 1 length: {length_1}, input 2 length: {length_2}")
            LOGGER.info(f"Starting {number_of_runs} runs")
            for n in range(number_of_runs):
                record = recording(function, input_1, input_2)
                result.append(record)
    return result
