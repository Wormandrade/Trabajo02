#Realiza una función llamada area_circulo() que devuelva el área de un círculo a partir de un radio. 
#Calcula el área de un círculo de 5 de radio:

import math

def area_circulo(radio):
    area = float(radio)**2 * math.pi
    return area

print("===================================")
print("\tFUNCIONES - EJERCICIO 02")
print("===================================")
print("Calcular el área de un círculo\n")
vRadio = input("Digite el valor del radio del circulo: ")

if vRadio.isnumeric():
    print("El área del circulo es: ",round(area_circulo(vRadio),4))
else:
    print("El valor ingresado no es numérico")
    
print("\nEjecución exitosa!!")  