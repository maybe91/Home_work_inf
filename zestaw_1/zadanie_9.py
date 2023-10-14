PIN = 4623

Saldo = 1000
Ilość_Prób = 0


while True:

    Operacja = int(input(f"Wybierz typ operacji.\n"
                         f"1: Wpłata\n"
                         f"2: Wypłata\n"
                         f"3: Sprawdić saldo\n"
                         f"4: Wyjcie\n"))

    if Operacja == 4:
        break

    Wpisany_PIN = int(input("Proszę wpisać  PIN kod: "))

    if Ilość_Prób == 2:
        print("Konto jest zablokowane")
        quit()

    if Wpisany_PIN != PIN:
        print("Wprowadzony kod jest nie prawidłowy. Sprobuj ponownie.")
        Ilość_Prób += 1
        continue
    elif Wpisany_PIN == PIN:
        if Operacja == 1:
            Summa_Wpłaty = int(input("Wpisz summę wpłaty: "))
            Saldo += Summa_Wpłaty
            print(f"Saldo: {Saldo} zł")
            Ilość_Prób = 0
            Kolejny_Krok = input(f"Czy chcesz kontynuować?\n"
                                 f"1: Tak\n"
                                 f"2: Nie\n")
            if Kolejny_Krok == 1:
                continue
            elif Kolejny_Krok == 2:
                break
        elif Operacja == 2:
            Summa_Wypłaty = int(input("Wpisz summę wypłaty: "))
            if Saldo - Summa_Wypłaty < 0:
                print("Saldo jest mniejsze od summy wypłaty.")
                Ilość_Prób = 0
                continue
            else:
                Saldo -= Summa_Wypłaty
                print(f"reszta saldo: {Saldo} zł")
                Ilość_Prób = 0
                Kolejny_Krok = input(f"Czy chcesz kontynuować?\n"
                                     f"1: Tak\n"
                                     f"2: Nie\n")
                if Kolejny_Krok == 1:
                    continue
                elif Kolejny_Krok == 2:
                    break
        elif Operacja == 3:
            print(f"Saldo wynosi {Saldo} zł")
            Kolejny_Krok = input(f"Czy chcesz kontynuować?\n"
                                 f"1: Tak\n"
                                 f"2: Nie\n")
            if Kolejny_Krok == 1:
                continue
            elif Kolejny_Krok == 2:
                break

print("Dziękujemy za użycie naszego banku")
