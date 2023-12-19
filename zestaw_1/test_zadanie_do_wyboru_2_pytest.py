import pytest
from zadanie_do_wyboru_2 import zadanie


@pytest.mark.parametrize("list, result_list", [([4, 5, 6, 8, 10], [4, 5, 6, 7, 8, 9, 10]),
                                               ([-5, -3, -2, -1, 1],
                                                [-5, -4, -3, -2, -1, 0, 1]),
                                               ([1, 3, 1, 4, 5], [1, 2, 3, 2, 1, 2, 3, 4, 5])])
def test_zadanie_pytest(list, result_list):
    assert zadanie(list) == result_list


@pytest.mark.parametrize("error, list", [(TypeError, [4, 5, 6, 8, False]),
                                         (TypeError,
                                          [-5, -4, -3, -2, -1, 0, "1"]),
                                         (TypeError, [1, 2, 3, 2, 1, 2, 3, 5.04, 5])])
def test_zadanie_pytest(error, list):
    with pytest.raises(error):
        zadanie(list)
