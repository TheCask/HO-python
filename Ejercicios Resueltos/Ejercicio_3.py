## EJERCICIO 1
#==============
#ENUNCIADO
#Los factores primos en 13195 son 5, 7, 13 y 29 ¿ Cuál es el factor primo más grande en el número 600851475143 ?

def maxPrimeFactor(integer, granul):
    primeDivisorList = []
    step = integer // granul
    progress = 0
    checkpoint = 3
    tempProgress = 1
    for i in range(3, integer):
        if i == checkpoint:
            if tempProgress != round(progress*100/granul, 2):
                print("Calculating: " + str("%.2f" % (progress*100/granul)) + "%")
                tempProgress = round(progress*100/granul, 2)
            progress += 1
            checkpoint += step
        if isDivisor(i,integer) and isPrime(i):
            primeDivisorList.append(i)
            if mul(primeDivisorList) >= integer:
                break
    return primeDivisorList

def is_Prime(integer):
    isPrime = True
    print("Checking if " + str(integer) + " is prime")
    for i in range(integer-1, 1, -1):
        if isDivisor(i, integer):
            isPrime = False
            break
    return isPrime

def mul(listIntegers):
    result = 1
    for i in listIntegers:
        result *= i
    return result

def isDivisor(i, integer):
    return integer % i is 0

def isPrime(n):
    isPrime = False
    print("Checking if " + str(n) + " is prime")
    if n <= 1:
        pass
    elif n <= 3:
        isPrime = True
    elif n % 2 == 0 or n % 3 == 0:
        pass
    else:
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                pass
            i = i + 6
        isPrime = True
    print(isPrime)
    return isPrime

print(maxPrimeFactor(600851475143, 10000))