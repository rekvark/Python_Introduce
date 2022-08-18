#6. Реализовать два небольших скрипта:
#а) итератор, генерирующий целые числа, начиная с указанного,
#б) итератор, повторяющий элементы некоторого списка, определенного заранее.
#
#Подсказка: использовать функцию count() и cycle() модуля itertools.
#Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
#Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
#Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count
from itertools import cycle


def count_func(start_number, stop_number):
    for el in count(start_number):
        if el > stop_number:
            break
        else:
            print(el)


def cycle_func(iter_list, iteration):
    i = 0
    iter = cycle(iter_list)
    while i < iteration:
        print(next(iter))
        i+=1


count_func(start_number=int(input("Введите начальное число: ")), stop_number=int(input("Введите конечное число: ")))
cycle_func(iter_list=[1, 2, 3, 4], iteration=int(input("Введите количество итераций: ")))
