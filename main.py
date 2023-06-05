from os import path
"""создание телефонного справочника"""
file_base = "phone_base.txt"  
all_data = []         
last_id = 0          

if not path.exists(file_base):
    with open(file_base, "w",encoding="utf-8") as _:
        pass

def read_records():
    global all_data,last_id
    with open(file_base,encoding="utf-8") as f:  
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split()[0])  
            return all_data        
        return[]                 


def show_all():
    if all_data:
        print(*all_data, sep="\n")
    else:
        print("База пустая,заполните!\n")


"""функция  введения новой записи контакта"""
def add_new_contact():
 global last_id

 array = ['фамилия', 'имя', 'отчество', 'номер телефона']
 user_data = []
 for i in array:
     user_data.append(data_collections(i))

 if not exit_contact(0, " ".join(user_data)):
     last_id += 1
     user_data.insert(0, str(last_id))

     with open(file_base, 'a', encoding="utf-8") as l:
         l.write(f'{" ".join(user_data)}\n')
     print("Ваша запись  добавлена !\n")
 else:
     print("Введённые вами данные уже имеются в справочнике!")        



 
"""функция редактирования данных контакта"""       
add_contact= {"1":"Фамилия" , "2": "Имя","3":"Отчество","4":"Номер телефона"}

show_all()
record_id= input("Введите идентификатор записи контакта")

if exit_contact(record_id,""):
    while True:
        print("\nChading:")
        change_contact=input("1. Фамилия\n"
                             "2. Имя\n"
                             "3. Отчество\n"
                             "4. Номер телефона\n"
                             "5. Выход\n")
        match change_contact:
            case "1"|"2"|"3"|"4":
                return record_id,change_contact, data_collection(add_contact[change_contact])
            case "5":
                return 0
            case _:
                print("Данные не могут вводиться повторно!")
else:
    print("Эти данные некорректные!")                

def search_contact():
   



 """функция редактирования уже существующей записи контакта"""
def change_contact():
    
    global all_data
    symbol= "\n"

    record_id, num_data, data=data_typle

for i, s in enumerate(all_data):
    if s.split()[0]== record_id:
        s = s.split()
        s[int(num_data)]= all_data
        if exit_contact(0, " ".join(s[1:])):
            print("Введённые данные уже скуществуют")
            return
        all_data[1]= " ".join(s) 
        break
with open(file_base, "w" , encoding="utf-8") as f:
    f.write(f'{symbol.join(all_data)}\n')
print("Внести изменения в справочник\n")           

"""функция удаления записи"""
def delete_contact():
    global all_data
    symbol="\n"
    show_all()
    delete_contact= input("Введите идентификатор пользователя: ")

    if exit_contact(delete_contact,""):
        all_data = [s for s all_data if s.split()[]!= del_record]

        with open(file_base,'w', encoding="utf-8") as s:
            s.write(f'{symbol.join(all_data)}\n')
        print("Удалить данную запись!")
    else:
        print("Введённые вами данные некорректны!")        

def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Телефонный справочник:\n"
                       "1. Показать контакт\n"
                       "2. Добавть контакт\n"
                       "3. Поиск контакта\n"
                       "4. Редактировать контакт\n"
                       "5. Удаление контакта\n"
                       "6. Импорт контакта\n"
                       "7. Выход\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_contact()
            case "3":
                search_contact()
            case "4":
                change_contact()
            case "5":
                play = False
            case _:
                print("Введены некорректные данные!!!\n")                       

