""" Задайте список из нескольких чисел. Напишите программу,
которая найдёт сумму элементов списка, стоящих на нечётной позиции.
"""

from functools import reduce

list = input('Введи числа через пробел: ').split()
list = [int(x) for x in list]
sum = reduce(type(list[0]).__add__, list[1::2])
list[list.index(min(list))], list[list.index(max(list))] = max(list), min(list)

print(f'{list}\nСумма элементов на нечётной позиции: {sum}')