
import math
import random
import os
import time


#contaste el valor de la mina
MINA= -1

def crear_tablero(nro_filas, nro_columnas, porc_minas = 30):
    # crear una listas por comprensión
    tablero = [[0 for j in range (nro_columnas)]for i in range(nro_filas)]
    
    llenar_tablero_con_minas(tablero, porc_minas)
    conteo_minas(tablero)
    conteo_minas_izquierdo(tablero)
    conteo_minas_derecho(tablero)
    conteo_minas_superior(tablero)
    conteo_minas_inferior(tablero)
    conteo_minas_esquina_superior_izquierda(tablero)
    conteo_minas_esquina_superior_derecha(tablero)
    conteo_minas_esquina_inferior_izquierda(tablero)
    conteo_minas_esquina_inferior_derecha(tablero)
    # mostrar_Tablero(tablero)
    return tablero

# Función para insertar las minas en el tablero
def llenar_tablero_con_minas(tablero, porc_minas):
    
    #contador minas
    contador_minas = 0
    #calcular el numero de minas
    nro_filas = len(tablero)
    nro_cols = len(tablero[0])
    nro_minas = math.ceil(len(tablero[0]) *  len (tablero) * (porc_minas / 100))
    
    while contador_minas < nro_minas:
        fila = random.randint(0, nro_filas - 1)
        columna = random.randint(0, nro_cols - 1)
        
        if tablero[fila][columna] != MINA:
            tablero[fila][columna] = MINA
            contador_minas += 1
        else:
            continue   
        
# Función para hallar el número de minas alrededor de 
# una celda         
def conteo_minas(tablero):
    # recorrido del tablero por indices
    nro_filas = len(tablero)
    nro_cols =len(tablero[0])
    
    for i in range(1, nro_filas - 1):
        for j in range(1, nro_cols - 1):
            if tablero[i][j] != MINA:
                if tablero[i - 1][j - 1] == MINA:
                    tablero[i][j] += 1
                    
                if tablero[i - 1][j] == MINA:
                    tablero[i][j] += 1 
                
                if tablero[i - 1][j + 1] == MINA:
                    tablero[i][j] += 1
                
                if tablero[i][j - 1] == MINA:
                    tablero[i][j] += 1           
                
                if tablero[i][j + 1] == MINA:
                    tablero[i][j] += 1 
                
                if tablero[i + 1][j - 1] == MINA:
                    tablero[i][j] += 1 
                    
                if tablero[i + 1][j] == MINA:
                    tablero[i][j] += 1
                    
                if tablero[i][j + 1] == MINA:
                    tablero[i][j] += 1            
            # else:
            #     continue
    
            
            
# Función para el conteo de las mismas del extremo 
# izquierdo
def conteo_minas_izquierdo(tablero):
    nro_filas = len(tablero)
    
    
    # recorrido sobre las filas
    for i in range(1, nro_filas - 1):
        if tablero[i][0] != MINA:
            
            if tablero[i - 1][0] == MINA:
                tablero[i][0] += 1
                
            if tablero[i - 1][1] == MINA:
                tablero[i][0] += 1
                
            if tablero[i][1] == MINA:
                tablero[i][0] += 1
                
            if tablero[i][+1] == MINA:
                tablero[i][0] += 1
                
            if tablero[i + 1][1] == MINA:
                tablero[i][0] += 1    
                
                
# Función para el conteo de las minas del extremo                
def conteo_minas_derecho(tablero):
     nro_filas = len(tablero)
    
    
     # recorrido sobre las filas
     for i in range(1, nro_filas - 1):
       if tablero[i][-1] != MINA:   
             if tablero[i - 1][-1] == MINA:
                 tablero[i][-1] += 1
             if tablero[i - 1][-2] == MINA:
                 tablero[i][-1] += 1
             if tablero[i][-2] == MINA:
                 tablero[i][-1] += 1
             if tablero[i + 1][-1] == MINA:
                tablero[i][-1] += 1
             if tablero[i + 1][-2] == MINA:
                 tablero[i][-1] += 1  
                 
# Función para el conteo de las minas del extremo superior               
def conteo_minas_superior(tablero):
     nro_columnas = len(tablero[0])
    
    
     # recorrido sobre las columnas
     for j in range(1, nro_columnas - 1):
       if tablero[0][j] != MINA:   
             if tablero[0][j - 1] == MINA:
                 tablero[0][j] += 1
             if tablero[0][j + 1] == MINA:
                 tablero[0][j] += 1
             if tablero[1][j - 1] == MINA:
                 tablero[0][j] += 1
             if tablero[1][j] == MINA:
                tablero[0][j] += 1
             if tablero[1][j + 1] == MINA:
                 tablero[0][j] += 1  
                 
# Función para el conteo de las minas del extremo inferior
# sin tener en cuenta las esquinas               
def conteo_minas_inferior(tablero):
     nro_columnas = len(tablero[0])
    
    
     # recorrido sobre las columnas
     for j in range(1, nro_columnas - 1):
       if tablero[-1][j] != MINA:   
             if tablero[-1][j - 1] == MINA:
                 tablero[-1][j] += 1
             if tablero[-1][j + 1] == MINA:
                 tablero[-1][j] += 1
             if tablero[-2][j - 1] == MINA:
                 tablero[-1][j] += 1
             if tablero[-2][j] == MINA:
                tablero[-1][j] += 1
             if tablero[-2][j + 1] == MINA:
                 tablero[-1][j] += 1  
                 
