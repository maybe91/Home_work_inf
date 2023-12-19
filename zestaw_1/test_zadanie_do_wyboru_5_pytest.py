import pytest
from zadanie_do_wyboru_5 import szachownica, Hetman


@pytest.mark.parametrize("error, dane", [(TypeError, [Hetman(1, 14), Hetman(0.6, 99), Hetman(2, 1), Hetman(4, 8)]),
                                         (TypeError, [Hetman(1, 14), Hetman(
                                             99, 99), Hetman(False, 1), Hetman(4, 8)]),
                                         (TypeError, [(1, 14), Hetman(
                                             99, 99), Hetman(2, 1), Hetman(4, 8)]),
                                         (TypeError, [Hetman(1, 14), Hetman(99, 99), Hetman(2, 1), "Hetman(4, 8)"]),])
def test_szachownica(error, dane):
    with pytest.raises(error):
        szachownica(dane)
