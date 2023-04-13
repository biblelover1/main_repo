# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются 
# так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; 
# J, X – 8 очков; Q, Z – 10 очков. 
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; 
# Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, 
# либо только русские буквы.

# *Пример:*

# ноутбук
#     12


dictEng_1 = dict.fromkeys(['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'], 1)
dictEng_2 = dict.fromkeys(['D', 'G'], 2)
dictEng_3 = dict.fromkeys(['B', 'C', 'M', 'P'], 3)
dictEng_4 = dict.fromkeys(['F', 'H', 'V', 'W', 'Y'], 3)
dictEng_5 = dict.fromkeys('K', 5)
dictEng_6 = dict.fromkeys(['J', 'X'], 8)
dictEng_7 = dict.fromkeys(['Q', 'Z'], 10)
eng_dict = {**dictEng_1, **dictEng_2, **dictEng_3, **dictEng_4, **dictEng_5, **dictEng_6, **dictEng_7}
# print(eng_dict)
dictRus1 = dict.fromkeys(['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'], 1)
dictRus2 = dict.fromkeys(['Д', 'К', 'Л', 'М', 'П', 'У'], 2)
dictRus3 = dict.fromkeys(['Б', 'Г', 'Ё', 'Ь', 'Я'], 3)
dictRus4 = dict.fromkeys(['Й', 'Ы'], 4)
dictRus5 = dict.fromkeys(['Ж', 'З', 'Х', 'Ц', 'Ч'], 5)
dictRus6 = dict.fromkeys(['Ш', 'Э', 'Ю'], 8)
dictRus7 = dict.fromkeys(['Ф', 'Щ', 'Ъ'], 10)
rus_dict = {**dictRus1, **dictRus2, **dictRus3, **dictRus4, **dictRus5, **dictRus6, **dictRus7}
# print(rus_dict)
word = input("Enter word: ")
word = word.upper()
sum = 0
# print(word)
for i in word:
    if i in rus_dict:
        for k in rus_dict.keys():
            if k == i:
                sum += int(rus_dict[k])
    else:
        for k in eng_dict.keys():
            if k == i:
                sum += int(eng_dict[k])
print(sum)