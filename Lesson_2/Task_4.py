my_str = input('Введите строку: ')
my_list = my_str.split()
for index, element in enumerate(my_list):
    if len(element)>9:
        print(index, element[:9])
    else:
        print(index, element) 
