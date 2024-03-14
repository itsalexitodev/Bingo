import timeit
import random

def ver_cartones(cartones):
    for index, carton in enumerate(cartones, start=1):
        print(f"Cartón {index}:")
        for fila in carton:
            print("|", end=" ")  # Separador inicial de la fila
            for num in fila:
                print("{:2}".format(num), end=" | ")  # Ajuste para imprimir números con 2 dígitos
            print() 
        print()

# Generar algunos cartones de ejemplo
cartones = [[[random.randint(1, 99) for _ in range(5)] for _ in range(3)] for _ in range(3)]

# Medir el tiempo de ejecución de ver_cartones
tiempo_ejecucion = timeit.timeit(lambda: ver_cartones(cartones), number=1)

print("Tiempo de ejecución:", tiempo_ejecucion, "segundos")
