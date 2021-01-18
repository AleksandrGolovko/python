sec = int(input('Введите время в секундах: '))
sec1 = sec % 60 % 60
min1 = sec // 60 % 60
hour1 = sec // 3600
print(f'{hour1:0{2}}', ':',
      f'{min1:0{2}}', ':',
      f'{sec1:0{2}}')
