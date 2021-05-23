import os

from sources.algorithms import base_algorithms, search
import data_handler
import measure
import util


def repeat(function, sorted_input, returns_list):
    range_low = 1000
    range_high = 10000
    increment = 1000
    number_of_runs = 10

    result = measure.measure_double_arg_function(function, range(range_low, range_high + 1, increment),
                                                 number_of_runs, sorted_input, returns_list)
    return result


def collect(function, sorted_input=False, returns_list=False):
    out_folder = "out"
    os.makedirs(out_folder, exist_ok=True)
    file_name = util.create_file_name(function)
    out_path = os.path.join(out_folder, file_name)
    data = repeat(function, sorted_input, returns_list)
    data_handler.write_data(data, out_path)


def main():
    # Base algorithms
    # collect(base_algorithms.intersection, returns_list=True)
    # collect(base_algorithms.union, returns_list=True)
    # collect(base_algorithms.merge_sorted, sorted_input=True, returns_list=True)

    # Search algorithms
    collect(search.linear_unsorted)
    collect(search.strazsas_unsorted)
    collect(search.linear_sorted, sorted_input=True)
    collect(search.binary_sorted, sorted_input=True)


if __name__ == '__main__':
    main()
