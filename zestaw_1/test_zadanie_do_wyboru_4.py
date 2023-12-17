import unittest
from zadanie_do_wyboru_4 import read_my_files


class Test_Read_My_Files(unittest.TestCase):

    def test_read_my_files(self):
        self.assertRaises(FileNotFoundError, read_my_files,
                          r"C:/Users/Admin/Destop")
        self.assertRaises(FileNotFoundError, read_my_files,
                          r"C:/Users/Amin/Desktop")


unittest.main(argv=[''], defaultTest='Test_Read_My_Files',
              verbosity=2, exit=False)
