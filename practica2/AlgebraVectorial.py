import math

class Vector:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x
    def getY(self):
        return self.__y

    def modulo(self):
        return math.sqrt(self.__x**2 + self.__y**2)

    def punto(self, v):
        return self.__x * v.getX() + self.__y * v.getY()

    def cruz(self, v):
        return self.__x * v.getY() - self.__y * v.getX()

    def __add__(self, v):
        return Vector(self.__x + v.getX(), self.__y + v.getY())

    def __sub__(self, v):
        return Vector(self.__x - v.getX(), self.__y - v.getY())

    def __str__(self):
        return f"({self.__x:.2f}, {self.__y:.2f})"


class AlgebraVectorial:
    def __init__(self, a=None, b=None):
        self.__a = a
        self.__b = b

    def perpendicular(self, tipo=1):
        a, b = self.__a, self.__b
        
        if tipo == 1:
            return abs((a + b).modulo() - (a - b).modulo()) < 0.0001
        
        elif tipo == 2:
            return abs((a - b).modulo() - (b - a).modulo()) < 0.0001
            
        elif tipo == 3:
            return a.punto(b) == 0
            
        elif tipo == 4:
            izq = (a + b).modulo()**2
            der = a.modulo()**2 + b.modulo()**2
            return abs(izq - der) < 0.0001

    def paralela(self, tipo=1):
        a, b = self.__a, self.__b
        
        if tipo == 1:
            if b.getX() != 0:
                r = a.getX() / b.getX()
                return abs(a.getY() - r * b.getY()) < 0.0001
            elif b.getY() != 0:
                r = a.getY() / b.getY()
                return abs(a.getX() - r * b.getX()) < 0.0001
            return False
            
        elif tipo == 2:
            return a.cruz(b) == 0

    def proyeccion(self):
        a, b = self.__a, self.__b
        denominador = b.modulo()**2
        if denominador == 0: return Vector(0, 0)
        escalar = a.punto(b) / denominador
        return Vector(b.getX() * escalar, b.getY() * escalar)

    def componente(self): 
        a, b = self.__a, self.__b
        if b.modulo() == 0: return 0.0
        return a.punto(b) / b.modulo()


class Main:
    v1 = Vector(5, 6)
    v2 = Vector(7, 8)
    av = AlgebraVectorial(v1, v2)
    if av.perpendicular(1):
        print("a) es perpendicular")
    else:
        print("a) no es perpendicular")
    if av.perpendicular(2):
        print("b) es perpendicular")
    else:
        print("b) no es perpendicular")
    if av.perpendicular(3):
        print("c) es perpendicular")
    else:
        print("c) no es perpendicular")
    if av.perpendicular(4):
        print("d) es perpendicular")
    else:
        print("d) no es perpendicular")
    if av.paralela(1):
        print("e) es paralelo")
    else:
        print("e) no es paralelo")
    if av.paralela(2):
        print("f) es paralelo")
    else:
        print("f) no es paralelo")
    print(f"g) proyeccion: {av.proyeccion()}")
    print(f"h) componente: {av.componente():.15f}")