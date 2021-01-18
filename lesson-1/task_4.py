num = input('Введите число ')
c = 0  # Самое большое число
a = 0  # Счетчик
z = len(num)
while a < z:
    b = int(num[a])
    if c < b:
        c = b
    a += 1
print(c)

