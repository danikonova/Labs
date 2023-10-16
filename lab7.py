from fractions import Fraction

class FractionPair:
    
    def __init__(self, fraction1, fraction2):
        self.fraction1 = fraction1
        self.fraction2 = fraction2
    
    def get_sum(self):
        a_num, a_den = self.fraction1.as_integer_ratio()
        b_num, b_den = self.fraction2.as_integer_ratio()
        num_sum = int(str(a_num + b_num)[-1]) + int(str(a_den + b_den)[-1])
        return num_sum

    def get_fractions(self):
        return (self.fraction1, self.fraction2)

numbers = [3, 5, 7, 11, 13, 17]
fractions = set()

# Генерация всех дробей и добавление их во множество fractions
for i in range(len(numbers)):
    for j in range(len(numbers)):
        fractions.add(Fraction(numbers[i], numbers[j]))
        fractions.add(Fraction(numbers[j], numbers[i]))
        fractions.add(Fraction(numbers[i], numbers[i]))
        fractions.add(Fraction(numbers[j], numbers[j]))

fraction_pairs = []

# Итерация по всем возможным комбинациям дробей из fractions
fractions_list = list(fractions)
for i in range(len(fractions_list)):
    for j in range(i + 1, len(fractions_list)):
        a = fractions_list[i]
        b = fractions_list[j]
        a_num, a_den = a.as_integer_ratio()
        b_num, b_den = b.as_integer_ratio()
        if ((a_num + b_num) % 2 == 0) and ((a_den + b_den) % 2 == 0):
            num_sum = int(str(a_num + b_num)[-1]) + int(str(a_den + b_den)[-1])
            if num_sum % 5 == 0:
                fraction_pairs.append(FractionPair(a, b))

# Поиск пары дробей с максимальной суммой
max_sum = max([pair.get_sum() for pair in fraction_pairs])
max_fraction_pairs = [pair for pair in fraction_pairs if pair.get_sum() == max_sum]

print('Максимальная сумма:', max_sum)
for pair in max_fraction_pairs:
    print(pair.get_fractions())
