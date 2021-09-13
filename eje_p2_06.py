#Realiza una función separar() que tome una lista de números enteros 
#y devuelva dos listas ordenadas. La primera con los números pares, 
# y la segunda con los números impares:

def separar(*args):
    lista = sorted(args)
    lista_pares = []
    lista_impares = []
    for arg in lista:
        if arg % 2 == 0:
            lista_pares.append(arg)
        else:
            lista_impares.append(arg)
    return lista_pares, lista_impares


print("===================================")
print("\tFUNCIONES - EJERCICIO 06")
print("===================================")
print("Listas con numeros\n")
num = input("Digite los valores numéricos de la lista, separada por , (coma): ")
lista_num = list(map(int, num.split(',')))
par, impar = separar(*lista_num)
print("La lista con numeros pares es: \n",par)
print("La lista con numeros impares es: \n",impar)