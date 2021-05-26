import os

import data_handler
import log
import measure
import util
from measure import AlgorithmType
from sources.algorithms import base, search, sort


LOGGER = log.get_logger(__name__)


def repeat(function_list, algorithm_type, sorted_input):
    input_low = 1000
    input_high = 10000
    increment = 1000

    input_lengths = range(input_low, input_high + 1, increment)
    number_of_runs = 100

    measurer = None

    if algorithm_type == AlgorithmType.SORT:
        measurer = measure.measure_sorting_algorithms
    elif algorithm_type == AlgorithmType.SEARCH:
        measurer = measure.measure_search_algorithms
    elif algorithm_type == AlgorithmType.BASE:
        measurer = measure.measure_base_algorithms

    LOGGER.info(f"======= Running {util.concat_function_names(function_list)} =======")
    result = measurer(function_list, input_lengths, number_of_runs, sorted_input)

    return result


# Comparable algorithms should come in one call, hence function list
def generate_and_write(name, function_list, algorithm_type, sorted_input=False):
    out_folder = os.path.join("out", "out_data")
    os.makedirs(out_folder, exist_ok=True)
    file_name = util.create_file_name(name)
    out_path = os.path.join(out_folder, file_name)
    data = repeat(function_list, algorithm_type, sorted_input)
    data_handler.write_data(data, out_path)
    LOGGER.info(f"Wrote file: {out_path}")


def main():
    # Base algorithms
    # generate_and_write("intersection", [base.intersection], AlgorithmType.BASE)
    # generate_and_write("union", [base.union], AlgorithmType.BASE)
    # generate_and_write("merge", [base.merge_sorted], AlgorithmType.BASE, sorted_input=True)

    # Search algorithms
    generate_and_write("search_unsorted", [search.linear_unsorted, search.sentinel_unsorted], AlgorithmType.SEARCH)
    generate_and_write("search_sorted",
                       [search.linear_sorted, search.binary_sorted, search.jump_sorted],
                       AlgorithmType.SEARCH,
                       sorted_input=True)

    # Sort algorithms
    generate_and_write("sorting",
                       [sort.insertion_sort, sort.bubble_sort, sort.selection_sort, sort.comb_sort,
                        sort.enhanced_cocktail_sort, sort.quicksort],
                       AlgorithmType.SORT)


if __name__ == '__main__':
    main()
