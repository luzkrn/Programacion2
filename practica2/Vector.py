import math

class VectorTridimensional :
    def __init__(self, a1=0.0, a2=0.0, a3=0.0):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3


    def __add__(self, b):
        return VectorTridimensional(self.a1 + b.a1, self.a2 + b.a2, self.a3 + b.a3)


    def __mul__(self, r):
        return VectorTridimensional(r * self.a1, r * self.a2, r * self.a3)


    def __abs__(self):
        return math.sqrt(self.a1**2 + self.a2**2 + self.a3**2)

    def normalizar(self):
        mag = math.sqrt(self.a1**2 + self.a2**2 + self.a3**2)
        return VectorTridimensional(self.a1 / mag, self.a2 / mag, self.a3 / mag)


    def __matmul__(self, b):
        return (self.a1 * b.a1) + (self.a2 * b.a2) + (self.a3 * b.a3)


    def __xor__(self, b):
        aux_a1 = self.a2 * b.a3 - self.a3 * b.a2
        aux_a2 = self.a3 * b.a1 - self.a1 * b.a3
        aux_a3 = self.a1 * b.a2 - self.a2 * b.a1
        return VectorTridimensional(aux_a1, aux_a2, aux_a3)

    def __str__(self):
        return f"({self.a1}, {self.a2}, {self.a3})"

class Main:
    v1 = VectorTridimensional(7, 6, 5)
    v2 = VectorTridimensional(1, 2, 0)

    print(f"Vector A: {v1}")
    print(f"Vector B: {v2}")
    print(f"Suma (A + B): {v1 + v2}")
    print(f"Escalar (3 * A): {v1 * 3}")
    print(f"Longitud |A|: {abs(v1):.2f}")
    print(f"Producto Escalar (A . B): {v1 @ v2}")
    print(f"Producto Vectorial (A x B): {v1 ^ v2}")
    print(f"Vector A normalizado: {v1.normalizar()}")