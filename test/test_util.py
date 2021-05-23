def assert_list(actual: list, expected: list):
    assert len(actual) == len(expected)
    assert all([a == e for a, e in zip(actual, expected)])


def assert_list_without_order(actual: list, expected: list):
    assert len(actual) == len(expected)
    assert all([a == e for a, e in zip(sorted(actual), sorted(expected))])
