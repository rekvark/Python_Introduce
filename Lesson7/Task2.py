# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда,
# которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
# параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы
# для основных классов проекта, проверить на практике работу декоратора @property.


from abc import ABC, abstractmethod


class AbsCloth(ABC):
    @abstractmethod
    def calc_consumption_coat(self):
        pass

    @abstractmethod
    def calc_consumption_costume(self):
        pass

    def calc_consumption_total(self):
        pass


class Clothes(AbsCloth):
    def __init__(self, v, h):
        self.v = v
        self.h = h
        self.consumption_coat = self.v / 6.5 + 0.5
        self.consumption_costume = self.h * 2 + 0.3

    def calc_consumption_coat(self):
        return str(f'Расхода ткани на пальто: {self.consumption_coat:.2f} кв.м')

    def calc_consumption_costume(self):
        return str(f'Расхода ткани на костюм: {self.consumption_costume:.2f} кв.м')

    @property
    def calc_consumption_total(self):
        return str(f'Общий расход ткани: {self.consumption_coat + self.consumption_costume:.2f} кв.м')


clothes = Clothes(52, 1.8)

print(clothes.calc_consumption_coat())
print(clothes.calc_consumption_costume())
print(clothes.calc_consumption_total)
