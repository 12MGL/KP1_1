import json    #импортируем json
from random import randint  #на всякий случай
from datetime import datetime   #для временных меток



def count():                        #функция для подсчёта количаства заметок
    with open("notes.json") as n:   #загружаем файл
        notes = json.load(n)        
    if not notes:                   #если заметок не найдено
        return 0                    #возвращаем 0
    last_note = notes[-1]           #если есть - вернётся номер последней заметки
    return last_note['Notecount']   #возвращаем номер последней заметки

 
def create_note():                  #функция создания заметки
    notecount = count()+1           #номер создаваемой заметки будет следующим за номером последней   
    notetitle = str(input('Введите заголовок заметки:    '))
    notetext = str(input('Введите тело заметки:    '))
    dates = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {                        #определяем заметку как словарь
    'Notecount': notecount,         #номер заметки
    'Notetitle': notetitle,         #название заметки
    'Dates': dates,                 #дата создания заметки
    'Text': notetext,               #тело заметки
    }
    return note


def save_note(notes):               #функция сохранения заметки
    with open("notes.json", "w") as n:  #загружаем файл для редактирования
        json.dump(notes, n)         #сохраняем в формате json


def all_notes():          #функция просмотра всех заметок   
    print("Все заметки")
    with open("notes.json") as n:   #загружаем файл
        notes = json.load(n)  
    for note in notes:
        print(f"Номер заметки: {note['Notecount']}, Название заметки: {note['Notetitle']}, Дата создания: {note['Dates']}")
    

def filter(dates):           #функция фильтрации по дате 
    print(f"Заметки для даты {dates}:")
    with open("notes.json") as n:
        notes = json.load(n)
    for note in notes:
        if dates == note['Dates'].split()[0]:
            print(f"Номер заметки: {note['Notecount']}, Название заметки: {note['Notetitle']}, Дата создания: {note['dates']}")


def delete_note():          #функция удаления заметки
    all_notes()
    notecount = int(input("Введите номер заметки, которую нужно удалить: "))
    with open("notes.json") as n:
        notes = json.load(n)
    notes = [note for note in notes if note["Notecount"] != notecount]  #выбираем все заметки, кроме указанной
    save_note(notes)        #сохраняем в файл
    print(f"Заметка с номером {notecount} была успешно удалена!")


def redact_note():      #фукнция редактирования заметки
    all_notes()
    notecount = int(input("Введите номер заметки для редактирования:  "))
    with open("notes.json") as n:
        notes = json.load(n)
    for note in notes:
        if note["Notecount"] == notecount:
            note["Notetitle"] = input(f"Название заметки ({note['Notetitle']}): ")
            note["Notetext"] = input(f"Тело заметки ({note['Notetext']}): ")
            note["Dates"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    save_note(notes)
    print(f"Заметка с номером {notecount} успешно обновлена!")


def main():             #функция главного меню
     while True:
        print("Выберите опцию")
        print("1. Посмотреть список всех заметок")
        print("2. Добавить новую заметку")
        print("3. Редактировать существующую заметку")
        print("4. Удалить существующую заметку")
        print("5. Посмотреть заметки c фильтром по дате")
        print("6. Выйти из программы")

        choice = input("Вариант: ")

        if choice == "1":
            all_notes()

        elif choice == "2":
            note = create_note()
            with open("notes.json") as n:
                notes = json.load(n)
            notes.append(note)
            save_note(notes)
            print("Заметка успешно добавлена!")

        elif choice == "3":
            redact_note()

        elif choice == "4":
            delete_note()

        elif choice == "5":
            date = input("Введите дату в формате год-месяц-день: ")
            filter(date)

        elif choice == "6":
            print("До свидания!")
            break

        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()