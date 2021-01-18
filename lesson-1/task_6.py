current_distance = float(input('Введите результат за первый день (км): '))
end_distance = float(input('Введите какое расстояние необходимо преодолеть (км): '))
day = 0
while current_distance < end_distance:
    print(day, '-й день: ', "%.2f" % current_distance, ' км.')
    day += 1
    current_distance = current_distance * 1.10
print('На ', day, '-й день спортсмен достиг результата - не менее ', "%.2f" %  current_distance, ' км.')
