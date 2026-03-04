
import math
#funcion
def promedio(datos):
    return sum(datos)/len(datos)

def desviacion(datos):
    n=len(datos)
    if n<=1:
        return 0
    #llamada de la funcion
    media=promedio(datos)
    cuadrado=sum((i-media)**2 for i in datos) 
    return math.sqrt(cuadrado/(n-1))

print("por Programacion Modular-Estructura")
print("ingrese 10 numeros (uno por uno):")
numeros = []
for i in range(10):
    numero = float(input(f"numero {i+1}: "))
    numeros.append(numero)

print("el promedio es: ", promedio(numeros))
print("la desviacion estandar es: ", desviacion(numeros))