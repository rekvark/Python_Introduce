# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов.

def my_func(x, y, z):
    a = [x, y, z]
    a.sort(reverse=True)
    print(sum(a[:2]))


my_func(int(input("Введите первое число:")), int(input("Введите второе число:")), int(input("Введите третье число:")))




