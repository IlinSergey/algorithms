from main import binary_search
import pytest

@pytest.mark.parametrize('list, item, expected_result', [([0, 1, 2, 5, 8 ,9, 11, 15], 5, 3),
                                                         ([2, 4, 6, 15, 24, 32, 44], 44, 6),
                                                         ([0, 2, 3, 5, 11, 12, 24], 4, None)])
def test_binary_search(list, item, expected_result):
    assert binary_search(list, item) == expected_result