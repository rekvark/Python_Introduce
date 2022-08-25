# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker():

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus  #бонус задаём в % от оклада
        self._income = {'wage': self.wage, 'bonus':  self.wage * self.bonus / 100}


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


worker = Position('Иван', 'Иванов', 'электромонтер', 1000, 25)
print('Полное имя:', worker.get_full_name())
print('Должность:', worker.position)
print('Оклад, руб.:', worker.wage)
print('Размер премии, %:', worker.bonus)
print('Размер дохода, руб.:', worker.get_total_income())