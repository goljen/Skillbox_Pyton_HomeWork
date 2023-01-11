print('Задача 3. Убийца Steam')

# Вы пишете программу-инсталлятор для компьютерной игры.
# Пока инсталлятор скачивает обновление,
# пользователю нужно показать сколько процентов уже скачалось,
# чтобы он мог решить пойти заварить чаю, или подождать у экрана компьютера.
# 
# Обновления игры всегда занимают разное количество мегабайт,
# да и скорость интернет-соединения у игроков разная.
# 
# Напишите программу,
# принимающую на вход размер файла обновления в мегабайтах
# и скорость интернет соединения в мегабайтах в секунду.
# 
# Для каждой секунды программа рассчитывает
# и выводит на экран сколько процентов от всего объема уже скачано,
# до тех пор пока не будет скачан весь объем.
# В конце программа должна показать сколько всего секунд заняло скачивание обновления.
# Обеспечьте контроль ввода.
# 
# Пример:
# 
# Укажите размер файла для скачивания: 123
# Какова скорость вашего соединения? 27
# 
# Прошло 1 сек. Скачано 27 из 123 Мб (22%)
# Прошло 2 сек. Скачано 54 из 123 Мб (44%)
# Прошло 3 сек. Скачано 81 из 123 Мб (66%)
# Прошло 4 сек. Скачано 108 из 123 Мб (88%)
# Прошло 5 сек. Скачано 123 из 123 Мб (100%)

import math

downloaded = 0.0

file_size = float(input('Введите размер файла обновления, Мб: '))
internet_connection_speed = float(input('Введите скорость Интернет соединения, Мб/с: '))
number_cycles = math.ceil(file_size / internet_connection_speed)
for sec in range (1, number_cycles + 1):
  downloaded = sec * internet_connection_speed
  if downloaded > file_size: downloaded = file_size
  print('Прошло %d сек.'%(sec), end = ' ')
  print('Скачано %f из %f Мб (%d'%(downloaded, file_size, round(downloaded / file_size * 100, 1)), '%)')