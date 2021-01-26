""" 1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
обработку ситуации деления на ноль."""


def my_func(dividend, divider):
    try:
        answer = dividend / divider
        print(answer)
    except ZeroDivisionError:
        print('Делитель равен нулю')


var1 = int(input('Введите делимое: '))
var2 = int(input('Введите делитель: '))
my_func(var1, var2)



