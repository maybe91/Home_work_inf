import pytest
from zadanie_do_wyboru_6 import rozbicie_liczby\



@pytest.mark.parametrize("error, liczba", [(TypeError, False),
                                           (TypeError, 5.324),
                         (ValueError, -653)])
def test_rozbice_liczby(error, liczba):
    with pytest.raises(error):
        rozbicie_liczby(liczba)
