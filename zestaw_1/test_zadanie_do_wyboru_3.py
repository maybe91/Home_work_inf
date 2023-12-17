import unittest
from zadanie_do_wyboru_3 import iloczyn_macierzym1m2, iloczyn_macierzym2m1, determinant, wyznacznick, mnożenie_macierzy_przez_skalar


class Test_iloczyn_macierzym1m2(unittest.TestCase):

    def test_macierzm1(self):
        self.assertRaises(TypeError, iloczyn_macierzym1m2, [True, [1, 0]])
        self.assertRaises(TypeError, iloczyn_macierzym1m2, ["five", [1, 0]])
        self.assertRaises(TypeError, iloczyn_macierzym1m2, [3, [1, 0]])


unittest.main(
    argv=[''], defaultTest='Test_iloczyn_macierzym1m2', verbosity=2, exit=False)
