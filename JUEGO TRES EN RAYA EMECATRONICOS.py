#!/usr/bin/env python
# coding: utf-8

# <h1><center>Tres en Raya</center></h1>
# 
# 
# ![calendar](https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Tic_tac_toe.svg/200px-Tic_tac_toe.svg.png)

# ### Requerimientos del programa
# Considere las siguientes funciones y el codigo asociado:

# In[1]:


def juegaTablero(tbl):
    """Funcion que muestra el tablero del juego, asi como el estado
    actual del tablero de juego.
    """
    print("""
    \t\t    Tres en raya
    \t\t    ============
    
    \t{0:^3}|{1:^3}|{2:^3}\t        {9:^3}|{10:^3}|{11:^3}
    \t------------     \t------------
    \t{3:^3}|{4:^3}|{5:^3}\t        {12:^3}|{13:^3}|{14:^3}
    \t------------     \t------------
    \t{6:^3}|{7:^3}|{8:^3}\t        {15:^3}|{16:^3}|{17:^3}
    """.format(1, 2, 3,
               4, 5, 6,
               7, 8, 9,
               tbl[0], tbl[1], tbl[2], 
               tbl[3], tbl[4], tbl[5],
               tbl[6], tbl[7], tbl[8],))
    return int(input("Ingrese su movimiento [1-6]: "))
def escogeSimbolo():
    """Funcion que pide al usuario que escoga un simbolo entre las opciones
    'X' o 'Y' para jugar al 3 en raya.
    """
    
    simb = input("Ingrese el simbolo a utilizar [X/O]: ").upper()
    while not(simb == 'X' or simb == 'O'):
        print("SIMBOLO INVALIDO: Vuelva a seleccionar un simbolo")
        simb = input("Ingrese el simbolo a utilizar [X/O]: ").upper()
    else:
        return simb
# El usuario escoge el simbolo a utilizar
simb = escogeSimbolo()

# Tablero con la impresion del juego
tablero = [' ', ' ', ' ',
           ' ', ' ', ' ',
           ' ', ' ', ' ']

# Test de juego...
jug = juegaTablero(tablero)
tablero[jug-1] = simb
jug = juegaTablero(tablero)


# El codigo muestra dos funciones:
# 
#     def juegaTablero(tbl)
#     def escogeSimbolo()
#     
# La primera función es un prototipo de interfaz de usuario. En esta se tiene dos tableros de tres-en-raya: a la izquierda un tablero con las posiciones de juego numeradas; a la derecha, el estado del juego según las jugadas se vayan sucediendo.
# 
# La segunda función es la que se encarga de seleccionar cual será el simbolo que utilizara el usuario para lanzar sus lanzamientos. Esta funcion si se encuentra mas completa que la anterior, ya que valida que el simbolo generado sea valido. Sin embargo, solo considera un solo jugador cuando deberia de haber dos.

# ### Juege a tres-en-raya con la PC
# El desafio consiste en crear un programa con el que pueda jugar al tres-en-raya con la computadora.
# 
# _**Reglas del juego**_
# 
# _Implemente un algoritmo basado en selecciones aleatorias para la elección del la PC. Una vez que usted ha ingresado su jugada, la PC ingresa la suya (de ser posible) y muestra el estado actual del juego con las dos jugadas ingresadas. En caso haya un ganador se muestra con un mensaje quien es el para luego pedir si se desea reanudar una nueva partida o terminar el juego._
# 
# Utilice las funciones dadas como ejemplo para partir con el proyecto, pero completelas de tal forma que:
# 
# - **def juegaTablero(tab)** considere que la jugada ingresada se encuentre en el rango correcto (1-9) y que la casilla este vacia.
# - **def escogeSimbolo()** retorne dos valores con los simbolos tanto del jugador como de la PC
# 
# Luego, cree funciones adicionales que le ayuden a construír un código eficiente. Por ejemplo:
# 
#     def compruebaGanador(tbl):
#     """Funcion que retorna tres posibles valores:
#          - 1 Si el jugador ha ganado
#          - 2 Si la PC ha ganado
#          - 0 Si ninguno de los jugadores ha ganado
#     """
#        
#     def juegaPC(simboloPC, tbl):
#     """Funcion que genera un valor aleatorio entre las posibles
#     opciones que estan libres en el tablero y actualiza la lista
#     tbl con el simbolo de la PC
#     """
#     
# Vaya construyendo su código poco a poco para luego integrar todo en un programa principal (main) que permita jugar contra la PC.

# In[2]:


