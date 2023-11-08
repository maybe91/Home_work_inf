'''Proszę napisać program, który pobierze od użytkownika 5
 różnych liczb całkowitych i doda je do listy. 
 Program ma za zadanie uzupełnić listę liczbami całkowitymi znajdującymi się
 pomiędzy kolejnymi liczbami a następnie wypisać listę. Przykładowe dane wejściowe: 
[0,7,13,8,12], pożądane wyjście: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,12,11,10,9,8,9,10,11,12]. 
Należy obsłużyć wyjątek, w którym dwie sąsiadujące ze sobą wprowadzone przez 
użytkownika liczby są takie same.'''
list_1 = []
list_2 = []

# wczytujemy liczby użytkownika i dodajemy je do listy
for num in range(5):
    num_1 = int(input("Wpisz  liczbę: "))
    list_1.append(num_1)


i = 0
# bierzemy dwie liczby z listy i dodajemy wszytkie liczby między nimi do listy włącznie z tymi liczbami w inny list
while i < 4:
    start = list_1[i]
    stop = list_1[i+1]
    # Jeżeli liczba jest mniejsza następnej idziemy po kolei w pętli for
    if start < stop:
        for k in range(start, stop):
            list_2.append(k)
    # Jeżeli liczba jest większa następnej idziemy po kolej w pętli for z krokiem -1
    else:
        for k in range(start, stop, -1):
            list_2.append(k)
    i += 1

# dodawanie liczby końcowej do listy
if start < stop:
    list_2.append(list_2[len(list_2) - 1] + 1)
else:
    list_2.append(list_2[len(list_2) - 1] - 1)
print(list_2)
