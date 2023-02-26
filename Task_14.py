# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N
max_number = int(input('Введите число до которого необходимо вывести степени числа 2: '))
number = 2
for i in range (max_number):
  if number < max_number:
    print (number, end= ', ')
    number *= 2
  else:
    break