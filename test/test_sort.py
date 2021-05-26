import pytest

from sources.algorithms import sort
import testing_util

test_cases = [
    ([0, 3, 2, 7, 5, 1, 6], [0, 1, 2, 3, 5, 6, 7]),  # random
    ([2, 3, -5, 7, 4, 3, 1], [-5, 1, 2, 3, 3, 4, 7]),  # random with duplicated elements
    ([-3, 0, 0, 1, 5, 8], [-3, 0, 0, 1, 5, 8]),  # sorted
    ([99, 76, 0, -43, -50], [-50, -43, 0, 76, 99])  # reversed
]


# @pytest.mark.skip
@pytest.mark.parametrize("array,expected", test_cases)
def test_insertion_sort(array, expected):
    actual = sort.insertion_sort(array)
    testing_util.assert_list(actual, expected)


# @pytest.mark.skip
@pytest.mark.parametrize("array,expected", test_cases)
def test_bubble_sort(array, expected):
    actual = sort.bubble_sort(array)
    testing_util.assert_list(actual, expected)


# @pytest.mark.skip
@pytest.mark.parametrize("array,expected", test_cases)
def test_selection_sort(array, expected):
    actual = sort.selection_sort(array)
    testing_util.assert_list(actual, expected)


# @pytest.mark.skip
@pytest.mark.parametrize("array,expected", test_cases)
def test_comb_sort(array, expected):
    actual = sort.comb_sort(array)
    testing_util.assert_list(actual, expected)


# @pytest.mark.skip
@pytest.mark.parametrize("array,expected", test_cases)
def test_enhanced_cocktail_sort(array, expected):
    actual = sort.enhanced_cocktail_sort(array)
    testing_util.assert_list(actual, expected)


@pytest.mark.parametrize("array,expected", test_cases)
def test_quicksort(array, expected):
    sort.quicksort(array)
    testing_util.assert_list(array, expected)


# @pytest.mark.skip
@pytest.mark.parametrize("in_array,expected_changed_array,expected_pivot_index",
                         [
                             ([1, 4, 3, 7, 6], [1, 4, 3, 6, 7], 3),
                             ([8, 4, 3, 7, 4], [4, 3, 4, 7, 8], 2),
                             ([5, 2, 8, 6, 1], [1, 2, 8, 6, 5], 0),
                             ([6, 2, 8, 4, 9], [6, 2, 8, 4, 9], 4),
                             ([3, 7, 8, 4, 2, 1, 9, 5, 5], [3, 4, 2, 1, 5, 5, 9, 8, 7], 5),
                         ])
def test_quicksort_partition(in_array, expected_changed_array, expected_pivot_index):
    array = in_array[:]
    actual_pivot_index = sort.quicksort_partition(array, 0, len(array) - 1)
    assert actual_pivot_index == expected_pivot_index
    testing_util.assert_list(array, expected_changed_array)
