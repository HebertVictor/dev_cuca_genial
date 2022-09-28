# Projeto: Cuca Genial
# Programa: library.py
# Criado em: 27/09/2022
# Objetivo: Cria as janelas do programa

import winsound
import PySimpleGUI as sg
from config.cfg_sistema import *
from database import *


# Função: show_splash_screen()
# Parâmetros: None
# Objetivo: Cria a janela splash screen
def show_splash_screen():
    sg.Window(STR_WINDOW_TITLE_SPLASH,
            [[sg.Image(filename=SPLASH_SCREEN_IMAGE, size=SPLASH_SCREEN_SIZE)]], 
            transparent_color=sg.theme_background_color(), 
            no_titlebar=True,keep_on_top=True).read(timeout=SPLASH_SCREEN_DELAY,
            close=True
            )


# Função: show_dashboard()
# Parâmetros: None
# Objetivo: Cria a janela dashboard
def show_dashboard():
    sg.theme(config_theme)


    layout = [ #[sg.Push(),sg.Text(STR_NAME_PROJECT, 
                #size=(13,1), font=("Arial",60), pad=(30) ),sg.Push()],
                
            [sg.Push(), sg.Image(source = DASHBOARD_TITLE_IMAGE, size = (440,240)), sg.Push()], 

                #[sg.Push(),sg.Text(STR_REGISTER_START_GAME, 
                #size=(25,1), font=("Arial",30), pad=(20) ),sg.Push()],

                #[sg.Push(),sg.Text('Usuário:',size=(6,1), font=("Arial",30),pad=(30)), 

                [sg. Push(), sg.InputText(default_text='GUEST', justification= 'center', background_color='white', text_color=COLOR_GOLD , key='-CHECK_USER-', size=(15,1),font=("Arial",30),pad=(30)),sg.Push()],

                [sg.Push(),sg.Button('JOGAR',button_color=(COLOR_GOLD, COLOR_BLUE),font=("Arial",30)), sg.Push()],
                
                [sg.Button('Créditos',button_color=(COLOR_GOLD, COLOR_BLUE),font=("Arial",15), key='-CREDITS-'), sg.Push()],
            ]

    window = sg.Window(STR_WINDOW_TITLE_DASHBOARD, layout, size=(900,500))

    while True:
        event, values = window.read()

        # Nome do jogador
        player_name =  values['-CHECK_USER-']
        
        # Abrir tela de jogo
        if event == 'JOGAR':
            player_name = player_name[0:5]
            window.close()
            show_palco(player_name)
            
        # Abrir os créditos
        if event == '-CREDITS-':
            show_creditos()

        # Fechar janela    
        if event == sg.WIN_CLOSED: 
            break   
  
  
# Função: show_creditos()
# Parâmetros: None
# Objetivo: Cria a janela creditos  
def show_creditos():
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

        # Fechar janela    
        if event == sg.WIN_CLOSED: 
            break        


