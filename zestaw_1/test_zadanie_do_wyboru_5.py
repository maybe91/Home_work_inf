import unittest
from zadanie_do_wyboru_5 import czy_szachują_się_hetmany, Hetman


class Test_Czy_Szachują_Się_Hetmany(unittest.TestCase):

    def test_czy_szachują_się_hetmany(self):
        self.assertRaises(TypeError, czy_szachują_się_hetmany, [
                          Hetman(1, 14), Hetman(99, 99), Hetman(2, 1), Hetman(4, 8)])
        self.assertRaises(TypeError, czy_szachują_się_hetmany, [
                          (1, 14), Hetman(99, 99), Hetman(2, 1), Hetman(4, 8)])
        self.assertRaises(TypeError, czy_szachują_się_hetmany, [
                          "string", Hetman(99, 99), Hetman(2, 1), Hetman(4, 8)])


unittest.main(argv=[''], defaultTest='Test_Czy_Szachują_Się_Hetmany',
              verbosity=2, exit=False)
