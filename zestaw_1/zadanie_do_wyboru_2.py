# Tworzymy czy listy, potem dowiecie dlaczego
list_1 = []
list_2 = []
list_3 = []

# wczytujemy liczby użytkownika i dodajemy je do listy
for num in range(5):
    num_1 = int(input("Wpisz  liczbę: "))
    list_1.append(num_1)


i = 0
# bierzemy dwie liczby z listy i dodajemy wszytkie liczby między nimi do listy włącznie z tymi liczbami w inny list
while i < 4:
    start = list_1[i]
    stop = list_1[i+1] + 1
    # Jeżeli liczba jest mniejsza następnej idziemy po kolei w pętli for
    if start < stop:
        for k in range(start, stop):
            list_2.append(k)
    # Jeżeli liczba jest większa następnej idziemy po kolej w pętli for z krokiem -1
    elif start > stop:
        for k in range(start, stop-2, -1):
            list_2.append(k)
    i += 1

# dlatego że ostatnio wychodził podobny list [5, 6, 7, 7, 5, 4], stwożyłem nowy list gdzie usunęłem liczby powtórzające
for p in range(len(list_2) - 1):
    if list_2[p] != list_2[p+1]:
        list_3.append(list_2[p])

# Ale do lista nie była dodawana ostania liczba, dlatego ten odcinek kodu to robi
list_3.append(list_2[len(list_2)-1])

# Tak, mój kod działa, ale to było pierwsze co przyszło mnie do głowy, potem zapomniałem zrobić optymizacje.
# Dlatego mamy to, co widzimy
print(list_3)
