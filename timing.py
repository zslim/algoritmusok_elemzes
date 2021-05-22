import time

TIMES = []


def timer(collector: list):
    def decorator(function):
        def wrapper(*args, **kwargs):
            start = time.time()
            returned_value = function(*args, **kwargs)
            stop = time.time()
            record = {"function": function.__name__, "parameter lengths": [len(e) for e in args],
                      "seconds": stop - start, "returned": returned_value}
            collector.append(record)
            return returned_value
        return wrapper
    return decorator
