#  Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.



# numb1 = int(input("Enter size of first list: "))
# numb1 = int(input("Enter size of second list: "))

list1 = [int(input("numb: ")) for i in range(int(input("Enter size of first list")))]
list2 = [int(input("numb: ")) for i in range(int(input("Enter size of second list")))]
set1 = set(list1)
set2 = set(list2)
res = set1.intersection(set2)
print(sorted(res))



