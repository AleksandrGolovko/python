my_str = input('Введите строку из нескольких слов: ')
my_list = my_str.split(' ')
for ind, el in enumerate(my_list, 1):
    print(ind, el[:10])
