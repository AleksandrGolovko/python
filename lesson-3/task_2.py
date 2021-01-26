""" 2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы. Реализовать вывод данных
о пользователе одной строкой. """


def my_func(name, surname, date_of_birth,city, email, telefon):
    kwargs = ('Имя ' + name + ', Фамилия ' + my_surname + ', Дата рождения ' + my_date_of_birth
    + ', Город проживания ' + my_city + ', Адрес электронной почты ' + my_email + ', Номер телефона ' + my_telefon)
    return kwargs


my_name = input('Введите имя: ')
my_surname = input('Введите фамилию: ')
my_date_of_birth = input('Введите дату рождения: ')
my_city = input('Введите город: ')
my_email = input('Введите адрес электронной почты: ')
my_telefon = input('Введите номер телефона: ')
print(my_func(name=my_name, surname=my_surname, date_of_birth=my_date_of_birth, city=my_city, email=my_email, telefon=my_telefon))