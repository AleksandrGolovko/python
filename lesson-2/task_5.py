a = int(input('Введите число: '))
my_list = [7, 5, 3, 3, 2]
z = 1
for el in my_list:
    # if int(len(my_list)) >= z:
    #     print(len(my_list) > z, el < a)
    if el <= a:
        my_list.insert(z-1, a)
        break
    elif len(my_list) == z:
        my_list.append(a)
        break
    z += 1
print(my_list)
