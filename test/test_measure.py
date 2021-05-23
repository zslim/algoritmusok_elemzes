from sources import measure

import pytest


@pytest.mark.parametrize("length,sorting",
                         [
                             (3, False),
                             (0, True),
                             (15, True)
                         ])
def test_generate_numeric_input(length, sorting):
    actual = measure.generate_numeric_array(length, sorting)
    assert len(actual) == length
    if sorting:
        assert sorted(actual) == actual
