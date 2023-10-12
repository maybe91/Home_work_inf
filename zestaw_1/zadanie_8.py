import random
num = int(input("Wpisz liczbę: "))
stump = num
star = 3

list = ['*', '*', 'o']
print((' ' * (num-1)) + 'X')

while num-2 >= 0:
    print(' ' * (num-2), end='')
    random.shuffle(list)
    for i in range(0, star):
        print(list[i], end='')
    print('')
    list.append('*')
    list.append('*')
    star += 2
    num -= 1

print((' ' * (stump-1)) + 'U')
