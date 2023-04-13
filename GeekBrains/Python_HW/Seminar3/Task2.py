# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
# #     -> 5

#list_1 = [i for i in range(1, int(input("Enter number: ")) + 1)]
list_1 = [1, 2, 6, 9, 10]
# print(list_1)
find_numb = int(input("Enter near number you want to find to: "))
list_1.append(find_numb)
i1 = list_1.index(find_numb)
list_1.sort()
i2 = list_1.index(find_numb)
# print(i1, i2)
if i2 == 0:
    print(list_1[i2 + 1])
elif i2 == (len(list_1) - 1):
    print(list_1[i2 - 1])
elif i2 < (len(list_1) - 1):
    res1 = list_1[i2] - list_1[i2 - 1]
    res2 = list_1[i2 + 1] - list_1[i2]
    if res1 > res2:
        print(list_1[i2 + 1])
    elif res1 < res2:
        print(list_1[i2 - 1])
    else:
        print(f"Equal: {list_1[i2 - 1]} and {list_1[i2 + 1]}")
else:
    print("Error")











    