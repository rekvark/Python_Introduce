# Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].

rt = [7, 5, 3, 3, 2]
new_num = int(input("Введите число: "))
value_list = [value for i, value in enumerate(rt)]

if new_num > max(rt):
    rt.insert(0, new_num)
    print(rt)

elif new_num < min(rt):
    rt.append(new_num)
    print(rt)

elif new_num != value_list:
     in_list = [i for i, value in enumerate(rt) if value > new_num]
     new_ind = max(in_list) + 1
     rt.insert(new_ind, new_num)
     print(rt)

else:
    in_list1 = [i for i, value in enumerate(rt) if value == new_num]
    new_ind1 = max(in_list1) + 1
    rt.insert(new_ind1, new_num)
    print(rt)