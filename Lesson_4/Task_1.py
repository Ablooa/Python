def salary():
    try:
        work_hours, pay_per_hour, bonus = float(input('Выработка в часах: ')), float(input('Ставка в час в рублях: ')), float(input('Премия в рублях: '))
        return ((work_hours * pay_per_hour) + bonus)
    except ValueError:
        return 'Неправильные входные данные! Введите число'

print(salary())
