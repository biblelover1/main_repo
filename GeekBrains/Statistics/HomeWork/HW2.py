import math
# Задание 1: Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8.
# Стрелок выстрелил 100 раз. Найдите вероятность того, что стрелок попадет в цель ровно 85 раз.
# Первый вариант: P(X = k) = Cn(k)p^k*q^(n-k), где p = 0,8; n = 100; k = 85

P1 = (math.factorial(100)/(math.factorial(85)*math.factorial(100-85))) * \
    (0.8**85)*(0.2**(100-85))
print(f'Первый вариант: {P1}')
# Ответ 1: 0.048061793700746556

# Второй вариант: P = λ^m/m!*e^(-λ)
P1_2 = (((100*0.8)**85)/(math.factorial(85)))*(math.e**(-80))
print(f'Ответ: {P1_2}')
# Ответ 2: 0.037092614343691946

# Задание 2: Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004.
# В жилом комплексе после ремонта в один день включили 5000 новых лампочек.

                        # Какова вероятность, что ни одна из них не перегорит в первый день?

def bulb(p: float, n: int, m: int) -> float:
    P = (((n*p)**(m))/(math.factorial(m)))*(math.e**(-(n*p)))
    return P


print(f'Ответ: {bulb(0.0004, 5000, 0)}')  # Ответ: 0.1353352832366127


                                    # Какова вероятность, что перегорят ровно две?
print(f'Ответ {bulb(0.0004, 5000, 2)}')  # Ответ: 0.2706705664732254


                    # Задание 3: Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?
def bern(n, k, p):
    P3 = (math.factorial(n)/(math.factorial(k)*math.factorial(n-k))) * \
        (p**k)*((1-p)**(n-k))
    return P3


print(f'Ответ: {bern(144, 70, 0.5)}')  # Ответ: 0.06281178035144776

# Задание 4: В первом ящике находится 10 мячей, из которых 7 - белые.
# Во втором ящике - 11 мячей, из которых 9 белых. Из каждого ящика вытаскивают случайным образом по два мяча.

                                    # Какова вероятность того, что все мячи белые?


def prob(n, k, n1):
    p = (math.factorial(n)/(math.factorial(k)*math.factorial(n-k))) / (math.factorial(n1)/(math.factorial(k)*(math.factorial(n1-k))))
    return p


def all_balls_white(p1, p2):
    return p1*p2


p1 = prob(7, 2, 10)
p2 = prob(9, 2, 11)

print(f'Ответ 4: {all_balls_white(p1, p2)}')  # Ответ 4: 0.3054545454545455

                                # Какова вероятность того, что ровно два мяча белые?

# Варианты: (бб)(чч) + (бч)(бч) + (чч)(бб)

def prob_variant(n1, k1, n2, k2):
    white_ball_C = (math.factorial(n1)/(math.factorial(k1)*math.factorial(n1-k1)))
    black_ball_C = (math.factorial(n2)/(math.factorial(k2)*math.factorial(n2-k2)))
    all_combinations = (math.factorial(n1+n2)/(math.factorial(k1+k2)*math.factorial((n1+n2)-(k1+k2))))
    p = (white_ball_C * black_ball_C)/all_combinations
    return p

first_variant = prob_variant(7, 2, 3, 0)
second_variant = prob_variant(7, 1, 3, 1)
third_variant = prob_variant(7, 0, 3, 2)

variants = [first_variant, second_variant, third_variant]
def variants_mult(a, b, c):
    return a*b*c
        

print(variants_mult(first_variant,second_variant,third_variant)) #  Ответ 0.01451851851851852

                            # Какова вероятность того, что хотя бы один мяч белый?
# Если все мячи черные:
first_box_black_balls = prob(3, 2, 10)
second_box_black_balls = prob(2, 2, 11)

# 1 - вероятность, что все мячи черные
print(f'{1-(first_box_black_balls+second_box_black_balls)}') # Ответ 0.9151515151515152

