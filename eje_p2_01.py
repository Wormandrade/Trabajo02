#Realiza una función llamada area_rectangulo() que devuelva el área del rectangulo a partir de una base y una altura. 
# Calcula el área de un rectángulo de 15 de base y 10 de altura.

def area_rectangulo(base, altura):
    return float(base) * float(altura)

print("===================================")
print("\tFUNCIONES - EJERCICIO 01")
print("===================================")
print("Calcular el área de un rectángulo\n")

vBase = input("Digite el valor de la base: ")
vAltura = input("Digite el valor de la altura: ")

if (vBase.isnumeric() and vAltura.isnumeric()):
    print("El área del rectángulo es: ",round(area_rectangulo(vBase, vAltura),4))
else:
    print("Los valores ingresados no son numéricos")
    
print("\nEjecución exitosa!!")  