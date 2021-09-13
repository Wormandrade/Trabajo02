# Realiza un programa que lea un número impar por teclado.
# Si el usuario no introduce un número impar, debe repetise el proceso hasta que lo introduzca correctamente.
print("========================")
print("\tEJERCICIO 02")
print("========================")


def impar(a):
    if a % 2 == 0:
        return True
    else:
        return False


print("Validar un numero impar")
while True:
    num = int(input("Ingrese en numero a validar: "))
    if impar(num):
        print(f"El numero {num} no es impar")
    else:
        print(f"El numero {num} es impar")
        break
print("\nEjecucion exitosa!!!")
