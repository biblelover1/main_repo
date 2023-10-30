# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n

# str = "a b a b c a d d a c"
# str = str.split()
# for i in str:
#     count = 0
#     for j in str[i+1]:
#         if i == j:
#             count += 1
#             j = f'{j}_{count}'
#             print(j)

sp = input().split()
result = {}
for i in sp:
    if i in result:
        print(f'{i}_{result[i]}', end=' ')
    else:
        print(i, end=' ')
    result[i] = result.get(i, 0) + 1
    print('!', result[i])


