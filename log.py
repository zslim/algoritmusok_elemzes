import logging


def get_logger(name):
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s | %(filename)s:%(lineno)s | %(levelname)s > %(message)s")
    return logging.getLogger(name)


def print_list_of_dicts(data):
    for dictionary in data:
        print(dictionary, "\n")