# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

num = int(input("Enter number: "))
a = 2
i = 2
sum=2
for i in range(2, 100):
    sum = sum*a
    if sum < num:
        print(f"{i}:{sum}")
    else:
        break