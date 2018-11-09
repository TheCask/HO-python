## EJERCICIO 4, 5 y 6
#==============
#ENUNCIADO
#Dado el siguiente set de datos, obtenga un gráfico tipo scatter plot para X en función de Y
#Intente realizar un ajuste lineal o de algún polinomio utilizando este set de datos.
#Intente colocar label para los ejes y los datos

import matplotlib.pyplot as pp
import numpy as np
from scipy.optimize import curve_fit

# Funcion principal, toma los datos de un archivo de texto plano de dos columnas tabuladas, 
# omite la primer linea (rotulos). El delimitador decimal puede ser coma o punto.
def scatterPlotXY(inputFile):
    input = open(inputFile, 'r') #abre el archivo con los datos
    data = []
    #lee el archivo y agrega los valores a una lista, cada valor es una linea del archivo con dos valores
    #asociados. Si los delimitadores decimales son coma, los pasa a punto.
    for line in input:
        value = line.replace('\n','')
        value = value.replace(',','.')
        data.append(value)

    #crea un array numpy con los datos de la lista y lo usa para preparar los datos para su ploteo
    npArray = np.array(data)
    plotData = np.loadtxt(npArray, delimiter='\t', skiprows=1) #utiliza como delimitador la tabulacion y saltea la primer linea (rotulos)
    plotData = np.transpose(plotData) #transpone los datos para referirse a columna de X y columna de Y
    x = plotData[0] #columna x
    y = plotData[1] #columna y

    #utiliza la libreria optimize para hacer una ajuste (lineal) y guardar parametros de este
    fitParams, fitCovariances = curve_fit(linearFitXY,x,y)
    sigma = [fitCovariances[0,0], fitCovariances[1,1]]

    #se crea y configura la figura para graficar los datos
    pp.figure(figsize=(12, 6))
    pp.ylabel('Position (cm)', fontsize = 16)
    pp.xlabel('Time (s)', fontsize = 16)
    pp.errorbar(x, y, fmt = 'ro', yerr = sigma[1])
    #pp.scatter(plotData[0],plotData[1])
    pp.plot(x, linearFitXY(x, fitParams[0], fitParams[1]))
    pp.plot(x, linearFitXY(x, fitParams[0] + sigma[0], fitParams[1] + sigma[1])) 
    pp.plot(x, linearFitXY(x, fitParams[0] - sigma[0], fitParams[1] - sigma[1]))
    #pp.savefig('dataFitted.png', bbox_inches=0, dpi=300)
    pp.show()
    
#funcion lineal de modelo para el ajuste
def linearFitXY(x, m, b):
    return m * x + b

scatterPlotXY('Input_Ejercicio_4.txt')