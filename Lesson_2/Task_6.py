goods = {}
i = 1
while True:
    goods.append(
        (int(input('Введите ID товара: ')),
         dict({
             'название': str(input('Введите название: ')),
             'цена': float(input('Введите цену товара: ')),
             'количество': float(input('Введите кол-во товара: ')),
             'ед': str(input('Введите единицу измерения: ')),
         }))
    )
    print('Товар был успешно добавлен!')
    answer = input('Добавить еще один товар? (да/нет): ') 
    if answer == 'нет':
        break
    i +=1
print(f'Весь список товаров:{goods}')
