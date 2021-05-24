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


def parse_search_result(dict_string):
    content = dict_string[1:-1]
    cut = [d.split(":") for d in content.split(",")]
    result = {"found": cut[0][1] == " True", "index": int(cut[1][1])}
    return result
