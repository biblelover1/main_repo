# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива

# Variant1
# list1 = [int(input()) for i in range(int(input("Enter number of elements in list1: ")))]
# list2 = [int(input()) for i in range(int(input("Enter number of elements in list1: ")))]
# list3 = []
# for i in list1:
#     if i not in list2:
#         list3.append(i)
# print(*list3)

# Variant2

# list1 = [int(input()) for i in range(int(input("Enter number of elements in list1: ")))]
# list2 = [int(input()) for i in range(int(input("Enter number of elements in list1: ")))]
# set1 = set(list1)
# set2 = set(list2)
# print(*set1.difference(set2))
