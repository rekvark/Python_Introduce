# Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def total():
    result = 0
    s = True
    while s:
        number = input("Введите числа через пробел или #, чтобы выйти: ").split()
        prom_res = 0
        for el in range(len(number)):
            if number[el] == '#':
                s = False
                break
            else:
                prom_res = prom_res + int(number[el])
        result = result + prom_res
        print(f"Промежуточный результат: {result}")
    print(f"Итоговый результат: {result}")


total()









