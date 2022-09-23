# Projeto: Cuca Genial
# Programa: dashboard.py
# Descrição: Gera a tela de registro do usuário
# Criado em: 19/09/2022

from config.cfg_sistema import *
import PySimpleGUI as sg


sg.theme(config_theme)


layout = [ #[sg.Push(),sg.Text(STR_NAME_PROJECT, 
            #size=(13,1), font=("Arial",60), pad=(30) ),sg.Push()],
            
           [sg.Push(), sg.Image(source = DASHBOARD_TITLE_IMAGE, size = (440,240)), sg.Push()], 

            #[sg.Push(),sg.Text(STR_REGISTER_START_GAME, 
            #size=(25,1), font=("Arial",30), pad=(20) ),sg.Push()],

            #[sg.Push(),sg.Text('Usuário:',size=(6,1), font=("Arial",30),pad=(30)), 

            [sg. Push(), sg.InputText(default_text='GUEST', justification= 'center', background_color='white', text_color=COLOR_GOLD , key='-CHECK_USER-', size=(15,1),font=("Arial",30),pad=(30)),sg.Push()],

            [sg.Push(),sg.Button('JOGAR',button_color=(COLOR_GOLD, COLOR_BLUE),font=("Arial",30)), sg.Push()],
        ]

window = sg.Window(STR_WINDOW_TITLE_DASHBOARD, layout, size=(900,500))

while True:
    event, values = window.read()

    # Nome do jogador
    player_name =  values['-CHECK_USER-']
    
    # Abrir tela de jogo
    if event == 'JOGAR':
        window.close()
        from palco import *

    # Fechar janela    
    if event == sg.WIN_CLOSED: 
        break
    