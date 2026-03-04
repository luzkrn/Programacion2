import math
#clase
class EcuacionLineal:
    #atributos
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
    #metodos get
    def getA(self):
        return self.__a
    
    def getB(self):
        return self.__b
    
    def getC(self):
        return self.__c
    #metodos
    def getDiscriminante(self):
        return self.__b**2 - 4 * self.__a * self.__c
    
    def getRaiz1(self):
        y=self.getDiscriminante()
        if  y >= 0:
            return (-self.__b + math.sqrt(y)) / (2 * self.__a)
        else:
            return 0
    
    def getRaiz2(self):
        x= self.getDiscriminante()
        if x >= 0:
            return (-self.__b - math.sqrt(x)) / (2 * self.__a)
        else:
            return 0
        
    def TieneRaicesReales(self):
        return self.getDiscriminante() > 0
    
    def TieneRaizUnica(self): 
        return self.getDiscriminante() == 0
    #string
    def __str__(self):
        return f"{self.__a}x^2 + {self.__b}x + {self.__c} = 0"
    
class Main():
    print("Ingrese a, b, c:")
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))

    ecuacion = EcuacionLineal(a, b, c   )

    discriminante = ecuacion.getDiscriminante()

    if discriminante > 0:
        print("La ecuación tiene dos raíces",
            ecuacion.getRaiz1(), "y", ecuacion.getRaiz2())

    elif discriminante == 0:
        print("La ecuación tiene una raíz",
            ecuacion.getRaiz1())

    else:
        print("La ecuación no tiene raíces reales")