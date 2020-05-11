import hangman
import reversegam
import tictactoe
import PySimpleGUI as sg
import json
import time
import os.path


sg.theme('LightGrey2')
layout = [  [sg.Text('Nombre de Jugador: '), sg.InputText()],
            [sg.Text('Elige un juego para jugar:')],
            [sg.Button('Hangman'),
            sg.Button('Reverse'),
            sg.Button('TicTacToe'),
            sg.Button('Salir')] ]

window = sg.Window('Juegos!', layout)
infoJugador = []

while True:
    event, values = window.read()
    if event in (None,'Salir'):
        break
    if (values[0] == ''):
        sg.popup('Ingrese nombre')
    else:
        if event in('Hangman'):
            infoJugador.append({'Nombre Jugador':values[0], 'Juego': 'Ahorcado'})
            window.close()
            hangman.main()
        if event in('Reverse'):
            infoJugador.append({'Nombre Jugador':values[0], 'Juego': 'Reverse'})
            window.close()
            reversegam.main()
        if event in('TicTacToe'):
            infoJugador.append({'Nombre Jugador':values[0], 'Juego': 'Tateti'})
            window.close()
            tictactoe.main()
        archivo = open("Informacion.txt", "a")
        json.dump(infoJugador, archivo)
        archivo.close()
window.close()
