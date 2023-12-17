import unittest
from zadanie_do_wyboru_6 import rozbicie_liczby


class Test_Rozbicie_Liczby(unittest.TestCase):

    def test_values(self):
        self.assertRaises(ValueError, rozbicie_liczby, -5)

    def test_types(self):
        self.assertRaises(TypeError, rozbicie_liczby, 5+6j)
        self.assertRaises(TypeError, rozbicie_liczby, True)
        self.assertRaises(TypeError, rozbicie_liczby, "coś tam")
        self.assertRaises(TypeError, rozbicie_liczby, [42])


unittest.main(argv=[''], defaultTest='Test_Rozbicie_Liczby',
              verbosity=2, exit=False)
