import unittest
from zadanie_do_wyboru_2 import zadanie


class Test_Zadanie(unittest.TestCase):

    def test_list(self):
        self.assertListEqual(
            zadanie([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertListEqual(zadanie([1, 3, 6, 9, 12]), [
                             1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_types(self):
        self.assertRaises(TypeError, zadanie, [True, 1, 4, 5, False])
        self.assertRaises(TypeError, zadanie, [4, 1, 4, 5, 'five'])
        self.assertRaises(TypeError, zadanie, [51, 1, 4, 5, 5+2j])


unittest.main(argv=[''], defaultTest='Test_Zadanie', verbosity=2, exit=False)