import time
from random import *
# Funciones
def juegaTablero(tbl):
    """Funcion que muestra el tablero del juego, asi como el estado
    actual del tablero de juego.
    """
    print("""
    \t\t    Tres en raya
    \t\t    ============
    
    \t{0:^3}|{1:^3}|{2:^3}\t        {9:^3}|{10:^3}|{11:^3}
    \t------------     \t------------
    \t{3:^3}|{4:^3}|{5:^3}\t        {12:^3}|{13:^3}|{14:^3}
    \t------------     \t------------
    \t{6:^3}|{7:^3}|{8:^3}\t        {15:^3}|{16:^3}|{17:^3}
    """.format(1, 2, 3,
               4, 5, 6,
               7, 8, 9,
               tbl[0], tbl[1], tbl[2], 
               tbl[3], tbl[4], tbl[5],
               tbl[6], tbl[7], tbl[8],))
    
def ingresojugada(tbl,simb):
    empylist=lugaresdispo(tbl)
    while True:
        ingreso=int(input("Ingrese su movimiento [1-9]: "))
        if ingreso in empylist:
            tbl[ingreso-1] = simb
            return tbl
        else:
            print("No es una posicion valida intente nuevamente")
            print()
            
def lugaresdispo(tbl):
    listad=[]
    for x in range(9):
        if tbl[x]==" ":
            listad.append(x+1)
    return listad

def compruebaGanador(tbl,PC,simb):
    if ((tbl[0]==tbl[1]==tbl[2]) and tbl[0]==PC ) or (tbl[3]==tbl[4]==tbl[5] and tbl[3]==PC) or ((tbl[6]==tbl[7]==tbl[8]) and tbl[6]==PC):
        return 2
    elif ((tbl[0]==tbl[1]==tbl[2]) and tbl[0]==simb ) or ((tbl[3]==tbl[4]==tbl[5]) and tbl[3]==simb) or ((tbl[6]==tbl[7]==tbl[8]) and tbl[6]==simb): 
        return 1
    elif ((tbl[0]==tbl[3]==tbl[6]) and tbl[0]==PC) or ((tbl[1]==tbl[4]==tbl[7]) and tbl[1]==PC) or ((tbl[2]==tbl[5]==tbl[8]) and tbl[2]==PC):
        return 2
    elif((tbl[0]==tbl[3]==tbl[6]) and tbl[0]==simb) or ((tbl[1]==tbl[4]==tbl[7]) and tbl[1]==simb) or ((tbl[2]==tbl[5]==tbl[8]) and tbl[2]==simb):
        return 1
    elif (tbl[0]==tbl[4]==tbl[8] or tbl[2]==tbl[4]==tbl[6] ) and  tbl[4]==PC:
        return 2
    elif (tbl[0]==tbl[4]==tbl[8] or tbl[2]==tbl[4]==tbl[6] ) and  tbl[4]==simb: 
        return 1
    else:
        return 0
    
def juegaPC(simboloPC, tbl):
    empylist=lugaresdispo(tbl)
    playnumb=empylist[randrange(len(empylist))]
    tbl[playnumb-1]=simboloPC
    return tbl
    
def escogeSimbolo():
    """Funcion que pide al usuario que escoga un simbolo entre las opciones
    'X' o 'Y' para jugar al 3 en raya.  """
    
    simb = input("Ingrese el simbolo a utilizar [X/O]: ").upper()
    while not(simb == 'X' or simb == 'O'):
        print("SIMBOLO INVALIDO: Vuelva a seleccionar un simbolo")
        simb = input("Ingrese el simbolo a utilizar [X/O]: ").upper()
    else:
        if simb=="X":
            PC="O"
            return PC,simb
        elif simb=="O":
            PC="X"
            return PC,simb

# ------------------------------ main -----------------------------------------
finish = False
    
while not finish:
    # EL algoritmo del juego inicia aqui...
    # El usuario escoge el simbolo a utilizar
    PC,simb = escogeSimbolo()

    # Tablero con la impresion del juego
    tablero = [' ', ' ', ' ',
           ' ', ' ', ' ',
           ' ', ' ', ' ']

    # Test de juego...
    while True:
        juegaTablero(tablero)
        if compruebaGanador(tablero,PC,simb)==2:
            print("La PC ganó la partida")
            break
        tablero=ingresojugada(tablero,simb)
        juegaTablero(tablero)
        if compruebaGanador(tablero,PC,simb)==1:
            print("Usted ganó la partida")
            break
        elif compruebaGanador(tablero,PC,simb)==0 and tablero.count(" ")==0:
            print("Nadie ganó la partida")
            break
        tablero=juegaPC(PC,tablero)
                        
    # Si finaliza la partida debe de pedir si desea una nueva partida
    seguir = input("Otra partida [s/n]: ").upper()
    if seguir == 'N' or seguir=='NO':
        print("Adios")
        finish = True
    else:
        print("Iniciando otra partida en 3", end='')
        for i in range(2, 0, -1):
            time.sleep(1)
            print(", {}".format(i), end='')
        else:
            print()


# In[ ]:




