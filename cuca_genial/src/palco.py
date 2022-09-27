# Projeto: Cuca Genial
# Programa: palco.py
# Descrição: Gera o fluxo do game
# Criado em: 19/09/2022

from config.cfg_sistema import * 
import PySimpleGUI as sg
from database import *
from dashboard import player_name

sg.theme(config_theme)   

pontos = 0

# frame do placar 
#frame_placar=sg.Column([[sg.Frame(STR_FRAME_TITLE_PALCO, 
                     #[[sg.Column([[sg.Text(player_name, key=('-PLAYER-'),background_color='white',text_color= COLOR_DARKBLUE,font=("Arial",15)),
                       #sg.Text(pontos, key=('-PONTOS-'), background_color='white',text_color=COLOR_DARKBLUE,font=("Arial",15)),  ]],
                # size=(200,40), background_color='white')]], border_width=0 ,title_color='white', font=("Arial",15))]])


framezinho = sg.Column([[sg.Frame(STR_FRAME_TITLE_PALCO, 
                     [[sg.Column([[sg.Push(background_color=COLOR_GOLD),
                     sg.Image(source = PALCO_USER_IMAGE,background_color=COLOR_GOLD, size = (85,90)), #imagem do jogador
                    sg.Text(player_name, key=('-PLAYER-'),background_color=COLOR_GOLD,  text_color= COLOR_DARKBLUE,font=("Arial",20)),
                    sg.Push(background_color=COLOR_GOLD),sg.Text(pontos, key=('-PONTOS-'), background_color=COLOR_GOLD, text_color=COLOR_DARKBLUE,font=("Arial",25)), 
                    sg.Push(background_color=COLOR_GOLD)
                    ],],
                 size=(350,90), background_color=COLOR_GOLD)]], border_width=0 , title_color='white', font=("Arial",10))]])


# layout
layout = [ 
            [sg.Image(source = PALCO_CLOCK_IMAGE, size = (80,80)),
           sg.Text(size=(5, 1), font=('Helvetica', 40), key='-OUTPUT-'), # Layout do Counter
           #sg.Text(STR_TITLE_PALCO, size=(13,1), font=("Arial",60), pad=(50)),
           sg.Push(),sg.Image(source = PALCO_LOGO_IMAGE, size = (400,225)), sg.Push(),#imagem de logo

           framezinho,
           #frame_placar,
           ],
          # [sg.Push(),sg.Text(pontos, key=('-PONTOS-'), background_color='white', text_color=COLOR_DARKBLUE,font=("Arial",25))], #pontuação

            #------------#
            [sg.Push(),sg.Text(questões[indice][0], background_color=COLOR_GOLD, text_color= BACKGROUND_COLOR_BLUE, justification='center' , key=('-PERGUNTA-'), font=("Arial",40), 
            size=(35,1), pad=(20, 50) ),sg.Push()],

            [sg.Push(),sg.Button(respostas[indice][0], button_color=(BACKGROUND_COLOR_BLUE, 'white'), key=('-0-'), font=("Arial",25), 
            size=(20,1), pad=(20) ), 
            
            sg.Button(respostas[indice][1], button_color=(BACKGROUND_COLOR_BLUE, 'white'), key=('-1-'), font=("Arial",25), 
            size=(20,1), pad=(20) ),sg.Push()],

            [sg.Push(),sg.Button(respostas[indice][2], button_color=(BACKGROUND_COLOR_BLUE, 'white'), key=('-2-'), font=("Arial",25), 
            size=(20,1), pad=(20) ),

            sg.Button(respostas[indice][3], button_color=(BACKGROUND_COLOR_BLUE, 'white'), key=('-3-'), font=("Arial",25), 
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
            print(BEEP) # Efeito sonoro
            window['-VERIFICOU-'].update(STR_RESPOSTA_CORRETA_PALCO, visible=True,background_color='green')

        if event != resposta_escolhida:
            # Resposta incorreta
            window['-VERIFICOU-'].update(STR_RESPOSTA_INCORRETA_PALCO,visible=True,background_color='red')

        # Atualizando indice e contador
        indice  = indice + 1
        counter = 2000  
        
        # Atualizar janelas
        window['-PONTOS-'].update(str(pontos))
        window['-PERGUNTA-'].update(questões[indice][0])
        window['-0-'].update(respostas[indice][0])
        window['-1-'].update(respostas[indice][1])
        window['-2-'].update(respostas[indice][2])
        window['-3-'].update(respostas[indice][3])

    # Contador zerou        
    if counter < 0:
        window['-VERIFICOU-'].update('Tempo acabou', visible=True, background_color='red')
        counter = 2000
        indice  = indice + 1
        window['-0-'].update(respostas[indice][0])
        window['-1-'].update(respostas[indice][1])
        window['-2-'].update(respostas[indice][2])
        window['-3-'].update(respostas[indice][3])
     
    #  Fechar janela
    if event == sg.WIN_CLOSED or event == 'Sair': 
        break
