from tkinter import *
from googletrans import Translator

def trans():
    text = t1.get('1.0', END)
    trans = translator.translate(text, dest='en')
    t2.delete('1.0', END)
    t2.insert('1.00', trans.text)

root = Tk()
root.geometry('800x600')
root.title('Переводчик')
root.resizable(width=False, height=False)
root['bg'] = 'black'
translator = Translator()

label = Label(root, fg='white', bg='black', font='Arial 15 bold', text='Введите текст')
label.place(relx=0.5, y=30, anchor=CENTER)
t1 = Text(root, width=35, height=5, font='Arial 12 bold')
t1.place(relx= 0.5, y=100, anchor=CENTER)

btn = Button(root, width=45, text="Перевести", command=trans)
btn.place(relx=0.5, y=180, anchor=CENTER)

t2 = Text(root, width=35, height=5, font='Arial 12 bold')
t2.place(relx= 0.5, y=260, anchor=CENTER)

root.mainloop()
