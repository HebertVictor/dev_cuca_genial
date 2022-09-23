# Projeto: Cuca Genial
# Programa: splash_screen.py
# Criado em: 19/09/2022


from config.cfg_sistema import *
from library.my_library import *
import PySimpleGUI as sg

# Define o tema do sistema
sg.theme(config_theme)  

# Cria a janela splash screen
sg.Window(STR_WINDOW_TITLE_SPLASH,
         [[sg.Image(filename=SPLASH_SCREEN_IMAGE, size=SPLASH_SCREEN_SIZE)]], 
         transparent_color=sg.theme_background_color(), 
         no_titlebar=True,keep_on_top=True).read(timeout=SPLASH_SCREEN_DELAY,
         close=True
         )

# Cria janela de login
from dashboard import *