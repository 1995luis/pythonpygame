import math
import os
import pygame
import threading
import time
from Modulobm import buscaminas as bm



MINA= -1
pygame.init()
tiempo_limite = 10  # 5 minutos


while True:
    os.system('cls')
    print("Bienvenido al juego de buscaminas por consola")
    
    filas = int (input("ingrese el número de filas: "))
    columnas = int(input("ingrese el número de columnas: "))
    tablero = bm.crear_tablero(filas, columnas)

        ## recorrido por elemento
        #for f in tablero:
        #   print(f)

        ## recorrido por indices
        # for i in range(len(tablero)):
        #     print("[", end=" ")
        #     for j in range(columnas):
        #         print(f"{tablero[i][j]:2d}", end=", ")
        #     print(" ]")
        
    bm.mostrar_tablero(tablero)
        
        #inicio del juego
        
    nro_celdas = math.floor(filas * columnas * 0.7)
    conteo_celdas = 0
        
    tiempo_inicio =time.time()
    
    while True:
        
        tiempo_actual = time.time()
        tiempo_transcurrido = tiempo_actual - tiempo_inicio
        if tiempo_transcurrido >= tiempo_limite:
            print("Tiempo agotado. Has perdido.")
            break
        
        print(f"Tiempo restante: {tiempo_limite - int(tiempo_transcurrido)} segundos")
                    
        print("Ingrese la celda a descubrir:")
        fila = int(input("Ingrese la fila: "))
        columna = int(input("Ingrese la columna: "))
        
        if tablero[fila -1][columna - 1] == MINA:
            bm.mostrar_minas(tablero)
            print("¡Booom! lo siento has perdido...")
            Sonido_exp = pygame.mixer.Sound("Modulobm/sonido/explosion.mp3")
            Sonido_exp.play()
            break  #perdido = True
        else:
            bm.destapar_celda(tablero, fila -1, columna -1)
            tablero[fila -1][columna -1] = str(tablero[fila -1][columna -1])
            conteo_celdas += 1
            
            if conteo_celdas > nro_celdas:
                print("¡Felicitaciones! has llegado al final del juego")
                break
    
             
                 
    respuesta = input("¿Desea jugar de nuevo? [s/n]")
             
            
    if respuesta.upper() == "N":
        print("El juego ha finalizado...")
        break

pygame.quit()