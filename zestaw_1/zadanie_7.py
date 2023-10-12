start = int(input("Wpisz początek ciągu: "))
stop = int(input("Wpisz koniec ciągu: "))

if stop - start > 19 and (stop - start) % 2 == 0:
    ave_num = (stop + start) // 2
    for i in range(1, 4):
        print(f"{ave_num + i}, {ave_num - i}")
elif stop - start > 19 and (stop - start) % 2 != 0:
    ave_num = (stop + start) // 2
    for i in range(1, 4):
        print(f"{ave_num + i + 1}, {ave_num - i}")
else:
    for i in range(start, stop+1):
        print(i)
