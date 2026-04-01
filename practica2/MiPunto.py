import math
from multimethod import multimethod
class MiPunto:
    def __init__(self,x=0,y=0):
        self.__x=x
        self.__y=y

    def getx(self):
        return self.__x
    
    def gety(self):
        return self.__y
    
    @multimethod
    def distancia(self,otro:'MiPunto' ):
        distanciax= self.__x - otro.getx()
        distanciay=self.__y - otro.gety()
        return math.sqrt((distanciax**2)+(distanciay**2))
    @multimethod
    def distancia(self,x,y):
        distanciax=self.__x-x
        distanciay= self.__y-y
        return math.sqrt((distanciax**2+distanciay**2))
    
    def __str__(self):
        return  f"({self.__x},{self.__y})"
class Main:
    
    p1 = MiPunto()
    p2 = MiPunto(10 , 30.5)
    print("punto 1",p1)
    print("punto 2",p2)
    print("distanciacon MiPunto",p1.distancia(p2))        
    print("distancia x,y especificadas",p1.distancia(10, 30.5))  
