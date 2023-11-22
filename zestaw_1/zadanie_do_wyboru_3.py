# tworzenie pierwszej macierzy
kolumna_1 = int(input("wpisz ilośc kolumn macierzy 1: "))
wiersz_1 = int(input("Wpisz ilość wierszy macierzy 1: "))
macierz_1 = []
macierz_2 = []

for i in range(wiersz_1):
    wiersz = []
    for i in range(kolumna_1):
        wiersz.append(int(input("Wpisz element macierzy: ")))
    macierz_1.append(wiersz)

# tworzenie drugiej macierzy
kolumna_2 = int(input("wpisz ilośc kolumn macierzy 2: "))
wiersz_2 = int(input("Wpisz ilość wierszy macierzy 2: "))

for i in range(wiersz_2):
    wiersz = []
    for i in range(kolumna_2):
        wiersz.append(int(input("Wpisz element macierzy: ")))
    macierz_2.append(wiersz)


def iloczyn_macierzym1m2(macierz_1, macierz_2):
    # Sprawdzamy czy można przemnożyć macierzy
    if len(macierz_1[0]) != len(macierz_2):
        print("Nie można mnożyc: ilość kolumn pierwszej macierzy nie jest równa ilości wierszy drugiej macierzy.")
        return None

    # Macierz - iloczyn macierzy m1*m2
    result = [[0 for _ in range(len(macierz_2[0]))]
              for _ in range(len(macierz_1))]

    # Process mnożenia
    for i in range(len(macierz_1)):
        for j in range(len(macierz_2[0])):
            for k in range(len(macierz_2)):
                result[i][j] += macierz_1[i][k] * macierz_2[k][j]
    print("iloczyn macierzy 1 i macierzy 2:", result)
    return


def iloczyn_macierzym2m1(macierz_1, macierz_2):
    # Sprawdzamy czy można przemnożyć macierzy
    if len(macierz_2[0]) != len(macierz_1):
        print("Nie można mnożyc: ilość kolumn drugiej macierzy nie jest równa ilości wierszy pierwszej macierzy.")
        return None

    # Macierz - iloczyn macierzy m1*m2
    result = [[0 for _ in range(len(macierz_1[0]))]
              for _ in range(len(macierz_2))]

    # Process mnożenia
    for i in range(len(macierz_2)):
        for j in range(len(macierz_1[0])):
            for k in range(len(macierz_1)):
                result[i][j] += macierz_2[i][k] * macierz_1[k][j]
    print("iloczyn macierzy 2 i macierzy 1:", result)
    return


def determinant(matrix):
    rozmiar = len(matrix)

    # Jeśli rozmiar macierzy 2x2, używamy formułę dla wyznaczenia wyznacznika
    if rozmiar == 2:
        det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        return det

    det = 0
    for i in range(rozmiar):
        # Szukamy minor dla elementa matrix[0][i]
        minor = [[matrix[row][col] for col in range(
            rozmiar) if col != i] for row in range(1, rozmiar)]

        # Szukamy wyznacznik rekurencyjnie dla każdego minora
        det += ((-1) ** i) * matrix[0][i] * determinant(minor)

    return det


def wyznacnick(macierz_2, macierz_1):
    if len(macierz_2) != len(macierz_2[0]) and len(macierz_1) != len(macierz_1[0]):
        print("Wyznacznik się liczy tulko dla macierzy kwadratowych")
        return
    elif len(macierz_2) == len(macierz_2[0]) and len(macierz_1) != len(macierz_1[0]):
        det_last = determinant(macierz_2)
        return det_last
    elif len(macierz_2) != len(macierz_2[0]) and len(macierz_1) == len(macierz_1[0]):
        det_last = determinant(macierz_1)
        return det_last
    else:
        # Liczymy wyznacznik
        det1 = determinant(macierz_1)
        det2 = determinant(macierz_2)
        det_last = det1 + det2
        print("Wyznacnik macierzy:", det_last)
        return det_last


def mnożenie_macierzy_przez_skalar(macierz_1, macierz_2):
    for i in range(len(macierz_1)):
        for j in range(len(macierz_1[0])):
            macierz_1[i][j] = det_last * macierz_1[i][j]
    for k in range(len(macierz_2)):
        for l in range(len(macierz_2[0])):
            macierz_2[k][l] = det_last * macierz_2[k][l]
    print(macierz_1, macierz_2)
    return


iloczyn_macierzym1m2(macierz_1, macierz_2)
iloczyn_macierzym2m1(macierz_1, macierz_2)
det_last = wyznacnick(macierz_1, macierz_2)
mnożenie_macierzy_przez_skalar(macierz_1, macierz_2)
