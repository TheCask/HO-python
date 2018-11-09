## EJERCICIO 7,8 y 9
#==============
#ENUNCIADO
#Graficar el siguiente polinomio, su derivada y puntos extremos: f(x)=x³+x²-4x+4
#Colocar titulo a los ejes y agregarle una grilla en ambos. Definir el rango de la función entre -10 y 10.
#Colocar titulo y colores distintos para la función y la derivada.
#Guardar los resultados de evaluar la función en el rango del punto a cada 0.1 unidades en un archivo de texto.

import matplotlib.pyplot as pp
import numpy as np
from scipy.optimize import curve_fit

def polinomePlot(coeficients, rangeMin, rangeMax):

    if coeficients == []:
        print("LA LISTA DE COEFICIENTES ESTA VACIA!!")
        return

    #se eliminan coeficientes nulos iniciales si los hay
    while coeficients[0] is 0:
        coeficients.remove(0)

    #crea un muestreo de 50 numeros en el rango dado
    x = np.arange(rangeMin, rangeMax, 0.1)
    #se crea un polinomio con los coeficientes
    pol = np.poly1d(coeficients)
    #se crea una funcion anonima de evaluación del polinomio para x
    y = pol(x)
    #se calcula la derivada del polinomio
    polDer = np.polyder(pol)
    #se crea una funcion anonima de evaluación de la derivada del polinomio para x
    y2 = polDer(x)
    
    #calcula raices del polinomio (array de salida) e imprime en pantalla
    roots = np.roots(pol)
    for root in roots:
        print("ROOT: " + str(root))

    #calcula raices del polinomio derivado (array de salida) e imprime en pantalla
    rootsDer = np.roots(polDer)
    for root in rootsDer:
        print("DER_ROOT: " + str(root))

    #crea y guarda los datos del polinomio evaluado en el rango dado en un archivo de texto txt
    array = np.transpose([x,y])
    file = open('polinome.txt', 'w')
    np.savetxt('polinome.txt', array, fmt='%.1f', delimiter='\t', header="x\tf(x)")
    file.close()

    #se crea y configura la figura para graficar los datos
    pp.figure(figsize=(12, 6))
    pp.ylabel('f(x)', fontsize = 16)
    pp.xlabel('x', fontsize = 16)
    pp.scatter(x,y,c='R', label = 'f(x) = ' + str(str(pol).splitlines()[1]))
    pp.scatter(x,y2,c='B', label= 'f\'(x) = ' + str(str(polDer).splitlines()[1]))
    pp.legend(loc='upper left')
    pp.show()

#el primer parámetro es la lista con los coeficientes del polinomio
#los últimos 2 son el rango de calculo (min y max)
print("Igrese los coeficientes del polinomio de a uno, presione [ENTER] luego de cada uno. Cuando termine, presione [ENTER]")
rawCoeff = input()
coeffList = []
while rawCoeff is not '':
    coeffList.append(float(rawCoeff))
    rawCoeff = input()
print("La lista de coeficientes es: " + str(coeffList))
print("Igrese el rango mínimo de ploteo como entero. Ej. -4")
minRange = int(input())
print("Igrese el rango máximo de ploteo como entero. Ej. -4")
maxRange = int(input())
polinomePlot(coeffList, minRange, maxRange)