my_list = list(input('Введите список: '))
i = 0
for el in my_list:
    if i+1 < len(my_list):
        my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
        i += 2
    else:
        break
print(my_list)
