# Realiza una función llamada relacion() que a partir de dos números cumpla
# lo siguiente:
#   Si el primer número es mayor que el segundo, debe devolver 1.
#   Si el primer número es menor que el segundo, debe devolver -1.
#   Si ambos números son iguales, debe devolver un 0.


def relacion(num1, num2):
    resp = 0
    if num1 > num2:
        resp = 1
    elif num2 > num1:
        resp = -1

    return resp


print("===================================")
print("\tFUNCIONES - EJERCICIO 03")
print("===================================")
print("Validación de 2 números\n")
val1 = input("Digite el valor 1: ")
val2 = input("Digite el valor 2: ")

if (val1.isnumeric() and val2.isnumeric()):
    print(f"El resutado de la validación es: {relacion(int(val1), int(val2))}")
else:
    print("los valores ingresado no son numéricos")
print("Ejecución exitosa!!..")