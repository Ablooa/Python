#Вариант 1
def my_func(x, y):
    if x <= 0:
        print('X должен быть больше 0')
    elif y >= 0:
        print('У должен быть меньше 0')
    else:
        return x ** y
    
my_func(3, -3)

#Вариант 2
def my_func(x, y):
    if x <= 0:
        print('X должен быть больше 0')
    elif y >= 0:
        print('У должен быть меньше 0')
    else:
        result = 1
        while y < 0:
            result *= x
            y += 1
        result = 1 / result
        return result
    
my_func(3, -3)
