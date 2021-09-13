# Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas,
# pero no debe repetise ningún elemento en la nueva lista:
print("========================")
print("\tEJERCICIO 07")
print("========================")
print("\nListas\n")


def compara_lista(lista01, lista02):
    lista03 = []
    for cont01 in lista01:
        for cont02 in lista02:
            if cont01 == cont02:
                lista03.append(cont02)
    lista03 = set(lista03)
    lista03 = list(lista03)
    return lista03


list_01 = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 25, 10, 19]
list_02 = [2, 3, 4, 5, 6, 67, 7, 8, 9, 10, 15, 25]
print("Los valores de la lista 1: ", list_01)
print("Los valores de la lista 2: ", list_02)
print("Los valores de la lista Resultante: ", compara_lista(list_01, list_02))