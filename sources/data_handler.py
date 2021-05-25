import pandas


def write_data(data, path):
    df = pandas.DataFrame(data)
    df.to_csv(path)


def read_data(path):
    df = pandas.read_csv(path)
    return df
