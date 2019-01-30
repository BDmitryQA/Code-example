from bisect import bisect
from datetime import datetime
from collections import namedtuple

# Периоды влияния знаков задиака
zodiacs = [(1,20,"Capricorn"), (2,18,"Aquarius"), (3,20,"Pisces"), (4,20,"Ari"),
     (5,21,"Taurus"), (6,21,"Gemini"), (7,22,"Cancer"), (8,23,"Leo"),
     (9,23,"Virgo"), (10,23,"Libra"), (11,22,"Scorpion"), (12,22,"Sagittarius"),
     (12,31,"Capricorn")]

age_zodiac = namedtuple('zodiac_age', ['age', 'zodiac'])

def zodiac_sign(date):

    date = datetime.strptime(date, "%d-%m-%Y")

    d= date.day
    m= date.month
    y= date.year

    # Расчет даты рождения
    today = date.today()
    age = today.year - y - ((today.month, today.day) < (m, d))
    print("Ваш возраст - " +str(age))

    # Сравнение даты рождения с периодом влияния знака зодиака
    zodiac = zodiacs[bisect(zodiacs, (m, d))][2]
    print("Ваш знак зодиака - "+zodiac)

    return age_zodiac(age, zodiac)

if __name__ == '__main__':
    print('Введите дату рождения в формате день-месяц-год (01-01-1970): ')
    zodiac_sign(input())
