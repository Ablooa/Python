# Задание 1

from datetime import date

class Date:
    def __init__(self, dd_mm_yy):
        self.dd_mm_yy = dd_mm_yy.split('-')
        
    @classmethod
    def date_int(cls, dd_mm_yy):
        try:
            dd, mm, yy = [int(i) for i in dd_mm_yy.split('-')]
            return dd, mm, yy
        except ValueError:
            return 'Указана некорректная дата!'
    
    @staticmethod
    def date_valid(dd_mm_yy):
        try:
            day, month, year = dd_mm_yy.split('-')
            date(int(year), int(month), int(day))
            return 'Дата существует'
        except ValueError:
            return 'Указана некорректная дата!'
    
    
test_date = Date('25-02-2015')
print(test_date.date_valid('29-06-2036'))
print(test_date.date_int('29-06-2036'))

#-----------------------------------------------------------------------------------------------------



# Задание 2

class Exception:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def division(x, y):
        try:
            return f'Частное = {x/y}'
        except ZeroDivisionError:
            return 'Деление на 0 запрещено'
        
print(Exception.division(int(input('Введите делимое: ')), int(input('Введите делитель: '))))
#-----------------------------------------------------------------------------------------------------




# Задание 3
class Exception_2:
    def number(my_string):
        while True:
            my_string = input('Введите строкку или stop для остановки цикла: ')
            if my_string == 'stop':
                break
            else:
                new_list = []
                for i in my_string:
                    if i.isnumeric() == True:
                        new_list.append(i)
                print(new_list)
    
Exception_2.number('text')
#-----------------------------------------------------------------------------------------------------




# Задание 4 - 6
class Wharehouse:

    def __init__(self, name, price, quantity, index, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.index = index
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    def reception(self):
        try:
            unit = input(f'Введите наименование ')
            unit_p = int(input(f'Введите цену за ед '))
            unit_q = int(input(f'Введите количество '))
            unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Текущий список -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных'

        e = input(f'Записать еще один товар? Да/Нет')
        if e == 'Нет' or e == 'нет':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
            return f'Выход'
        else:
            return Wharehouse.reception(self)


class Printer(Wharehouse):
    def do_print(self):
        return f'to print smth {self.index} times'


class Scanner(Wharehouse):
    def do_scan(self):
        return f'to scan smth {self.index} times'


class Copier(Wharehouse):
    def do_copy(self):
        return f'to copier smth  {self.index} times'


unit_1 = Printer('HP', 4000, 4, 10)
unit_2 = Scanner('Canon', 3500, 2, 7)
unit_3 = Copier('Pantum', 6500, 1, 5)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.do_print())
print(unit_2.do_scan())
print(unit_3.do_copy())
#-----------------------------------------------------------------------------------------------------




# Задание 7
class ComplexNumber:
    
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
    
    def __add__(self, other):
        print(f'Сумма c_1 и c_2 равна')
        return f'c = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение c_1 и c_2 равно')
        return f'c = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'c = {self.a} + {self.b} * i'


c_1 = ComplexNumber(1, -3)
c_2 = ComplexNumber(3, 4)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)
