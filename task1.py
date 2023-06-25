import json    #импортируем json
from random import randint  #на всякий случай
from datetime import datetime   #для временных меток


notesfile = open("notes.json", "w")
notes = {} 
#users = []
dates = datetime

data = json.loads(str)


#usrname = str(input('Введите имя пользователя:    '))     #представляемся программе для личных заметок
#print(item(['notecount'], item['dates'],)) 
#print ()
## notecount = str(input('Введите номер заметки:    '))

notetext = str(input('Введите тело заметки:    '))
dates = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
notetitle = str(input('Введите заголовок заметки:    '))

note = {                        #определяем заметку как словарь
    #'Username': usrname,
    'Notecount':  notecount,
    'Notetitle': notetitle,
    'Dates': dates,
    'Text': notetext,
}
 
def create_note(): {}     #функция создания заметки. заготовка-пустышка.

def save_note():{}        #функция сохранения заметки. заготовка-пустышка
    
def all_notes():{}        #функция просмотра всех заметок   
    
def filter(): {}          #функция фильтрации по дате 

def delete_note(): {}     #функция удаления заметки

def redact_note(): {}     #фукнция редактирования заметки

def menu(): {}            #функция главного меню