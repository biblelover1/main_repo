# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4

# Output: 1 3 3 3 1


# Variant 1:
lst1 = [int(input("Enter mark: ")) for i in range(int(input("Enter number: ")))]
print(lst1)
# max = max(lst1)
# min = min(lst1)
# lst2 = [min if i == max else i for i in lst1]

# print(lst2)
# for i in range(len(lst1)):
#     print(lst1[i])
#     if lst1[i] == max(lst1):
#         lst1[i] = min(lst1)

for i in lst1:
    print(i)
    if i == max(lst1):
        i = min(lst1)


print(lst1)