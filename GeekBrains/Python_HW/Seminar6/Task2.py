# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

list1 = [int(input()) for i in range(int(input("Enter number of elements: ")))]
max = int(input("Enter max number: "))
min = int(input("Enter min number: "))
for i in list1:
    if i > min and i < max:
        print(list1.index(i))