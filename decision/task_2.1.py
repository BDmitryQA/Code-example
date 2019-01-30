import calendar
import datetime
from datetime import date

# Вариант 1
def black_days():

    # Создаем список и определяем границы поиска
    fridays = []
    now = datetime.datetime.now()
    years = [y for y in range(now.year, now.year+100)]

    # Перебираем каждый год в поисках нужной даты
    for year in years:
        if len(fridays) != 10:
            for month in range(1, 13):
                _, days_in_month = calendar.monthrange(year, month)
                for day in range(1, days_in_month + 1):
                    weekday = calendar.weekday(year, month, day)
                    if weekday == 4 and day == 13:
                        # Перед записью проверяем что искомая дата новее текущей
                        friday_date = date(year, month, day)
                        current_date = now.date()
                        if friday_date > current_date :
                            fridays.append(date(year, month, day))
        # Останавливаем поиск когда найдено 10 дат
        elif len(fridays) == 10:
            print('Ближайшие 10 пятниц 13 будут: ')
            print(str(fridays).replace('[', '').replace(']', '').replace('datetime.date', ''))
            break

# Вариант 2
def black_days_2():

    # Создаем список дат, определяем текущее время
    fridays = []
    now = datetime.datetime.now()

    # Перебериаем каждую дату в поисках искомой, до нахождения 10 дат
    while len(fridays) < 10:
        now += datetime.timedelta(days=1)
        weekday = calendar.weekday(now.year, now.month, now.day)
        if weekday == 4 and now.day == 13:
            fridays.append(now)

    print('Ближайшие 10 пятниц 13 будут: ')
    print(str(fridays).replace('[', '').replace(']', '').replace('datetime.date', ''))

if __name__ == '__main__':
    black_days()
    # black_days_2
