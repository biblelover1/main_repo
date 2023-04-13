# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first_numb = int(input("Enter first number: "))
count_numb = int(input("Enter count of numbers: "))
d = int(input("Enter difference: "))
alg_prog = [first_numb]
for i in range(2, count_numb+1):
    a = first_numb + (i-1)*d
    alg_prog.append(a)
print(alg_prog)