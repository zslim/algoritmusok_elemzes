import pytest

import testing_util
from sources.algorithms import base


@pytest.mark.parametrize("input_list,input_element,expected",
                         [
                             ([1, 3, 5, 6, 7], 3, True),
                             ([1, 3, 5, 6, 7], 8, False),
                             ([0], 1, False),
                             ([], 4, False),
                             (["ed", "al", "wi"], "ho", False),
                             (["ed", "al", "wi"], "ed", True)
                         ]
                         )
def test_inclusion(input_list, input_element, expected):
    result = base._does_include(input_list, input_element)
    assert result == expected


@pytest.mark.parametrize("array1,array2,expected",
                         [
                             ([8, 3, 1, 5, 6], [1, 2, 5], [1, 5]),
                             ([5, 2, 1, 3], [], []),
                             (["ed", "al", "wi"], ["ho", "ed"], ["ed"])
                         ])
def test_intersection(array1, array2, expected):
    result = base.intersection(array1, array2)
    testing_util.assert_list_without_order(result, expected)


@pytest.mark.parametrize("array1,array2,expected",
                         [
                             ([1, 3, 5, 6], [1, 2, 5], [1, 2, 3, 5, 6]),
                             ([1, 2, 5], [1, 3, 5, 6], [1, 2, 3, 5, 6]),
                             ([8, 3, 5, 6], [], [3, 5, 6, 8]),
                         ])
def test_union(array1, array2, expected):
    result = base.union(array1, array2)
    testing_util.assert_list_without_order(result, expected)


@pytest.mark.parametrize("array1,array2,expected",
                         [
                             ([1, 2], [3, 4], [1, 2, 3, 4]),
                             ([0, 3, 5], [1, 2, 5], [0, 1, 2, 3, 5]),
                             ([-4, 3, 7], [5, 8], [-4, 3, 5, 7, 8]),
                             ([1, 6, 9], [], [1, 6, 9])
                         ])
def test_merge_sorted(array1, array2, expected):
    result = base.merge_sorted(array1, array2)
    testing_util.assert_list(result, expected)
