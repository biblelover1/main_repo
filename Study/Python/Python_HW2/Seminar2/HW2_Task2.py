# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

import math


s = int(input('Enter the sum of numbers: '))
p = int(input("Enter the result of numbers' multiplication: "))

# x = 0
# y = 0
# for x in range(s):
#     for y in range(s):
#         if x + y == s and x*y == p:
#             print(x, y)
d = s**2 + 4*p
if d < 0:
    print("There is no solution")
else:
    y1 = (s**2 - d**0.5)/2
    x1 = s - y1
    if (y1 - y1//y1) > 0 or (x1 - x1//x1) > 0 or p == 0:
        print("Numbers must be int type")
    elif x1 > 1000 or y1 > 1000:
        print("Error")
    else:
        print(int(x1), int (y1))

            

