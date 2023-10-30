from variables import *
import ViewModule as view
from tabulate import tabulate
import Control as control

def new_contact():
    user = {}
    user[info_list[0]] = id
    for key in info_list[1:]:
        user[key] = input(f"{key}: ")
    users_list.append(user)
    increase_id()
    with open("phone_book.txt", "a") as file:
        for key in user:
            file.write(f"{str(user.get(key))} ")
        file.write("\n")
    print(tabulate(users_list, headers="keys"))




def increase_id():
    global id
    id += 1
    return id



def find_contact():
    new_id = 1
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
                find_user.append(user)
            search = input("Ведите запрос: ")
            if len(find_user) != 0:
                for i in range(len(find_user)):
                    for key in find_user[i]:
                        if find_user[i][key] == search:
                            print(find_user[i])
            else: print("Контакт не найден")
    except:  
        print("Файл пуст или не существует.\nВнесите новый контакт для продолжения\n")
        control.run()

            

def del_contact():
    try:
        new_id = 1
        with open("phone_book.txt", "r") as file:
            for record in file:
                user = {}
                for k, v in zip(info_list, record.split()):
                    if k == info_list[0]:
                        user[k] = new_id          
                    else:
                        user[k] = v
                find_user.append(user)
                new_id += 1
            if len(find_user) == 0:
                print("Справочник пуст\nВнесите первый контакт")
                control.run()
            else:
                search = input("Ведите запрос для удаления пользователя: ")
                for i in range(len(find_user)):
                    for key in find_user[i]:
                        if find_user[i][key] == search:
                            a = i
                print(f"user: {find_user.pop(a)} deleted")
                new_file()
    except FileNotFoundError:
        print("Справочника не существует\n")
        control.run()

def new_file():
    global find_user
    file = open("phone_book.txt", "w")
    for i in range(len(find_user)):
        for key in find_user[i]:
            file.write(f"{str(find_user[i][key])}")
    print(tabulate(find_user, headers=info_list))

    # new_id = 1
    # with open("phone_book.txt", "r") as file:
    #         for record in file:
    #             user = {}
    #             for k, v in zip(info_list, record.split()):
    #                 if k == info_list[0]:
    #                     user[k] = new_id          
    #                 else:
    #                     user[k] = v
    #             new_id += 1        
    #             find_user.append(user)
    # print("Справочник", "\n", end = " ")
    # print(tabulate(find_user, headers="keys"))
    # print("\n")