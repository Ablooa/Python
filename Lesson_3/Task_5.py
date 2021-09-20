# Специальный символ: любое не int значение
def sum_calc(*nums):
    sum = 0
    special_symbol = False
    for num in nums:
        try:
            if num:
                sum += float(num)
        except ValueError:
            special_symbol = True
    return sum, special_symbol

total_sum = 0

while True:
    numbers_string = input('Введите числа: ').split()
    sum, stop = sum_calc(*numbers_string)
    total_sum += sum
    print(f'Сумма = {total_sum}')

    if stop:
        break
