# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень). Решение через list.

my_date = input("введите номер меясца ")
my_year = ['12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']

i = str(my_date)

if i in my_year[1:3:1]:
    print("зима")

elif i in my_year[3:6:1]:
    print("весна")

elif i in my_year[6:9:1]:
    print("лето")

elif i in my_year[9:12:1]:
    print("осень")

else:
    print("в году 12 месяцев и да, их значение не может быть отрицательным или 0")
