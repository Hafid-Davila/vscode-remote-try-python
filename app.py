#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

#Desarrolla un minijuego de consola para jugar 'piedra, papel o tijera'. Crea funciones para: elegir aleatoriamente la opción del oponente, validar la elección del usuario, determinar el ganador de cada ronda y manejar la lógica del juego. Asegúrate de que el juego permita múltiples rondas y mantenga la puntuación, ofreciendo al jugador la opción de jugar nuevamente o terminar el juego. Incluye comentarios en el código explicando cada función y su propósito en el juego. 

#crea una funcion para elegir aleatoriamente la opcion del oponente
import random 
def oponente():
    opcion = random.randint(1,3)
    if opcion == 1:
        return "piedra"
    elif opcion == 2:
        return "papel"
    else:
        return "tijera" 

#crea una funcion para validar la eleccion del usuario
def usuario():
    opcion = input("Elige piedra, papel o tijera: ")
    if opcion == "piedra":
        return "piedra"
    elif opcion == "papel":
        return "papel"
    elif opcion == "tijera":
        return "tijera"
    else:
        print("Opcion invalida")
        return usuario()

#crea una funcion para determinar el ganador de cada ronda
def ganador(opcion1, opcion2):
    if opcion1 == opcion2:
        return "Empate"
    elif opcion1 == "piedra":
        if opcion2 == "papel":
            return "Gana el oponente"
        else:
            return "Gana el usuario"
    elif opcion1 == "papel":
        if opcion2 == "tijera":
            return "Gana el oponente"
        else:
            return "Gana el usuario"
    elif opcion1 == "tijera":
        if opcion2 == "piedra":
            return "Gana el oponente"
        else:
            return "Gana el usuario"

def verificar_fin_del_juego(jugador_quiere_continuar, rondas_jugadas, puntuacion_jugador, puntuacion_oponente):
    if not jugador_quiere_continuar or rondas_jugadas >= 3:  # Suponiendo un máximo de 3 rondas
        print(f"Juego terminado. Tu puntuación: {puntuacion_jugador}, Puntuación del oponente: {puntuacion_oponente}")
        return True
    return False

#crea una funcion que Compruebe si el minijuego ha terminado y si muestra su puntuación, informándole del número de victorias y rondas.
def minijuego():
    puntuacion_jugador = 0
    puntuacion_oponente = 0
    rondas_jugadas = 0
    jugador_quiere_continuar = True
    while not verificar_fin_del_juego(jugador_quiere_continuar, rondas_jugadas, puntuacion_jugador, puntuacion_oponente):
        opcion1 = usuario()
        opcion2 = oponente()
        print(f"Oponente: {opcion2}")
        resultado = ganador(opcion1, opcion2)
        if resultado == "Gana el usuario":
            puntuacion_jugador += 1
        elif resultado == "Gana el oponente":
            puntuacion_oponente += 1
        print(resultado)
        rondas_jugadas += 1
        jugador_quiere_continuar = input("¿Quieres continuar? (s/n): ") == "s"
    print("Fin del juego")

minijuego()




