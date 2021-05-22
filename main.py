import base_algorithms
import run
import util


def create_data():
    range_low = 1000
    range_high = 10000
    increment = 1000
    number_of_runs = 5
    data = []

    intersection_data = run.measure_double_arg_function(base_algorithms.intersection,
                                                        range(range_low, range_high + 1, increment),
                                                        number_of_runs)

    data.append(intersection_data)
    return data


if __name__ == '__main__':
    data = create_data()
    util.print_list_of_dicts(data)
