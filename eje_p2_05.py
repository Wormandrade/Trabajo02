#Realiza una función llamada recortar() que reciba tres parámetros. 
# El primero es el número a recortar, el segundo es el límite inferior y el tercero el límite superior. 
# La función tendrá que cumplir lo siguiente:
#   Devolver el límite inferior si el número es menor que éste
#   Devolver el límite superior si el número es mayor que éste.
#   Devolver el número sin cambios si no se supera ningún límite.

def recortar(num1, l_inf, l_sup):
    num_min = min(num1, l_sup)
    num_max = max(num_min, l_inf)
    return num_max


print("===================================")
print("\tFUNCIONES - EJERCICIO 05")
print("===================================")
print("Límites con numeros\n")
num = input("Digite el valor a recortar: ")
lim_inf = input("Digite el valor del límite inferior: ")
lim_sup = input("Digite el valor del límite superio: ")

if ((lim_inf.isnumeric() and lim_sup.isnumeric()) and  num.isnumeric()):
    print(f"El valor del recorte es: {recortar(int(num), int(lim_inf), int(lim_sup))}")
else:
    print("los valores ingresado no son numéricos")
print("Ejecución exitosa!!..")