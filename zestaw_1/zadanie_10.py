import random


while True:
    num_1 = int(input("wpisz pierwszą liczbę: "))
    num_2 = int(input("wpisz drugą liczbę: "))
    typ_operacji = input(f"Wybierz jeden typ operacji:\n"
                         f"suma: '+'\n"
                         f"różnica: '-'\n"
                         f"mnożenie: '*'\n"
                         f"dzielenie: '/'\n"
                         f"pierwistkowanie: '#'\n"
                         f"potęgowanie: '^'\n"
                         f"losowanie: 'x'\n")
    print(num_1 + num_2)
    if typ_operacji == "+":
        print(f"{num_1} + {num_2} = {num_1 + num_2}\n")
        Wybór = input(f"czy chcesz wprowadzić nowe dane?\n"
                      f"'T': Tak\n"
                      f"'N': Nie\n")
        if Wybór == 'T':
            continue
        elif Wybór == 'N':
            break
    elif typ_operacji == "-":
        print(f"{num_1} - {num_2} = {num_1 - num_2}\n")
        Wybór = input(f"czy chcesz wprowadzić nowe dane?\n"
                      f"'T': Tak\n"
                      f"'N': Nie\n")
        if Wybór == 'T':
            continue
        elif Wybór == 'N':
            break
    elif typ_operacji == "*":
        print(f"{num_1} * {num_2} = {num_1 * num_2}\n")
        Wybór = input(f"czy chcesz wprowadzić nowe dane?\n"
                      f"'T': Tak\n"
                      f"'N': Nie\n")
        if Wybór == 'T':
            continue
        elif Wybór == 'N':
            break
    elif typ_operacji == "/":
        print(f"{num_1} / {num_2} = {num_1 / num_2}\n")
        Wybór = input(f"czy chcesz wprowadzić nowe dane?\n"
                      f"'T': Tak\n"
                      f"'N': Nie\n")
        if Wybór == 'T':
            continue
        elif Wybór == 'N':
            break
    elif typ_operacji == "#":
        print(f"{num_1} # {num_2} = {(num_1) ** (1/num_2)}\n")
        Wybór = input(f"czy chcesz wprowadzić nowe dane?\n"
                      f"'T': Tak\n"
                      f"'N': Nie\n")
        if Wybór == 'T':
            continue
        elif Wybór == 'N':
            break
    elif typ_operacji == "^":
        print(f"{num_1} ^ {num_2} = {num_1 ** num_2}\n")
        Wybór = input(f"czy chcesz wprowadzić nowe dane?\n"
                      f"'T': Tak\n"
                      f"'N': Nie\n")
        if Wybór == 'T':
            continue
        elif Wybór == 'N':
            break
    elif typ_operacji == "x":
        print(f"{num_1} x {num_2} = {random.randrange(num_1,  num_2)}\n")
        Wybór = input(f"czy chcesz wprowadzić nowe dane?\n"
                      f"'T': Tak\n"
                      f"'N': Nie\n")
        if Wybór == 'T':
            continue
        elif Wybór == 'N':
            break
    else:
        print(f"wybrałeś nie istniejącą operacje, sprobuj ponownie")
        continue

print("Dziękujemy za użycie naszego kalkulatora!")
