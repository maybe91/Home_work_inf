import pytest
from zadanie_do_wyboru_4 import read_my_files


@pytest.mark.parametrize("error, file", [(FileNotFoundError, r"C:/Users/Admin/Destop"),
                                         (FileNotFoundError, r"C:/Users/Adin/Desktop")])
def test_read_my_files(error, file):
    with pytest.raises(error):
        read_my_files(file)
