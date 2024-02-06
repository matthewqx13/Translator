from tkinter import *
from googletrans import Translator

def trans():
    text = t1.get('1.0', END)
    trans = translator.translate(text, dest='en')
    t2.delete('1.0', END)
    t2.insert('1.00', trans.text)

root = Tk()
root.geometry('800x600')
image = PhotoImage(file="translate.ico")
root.iconphoto(False, image)
root.title('Переводчик')
root.resizable(width=False, height=False)
root.config(bg='#638889')
translator = Translator()

label = Label(root, fg='black', bg='#638889', font='Elephant 15', text='Введите текст для перевода')
label.place(relx=0.5, y=35, anchor=CENTER)

t1 = Text(root, width=33, height=10, font='Arial 14')
t1.place(x=200, y=200, anchor=CENTER)

t2 = Text(root, width=33, height=10, font='Arial 14')
t2.place(x=600, y=200, anchor=CENTER)

btn = Button(root, width=45, text="Перевести", command=trans)
btn.place(relx=0.5, y=350, anchor=CENTER)


root.mainloop()
