import os

from sources.algorithms import base_algorithms
import data_handler
import measure
import util


def repeat(function, sorted_input):
    range_low = 1000
    range_high = 10000
    increment = 1000
    number_of_runs = 10

    result = measure.measure_double_arg_function(function, range(range_low, range_high + 1, increment),
                                                 number_of_runs, sorted_input)
    return result


def collect(function, sorted_input=False):
    out_folder = "out"
    os.makedirs(out_folder, exist_ok=True)
    file_name = util.create_file_name(function)
    out_path = os.path.join(out_folder, file_name)
    data = repeat(function, sorted_input)
    data_handler.write_data(data, out_path)


def main():
    # Running main algorithms
    collect(base_algorithms.intersection)
    collect(base_algorithms.union)
    collect(base_algorithms.merge_sorted, True)


if __name__ == '__main__':
    main()
