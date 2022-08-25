# 4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'The {self.name} is going.'

    def stop(self):
        return f'\nThe {self.name} has stopped.'

    def turn(self, direction):
        return f'\nThe {self.name} has turned {direction}'

    def show_speed(self):
        return f'\nCar speed is {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nCar speed is higher than allow! Current speed is {self.speed}!'
        else:
            return f'Speed of {self.name} is normal'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nYour speed is higher than allow! Your speed is {self.speed}'
        else:
            return f'Speed of {self.name} is normal'


class PoliceCar(Car):
    pass


town = TownCar('SomeTownCar', 85, 'grey', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('right'), town.stop())

sport = SportCar('SomeSportCar', 150, 'red', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('left'), sport.stop())

work = WorkCar('SomeWorkCar', 30, 'white', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('right'), work.stop())

police = PoliceCar('SomePoliceCar', 100, 'yellow', True)
print('4:\n' + work.go(), work.show_speed(), work.turn('right'), work.stop())