import pytest

import test_util
from sources.algorithms import search


@pytest.mark.parametrize("array,checked,expected",
                         [
                             ([1, 3, 2, 5, 6], 5, {"found": True, "index": 3}),
                             ([1, 3, 2, 5, 0], 0, {"found": True, "index": 4}),
                             ([1, 3, 2, 5, 0], 9, {"found": False, "index": -1}),
                             ([1, 3, 2, 5, 0], "ed", {"found": False, "index": -1}),
                         ])
def test_linear_unsorted(array, checked, expected):
    actual = search.linear_unsorted(array, checked)
    test_util.assert_search_result(actual, expected)
