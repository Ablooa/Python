def user_info(**kwargs):
    print(f"Пользователь {kwargs['name']} {kwargs['surname']} родился в {kwargs['birth_year']} году, проживает в городе {kwargs['city']}. Контактные данные: почта: {kwargs['email']}, телефон: {kwargs['tel']}.")
    
user_info(name = 'Иван', surname = 'Иванов', birth_year = 1999, city = 'Москва', email = 'iivanov@mail.ru', tel = '88005553535')
