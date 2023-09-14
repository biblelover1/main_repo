from math import factorial as f, sqrt

# Даны значения зарплат из выборки выпускников: 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150. Посчитать (желательно без использования статистических методов наподобие std, var, mean) среднее арифметическое, среднее квадратичное отклонение, смещенную и несмещенную оценки дисперсий для данной выборки.

salaries = [100, 80, 75, 77, 89, 33, 45, 25, 65,
            17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]


def mean(ls):
    sum = 0
    for i in range(len(ls)):
        sum += ls[i]
    mean_val = sum/len(ls)
    return mean_val


res = mean(salaries)
print(f'Среднее арифметическое: {res}')


def dispersion(ls, mean_value):
    sum = 0
    res = 0
    for i in range(len(ls)):
        res = pow((ls[i] - mean_value), 2)
        sum += res
    displaced_disp = sum/len(ls)
    sample_dispersion = sum/(len(ls)-1)
    return displaced_disp, sample_dispersion


disp_displaced, disp_sample = dispersion(salaries, res)
print(
    f'Смещенная дисперсия: {round(disp_displaced, 2)}\nНесмещенная дисперсия: {round(disp_sample, 2)}')


def standard_deviation(std_displaced_disp):
    return sqrt(std_displaced_disp)


std = standard_deviation(disp_sample)
print(f"Std: {round(std, 2)}")


# Задача 2. В первом ящике находится 8 мячей, из которых 5 - белые. Во втором ящике - 12 мячей, из которых 5 белых. Из первого ящика вытаскивают случайным образом два мяча, из второго - 4 мяча. Какова вероятность того, что 3 мяча белые?
# 1 variant: (1 and 2)
# 2 variant: (2 and 1)
# 3 variant: (0 and 3)
def prob_variant(n1, k1, n2, k2):
    white_ball_C = (f(n1)/(f(k1)*f(n1-k1)))
    black_ball_C = (f(n2)/(f(k2)*f(n2-k2)))
    all_combinations = (f(n1+n2)/(f(k1+k2)*f((n1+n2)-(k1+k2))))
    p = (white_ball_C * black_ball_C)/all_combinations
    return p


first_variant_1box = prob_variant(5, 1, 3, 1)
second_variant_1box = prob_variant(5, 2, 3, 0)
third_variant_1box = prob_variant(5, 0, 3, 2)

first_variant_2box = prob_variant(5, 2, 7, 2)
second_variant_2box = prob_variant(5, 1, 7, 3)
third_variant_2box = prob_variant(5, 3, 7, 1)


def variants_mult(a, b):
    return a*b


res1 = variants_mult(first_variant_1box, first_variant_2box)
res2 = variants_mult(second_variant_1box, second_variant_2box)
res3 = variants_mult(third_variant_1box, third_variant_2box)


def sum_prob(a, b, c):
    return a+b+c


print(f"answer is: {round(sum_prob(res1, res2, res3), 2)}")

# Задача 3. На соревновании по биатлону один из трех спортсменов стреляет и попадает в мишень. Вероятность попадания для первого спортсмена равна 0.9, для второго — 0.8, для третьего — 0.6. Найти вероятность того, что выстрел произведен: a). первым спортсменом б). вторым спортсменом в). третьим спортсменом.
P = ((1/3)*0.9) + ((1/3)*0.8) + ((1/3)*0.6)
p1 = ((1/3)*0.9)/P
p2 = ((1/3)*0.8)/P
p3 = ((1/3)*0.6)/P

print(f"Task3\nAnswer 1: {p1}\nAnswer 2: {p2}\nAnswer 3: {p3}")

# Задача 4. В университет на факультеты A и B поступило равное количество студентов, а на факультет C студентов поступило столько же, сколько на A и B вместе. Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8. Для студента факультета B эта вероятность равна 0.7, а для студента факультета C - 0.9. Студент сдал первую сессию. Какова вероятность, что он учится: a). на факультете A б). на факультете B в). на факультете C?

# A = B = x
# C = 2x
com_prob = ((1/4)*0.8)+((1/4)*0.7)+((1/2)*0.9)
A_faculty = ((1/4)*0.8)/com_prob
B_faculty = ((1/4)*0.7)/com_prob
C_faculty = ((1/2)*0.9)/com_prob

print(
    f"Task 4\nFaculty A: {A_faculty}\nFaculty B: {B_faculty}\nFaculty C: {C_faculty}")

# Задача 5. Устройство состоит из трех деталей. Для первой детали вероятность выйти из строя в первый месяц равна 0.1, для второй - 0.2, для третьей - 0.25. Какова вероятность того, что в первый месяц выйдут из строя: а). все детали б). только две детали в). хотя бы одна деталь г). от одной до двух деталей?
# a
details_prob = 0.1*0.2*0.25
print(f'Task A: {details_prob}')  # 0.005
# b Р - работает; С - сломано (РСС, СРС, ССР)
two_details = 0.9*0.2*0.25 + 0.1*0.8*0.25 + 0.1*0.2*0.75
print(f"Two details: {two_details}")  # 0.08

# c
atLeast_one_detail = 1 - (0.9*0.8*0.75)
print(f'Task c: {atLeast_one_detail}')  # 0.46

# d One detail (РРС + РСР + СРР)
from1_toTwo = ((0.9*0.8*0.25+0.9*0.2*0.75+0.1*0.8*0.75)+two_details)
print(f'Task d: {from1_toTwo}')  # 0.54
