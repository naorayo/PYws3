""" Задайте список из вещественных чисел.
Напишите программу, которая найдёт разницу между
максимальным и минимальным значением дробной части элементов.
"""

import math

list = input('Введи числа через пробел: ').split()
list = [float(x) for x in list]
list = [abs(x - int(x)) for x in list]
result = max(list) - min (list)

print(f'Разница между максимальным и минимальным значением дробной части: {round(result, 3)}')