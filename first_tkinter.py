import tkinter
import codecs
from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfile #Функции открыть и созанить как
from tkinter.messagebox import showerror #Показ всех ошиббок
from tkinter import messagebox  #Уводемления приложения
from settings import *

class Text_editor():
    def __init__(self):
        self.file_name = tkinter.NONE
    
    def new_file(self):
        self.file_name = 'No name'
        text.delete('1.0', tkinter.END)
    def open_file(self):
        inp = askopenfile(mode='r')
        if inp is None:
            return       
        data = inp.read()
        text.delete('1.0', tkinter.END)
        text.insert('1.0', data)

    def save_file(self):
        data = text.get('1.0', tkinter.END)
        output = open(self.file_name, 'w', encoding='utf-8')
        output.write(data)
        output.close()
    def save_as_file(self):
        output = asksaveasfile(mode='w', defaultextension='txt')
        data = text.get('1.0', tkinter.END)
        try:
            output.write(data.rstrip())
        except Exception:
            showerror(title='Ошибка', message='Ошибка при сохранении ')
    def get_info(self):
        messagebox.showinfo('Справка', APP_INFO)




app = tkinter.Tk() #Создать окно приложения
app.title(APP_NAME)    #Задаёт название приложения, берёт из файла settings
app.minsize(width=WIDTH, height=HEIGHT)     #Задаёт минимальный размер окна приложения
app.maxsize(width=WIDTH, height=HEIGHT)     #Задаёт максимальное значение окна приложения

text = tkinter.Text(app, width=WIDTH-50, height=HEIGHT, wrap='word')    #Создаётся переменная для окна текста, привязывается к окну приложения, задаётся её размер
scroll = Scrollbar(app, orient=VERTICAL, command=text.yview)  #Создаётся скролл
scroll.pack(side='right', fill='y') #Задаётся сторона его размещения и направление передвижения
text.configure(yscrollcommand=scroll.set)   #устанавливается скрол текста
text.pack() #Текст размещается в окне

editor = Text_editor()

menuBar = tkinter.Menu(app)    #Создаем меню
app_menu = tkinter.Menu(menuBar)    #Создаёт подпундкты для пункта 'файл'
app_menu.add_command(label = 'Новый файл', command=editor.new_file)
app_menu.add_command(label = 'Открыть', command=editor.open_file)
app_menu.add_command(label = 'Сохранить', command=editor.save_file)
app_menu.add_command(label = 'Сохранить как', command=editor.save_as_file)


menuBar.add_cascade(label='Файл', menu=app_menu)    #Создаём пункты основного меню
menuBar.add_cascade(label='Справка', command=editor.get_info)
menuBar.add_cascade(label='выход', command = app.quit)

app.config(menu=menuBar)



app.mainloop()  #Делает так, чтобы окно работало, пока не закрыть его