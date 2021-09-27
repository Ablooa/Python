import itertools

# а) итератор, генерирующий целые числа, начиная с указанного,
n = int(input("Введите целое число: "))
j = 0
for i in count(n):
    if j >=50:
        break
    j += 1
    print(i, end=' ')
    
    # б) итератор, повторяющий элементы некоторого списка, определенного заранее.
count = 0
for i in itertools.cycle([1, 2, 3, 4, 5, 6, 7]):
    if count >=50:
        break
    count += 1
    print(i, end = ' ')
