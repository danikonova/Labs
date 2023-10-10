#Двоичные числа, не превышающие 102410 расположенные в порядке возрастания. Для каждой такой последовательности минимальное число вывести прописью.
#Вариант 21
#Никонова Дарья ИСТбд-11
max_buffer_len = 100
buffer_len = 1
work_buffer = ''
work_buffer_len = buffer_len
b = 1000000000000000000000
a1 = {0: '', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
      6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
a2 = {0: '', 1: 'десять', 2: 'двадцать', 3: 'тридцать', 4: 'сорок',
      5: 'пятьдесят', 6: 'шестьдесят', 7: 'семьдесят',
      8: 'восемьдесят', 9: 'девяносто'}
a3 = {0: '', 10: 'десять', 11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать',
      14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать',
      17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать'}
a4 = {0: '', 1: 'сто', 2: 'двести', 3: 'триста', 4: 'четыреста',
      5: 'пятьсот', 6: 'шестьсот', 7: 'семьсот', 8: 'восемьсот',
      9: 'девятьсот'}
cout = 0
with open('1.txt', mode='r') as f:
    a = f.read(buffer_len)
    if not a:
        print('\n Файл в директории проекта пустой')
        exit()
    while a:
        while '0' <= a <= '9':
            if '0' <= a <= '9':
                work_buffer += a
            a = f.read(buffer_len)
        if len(work_buffer) > 0:
            c = False
            try:
                if cout == 0:
                    cout += 1
                    b = int(work_buffer, 2)
                elif cout == 1 and b < int(work_buffer, 2) and b <= 1024:
                    c = True
                    cout += 1
                elif b < int(work_buffer, 2) and b <= 1024:
                    cout += 1
                    c = False
                    b = int(work_buffer, 2)
                else:
                    b = int(work_buffer, 2)
                    cout = 1
            except Exception:
                b = 1000000000000000000000
                work_buffer = ''
                a = f.read(buffer_len)
                continue
            if c:
                i = str(b)
                b = int(work_buffer, 2)
                dlina = len(i)
                count = 0
                while len(i) != count:
                    if dlina == 4:
                        print('одна тысяча', end=' ')
                        dlina = dlina - 1
                        count += 1
                    if dlina == 3:
                        if int(i[count]) != 0:
                            print(a4[int(i[count])], end=' ')
                        dlina = dlina - 1
                        count += 1
                    if dlina == 2 and int(i[-2]) == 1:
                        if int(i[count]) != 0:
                            print(a3[int(i[count:])], end=' ')
                        dlina = dlina - 2
                        count += 2
                    elif dlina == 2:
                        if int(i[count]) != 0:
                            print(a2[int(i[count])], end=' ')
                        dlina = dlina - 1
                        count += 1
                    if dlina == 1:
                        if int(i[count]) != 0:
                            print(a1[int(i[count])], end=' ')
                        dlina = dlina - 1
                        count += 1
                    print()
        work_buffer = ''
        a = f.read(buffer_len)
