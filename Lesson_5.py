# 1
with open(r'C:\Users\12345\my_new_file.txt', 'w') as file_obj:
    users_text = input('Введите текст: ')
    while users_text:
        file_obj.write(users_text)
        users_text = input('Введите текст: ')
        if not users_text:
            break

with open(r'C:\Users\12345\my_new_file.txt', 'r') as file_obj:
    content = file_obj.readlines()
    print(content)
    
    
# 2
with open(r'C:\Users\12345\task_2.txt', 'r') as file_obj:
    content = file_obj.readlines()
    for i in range (len(content)):
         print(f"Строка: {i + 1}, кол-во символов: {len(content[i])}")
        
        
        
# 3
with open(r'C:\Users\12345\my_file_salary.txt', 'r') as my_file:
    salary = []
    small_salary = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           small_salary.append(i[0])
        salary.append(i[1])
print(f'Средний оклад: {sum(map(int, salary)) / len(salary)}')
print(f'Оклад < 20к: {small_salary}')



# 4
with open (r'C:\Users\12345\test_file.txt', 'r+',  encoding='utf-8') as file_obj:
    content = file_obj.read().split('\n')
    print(content)
    dictionary = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
    new_file = []
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)
    
with open('test_file_new.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)
    
    
    
# 5
def sum_numbers():    
    try:
        with open(r'C:\Users\12345\task_5.txt', 'w') as file_obj:
            line = input('Введите числа: ')
            file_obj.writelines(line)
            numbers = line.split()
            print(sum(map(int, numbers)))
    except ValueError:
        print('Необходимо ввести числа!')

sum_numbers()



# 6
def subjects():
    dictionary = {}
    with open(r'C:\Users\12345\task_6.txt', encoding='utf-8') as file_obj:
        for line in file_obj:
            subject, hours = line.split(':')
            name_sum = sum(map(int, ''.join([i for i in hours if i == ' ' or ('0' <= i <= '9')]).split()))
            dictionary[subject] = name_sum
        print(f"{dictionary}")

subjects()



# 7
import json

with open(r'C:\Users\12345\task_7.txt', 'r+', encoding='utf-8') as file_obj:
    result = []
    profit, average_profit = {}, {}
    average_int, profit_int, i = 0, 0, 3
    for line in file_obj:
        name, firm, income, costs = line.split()
        total = int(income) - int(costs)
        if total >= 0:
            profit_int = profit_int + total
        else:
            i -= 1
        profit[name] = total
    statistics.append(profit)
    if i != 0:
        (average_int) = prof / i
        average_profit['average_profit'] = round(average_int)
        result.append(average_profit)
    else:
        print('Компании в списке убыточные')
    print(result)
with open('file.json', 'a+', encoding='utf-8') as json_file:
    json.dump(statistics, json_file)