# Função: show_palco()
# Parâmetros: player_name
#   1 - player_name   =>   (nome do jogador)
# Objetivo: Cria a janela palco               
def show_palco(player_name):
    indice=0
    pontos = 0

    frame_placar = sg.Column([[sg.Frame(STR_FRAME_TITLE_PALCO, 
                        [[sg.Column([[sg.Push(background_color=COLOR_GOLD),
                        sg.Image(source = PALCO_USER_IMAGE,background_color=COLOR_GOLD, size = (85,90)), # Imagem do jogador
                        sg.Text(player_name, key=('-PLAYER-'),background_color=COLOR_GOLD,  text_color= COLOR_DARKBLUE,font=("Arial",20)),
                        sg.Push(background_color=COLOR_GOLD),sg.Text(pontos, key=('-PONTOS-'), background_color=COLOR_GOLD, text_color=COLOR_DARKBLUE,font=("Arial",25)), 
                        sg.Push(background_color=COLOR_GOLD)
                        ],],
                    size=(350,90), background_color=COLOR_GOLD)]], border_width=0 , title_color='white', font=("Arial",10))]])

    # layout
    layout = [ [sg.Image(source = PALCO_CLOCK_IMAGE, size = (80,80)),
                sg.Text(size=(5, 1), font=('Helvetica', 40), key='-OUTPUT-'),               # Layout do Counter
                sg.Push(),sg.Image(source = PALCO_LOGO_IMAGE, size = (400,225)), sg.Push(), # Imagem de logo
                
            frame_placar,
            ],
                #------------#
                [sg.Push(),sg.Text(str(indice+1)+' - '+questoes[indice][0], background_color=COLOR_GOLD, text_color= BACKGROUND_COLOR_BLUE, justification='center' , key=('-PERGUNTA-'), font=("Arial",40), 
                size=(35,1), pad=(20, 50) ),sg.Push()],

                [sg.Push(),sg.Button('A) '+respostas[indice][0], button_color=(BACKGROUND_COLOR_BLUE, 'white'), key=('-0-'), font=("Arial",25), 
                size=(20,1), pad=(20) ), 
                
                sg.Button('B) '+respostas[indice][1], button_color=(BACKGROUND_COLOR_BLUE, 'white'), key=('-1-'), font=("Arial",25), 
                size=(20,1), pad=(20) ),sg.Push()],

                [sg.Push(),sg.Button('C) '+respostas[indice][2], button_color=(BACKGROUND_COLOR_BLUE, 'white'), key=('-2-'), font=("Arial",25), 
                size=(20,1), pad=(20) ),

                sg.Button('D) '+respostas[indice][3], button_color=(BACKGROUND_COLOR_BLUE, 'white'), key=('-3-'), font=("Arial",25), 
                size=(20,1), pad=(20) ),sg.Push()],
                
                [sg.Push(),sg.Text(STR_RESPOSTA_PALCO, visible=False,background_color=COLOR_PURPLE, key=('-VERIFICOU-'), font=("Arial",20), 
                pad=(530,10)),sg.Push()]]

    # Config do Counter
    timer_running, counter = True, Time

    # Cria a janela do jogo
    window = sg.Window(STR_WINDOW_TITLE_PALCO , layout, size = (1280, 720))

    # Evento em loop
    while True:           
        event, values = window.read(timeout=1000) 

        # Atualiza o nome do jogador no placar
        window['-PLAYER-'].update(player_name)

        # Mostra o tempo restante
        if timer_running:
            window['-OUTPUT-'].update('{:02d}:{:02d}'.format((counter // 100) // 60, (counter // 100) % 60, counter % 100))
            counter -= 100
                
        resposta_escolhida = '-'+str(respostas[indice][4])+'-'
        
        window['-VERIFICOU-'].update(STR_RESPOSTA_PALCO,visible=False)

        # Verifica se foi pressionado botão de resposta
        if event in ['-0-','-1-','-2-','-3-']:
            if event == resposta_escolhida:
                # Resposta correta
                pontos = pontos + 10
                winsound.PlaySound('SystemExclamation', winsound.SND_ALIAS) # Efeito sonoro
                window['-VERIFICOU-'].update(STR_RESPOSTA_CORRETA_PALCO, visible=True,background_color='green')

            if event != resposta_escolhida:
                # Resposta incorreta
                window['-VERIFICOU-'].update(STR_RESPOSTA_INCORRETA_PALCO,visible=True,background_color='red')
            
            # Atualizando indice e contador
            if indice < len(questoes)-1:
                indice = indice + 1
            else:
                window.close()
                show_dashboard()
            
            counter = 2000  
            
            # Atualizar janelas
            window['-PONTOS-'].update(str(pontos))
            window['-PERGUNTA-'].update(str(indice+1)+' - '+questoes[indice][0])
            window['-0-'].update('A) '+respostas[indice][0])
            window['-1-'].update('B) '+respostas[indice][1])
            window['-2-'].update('C) '+respostas[indice][2])
            window['-3-'].update('D) '+respostas[indice][3])

        # Contador zerou        
        if counter < 0:
            window['-VERIFICOU-'].update('Tempo acabou', visible=True, background_color='red')
            counter = 2000
            indice  = indice + 1
            window['-PERGUNTA-'].update(str(indice+1)+' - '+questoes[indice][0])
            window['-0-'].update('A) '+respostas[indice][0])
            window['-1-'].update('B) '+respostas[indice][1])
            window['-2-'].update('C) '+respostas[indice][2])
            window['-3-'].update('D) '+respostas[indice][3])
        
        #  Fechar janela
        if event == sg.WIN_CLOSED or event == 'Sair': 
            break