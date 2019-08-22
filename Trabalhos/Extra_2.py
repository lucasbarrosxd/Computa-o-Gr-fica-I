"""
Extra 2 - Trabalho 2

Dados uma reta R = (Pr, v) e uma esfera E = (Po, r), calcular a interseção entre os dois.
"""

# Importar arquivos do projeto.
from python.raycaster.basic import Point, Vector, Line
from python.raycaster.object import Sphere
# Importar bibliotecas.
import math
import unittest

"""
SOLUÇÃO:

Queremos encontrar um ponto que esteja contido tanto na reta R quanto na esfera E. Logo temos:

(1) P = Pr + t * v     // Equação da reta.
(2) ||PPo|| = r        // Distância entre a interseção e o centro da esfera é igual ao raio.

Podemos desenvolver (2):

(2) ||PPo|| = r
    (PPo).(PPo) = r²
    (Po - P).(Po - P) = r²
    (Po - (Pr + t * v)).(Po - (Pr + t * v)) = r²
    ((Po - Pr) - t * v).((Po - Pr) - t * v) = r²
    (PrPo - t * v).(PrPo - t * v) = r²
    PrPo.PrPo - 2t * PrPo.v + t² * v.v = r²
    t² * (v.v) + t * (- 2 * PrPo.v) + (PrPo.PrPo - r²) = 0

Como encontramos uma equação de 2º grau, basta resolvê-la para encontrar o coeficiente t, e em seguida substituí-lo
na equação da reta. Mas antes é necessário verificar o delta da equação.

    delta = b² - 4 * a * c
    delta = 4 * (PrPo.v)² - 4 * (v.v) * (PrPo.PrPo - r²)

Se o delta for menor que zero, não há solução. Se for igual a zero, só há uma solução.

    t = ((-b) ± sqrt(delta)) / (2a)

Como o denominador é igual a 2a, se a for igual a zero é impossível encontrar solução. Mas também, se a for igual
a zero a equação deixa de ser do 2º grau.

    a * t² + b * t + c = 0
    0 * t² + b * t + c = 0
    b * t + c = 0
    t = - c / b

Lembrando que a = v.v, ou seja, só é igual a zero quando v for um vetor nulo, o que implica que a reta R na verdade é
um ponto. Prosseguindo, é necessário que o denominador seja diferente de zero novamente. Mas como só chegamos a esse
ponto quando v = (0, 0, 0), e b contém PrP0.v, b é sempre zero quando a é zero. 

    b * t + c = 0
    0 * t + c = 0
    c = 0

Se c = 0, então qualquer valor de t satisfaz a equação, significando que o ponto está exatamente na superfície da
esfera. Se c != 0, então nenhum valor de t satisfaz a equação, significando que o ponto não está sobre a esfera.
"""


def solve(line, sphere):
    if not isinstance(line, Line):
        raise TypeError("Argumento 'line' deve ser de tipo 'Line'.")
    if not isinstance(sphere, Sphere):
        raise TypeError("Argumento 'sphere' deve ser de tipo 'Sphere'.")

    v = line.direction
    w = sphere.center - line.origin

    a = v * v
    b = - 2 * (w * v)
    c = w * w - sphere.radius ** 2

    if math.isclose(a, 0):
        # Não há equação de 2º grau. A reta na verdade é um ponto.
        if math.isclose(c, 0):
            # O ponto está sobre a superfície da esfera. A interseção é o ponto.
            return line
        else:
            # O ponto não está sobre a superfície da esfera. Não há interseção.
            return None
    else:
        delta = b ** 2 - 4 * a * c

        if delta < 0:
            # Não há interseção.
            return None
        elif math.isclose(delta, 0):
            # Há uma interseção tangencial.
            t = (- b) / (2 * a)

            return line(t)
        else:
            # Há duas interseções.
            t1 = ((-b) - math.sqrt(delta)) / (2 * a)
            t2 = ((-b) + math.sqrt(delta)) / (2 * a)

            return line(t1), line(t2)


class Tests(unittest.TestCase):
    def test_1(self):
        line = Line(Point(0, 0, 0), Vector(1, 0, 0))
        sphere = Sphere(Point(2, 0, 0), 1)

        p1, p2 = solve(line, sphere)

        self.assertIsInstance(p1, Point)
        self.assertIsInstance(p2, Point)

        self.assertAlmostEqual(p1.x, 1)
        self.assertAlmostEqual(p1.y, 0)
        self.assertAlmostEqual(p1.z, 0)

        self.assertAlmostEqual(p2.x, 3)
        self.assertAlmostEqual(p2.y, 0)
        self.assertAlmostEqual(p2.z, 0)

    def test_2(self):
        line = Line(Point(0, 0, 0), Vector(1, 0, 0))
        sphere = Sphere(Point(1, 0, 0), 1)

        p1, p2 = solve(line, sphere)

        self.assertIsInstance(p1, Point)
        self.assertIsInstance(p2, Point)

        self.assertAlmostEqual(p1.x, 0)
        self.assertAlmostEqual(p1.y, 0)
        self.assertAlmostEqual(p1.z, 0)

        self.assertAlmostEqual(p2.x, 2)
        self.assertAlmostEqual(p2.y, 0)
        self.assertAlmostEqual(p2.z, 0)

    def test_3(self):
        line = Line(Point(0, 0, 0), Vector(1, 0, 0))
        sphere = Sphere(Point(0, 0, 0), 1)

        p1, p2 = solve(line, sphere)

        self.assertIsInstance(p1, Point)
        self.assertIsInstance(p2, Point)

        self.assertAlmostEqual(p1.x, -1)
        self.assertAlmostEqual(p1.y, 0)
        self.assertAlmostEqual(p1.z, 0)

        self.assertAlmostEqual(p2.x, 1)
        self.assertAlmostEqual(p2.y, 0)
        self.assertAlmostEqual(p2.z, 0)

    def test_4(self):
        line = Line(Point(-1, 1, 0), Vector(1, 0, 0))
        sphere = Sphere(Point(0, 0, 0), 1)

        p1 = solve(line, sphere)

        self.assertIsInstance(p1, Point)

        self.assertAlmostEqual(p1.x, 0)
        self.assertAlmostEqual(p1.y, 1)
        self.assertAlmostEqual(p1.z, 0)

    def test_5(self):
        line = Line(Point(-1, 2, 0), Vector(1, 0, 0))
        sphere = Sphere(Point(0, 0, 0), 1)

        result = solve(line, sphere)

        self.assertIsNone(result)

    def test_6(self):
        line = Line(Point(0, 0, 0), Vector(0, 0, 0))
        sphere = Sphere(Point(0, 0, 0), 1)

        result = solve(line, sphere)

        self.assertIsNone(result)

    def test_7(self):
        line = Line(Point(1, 0, 0), Vector(0, 0, 0))
        sphere = Sphere(Point(0, 0, 0), 1)

        l = solve(line, sphere)

        self.assertIsInstance(l, Line)

        self.assertAlmostEqual(l.origin.x, 1)
        self.assertAlmostEqual(l.origin.y, 0)
        self.assertAlmostEqual(l.origin.z, 0)
