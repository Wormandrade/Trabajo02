# Realiza una función llamada intermedio() que a partir de dos números,
# devuelva su punto intermedio

def intermedio(num1, num2):
    return (num1+num2)/2


print("===================================")
print("\tFUNCIONES - EJERCICIO 04")
print("===================================")
print("Intermedio de 2 números\n")
val1 = input("Digite el valor 1: ")
val2 = input("Digite el valor 2: ")

if (val1.isnumeric() and val2.isnumeric()):
    print(f"El valor intermedio es: {round(intermedio(int(val1), int(val2)),2)}")
else:
    print("los valores ingresado no son numéricos")
print("Ejecución exitosa!!..")
