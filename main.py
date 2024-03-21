from Bingo import *

def main():
    cartones = []  # Inicializamos la lista de cartones vacía
    numeros = []   # Lista para guardar los números sorteados
    numeros_bombo = list(range(1, 99))  # Números posibles en el bombo

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

        limpiar_pantalla()
        if opcion == 1:
            limpiar_pantalla()
            print("¿Cuántos cartones quieres?")
            num_cartones = int(input())
            cartones.extend(comprar_carton(num_cartones))  # Agregamos los cartones comprados a la lista
        elif opcion == 2:
            ver_cartones(cartones)  # Mostrar los cartones almacenados en la variable cartones
        elif opcion == 3:
            limpiar_pantalla()
            if not numeros_bombo:
                print("Se han acabado las bolas.")
                continue
            bola = random.choice(numeros_bombo)
            print(f"Ha salido la bola: {bola}")
            cartones = bombo(cartones, bola, numeros)
        elif opcion == 4:
            limpiar_pantalla()
            print(f"Los números que han salido son:", {numeros})
        elif opcion == 5:
            limpiar_pantalla()
            print("¡Gracias por usar mi Aplicación!")
            break

if __name__ == "__main__":
    main()