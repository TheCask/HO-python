## EJERCICIO 1
#==============
#ENUNCIADO
#Si hacemos una lista de todos los números naturales debajo de 10 que sean múltiplos de 3 o 5 obtendríamos 3, 5, 6 y 9. 
#La suma de los múltiplos es 23. Encuentre la suma de todos los múltiplos de 3 y 5 debajo de 1000.
#SOLUCION
# Suma todos los numeros enteros dentro del rango [min] y [max] que sean multiplos de los numeros enteros dentro de [listaBase].
# El ultimo argumento [asociation] indica si se desea la suma de los multiplos de cualquier numero de [listaBase] (OR) o solo de todos a la vez (AND)
def sumMultiplos(listBase, min=0, max=1000, asociation="OR"):
    integerList = list(range(min,max))
    if asociation is "OR":
        sum = _sumMultiplosOR(listBase, integerList)
    elif asociation is "AND":
        sum = _sumMultiplosAND(listBase, integerList)
    return sum

def _sumMultiplosOR(listBase, integerList):
    suma = 0
    for integer in integerList:
        if _isMultiplo(integer, listBase):
            suma += integer    
    return suma

def _isMultiplo(integer, listBase):
    isMultiplo = False
    for multiplo in listBase:
        if integer % multiplo is 0:
            isMultiplo = True
            break
    return isMultiplo            

def _sumMultiplosAND(listBase, integerList):
    suma = 0
    for integer in integerList:
        if integer % (_reduceMultiplication(listBase)) is 0:
                suma += integer
    return suma

def _reduceMultiplication(list):
    result = 1
    for integer in list:
        result *= integer
    return result

print(sumMultiplos([3,5],0,1000,"OR"))
print(sumMultiplos([3,5],0,1000,"AND"))