## EJERCICIO 1
#==============
#ENUNCIADO
#Cada término en la serie de Fibonacci es generado a partir de la suma de los dos términos previos, empezando de 1 y 2, 
#los diez primeros términos serán: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, … 
#Considerando los términos de la serie de Fibonacci que son impares, y por debajo de un millón encuentre la suma de dichos términos.

def sumFibonacciOdsTermsTo(limit):
    odsSum = 0
    for i in fibonacciListTo(limit):
        if i % 2 is not 0:
            odsSum += i 
    return odsSum

def fibonacciListTo(limit):
    fibonacciList = [0,1]
    while fibonacciList[-1] < limit:
        fibonacciList.append(fibonacciList[-1] + fibonacciList[-2])
    fibonacciList.remove(1)
    return fibonacciList[:-1]

def fibonacci(value):
    a, b = 0,1
    while a < value:
        a, b = b, a+b
    return a

print(sumFibonacciOdsTermsTo(1000000))
print(fibonacciListTo(1000000))

