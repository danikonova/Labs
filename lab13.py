'''
21.	Определить количество взрослых(=>18) на борту в возрастном 
интервале медиана +- 5 позиций и сколько из них выжило
'''
import csv

# Открываем файл
with open('titanic.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)

    adult_count = 0
    survived_count = 0

    adult_ages = []

 
    for row in csv_reader:
        age = row[5]
        if age.isdigit():
            age = int(age)
             # Проверяем, является ли пассажир взрослым
            if age >= 18:
                adult_count += 1
                adult_ages.append(age)
                # Проверяем, выжил ли пассажир
                if int(row[1]) == 1:
                    survived_count += 1

    # Сортируем массив возрастов взрослых пассажиров
    adult_ages.sort()

    # Вычисляем медиану возрастов взрослых пассажиров
    median = adult_ages[len(adult_ages) // 2]

    # Определяем диапазон возрастов, включающий медиану +/- 5 позиций
    age_start = median - 5
    age_end = median + 5

    # Выводим результаты
    print("Количество взрослых пассажиров в заданном возрастном интервале:", adult_count)
    print("Количество выживших взрослых пассажиров в заданном возрастном интервале:", survived_count)
    print("Медиана возрастов взрослых пассажиров:", median)
    print("Диапазон возрастов, включающий медиану +/- 5 позиций:", age_start, "-", age_end)