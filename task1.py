import json    #импортируем json
from random import randint  #на всякий случай
from datetime import datetime   #для временных меток


notesfile = open("notes.json", "w")
notes = {} 
dates = datetime
notetext = str(input('Введите тело заметки:    '))
dates = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
notetitle = str(input('Введите заголовок заметки:    '))


note = {                        #определяем заметку как словарь
    'Notecount':  notecount,    #номер заметки
    'Notetitle': notetitle,     #название заметк
    'Dates': dates,             #дата создания заметки
    'Text': notetext,           #тело заметки
}
 
def create_note():     #функция создания заметки. заготовка-пустышка.
    #notecount = !!!нужно ввести счётчик!!!
    notetext = str(input('Введите тело заметки:    '))
    dates = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    notetitle = str(input('Введите заголовок заметки:    '))
    return note


def save_note():          #функция сохранения заметки. заготовка-пустышка
    json.dump(note, notesfile)


def all_notes():          #функция просмотра всех заметок   
    print("Все заметки")
    notes = json.load(notesfile)
    for note in notes:
        print(f"Номер заметки: {note['Notecount']}, Название заметки: {note['Notetitle']}, Дата создания: {note['Dates']}")
    notecount = input("Введите номер заметки для просмотра: ")
    for note in notes:
        if note["Notecount"] == int(notecount):
            print(f"Номер заметки: {note['Notecount']}, Название заметки: {note['Notetitle']}, Дата создания: {note['Dates']}")
            return
        print(f"Заметка с номером {notecount} не найдена!")
    

def filter():           #функция фильтрации по дате 
    print(f"Заметки для даты {dates}:")
    notes = json.load(notesfile)


def delete_note():      #функция удаления заметки
    all_notes()
    notecount = int(input("Введите номер заметки, которую нужно удалить: "))
    notes = json.load(notesfile)
    for note in notes:
        if dates == note['Dates'].split()[0]:
            print(f"Номер заметки: {note['Notecount']}, Название заметки: {note['Notetitle']}, Дата создания: {note['Dates']}")
            notes = [note for note in notes if note["Notecount"] != notecount]
            save_note(notes)
    print(f"Заметка с номером {notecount} была успешно удалена!")


def redact_note():      #фукнция редактирования заметки
    all_notes()
    notecount = int(input("Введите номер заметки для редактирования:  "))
    notes = json.load(notesfile)
    for note in notes:
        if note["Notecount"] == notecount:
            note["Notetitle"] = input(f"Название заметки ({note['Notetitle']}): ")
            note["Notetext"] = input(f"Тело заметки ({note['Notetext']}): ")
            note["Dates"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    save_note(notes)
    print(f"Заметка с номером {notecount} успешно обновлена!")


def menu():             #функция главного меню
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
            notes = json.load(notesfile)
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

if __name__ == "__menu__":
    menu()