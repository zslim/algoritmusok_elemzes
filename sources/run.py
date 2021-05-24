import os

import data_handler
import log
import measure
import util
from measure import InputType
from sources.algorithms import base, search


LOGGER = log.get_logger(__name__)


def repeat(function, input_type: InputType, sorted_input, returns_list):
    input_low = 1000
    input_high = 10000
    increment = 1000

    input_lengths = range(input_low, input_high + 1, increment)
    number_of_runs = 100

    measurer = None

    if input_type == InputType.ONE_ARRAY:
        measurer = measure.measure_function_one_array
    elif input_type == InputType.ARRAY_AND_NUMBER:
        measurer = measure.measure_function_one_array_one_number
    elif input_type == InputType.TWO_ARRAYS:
        measurer = measure.measure_function_two_arrays

    LOGGER.info(f"======= Running <{function.__name__}> =======")
    result = measurer(function, input_lengths, number_of_runs, sorted_input, returns_list)

    return result


def generate_and_write(function, input_type: InputType, sorted_input=False, returns_list=False):
    out_folder = os.path.join("out", "out_data")
    os.makedirs(out_folder, exist_ok=True)
    file_name = util.create_file_name(function)
    out_path = os.path.join(out_folder, file_name)
    data = repeat(function, input_type, sorted_input, returns_list)
    data_handler.write_data(data, out_path)
    LOGGER.info(f"Wrote file: {out_path}")


def main():
    # Base algorithms
    # generate_and_write(base.intersection, InputType.TWO_ARRAYS, returns_list=True)
    # generate_and_write(base.union, InputType.TWO_ARRAYS, returns_list=True)
    generate_and_write(base.merge_sorted, InputType.TWO_ARRAYS, sorted_input=True, returns_list=True)

    # Search algorithms
    generate_and_write(search.linear_unsorted, InputType.ARRAY_AND_NUMBER)
    generate_and_write(search.strazsas_unsorted, InputType.ARRAY_AND_NUMBER)
    generate_and_write(search.linear_sorted, InputType.ARRAY_AND_NUMBER, sorted_input=True)
    generate_and_write(search.binary_sorted, InputType.ARRAY_AND_NUMBER, sorted_input=True)
    generate_and_write(search.jump_sorted, InputType.ARRAY_AND_NUMBER, sorted_input=True)


if __name__ == '__main__':
    main()
