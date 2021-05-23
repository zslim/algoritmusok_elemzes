def assert_list(actual: list, expected: list):
    assert len(actual) == len(expected)
    assert all([a == e for a, e in zip(actual, expected)])


def assert_list_without_order(actual: list, expected: list):
    assert len(actual) == len(expected)
    assert all([a == e for a, e in zip(sorted(actual), sorted(expected))])


def assert_search_result(actual, expected):
    """
    Search result is supposed to be a tuple: (found: bool, index: int)
    index is -1 if not found
    """
    assert actual["found"] == expected["found"]
    assert actual["index"] == expected["index"]
