import math
from multimethod import multimethod

class AlgebraVectorial:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getX(self): 
        return self.__x
    
    def getY(self):
        return self.__y

    def calcularPunto(self, v):
        return self.__x * v.getX() + self.__y * v.getY()

    def moduloCuadrado(self):
        return self.__x**2 + self.__y**2

    @multimethod
    def perpendicular(self, v: 'AlgebraVectorial'):
        return self.calcularPunto(v) == 0

    @multimethod
    def perpendicular(self, v: 'AlgebraVectorial', tipo: int):
        if tipo == 1:
            izq = (self.__x + v.getX())**2 + (self.__y + v.getY())**2
            der = (self.__x - v.getX())**2 + (self.__y - v.getY())**2
            return izq == der
        elif tipo == 2:
            izq = (self.__x - v.getX())**2 + (self.__y - v.getY())**2
            der = (v.getX() - self.__x)**2 + (v.getY() - self.__y)**2
            return izq == der
        elif tipo == 3:
            return self.calcularPunto(v) == 0
        elif tipo == 4:
            izq = (self.__x + v.getX())**2 + (self.__y + v.getY())**2
            der = self.moduloCuadrado() + v.moduloCuadrado()
            return izq == der
        return False

    @multimethod
    def paralela(self, v: 'AlgebraVectorial'):
        return (self.__x * v.getY() - self.__y * v.getX()) == 0

    @multimethod
    def paralela(self, v: 'AlgebraVectorial', tipo: int):
        if tipo == 1:
            if v.getX() != 0 and v.getY() != 0:
                return self.__x / v.getX() == self.__y / v.getY()
            return False
        elif tipo == 2:
            return (self.__x * v.getY() - self.__y * v.getX()) == 0
        return False

    def proyeccion(self, v):
        den = v.moduloCuadrado()
        if den == 0: 
            return (0, 0)
        esc = self.calcularPunto(v) / den
        return (v.getX() * esc, v.getY() * esc)

    def componente(self, v):
        mod_b = math.sqrt(v.moduloCuadrado())
        if mod_b == 0: 
            return 0.0
        return self.calcularPunto(v) / mod_b

    def __str__(self):
        return f"({self.__x}, {self.__y})"

class Main:
    v1 = AlgebraVectorial(1, 5)  
    v2 = AlgebraVectorial(3, 7) 

    print(f"Vector A: {v1}")
    print(f"Vector B: {v2}")
    if v1.perpendicular(v2):
        print("a) es perpendicular")
    else:
        print("a) no es perpendicular")
    if v1.perpendicular(v2, 2):
        print("b) es mutuamente ortogonal")
    else:
        print("b) no es mutuamente ortogonal")

    if v1.perpendicular(v2, 3):
        print("c) es ortogonal")
    else:
        print("c) no es ortogonal")

    if v1.perpendicular(v2, 4):
        print("d) es perpendicular")
    else:
        print("d) no es perpendicular")
    print(f"e) {'Es paralelo' if v1.paralela(v2, 1) else 'no es paralelo'}")
    print(f"f) {'Es paralelo (cruz = 0)' if v1.paralela(v2, 2) else 'no es paralelo'}")
    
    print(f"g) Proyeccion de A sobre B: {v1.proyeccion(v2)}")
    print(f"h) Componente de A en B: {v1.componente(v2):.2f}")
