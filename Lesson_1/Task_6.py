# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. 
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров. 
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
a = float(input('Введите кол-во км: '))
b = float(input('Введите кол-во км: '))
day = 1
while a<b:
    a*=1.1
    day+=1
    print(round(a, 2))
print(f'Ответ: На {day}-й день спортсмен достиг результата — не менее {b} км')
