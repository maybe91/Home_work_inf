"""
Program czyta 2 liczby użytkownika
i dalej oblicza ich sumę, różnicę, 
iloczyn, iloraz, kwadrat (obu liczb) 
oraz pierwiastek drugiego stopnia (obu liczb)."""
num_1 = int(input("pierwsza licba:"))  # przyswojenie pierwszej zmiennej
num_2 = int(input("druga liczba:"))  # przyswojenie drugie zmiennej

# wyświetlienie wszystkich działań nad liczbami
if num_1 < 0 and num_2 < 0:
    print("sorry, the numbers are lower than zero")
    exit()
elif num_1 < 0:
    num_1 = num_1 * (-1)
    print(f"summa liczb: {num_1 + num_2}\n"
          f"różnica liczb: {num_1 - num_2}\n"
          f"iloczyn liczb: {num_1 * num_2}\n"
          f"iloraz liczb: {num_1 / num_2}\n"
          f"kwadrat pierwszej liczby: {num_1 ** 2}\n"
          f"kwadrat drugiej liczby: {num_2 ** 2}\n"
          f"pierwiastek drugiego stopnia pierwszej liczby: {num_1 ** (1/2)}\n"
          f"pierwiastek drugiego stopnia drugiej liczby: {num_2 ** (1/2)}")
elif num_2 < 0:
    num_2 = num_2 * (-1)
    print(f"summa liczb: {num_1 + num_2}\n"
          f"różnica liczb: {num_1 - num_2}\n"
          f"iloczyn liczb: {num_1 * num_2}\n"
          f"iloraz liczb: {num_1 / num_2}\n"
          f"kwadrat pierwszej liczby: {num_1 ** 2}\n"
          f"kwadrat drugiej liczby: {num_2 ** 2}\n"
          f"pierwiastek drugiego stopnia pierwszej liczby: {num_1 ** (1/2)}\n"
          f"pierwiastek drugiego stopnia drugiej liczby: {num_2 ** (1/2)}")
else:
    print(f"summa liczb: {num_1 + num_2}\n"
          f"różnica liczb: {num_1 - num_2}\n"
          f"iloczyn liczb: {num_1 * num_2}\n"
          f"iloraz liczb: {num_1 / num_2}\n"
          f"kwadrat pierwszej liczby: {num_1 ** 2}\n"
          f"kwadrat drugiej liczby: {num_2 ** 2}\n"
          f"pierwiastek drugiego stopnia pierwszej liczby: {num_1 ** (1/2)}\n"
          f"pierwiastek drugiego stopnia drugiej liczby: {num_2 ** (1/2)}")

if num_1 * num_2 == 10:
    print("Yay!")
