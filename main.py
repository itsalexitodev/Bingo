from Bingo import *

def main():
    cartones = []  # Aquí debes definir la variable cartones
    while True:
        print("#" * 25)
        print("#        Bingo          #")
        print("#         by            #")
        print("# Alex Garcia Rodriguez #")
        print("#" * 25)

        print("\n-Menu-\n")
        print("- 1. Comprar cartón -")
        print("- 2. Ver Cartón -")
        print("- 3. Bombo -")
        print("- 4. Números sorteados -")
        print("- 5. Salir -")
        print("Selecciona una opcion (1 - 5):")

        opcion = int(input())

        if opcion == 1:
            limpiar_pantalla()
            print("¿Cuántos cartones quieres?")
            num_cartones = int(input())
            cartones = comprar_carton(num_cartones)  # Asignar el resultado de comprar_carton a cartones
        elif opcion == 2:
            limpiar_pantalla()
            ver_cartones(cartones)  # Mostrar los cartones almacenados en la variable cartones
        elif opcion == 3:
            limpiar_pantalla()
            bombo(cartones, bola)
        elif opcion == 4:
            limpiar_pantalla()
            print("Los números que han salido son:", numeros(numero, bola))
        elif opcion == 5:
            limpiar_pantalla()
            print("¡Gracias por usar mi Aplicación!")
            break
if __name__ == "__main__":
    main()