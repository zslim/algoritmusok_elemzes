from sources import input_generator

import pytest


@pytest.mark.parametrize("length,array_order",
                         [
                             (3, False),
                             (0, True),
                             (15, True)
                         ])
def test_generate_numeric_array(length, array_order):
    actual = input_generator.generate_numeric_array(length, array_order)
    assert len(actual) == length
    if array_order == input_generator.ArrayOrder.SORTED:
        assert sorted(actual) == actual
    elif array_order == input_generator.ArrayOrder.REVERSE:
        assert sorted(actual, reverse=True) == actual
