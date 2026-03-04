import random
import time
#clase
class Cronometro:
    #atributos,constructor

    def __init__(self):
        self.__inicia = time.time()
        self.__finaliza = None

    #metodos get

    def getinicia(self):
        return self.__inicia
    
    def getfinaliza(self):
        return self.__finaliza
    
    #metodos void

    def inicia(self):
        self.__inicia = time.time()
        self.__finaliza = None
    
    def detener(self):
        self.__finaliza = time.time()
    
    def lapsoDeTiempo(self):
        if self.__finaliza == None:
            return (time.time() - self.__inicia) * 1000
        else:
            return (self.__finaliza - self.__inicia) * 1000
    #String
    def __str__(self):
        return f"inicio: {self.__inicia}, final: {self.__finaliza}"
    
def ordenarPorSeleccion(lista):
    i = 0
    while i < len(lista) - 1:
        minimo = i
        j = i + 1
        
        while j < len(lista):
            if lista[j] < lista[minimo]:
                minimo = j
            j = j + 1
        
        guardar = lista[i]
        lista[i] = lista[minimo]
        lista[minimo] = guardar
        
        i = i + 1

class Main:
    print("Probando con 1000 numeros")
    numeros1 = [random.randint(1, 1000000) for _ in range(1000)]

    listaDeNumeros1 = numeros1.copy()
    t1 = Cronometro()
    ordenarPorSeleccion(listaDeNumeros1)
    t1.detener()
    
    print(f"El tiempo fue: {t1.lapsoDeTiempo():.2f} milisegundos")

    print("\nProbando con 100000 numeros")
    numeros2 = [random.randint(1, 1000000) for _ in range(100000)]  

    listaDeNumeros2 = numeros2.copy()
    t2 = Cronometro()
    ordenarPorSeleccion(listaDeNumeros2)
    t2.detener()
    
    print(f"El tiempo fue: {t2.lapsoDeTiempo():.2f} milisegundos") 