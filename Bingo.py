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
    numeros_ganadores = set()
    lineas_premiadas = set()
    ganadores_bingo = []

    numeros.append(bola)

    for id_carton, carton in cartones:
        for fila_idx, fila in enumerate(carton):
            if all(num == 'X' for num in fila):
                continue  # Si la fila ya está completa, pasamos a la siguiente
            if bola in fila:
                columna_idx = fila.index(bola)
                carton[fila_idx][columna_idx] = 'X'

                # Verificar si la fila ahora está completa
                if all(num == 'X' for num in fila):
                    lineas_premiadas.add((id_carton, fila_idx + 1))
                    print(f"Línea completa! La línea {fila_idx + 1} del cartón {id_carton} ha sido premiada con 20€.")

                # Verificar si el cartón ahora está completo
                if all(all(num == 'X' for num in fila) for fila in carton):
                    ganadores_bingo.append(id_carton)
                    carton_premiado = '\n'.join([' '.join(map(str, fila)) for fila in carton])
                    print(f"¡Bingo! El cartón {id_carton} ha cantado bingo.\nCartón ganador:\n{carton_premiado}")
                    premio_total = (len(lineas_premiadas) + 1) * 20 + len(ganadores_bingo) * 100
                    print(f"Cantidad ganada: {premio_total}€")
                    return cartones

    return cartones