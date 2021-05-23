from datetime import datetime


def create_file_name(function):
    now = datetime.now()
    timestamp = f"{now.year}{now.month}{now.day}_{now.hour}{now.minute}{now.second}"
    file_name = f"{function.__name__}_{timestamp}.csv"
    return file_name


def get_size(param):
    if isinstance(param, list):
        return len(param)
    else:
        return type(param)
