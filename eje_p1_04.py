# Realiza un programa que pida al usuario cuantos números quiere introducir.
# Luego lee todos los números y realiza una media aritmética:
print("========================")
print("\tEJERCICIO 04")
print("========================")
print("\nMedia Aritmetica\n")


def media_aritmetica(cantidad):
    cont = 1
    suma = 0
    while cont <= cantidad:
        val = float(input(f"Ingrese el valor {cont}:"))
        suma += val
        cont += 1
    media = suma / cantidad
    print(f"La media aritmetica de los datos ingresados es: {round(media,4)}")


num_datos = int(input("Digite el numero de datos a ingresar: "))
media_aritmetica(num_datos)
