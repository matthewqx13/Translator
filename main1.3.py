from tkinter import *
from tkinter import ttk
from googletrans import Translator
from PIL import ImageTk,Image
import customtkinter
from textwrap import wrap

def translate():
    for language, suffix in languages.items():
        if combo2.get() == language:
            text = t_input.get('1.0', END)
            translation = translator.translate(text, dest=suffix)
            t_output.delete('1.0', END)
            t_output.insert('1.0', translation.text)

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("800x600")
root.title('Переводчик')
root.resizable(width=False, height=False)
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

font = customtkinter.CTkFont(family='Comic Sans MS', 
                             size=15, 
                             weight='bold')

combo1 = customtkinter.CTkComboBox(master=root, 
                                   dropdown_font=font, 
                                   button_color='#513ba8', 
                                   width=350, 
                                   values=[lang for lang in languages], state='readonly')
combo1.grid(row=0, column=0)
combo1.place(anchor=customtkinter.CENTER, x=200, y=70)

combo2 = customtkinter.CTkComboBox(master=root, 
                                   dropdown_font=font, 
                                   button_color='#513ba8', 
                                   width=350, 
                                   values=[lang for lang in languages], state='readonly')
combo2.grid(row=0, column=0)
combo2.place(anchor=customtkinter.CENTER, x=600, y=70)

t_input = customtkinter.CTkTextbox(master=root, 
                                   scrollbar_button_color='#978bc7', 
                                   width=350, height=220, 
                                   font=font,
                                   wrap=WORD)
t_input.place(x=200, y=200, anchor=customtkinter.CENTER)

t_output = customtkinter.CTkTextbox(master=root, 
                                    scrollbar_button_color='#978bc7',
                                    width=350, height=220, 
                                    font=font,
                                    wrap=WORD)
t_output.place(x=600, y=200, anchor=customtkinter.CENTER)

btn = customtkinter.CTkButton(master=root, 
                              text="Перевести", 
                              command=translate, 
                              font=font, 
                              text_color='white', 
                              fg_color='#513ba8',
                              corner_radius=100)
btn.place(x=400, y=350, anchor=customtkinter.CENTER)


root.mainloop()
