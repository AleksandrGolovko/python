""" 3. Реализовать функцию my_func(), которая принимает
три позиционных аргумента, и возвращает сумму наибольших двух аргументов. """


def my_func(a, b, c):
    for el in (a, b, c):
        if min(a, b, c) < el < max(a, b, c):
            return max(a, b, c) + el


var1 = int(input('Введите первое число: '))
var2 = int(input('Введите второе число: '))
var3 = int(input('Введите третье число: '))
print(my_func(var1, var2, var3))
