import pytest

from sources.algorithms import sort
import testing_util


@pytest.mark.parametrize("array,expected",
                         [
                             ([0, 3, 2, 7, 5, 1, 6], [0, 1, 2, 3, 5, 6, 7]),
                             ([2, -5, 7, 4, 3, 1], [-5, 1, 2, 3, 4, 7]),
                             ([-3, 5, 0, 1, 8, 0], [-3, 0, 0, 1, 5, 8]),
                             ([99, -43, 76, -50, 0], [-50, -43, 0, 76, 99])
                         ])
def test_insertion_sort(array, expected):
    actual = sort.insertion_sort(array)
    testing_util.assert_list(actual, expected)


@pytest.mark.parametrize("array,expected",
                         [
                             ([0, 3, 2, 7, 5, 1, 6], [0, 1, 2, 3, 5, 6, 7]),
                             ([2, -5, 7, 4, 3, 1], [-5, 1, 2, 3, 4, 7]),
                             ([-3, 5, 0, 1, 8, 0], [-3, 0, 0, 1, 5, 8]),
                             ([99, -43, 76, -50, 0], [-50, -43, 0, 76, 99])
                         ])
def test_bubble_sort(array, expected):
    actual = sort.bubble_sort(array)
    testing_util.assert_list(actual, expected)


@pytest.mark.parametrize("array,expected",
                         [
                             ([0, 3, 2, 7, 5, 1, 6], [0, 1, 2, 3, 5, 6, 7]),
                             ([2, -5, 7, 4, 3, 1], [-5, 1, 2, 3, 4, 7]),
                             ([-3, 5, 0, 1, 8, 0], [-3, 0, 0, 1, 5, 8]),
                             ([99, -43, 76, -50, 0], [-50, -43, 0, 76, 99])
                         ])
def test_selection_sort(array, expected):
    actual = sort.selection_sort(array)
    testing_util.assert_list(actual, expected)


@pytest.mark.parametrize("array,expected",
                         [
                             ([0, 3, 2, 7, 5, 1, 6], [0, 1, 2, 3, 5, 6, 7]),
                             ([2, -5, 7, 4, 3, 1], [-5, 1, 2, 3, 4, 7]),
                             ([-3, 5, 0, 1, 8, 0], [-3, 0, 0, 1, 5, 8]),
                             ([99, -43, 76, -50, 0], [-50, -43, 0, 76, 99])
                         ])
def test_comb_sort(array, expected):
    actual = sort.comb_sort(array)
    testing_util.assert_list(actual, expected)


@pytest.mark.parametrize("array,expected",
                         [
                             ([0, 3, 2, 7, 5, 1, 6], [0, 1, 2, 3, 5, 6, 7]),
                             ([2, -5, 7, 4, 3, 1], [-5, 1, 2, 3, 4, 7]),
                             ([-3, 5, 0, 1, 8, 0], [-3, 0, 0, 1, 5, 8]),
                             ([99, -43, 76, -50, 0], [-50, -43, 0, 76, 99])
                         ])
def test_enhanced_cocktail_sort(array, expected):
    actual = sort.enhanced_cocktail_sort(array)
    testing_util.assert_list(actual, expected)
