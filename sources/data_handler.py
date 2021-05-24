import pandas


def write_data(data, path):
    df = pandas.DataFrame(data)
    df = separate_parameter_lengths(df)
    df.to_csv(path)


def read_data(path):
    df = pandas.read_csv(path)
    return df


def separate_parameter_lengths(df: pandas.DataFrame):
    returned_df = df.copy()
    returned_df[["param1", "param2"]] = pandas.DataFrame(df.parameterLengths.to_list(), index=df.index)
    return returned_df
