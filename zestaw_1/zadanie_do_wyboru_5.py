import matplotlib.pyplot as plt


class Hetman:
    def __init__(self, wiersz, kolumna):
        self.wiersz = wiersz
        self.kolumna = kolumna


def czy_szachują_się_hetmany(dane):
    for k in range(len(dane_1)):
        if dane_1[k] != tuple:
            raise TypeError("List must have only tuple type")
    # Sprawdzenie czy hetmany szachują się nawzajem
    for i in range(len(dane)):
        for j in range(i + 1, len(dane)):
            # Sprawdzenie czy hetmany znajdują się w tym samym rzędzie, kolumnie lub przekątnej
            if dane[i].wiersz == dane[j].wiersz or dane[i].kolumna == dane[j].kolumna or abs(dane[i].wiersz - dane[j].wiersz) == abs(dane[i].kolumna - dane[j].kolumna):
                return False  # Zwraca False jeśli dwa hetmany się szachują
    return True  # Zwraca True jeśli żadne dwa hetmany się nie szachują


def szachownica(dane):
    for k in range(len(dane_1)):
        if dane_1[k] != tuple:
            raise TypeError("List must have only tuple type")
    for k in range(len(dane_1)):
        for i in range(2):
            if dane_1[k][i] != int:
                raise TypeError("Tuple must have only integer type")
    # Utworzenie pustej planszy szachownicy
    szachownica = [['.' for _ in range(100)] for _ in range(100)]

    # Wypełnienie szachownicy hetmanami
    for hetman in dane:
        # Oznaczenie hetmana jako 'H'
        szachownica[hetman.wiersz][hetman.kolumna] = 'H'

    # Rysowanie szachownicy z hetmanami
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.matshow([[0 if col % 2 == row % 2 else 1 for col in range(100)]
               for row in range(100)], cmap='gray')

    # Dodanie hetmanów do szachownicy
    for hetman in dane:
        ax.text(hetman.kolumna, hetman.wiersz, 'H', va='center', ha='center',
                color='red', fontsize=3)

    plt.xlabel('Kolumna')
    plt.ylabel('Wiersz')

    plt.title('Rozkład hetmanów na szachownicy')
    plt.savefig('hetmany_szachownica.png')  # Zapisanie wykresu do pliku
    plt.show()


# Przykładowe dane hetmanów jako obiekty klasy Hetman
dane_1 = [Hetman(1, 14), Hetman(99, 99), Hetman(2, 1), Hetman(4, 8)]

# Wywołanie funkcji i wyświetlenie wyniku
