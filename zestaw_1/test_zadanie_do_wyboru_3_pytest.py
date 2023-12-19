import pytest
from zadanie_do_wyboru_3 import determinant, wyznacznick, mnożenie_macierzy_przez_skalar


@pytest.mark.parametrize("error, macierz_1, macierz_2", [(TypeError, ["[3, 3]", [5, 0]], [[1, 0], [0, 1]]),
                                                         (TypeError, [["five", 3], [5, 0]], [
                                                             [1, 0], [0, 1]]),
                                                         (TypeError, [5.4, [5, 0]], [
                                                          [1, 0], [0, 1]]),
                                                         (TypeError, [True, [5, 0]], [
                                                          [1, 0], [0, 1]]),
                                                         (ValueError, [[4, 2], [5, 0]], [
                                                          [1, 1, 2, 0], [0, 1]]),
                                                         (ValueError, [[5, 3, 2, 1], [5, 0]], [[1, 0], [0, 1]])])
def test_wyznacznik(error, macierz_1, macierz_2):
    with pytest.raises(error):
        wyznacznick(macierz_1, macierz_2)
