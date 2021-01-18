sales = int(input('Введите размер выручки:'))  # выручка
costs = int(input('Введите размер издержек:'))  # издержки
if sales > costs:
    profitability = sales - costs  # рентабильность
    workers = int(input('Введите количество сотрудников :'))  # работники
    print('Выручка на одного сотрудника: ', "%.2f" % (profitability / workers))
else:
    print('У вас издержки превышают выручку')