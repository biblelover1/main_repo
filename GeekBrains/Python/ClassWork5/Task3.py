numb = int(input("Enter number: "))
# count = 0
# for i in range(1, numb):
#     res = numb % i
#     if res == 0:
#         count += 1
# if count > 2:
#     print("no")
# else:
#     print("yes")

def check(num):
    for i in range(2, numb):
        return numb % i == 0    
print(check(numb))