# funcion para el conteo de minas de la esquina superior izquierda
def conteo_minas_esquina_superior_izquierda(tablero):
    if tablero[0][0] != MINA:
        if tablero[0][1] == MINA:
            tablero[0][0] += 1
        if tablero[1][1] == MINA:
            tablero[0][0] += 1
        if tablero[1][0] == MINA:
              tablero[0][0] += 1    
              
# funcion para el conteo de minas de la esquina inferior izquierda
def conteo_minas_esquina_inferior_izquierda(tablero):
    if tablero[-1][0] != MINA:
        if tablero[-1][1] == MINA:
            tablero[-1][0] += 1
        if tablero[-2][1] == MINA:
            tablero[-1][0] += 1
        if tablero[-2][0] == MINA:
              tablero[-1][0] += 1  
              
# funcion para el conteo de minas de la esquina superior derecha
def conteo_minas_esquina_superior_derecha(tablero):
    if tablero[0][-1] != MINA:
        if tablero[0][-2] == MINA:
            tablero[0][-1] += 1
        if tablero[1][-2] == MINA:
            tablero[0][-1] += 1
        if tablero[1][-1] == MINA:
              tablero[0][-1] += 1
              
# funcion para el conteo de minas de la esquina inferior derecha
def conteo_minas_esquina_inferior_derecha(tablero):
    if tablero[-1][-1] != MINA:
        if tablero[-1][-2] == MINA:
            tablero[-1][-1] += 1
        if tablero[-2][-2] == MINA:
            tablero[-1][-1] += 1
        if tablero[-2][-1] == MINA:
              tablero[-1][-1] += 1  
              
def mostrar_tablero(tablero):
    os.system('cls')
    nro_columnas = len(tablero[0])-2
    arriba(tablero, nro_columnas)
    
    for f in range(len(tablero)):
        for c in range(len(tablero[0])):
            print("│███", end="")  # '|' = alt+179, '█' =alt+219 
    
        print("| %2d"%(f + 1))
    
        if f < (len(tablero) - 1):
            print("├───", end="") # '├' = alt+195, '┼' = alt+197, '┤' =alt+180
            for l in range(nro_columnas):
                print("┼───", end="")
            print("┼───┤") 
    abajo(nro_columnas)   

# funcion para la parte de arriba del tablero
def arriba(tablero, nro_columnas):
    #nro_columnas = len(tablero[0]) - 2
    
    for i in range(1, len(tablero[0]) + 1):
        print(" %2d "%i, end="")
     
    print("\n┌───", end="")
    
    for l in range(nro_columnas):
        print("┬───", end="") # '┌' = alt+218, '─' = alt=196, '┬' = alt=194, '┐' = alt+191
        
    print("┬───┐") 
    

# funcion para la parte de abajo del tablero
def abajo(nro_columnas):
    #nro_columnas = len(tablero[0]) - 2
    
    print("└───", end="") # '├' = alt+195, '┼' =alt+197, '┤' = alt+180
    
    for l in range(nro_columnas):
        print("┴───", end="")
    
    print("┴───┘") # '└' = alt+192, '┴' = alt+193, '┘' = alt+217, '░' = alt+176, '█' = alt+219
        
def destapar_celda(tablero, fila, columna):
    os.system('cls')
    nro_columnas = len(tablero[0]) - 2
    filas = len(tablero)
    columnas = len(tablero[0])
    
    arriba(tablero,nro_columnas)
    
    for f in range(filas):
        for c in range(columnas):
            if f == fila and c == columna:
                if int(tablero[f][c] == MINA):
                    print("|💣 ",end="")
                else:
                    print("| %s "%tablero[f][c],end="")
            else:
                if type(tablero[f][c]) == str:
                    print("| %s "%tablero[f][c],end="")
                else:
                    print("│███",end="")                
                
        print("|%2d"%(f + 1))
        
        if f < (len(tablero)) -1:
            print("├───", end="") 
            for l in range(nro_columnas):
                print("┼───", end="") 
            print("┼───┤")
    
    abajo(nro_columnas)        
# funcion
def mostrar_minas(tablero):
    os.system('cls')
    nro_columnas = len(tablero[0]) - 2
    
    arriba(tablero,nro_columnas)
    
    f = 0
    
    for fila in tablero:
        for celda in fila:
            if type (celda) == str:
                if int(celda) == MINA:
                    print("|💣 ", end="")
                else:
                    print("| %s "%celda,end="")
            elif celda == MINA:
                print("|💣 ", end="")
            else:
                print("|███", end="")
                
        print("|%2d"%(f+1)) 
        if f < (len(tablero)) - 1:
            print("├───", end="") 
            for l in range(nro_columnas):
                print("┼───", end="")
            print("┼───┤")
            
        f += 1
        
    abajo(nro_columnas)
 


            
            
            