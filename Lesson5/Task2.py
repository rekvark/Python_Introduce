#2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
import re
with open('test_f2.txt') as myfile:
    cont = myfile.readlines()
    print(f'Количество строк в файле: {len(cont)}')

with open('test_f2.txt') as myfile:
    i = 1
    lines = myfile.readlines()
    for line in lines:
        words = (len(re.findall(" ", line)) + 1)
        print(f'Количество слов встроке {i}: {words}')
        i += 1

