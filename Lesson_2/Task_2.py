my_list = list(input("Введите элементы списка: "))
index = 0
for i in range(int(len(my_list)/2)):
    my_list[index], my_list[index+1] = my_list[index+1], my_list[index]
    index += 2
print(my_list)
