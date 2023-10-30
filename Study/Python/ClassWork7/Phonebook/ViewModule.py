import sys
import ProcessModule as process
from ProcessModule import users_list
import Control as control
from tabulate import tabulate
from variables import info_list


def greetings():
    print("Welcome to phonebook!")
    print("What do you want to do?")

def action():
    print("1 - Показать телефонную книгу")
    print("2 - Внести контакт")
    print("3 - Найти контакт")
    print("4 - Удалить контакт")
    print("5 - Выйти из справочника")

def show_phonebook():
    new_id = 1
    users_list
    info_list
    try:
         with open("phone_book.txt", "r") as file:
            for record in file:
                user = {}
                for k, v in zip(info_list, record.split()):
                    if k == info_list[0]:
                        user[k] = new_id          
                    else:
                        user[k] = v
                new_id += 1        
                users_list.append(user)
            print(tabulate(users_list, headers="keys"))
            print("\n")
            # if users_list != 0:
            #     print(tabulate(users_list, headers="keys"))
            # else: print(tabulate(file.read()))
    except FileNotFoundError:
        print("Справочника пуст или не существует.\nСоздать его?") 
        choise = int(input("1 - Да\n2 - Выход в меню\nВведите значение: "))
        if choise == 1:
            file = open("phone_book.txt", "w")
            file.close()
            print("File is created\nChoose another option")
            print("\n")
            control.run()
        else:
            control.run()
        
        # with open("phone_book.txt", "r") as data_base:
        #     for line in data_base:
        #         print(line)


def goodbye():
        print("Goodbye!")
        sys.exit()
    
    
    

def del_contact():
    print("Контакт удален!")

def contact_ins():
    print("Контакт записан!")