import timeit


def alex():
    carton = []

    print("filas:")
    filas = int(input())

    print("columnas:")
    columnas = int(input())

    for i in range(filas):
        fila = []  
        for j in range(columnas):
            fila.append(i * j)
        carton.append(fila)

def profe():
    arr = [[0]*100 for i in range(100)]

fun_alex = timeit.timeit(alex, number=1)
fun_profe = timeit.timeit(profe, number=1)
print("Tiempo de ejecución:", fun_alex, "segundos")
print("Tiempo de ejecución:", fun_profe, "segundos")
