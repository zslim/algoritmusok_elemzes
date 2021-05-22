import time


def recording(function, *args, **kwargs):
    start = time.time()
    returned_value = function(*args, **kwargs)
    stop = time.time()
    record = {"function": function.__name__, "parameter lengths": [len(e) for e in args],
              "seconds": stop - start, "returned": returned_value}
    return record


def measure(function, param_numbers, number_of_runs):
    result = []
    for n in range(number_of_runs):
        pass
