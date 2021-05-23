import pandas


def write_data(data, path):
    df = pandas.DataFrame(data)
    df.to_csv(path)
