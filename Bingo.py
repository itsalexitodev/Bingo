import random
import os
import platform

def limpiar_pantalla():
    sistema_operativo = platform.system()
    if sistema_operativo == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def comprar_carton(numero_cartones):
    limpiar_pantalla()
    print(f'Has comprado {numero_cartones} cartones.')
    print("Introduce el tamaño deseado:")
    filas = int(input("Filas:"))
    columnas = int(input("Columnas:"))
    cartones = [] 

    for id_carton in range(1, numero_cartones + 1):  # Generar IDs únicos para cada cartón
        carton = [[random.randint(1, 99) for i in range(columnas)] for j in range(filas)]
        cartones.append((id_carton, carton))  # Añadir una tupla con el ID y el cartón a la lista de cartones

    return cartones

def ver_cartones(cartones):
    limpiar_pantalla()
    for id_carton, carton in cartones:
        print(f"Cartón: {id_carton}")
        for fila in carton:
            fila_str = [str(elemento) for elemento in fila]  # Convertir cada elemento de la fila a cadena
            print(" ".join(fila_str))  # Unir los elementos de la fila con un espacio en blanco
        print()  # Imprimir una línea en blanco entre cartones

def bombo(cartones, bola, numeros):
   pass