import logging


def get_logger(name):
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s | %(filename)s:%(lineno)s | %(levelname)s > %(message)s")
    return logging.getLogger(name)


def get_elapsed_time_log_string(function_list, now, start):
    return f"Elapsed time running {concat_function_names(function_list)}: {now - start}"


def concat_function_names(function_list):
    return ", ".join([func.__name__ for func in function_list])
