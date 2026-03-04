#clase
class EcuacionLineal:
    #atributos
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
    #metodos 
    def TieneSolucion(self):
        z = self.__a * self.__d - self.__b * self.__c
        if z != 0.0:
            return True
        else:
            return False
    #metodos get
    def getX(self):
        if self.TieneSolucion():
            return (self.__e * self.__d - self.__b * self.__f) / (self.__a * self.__d - self.__b * self.__c)
        else:
            return "no tiene solucion"
    
    def getY(self):
        if self.TieneSolucion():
            return (self.__a * self.__f - self.__e * self.__c) / (self.__a * self.__d - self.__b * self.__c)
        else:
            return "no tiene solucion"
    #string
    def __str__(self):
        return "{},{},{},{}".format(self.__a, self.__b, self.__c, self.__d) 

class Main():
    print("Ingrese a, b, c, d, e, f:")

    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    d = float(input("d: "))
    e = float(input("e: "))
    f = float(input("f: "))

    ecuacion = EcuacionLineal(a, b, c, d, e, f)

    if ecuacion.TieneSolucion():
        print("x = ", ecuacion.getX(), ", y = ", ecuacion.getY())
    else:
        print("La ecuación no tiene solución")