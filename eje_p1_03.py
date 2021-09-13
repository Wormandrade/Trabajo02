# Realiza un programa que sume todos los números enteros pares desde el 0 hasta el 100:
print("========================")
print("\tEJERCICIO 03")
print("========================")
print("Suma de valores pares del 0 a 100")


def suma_pares():
    suma = 0
    for num in range(0, 101, 2):
        suma += num
    return suma


print("Opcion 1: ", sum(range(0, 101, 2)))
print("Opcion 2: ", suma_pares())
