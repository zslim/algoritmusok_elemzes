import pytest

import testing_util
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
    testing_util.assert_search_result(actual, expected)


@pytest.mark.parametrize("array,checked,expected",
                         [
                             ([1, 3, 6, 7], 6, {"found": True, "index": 2}),
                             ([1, 6, 3, 7], 7, {"found": True, "index": 3}),
                             ([1, 7, 2, 8], 4, {"found": False, "index": -1}),
                             ([], 3, {"found": False, "index": -1})
                         ])
def test_sentinel_unsorted(array, checked, expected):
    actual = search.sentinel_unsorted(array, checked)
    testing_util.assert_search_result(actual, expected)


@pytest.mark.parametrize("array,checked,expected",
                         [
                             ([2, 4, 7, 9, 15], 9, {"found": True, "index": 3}),
                             ([2, 4, 7, 9, 15], 2, {"found": True, "index": 0}),
                             ([2, 4, 7, 9, 15], 15, {"found": True, "index": 4}),
                             ([2, 4, 7, 9, 15], 0, {"found": False, "index": -1}),
                             ([2, 4, 7, 9, 15], 10, {"found": False, "index": -1}),
                             ([2, 4, 7, 9, 15], 20, {"found": False, "index": -1}),
                         ])
def test_linear_sorted(array, checked, expected):
    actual = search.linear_sorted(array, checked)
    testing_util.assert_search_result(actual, expected)


@pytest.mark.parametrize("array,checked,expected",
                         [
                             ([2, 4, 7, 9, 9, 15], 9, {"found": True, "index": 3}),
                             ([2, 2, 4, 7, 9, 15], 2, {"found": True, "index": 0}),
                             ([2, 4, 7, 9, 15, 15], 15, {"found": True, "index": 4}),
                             ([2, 4, 7, 9, 15], 0, {"found": False, "index": -1}),
                             ([2, 4, 7, 9, 15], 10, {"found": False, "index": -1}),
                             ([2, 4, 7, 9, 15], 20, {"found": False, "index": -1}),
                         ])
def test_binary_sorted(array, checked, expected):  # TODO: ahol a keresett elemből kettő is van, melyiket találja meg?
    actual = search.binary_sorted(array, checked)
    testing_util.assert_search_result(actual, expected)


@pytest.mark.parametrize("array,checked,expected",
                         [
                             ([2, 4, 7, 9, 15], 9, {"found": True, "index": 3}),
                             ([2, 4, 7, 9, 15], 2, {"found": True, "index": 0}),
                             ([2, 4, 7, 9, 15], 15, {"found": True, "index": 4}),
                             ([2, 4, 7, 9, 15], 0, {"found": False, "index": -1}),
                             ([2, 4, 7, 9, 15], 10, {"found": False, "index": -1}),
                             ([2, 4, 7, 9, 15], 20, {"found": False, "index": -1}),
                         ])
def test_jump_sorted(array, checked, expected):
    actual = search.jump_sorted(array, checked)
    testing_util.assert_search_result(actual, expected)
