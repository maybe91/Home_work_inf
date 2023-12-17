def rozbicie_liczby(suma, list=[]):
    if suma < 0:
        raise ValueError("Numbers must be pozitive")
    if type(suma) != int:
        raise TypeError("Suma mast have integer type")
    if suma == 0:
        print(*list)
    else:
        for i in range(1, suma + 1):
            if not list:
                rozbicie_liczby(suma - i, list+[i])
            elif list[-1] >= i:
                rozbicie_liczby(suma - i, list + [i])


rozbicie_liczby(1)
