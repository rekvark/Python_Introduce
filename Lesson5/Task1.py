#1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.


my_file = open(r'test_f1.txt', "w")
while True:
    str = input("Введите строки через Enter: \n")
    if str == '':
        break
    else:
        my_file.writelines(str + '\n')

my_file = open(r'test_f1.txt')
print(my_file.read())
my_file.close()

