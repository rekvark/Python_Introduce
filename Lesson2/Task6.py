# * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами,
# то есть характеристиками товара: название, цена, количество, единица измерения.
# Структуру нужно сформировать программно, запросив все данные у пользователя.
# Пример готовой структуры:
#
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
#
# Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например, название.
# Тогда значение — список значений-характеристик, например, список названий товаров.
# Пример:
#
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }


quest1 = input("Добавить данные? Введите да, если добавить или любое иное, если не добавлять ")
list_common = []  # создаем пустой "общий" список, в который будем складировать данные введёные пользователем
i = 0  # переменная для нумерации позиций в кортеже
list_item = []  # пустой список для "аналитики" наименований
list_price = []  # пустой список для "аналитики" цен
list_quan = []  # пустой список для "аналитики" количества
list_unit = []  # пустой список для "аналитики" единиц измерения
while quest1 == "да":  # создаём цикл для введения данных по товарам
    i = i + 1
    item = input("Введите наименование: ")
    list_item.append(item)  # добавляем в соответсвующий список введёное наименование для "аналитики"
    price = input("Введите цену: ")
    list_price.append(price)  # добавляем в соответсвующий список введёную цену для "аналитики"
    quan = input("Введите количество: ")
    list_quan.append(quan)  # добавляем введёное в соответсвующий список количество для "аналитики"
    unit = input("Введите единицу измерения: ")
    list_unit.append(unit)  # добавляем в соответсвующий список введёное наименование для "аналитики"
    dict = {'название' : item, 'цена' : price, 'количество' : quan, 'единицы' : unit}  # создаём словарь для дальнейшего добавления в кортеж введёных данных
    dict_an = {'название': list_item, 'цена': list_price, 'количество': list_quan, 'единицы': list_unit}  # создаём словарь для "аналитики" на основе составленных списков "аналитики"
    cort = (i, dict)
    list_common.append(cort)  # создаем список товаров на основе введёных данных
    quest1 = input("Вы хотите добавить данные? Введите да, если добавить или любое иное, если не хотите добавлять ")
else:
    if len(list_common) == 0:
        print("Нет данных для вывода")
    else:
        quest2 = input("Вывести аналитику по товарам? Введите да или нет: ")
        if quest2 == "нет":
            print("Ваш итоговый список:")
            for x in list_common:
                print(f" \n {x}")
        else:
            for key, val in dict_an.items():  # формируем и выводим аналитику на основе созданного в цикле словаря dict_an
                print(key, ':', val)







