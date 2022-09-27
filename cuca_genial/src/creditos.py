# Projeto: Cuca Genial
# Programa: creditos.py
# Descrição: Faz menção aos desenvolvedores do jogo
# Criado em: 19/09/2022

from config.cfg_sistema import *
import PySimpleGUI as sg

sg.theme(config_theme)

layout = [[sg.Push(), sg.Text('Orientador', font=('Arial', 27), background_color='red'), sg.Push()],
           
          [sg.Push(), sg.Text(STR_ORIENTADOR, justification='center', font=('Arial', 15)), sg.Push()],
          
          [sg.Push(), sg.Text('Desenvolvedores', font=('Arial', 27), justification='center', background_color='red'), sg.Push()],
          
          [sg.Push(), sg.Text(STR_TURMA, justification='center', font=('Arial', 14)), sg.Push()],
          
          [sg.Push(), sg.Button('Voltar', font=('Arial', 15), button_color='red', size=(5, 1))]
         ]

window = sg.Window(STR_WINDOW_TITLE_DASHBOARD, layout, size=(900,500))

while True:
    event, values = window.read()

    # Retornando a tela inicial
    if event == 'Voltar':
      window.close()
      from dashboard import *

    # Fechar janela    
    if event == sg.WIN_CLOSED: 
        break