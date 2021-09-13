# Realiza un programa que pida al usuario un número entero del 0 al 9,
# y que mientras el número no sea correcto se repita el proceso.
# Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:
print("========================")
print("\tEJERCICIO 05")
print("========================")
print("\nValiacion de numero en rango\n")


def valida(num):
    resp = False
    for val in range(0, 10):
        if val == num:
            resp = True
    return resp


while True:
    numero = int(input("Digite el valor a validar en el Rango: "))
    if valida(numero):
        break
    else:
        print("\tIntente de nuevo por favor..")

print("Ejecución exitosa!!!")
