# 1
#____________________________________________________________________________

import itertools       
import time

class TrafficLight:

    def running(self):
        print('Включено!')

        for i in itertools.cycle(['Красный', 'Желтый', 'Зеленый']):
            if i == 'Красный':
                print(f'Сигнал светофора: {i}')
                time.sleep(7)
            if i == 'Желтый':
                print(f'Сигнал светофора: {i}')
                time.sleep(2)
            if i == 'Зеленый':
                print(f'Сигнал светофора: {i}')
                time.sleep(7)

        while True:
            self.running()


traffic_light = TrafficLight()
print(traffic_light.running())  


# 2
#____________________________________________________________________________

class Road:
    
    __mass = 25
    __depth = 0.05
    
    def __init__(self, width, length):
        self._length = length
        self._width = width        
        
    def asphalt_mass(self):
        return self._length * self._width * self.__asphalt * self.__depth
        
total = Road(20, 5000)
print(mass.asphalt_mass())

# 3
#____________________________________________________________________________

class Worker:
     
        def __init__(self, name, surname, position, wage, bonus):
            self.name = name
            self.surname = surname
            self.position = position
            self._income = {"wage": int(wage), "bonus": int(bonus)}

            
class Position(Worker):
    
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


person_1 = Position('Ivav', 'Ivanov', 'DS', '110000', '25000')
print(person_1.get_full_name(), person_1.get_total_income())

# 4
#____________________________________________________________________________

class Car:

    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = bool(is_police)

    def go(self):
        return f'начал движение'

    def stop(self):
        return f'остановился'

    def turn_right(self):
        return f'повернул направо'

    def turn_left(self):
        return f'повернул налево'

    def show_speed(self):
        return self.speed

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'превысил скорость'
        else:
            return self.speed

class SportCar(Car):
    def sport_car(self):
        return f'- спортивный автомобиль'

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'превысил скорость'
        else:
            return self.speed

class PoliceCar(Car):
    def ispolice(self):
        if self.is_police is True:
            return "- полицейский автомобиль"

hyundai = TownCar("Hyundai", "Blue", 90, False)
kamaz = WorkCar("Kamaz", "Black", 40, False)
lamborghini  = SportCar("Lamborghini ", "Red", 150, False)
lada = PoliceCar("Lada", "White", 110, True)

print(f'Марка городского авто: {hyundai.name}.\nЦвет рабочей машины: {kamaz.color}. \nСкорость спортивного авто: {lamborghini.speed}км/ч.\nЛада - полицейский автомобиль: {lada.is_police}.')
print(f'Mazda {hyundai.show_speed()} и {hyundai.stop()}.')
print(f'Kamaz {kamaz.turn_right()} и текущая скорость {kamaz.show_speed()} км/ч.')
print(f'Lada {lada.ispolice()}.')
print(f'Lamborghini {lamborghini.sport_car()}.\nLamborghini {lamborghini.go()} и {lamborghini.turn_left()}.')


# 5
#____________________________________________________________________________

class Stationery:
    
    def __init__(self, title):
        self.title = title

    def draw(self):
        f'Запуск отрисовки.'
        

class Pen(Stationery):
    
    def draw(self):
        return f'Первый инструмент: {self.title}'
    
    
class Pencil(Stationery):
    
    def draw(self):
        return f'Второй инструмент: {self.title}'
    
    
class Handle(Stationery):
    
    def draw(self):
        return f'Третий инструмент: {self.title}'

pen = Pen("Ручка")
pencil = Pencil("Карандаш")
handle = Handle("Маркер")
print(pen.draw())
print(pencil.draw())
print(handle.draw())
