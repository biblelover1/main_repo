# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
txt = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
txt = txt.replace(".", " ")
txt = txt.lower()
txt = txt.split()
print(txt)
len_txt = set(txt)
print(len_txt)
print(len(len_txt))
