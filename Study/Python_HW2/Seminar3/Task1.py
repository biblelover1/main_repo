# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

list_1 = [i for i in range(1, int(input("Enter number: ")) + 1)]
find_numb = int(input("Enter number you want to find: "))
# Variant 1

# count = 0
# for i in list_1:
#     if i == find_numb:
#         count += 1
# print(count)

#Variant 2

print(list_1.count(find_numb))