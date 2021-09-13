#Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:
print("========================")
print("\tEJERCICIO 06")
print("========================")
print("\nListas dinamicas\n")

def listas(inicio, fin, salto):
    num_lista = []
    for num in range(inicio, fin+1,salto):
        num_lista.append(num)
    print(num_lista)

listas(0,10,1)
listas(-10,0,1)
listas(0,20,2)
listas(-19,0,2)
listas(0,50,5)