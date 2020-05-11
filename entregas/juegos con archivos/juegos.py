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
infoJugador = {}

while True:
    event, values = window.read()
    if event in (None,'Salir'):
        break
    if (values[0] == ''):
        sg.popup('Ingrese nombre')
    else:
        archivo = open("Informacion.txt", "a")
        if event in('Hangman'):
            infoJugador['Nombre'] = values[0]
            infoJugador['Juego'] = 'Hangman'
            infoJugador['Fecha'] = time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())
            window.close()
            hangman.main()
        if event in('Reverse'):
            infoJugador['Nombre'] = values[0]
            infoJugador['Juego'] = 'Reverse'
            infoJugador['Fecha'] = time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())
            window.close()
            reversegam.main()
        if event in('TicTacToe'):
            infoJugador['Nombre'] = values[0]
            infoJugador['Juego'] = 'TicTacToe'
            infoJugador['Fecha'] = time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())
            window.close()
            tictactoe.main()
        json.dump(infoJugador, archivo)
        archivo.close()
window.close()
