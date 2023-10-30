import ProcessModule as process
import ViewModule as view
from variables import *
# 1. Показать телефонную книгу
# 2. Внести контакт
# 3. Найти контакт
# 4. Удалить контакт
# 5. Прощание

def run():
    view.action()
    try:
        action = int(input('Введите значение: '))
        if action == 1:  # Показать телефонную книгу
            view.show_phonebook()
            run()
        if action == 2:  # Внести контакт
            process.new_contact()
            view.contact_ins()
            run()
        if action == 3:  # Найдем контакт
            process.find_contact()
            run()
        if action == 4:  # Удалить контакт
            process.del_contact()
        if action == 5:
            view.goodbye()
    
    
    except ValueError:
        print("Введите корректное значение!")