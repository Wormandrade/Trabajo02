# Realiza un programa que lea dos números por teclado
# y permita elegir entre 3 opciones en un menú
print("========================")
print("\tEJERCICIO 01")
print("========================")


def sumar(*args):
    suma = 0
    for num in args:
        suma += num
    return suma


def restar(*args):
    resta = 0
    for num in args:
        resta += num
    return resta


def producto(*args):
    prod = 1
    for num in args:
        prod *= num
    return prod


def menu():
    print("---Operaciones con numeros---\n")
    print("\t1. Suma\n\t2. Resta\n\t3. Multipliacion\n\tX. Salir")
    return input("Digite su operacion: ")


ciclo = True
while ciclo:
    op = menu()
    if op == "1":
        valores = input("Ingrese los valores a sumar, separados por ,:\n")
        args = tuple(map(int, valores.split(",")))
        print(f"El valor de la suma es: ", sumar(*args))
    if op == "2":
        valores = input("Ingrese los valores a restar, separados por ,:\n")
        args = tuple(map(int, valores.split(",")))
        print(f"El valor de la resta es: ", restar(*args))
    if op == "3":
        valores = input("Ingrese los valores a multiplicar, separados por ,:\n")
        args = tuple(map(int, valores.split(",")))
        print(f"El valor del producto es: ", producto(*args))
    elif op == "X" or op == "x":
        ciclo = False
    else:
        print("\n\tOpcion Incorrecta, intente de nuevo por favor...")
print("Gracias, proceso exitoso..")
