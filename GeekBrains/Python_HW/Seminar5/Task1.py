numb1 = int(input("Enter number 1: "))
numb2 = int(input("Enter number 2: "))

def degree(numb1, numb2):
    if numb2 == 0:
        return 1
    return numb1 * degree(numb1, numb2 - 1)

print(degree(numb1, numb2))