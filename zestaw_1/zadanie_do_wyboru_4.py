import os
import re


def print_letters(*args):
    print(' '.join(args[:5]))


def read_my_files(katalog):

    if not os.path.exists(katalog):
        raise FileNotFoundError("Nie ma takiego katalogu")

    txt_plik = [file for file in os.listdir(
        katalog) if file.endswith(".txt")]

    if not txt_plik:
        raise FileNotFoundError("W podanym katalogu nie ma plików .txt")

    for nazwa_pliku in txt_plik:
        with open(os.path.join(katalog, nazwa_pliku), 'r') as file:
            lines = file.readlines()
            for line in lines:
                litery = re.findall(r'[a-zA-Z]', line)
                print_letters(*litery)


# Przykładowe użycie
read_my_files(r"C:/Users/Admin/Desktop")
