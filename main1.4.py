from tkinter import *
from tkinter import ttk
import customtkinter
from googletrans import Translator
from PIL import ImageTk, Image
from textwrap import wrap
import pyttsx3

root = customtkinter.CTk()
root.geometry("800x600")
root.title('Переводчик')
root.resizable(width=False, height=False)
translator = Translator()

def translate():
    for language, suffix in languages.items():
        if combo2.get() == language:
            text = t_input.get('1.0', END)
            translation = translator.translate(text, dest=suffix)
            t_output.delete('1.0', END)
            t_output.insert('1.0', translation.text)

def switch():
    if btn_theme.get():
        customtkinter.set_appearance_mode("dark")
    else:
        customtkinter.set_appearance_mode("light")

def sound_input():
    engine = pyttsx3.init()
    engine.setProperty('rate', 175)
    engine.setProperty('volume', 0.8)
    engine.say(t_input.get('1.0',END))
    engine.runAndWait()

def sound_output():
    engine = pyttsx3.init()
    engine.setProperty('rate', 175)
    engine.setProperty('volume', 0.8)
    engine.say(t_output.get('1.0',END))
    engine.runAndWait()

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
    'Африканский': 'af',
    'Белорусский': 'be',
    'Азербайджанский': 'az',
    'Хинди': 'hi'
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
                             size=17, 
                             weight='bold')

combo1 = customtkinter.CTkComboBox(master=root, 
                                   font=font,
                                   dropdown_font=font, 
                                   button_color='#513ba8', 
                                   border_color='#6d22dd',
                                   width=350, 
                                   values=[lang for lang in languages], 
                                   state='readonly')
combo1.place(anchor=customtkinter.CENTER, x=200, y=120)
combo1.set('Выберите язык для перевода:')

combo2 = customtkinter.CTkComboBox(master=root, 
                                   font=font,
                                   dropdown_font=font, 
                                   button_color='#513ba8', 
                                   border_color='#6d22dd',
                                   width=350, 
                                   values=[lang for lang in languages], 
                                   state='readonly')
combo2.place(anchor=customtkinter.CENTER, x=600, y=120)
combo2.set('Выберите язык для перевода:')

t_input = customtkinter.CTkTextbox(master=root, 
                                   scrollbar_button_color='#978bc7', 
                                   width=350, height=250, 
                                   border_width=2,
                                   border_color='#6d22dd',
                                   bg_color='#222222',
                                   corner_radius=10,
                                   font=font,
                                   wrap=WORD)
t_input.place(x=200, y=270, anchor=customtkinter.CENTER)

t_output = customtkinter.CTkTextbox(master=root, 
                                    scrollbar_button_color='#978bc7',
                                    width=350, height=250, 
                                    border_width=2,
                                    border_color='#6d22dd',
                                    bg_color='#222222',
                                    corner_radius=10,
                                    font=font,
                                    wrap=WORD)
t_output.place(x=600, y=270, anchor=customtkinter.CENTER)

btn = customtkinter.CTkButton(master=root,
                              text="Перевести", 
                              command=translate, 
                              font=font, 
                              text_color='white', 
                              fg_color='#513ba8',
                              corner_radius=100)
btn.place(x=400, y=430, anchor=customtkinter.CENTER)

btn_theme = customtkinter.CTkSwitch(master=root,
                                   font=font,
                                   width=10,
                                   height=10,
                                   text='Сменить тему',
                                   command=switch)
btn_theme.place(x=600, y=20)

image_sound1 = customtkinter.CTkImage(Image.open('D:/Games/Translator/volume1.png'),
                                     size=(20,20))
image_sound2 = customtkinter.CTkImage(Image.open('D:/Games/Translator/volume2.png'),
                                     size=(20,20))
btn_sound1 = customtkinter.CTkButton(master=root,
                                    command=sound_input,
                                    fg_color='transparent',
                                    compound='top',
                                    hover_color='#DAC1EB',
                                    image=image_sound1,
                                    text='',
                                    width=10,
                                    height=10)
btn_sound1.place(x=325, y=350)
btn_sound2 = customtkinter.CTkButton(master=root,
                                    command=sound_output,
                                    fg_color='transparent',
                                    compound='top',
                                    hover_color='#DAC1EB',
                                    image=image_sound2,
                                    text='',
                                    width=10,
                                    height=10)
btn_sound2.place(x=725, y=350)


# pip install googletrans==3.1.0a0
root.mainloop()
