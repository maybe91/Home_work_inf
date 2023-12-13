import matplotlib.pyplot as plt
import random


def czy_szachują_się_hetmany(dane):
    # Sprawdzenie czy hetmany szachują się nawzajem
    for i in range(len(dane)):
        for j in range(i + 1, len(dane)):
            # Sprawdzenie czy hetmany znajdują się w tym samym rzędzie, kolumnie lub przekątnej
            if dane[i][0] == dane[j][0] or dane[i][1] == dane[j][1] or abs(dane[i][0] - dane[j][0]) == abs(dane[i][1] - dane[j][1]):
                return False  # Zwraca False jeśli dwa hetmany się szachują
    return True  # Zwraca True jeśli żadne dwa hetmany się nie szachują


def szachownica(dane):
    # Utworzenie pustej planszy szachownicy
    szachownica = [['.' for _ in range(100)] for _ in range(100)]

    # Wypełnienie szachownicy hetmanami
    for hetman in dane:
        wiersz, kolumna = hetman
        szachownica[wiersz][kolumna] = 'H'  # Oznaczenie hetmana jako 'H'

    # Rysowanie szachownicy z hetmanami
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.matshow([[0 if col % 2 == row % 2 else 1 for col in range(100)]
               for row in range(100)], cmap='gray')

    # Dodanie hetmanów do szachownicy
    for i in range(100):
        for j in range(100):
            if szachownica[i][j] == 'H':
                ax.text(j, i, 'H', va='center', ha='center',
                        color='red', fontsize=3)

    plt.xlabel('Kolumna')
    plt.ylabel('Wiersz')

    plt.title('Rozkład hetmanów na szachownicy')
    plt.savefig('hetmany_szachownica.png')  # Zapisanie wykresu do pliku
    plt.show()


# Przykładowe dane hetmanów
dane_1 = [(1, 14), (99, 99), (2, 1), (4, 8)]

dane = []

for i in range(random.randint(0, 100)):
    dane.append((random.randint(0, 99), random.randint(0, 100)))

print(dane)
# Wywołanie funkcji i wyświetlenie wyniku
wynik = czy_szachują_się_hetmany(dane)
if wynik:
    print("Żadne dwa hetmany się nie szachują.")
else:
    print("Co najmniej dwa hetmany się szachują.")

szachownica(dane)
