def fact(n):
    i, j = 1, 1
    for el in range(n):
        while i <= n:
            j *= i
            i += 1
            yield j

n = int(input('Введите число: '))
for el in fact(n):
    print(el)
