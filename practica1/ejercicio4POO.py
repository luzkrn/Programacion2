
import math
#clase
class Estadistica:
    #atributos
    def __init__(self, numeros):
        self.__numeros = numeros

    #metodos get
    def getPromedio(self):
        suma = 0
        for i in range(10):
            suma = suma + self.__numeros[i]
        return suma / 10
    
    def getDesviacion(self):
        prom = self.getPromedio()
        suma = 0
        for i in range(10):
            suma = suma + (self.__numeros[i] - prom) ** 2
        return math.sqrt(suma / 9)
    #string
    def __str__(self):
        return f"Estadistica con {len(self.__numeros)} números | Promedio: {self.getPromedio():.2f} | Desviación: {self.getDesviacion():.2f}"

class Main:
    print("por Programacion Orientada a Objetos")
    print("ingrese 10 numeros para sacar el promedio:")
    
    numeros = []
    for i in range(10):
        numero = float(input(f"numero {i+1}: "))
        numeros.append(numero)
    
    stats = Estadistica(numeros)
    promedio = stats.getPromedio()
    desviacion = stats.getDesviacion()
    
    print(f"el promedio es ", promedio)
    print(f"la desviación estándar es ", desviacion)