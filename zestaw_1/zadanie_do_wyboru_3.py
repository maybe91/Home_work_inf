kolumna_1 = int(input("wpisz ilośc kolumn macierzy 1: "))
wiersz_1 = int(input("Wpisz ilość wierszy macierzy 1: "))
macierz_1 = []
macierz_2 = []

# tworzenie pierwszej macierzy
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
print(macierz_1)
print(macierz_2)
# iloczyn macierzy
# if kolumna_1 != wiersz_2 and kolumna_2 != wiersz_1:
#     print("Macierzy nie można przemnożyć")
# elif kolumna_1 == wiersz_2 and kolumna_2 != wiersz_1:
#     iloczyn_m1_m2 = []
#     for i in range(wiersz_2):
#         wiersz = []
#         for k in range(kolumna_1):
#             wiersz.append()

[[1, 2],
 [3, 4]]
[[5, 6],
 [6, 7]]
