from tkinter import *
from tkinter import ttk
from googletrans import Translator
from PIL import ImageTk,Image

def translate():
    for language, suffix in languages.items():
        if combo2.get() == language:
            text = t_input.get('1.0', END)
            translation = translator.translate(text, dest=suffix)
            t_output.delete('1.0', END)
            t_output.insert('1.0', translation.text)

root = Tk()
root.geometry('800x600')
image = PhotoImage(file="translate.ico")
root.iconphoto(False, image)
root.title('Переводчик')
root.resizable(width=False, height=False)
root.config(bg='#856ff8')
translator = Translator()

languages = {
    'Русский': 'ru',
    'Английский': 'en',
    'Французский': 'fr',
    'Японский': 'ja',
    'Итальянский': 'it',
    'Казахский': 'kk',
    'Испанский': 'es',
    'Украинский': 'uk',
    'Шведский': 'sv',
    'Немецкий': 'de',
    'Чешский': 'cs',
    'Балгарский': 'bg',
    'Армянский': 'hy',
    'Арабский': 'ar',
    'Африканский': 'af'
    } 

combo1 = ttk.Combobox(root, width=58, values=[lang for lang in languages], state='readonly')
combo1.current(0)
combo1.grid(row=0, column=0)
combo1.place(anchor=CENTER, x=200, y=70)

combo2 = ttk.Combobox(root, width=58, values=[lang for lang in languages], state='readonly')
combo2.current(0)
combo2.grid(row=0, column=0)
combo2.place(anchor=CENTER, x=600, y=70)

label = Label(root, fg='black', bg='#856ff8', font='Elephant 15', text='Введите текст для перевода')
label.place(relx=0.5, y=35, anchor=CENTER)

t_input = Text(root, width=33, height=10, font='Arial 14')
t_input.place(x=200, y=200, anchor=CENTER)

t_output = Text(root, width=33, height=10, font='Arial 14')
t_output.place(x=600, y=200, anchor=CENTER)

btn = Button(root, width=45, text="Перевести", command=translate)
btn.place(relx=0.5, y=350, anchor=CENTER)

languages_list = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-cn': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'he': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish (kurmanji)',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar (burmese)',
    'ne': 'nepali',
    'no': 'norwegian',
    'or': 'odia',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sm': 'samoan',
    'gd': 'scots gaelic',
    'sr': 'serbian',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'so': 'somali',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'ug': 'uyghur',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu',
}

root.mainloop()
