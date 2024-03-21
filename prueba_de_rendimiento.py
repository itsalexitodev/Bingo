import timeit
import random

def comprar_carton(numero_cartones):
    print(f'Has comprado {numero_cartones} cartones.')
    print("Introduce el tamaño deseado:")
    filas = int(input("Filas:"))
    columnas = int(input("Columnas:"))
    cartones = []

    for _ in range(numero_cartones):
        carton = [[random.randint(1, 99) for _ in range(columnas)] for _ in range(filas)]
        cartones.append(carton)

    return cartones

# Medir el tiempo de ejecución de comprar_carton
tiempo_ejecucion = timeit.timeit(lambda: comprar_carton(3), number=1)

print("Tiempo de ejecución:", tiempo_ejecucion, "segundos")

