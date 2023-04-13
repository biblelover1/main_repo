# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
 
import random


num_coins = int(input('Enter number of coins: '))
a = list()
b = 0
c = 0
for i in range(num_coins):
    coins = random.randint(0, 1)
    a.append(coins)
    if coins == 1:
        b += 1
    else:
        c += 1
print(a)
if b > c:
    print(f'You have to turn minimum {c} coins to lay them by the same side')
elif b < c:
    print(f'You have to turn minimum {b} coins to lay them by the same side')
else:
    print(f"The min number of action is the equal")
