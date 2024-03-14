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
    print(f'Has comprado {numero_cartones} cartones\n')
    cartones = []
    for _ in range(numero_cartones):
        print("Introduce el tamaño del cartón:")
        filas = int(input("Filas: "))
        columnas = int(input("Columnas: "))
        
        carton = []
        for _ in range(filas):
            fila = []
            for _ in range(columnas):
                fila.append(random.randint(1, 99))  
            carton.append(fila)
        cartones.append(carton)
    return cartones


def ver_cartones(cartones):
    for index, carton in enumerate(cartones, start=1):
        print(f"Cartón {index}:")
        for fila in carton:
            print("|", end=" ") 
            for num in fila:
                print("{:2}".format(num), end=" | ")  
            print() 
        print()