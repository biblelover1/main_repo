

def sum(a, b):
    if b == 0:
        return a
    return a + sum(1, b - 1)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(sum(a, b))