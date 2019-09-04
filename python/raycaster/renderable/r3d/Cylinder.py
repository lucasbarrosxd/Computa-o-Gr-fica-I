# Importar arquivos do projeto.
from python.raycaster.physics import *

import math


class Cylinder:
    def __init__(self, bottom: Point, normal: Vector, height: float, radius: float) -> None:
        self.bottom = bottom
        self.normal = normal
        self.height = height
        self.radius = radius

    @classmethod
    def A(cls, bottom: Point, normal: Vector, height: float, radius: float):
        return cls(bottom, normal, height, radius)

    @classmethod
    def B(cls, bottom: Point, top: Point, radius: float):
        return cls(bottom, top - bottom, (top - bottom).norm, radius)

    @property
    def bottom(self) -> Point:
        return self._bottom

    @bottom.setter
    def bottom(self, value: Point) -> None:
        self._bottom = value

    @property
    def top(self) -> Point:
        return self._bottom + self.height * self.normal / self.normal.norm

    @top.setter
    def top(self, value: Point) -> None:
        self._normal = value - self.bottom
        self._height = self.normal.norm

    @property
    def normal(self) -> Vector:
        return self._normal

    @normal.setter
    def normal(self, value: Vector) -> None:
        self._normal = value

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float) -> None:
        self._height = value

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        self._radius = value

    def __str__(self):
        return "B: {0} T: {1} n:{2} h: {3} r: {4}".format(self.bottom, self.top, self.normal, self.height, self.radius)

    @staticmethod
    def intersection(cilindro: "Cilindro", line: Line, coef: bool = True, fwrd: bool = True):
        p0 = line.origin
        d = line.direction

        u = cilindro.normal.norm
        h = cilindro.height
        b = cilindro.bottom
        r = cilindro.radius

        v = (p0-b)-((p0-b)*u)**u
        w = d-(d*u)**u

        alpha = w*w
        beta = v*w
        c = v*v - r**2

        delta = beta**2 - 4*alpha*c
        t1 = None
        t2 = None

        if delta < 0:
            #Não há interseção
            return False
        else:
            if math.isclose(alpha, 0):
                if math.isclose(beta, 0):  
                    if math.isclose(c, 0):
                        return True
                    else:
                        return False
                else:
                    t1 = (-c)/beta
            else:
                if math.isclose(delta,0):
                    t1 = -beta/(2*alpha)
                else:
                    t1 = (math.sqrt(delta) - beta) / (2 * a)
                    t2 = (- math.sqrt(delta) - beta) / (2 * a)
        
        p1 = None
        p2 = None
        if t1:
            p1 = p0 + d*t1
        if t2:
            p2 = p0 + d*t2
        
        validp1 = False
        validp2 = False

        if 0 < (p1-b)*u and (p1-b)*u < h and t1 >= 0:
            validp1 = True

        if 0 < (p2-b)*u and (p2-b)*u < h and t2 >= 0:
            validp2 = True

        if validp1:
            if validp2:
                if t1 < t2:
                    return t1  
                else:
                    return t2
            else:
                return t1
        elif validp2:
            return p2
        else:
            return False

        

