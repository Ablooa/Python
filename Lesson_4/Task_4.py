my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
unique_elements = [i for i in my_list if my_list.count(i)== 1]
print(unique_elements)