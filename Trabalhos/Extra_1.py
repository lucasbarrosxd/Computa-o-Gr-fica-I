"""
Extra 1 - Trabalho 2

Dados uma Reta R = (Pr, v) e um Plano L = (Pl, u), calcular a interseção entre os dois.
"""

# Importar arquivos do projeto.
from python.raycaster.basic import Point, Vector, Line, Plane
# Importar bibliotecas.
import unittest
import math

"""
SOLUÇÃO:

Uma Reta em um espaço tridimensional pode ser representada por um Ponto contido na reta e um vetor que indica a
direção dessa reta. Um Plano pode ser representado por um Ponto contido nesse plano e um vetor perpendicular ao plano
representando sua normal.

Queremos encontrar um ponto que esteja contido no plano. Isto implica que o vetor PPl é perpendicular à normal do plano.
Com essas informações podemos montar nosso problema:

(1) P = Pr + t * v     // Equação da reta R.
(2) PPl.u = 0          // Equação de vetores perpendiculares.

Podemos desenvolver (2):

    PPl.u = 0
    (Pl - P).u = 0
    (Pl - (Pr + t * v).u = 0
    (Pl - Pr - t * v).u = 0
    PrPl.u - t * v.u = 0
    PrPl.u = t * v.u
    t = PrPl.u / v.u

Agora que encontramos t, basta substituí-lo na equação da reta, mas temos que prestar atenção no denominador de t:

    v.u

Este valor têm que ser diferente de zero para que haja solução. Caso seja igual a zero, encontramos uma fórmula para
vetores perpendiculares, e a equação deixa de ser do 1º grau:

    t * (v.u) - PrPl.u = 0
    t * 0 - PrPl.u = 0
    PrPl.u = 0

Isso implica que, se o segmento PrPl for perpendicular ao vetor u, qualquer valor de t é solução. Caso contrário,
nenhum valor de t é solução.
"""


def solve(line, plane):
    if not isinstance(line, Line):
        raise TypeError("Argumento 'line' deve ser de tipo 'Line'.")
    if not isinstance(plane, Plane):
        raise TypeError("Argumento 'plane' deve ser de tipo 'Plane'.")

    v = line.direction
    n = plane.normal

    if math.isclose(v * n, 0):
        # A reta e a normal do plano são perpendiculares.
        if math.isclose((plane.origin - line.origin) * n, 0):
            # A reta está sobre o plano.
            return line
        else:
            # A reta é paralela ao plano.
            return None
    else:
        t = ((plane.origin - line.origin) * n) / (v * n)

        return line(t)


class Tests(unittest.TestCase):
    def test_1(self):
        line = Line(Point(0, 0, 0), Vector(1, 0, 0))
        plane = Plane(Point(0, 0, 0), Vector(1, 0, 0))

        p = solve(line, plane)

        self.assertIsInstance(p, Point)

        self.assertAlmostEqual(p.x, 0)
        self.assertAlmostEqual(p.y, 0)
        self.assertAlmostEqual(p.z, 0)

    def test_2(self):
        line = Line(Point(-1, 0, 0), Vector(1, 0, 0))
        plane = Plane(Point(0, 0, 0), Vector(1, 0, 0))

        p = solve(line, plane)

        self.assertIsInstance(p, Point)

        self.assertAlmostEqual(p.x, 0)
        self.assertAlmostEqual(p.y, 0)
        self.assertAlmostEqual(p.z, 0)

    def test_3(self):
        line = Line(Point(1, 0, 0), Vector(1, 0, 0))
        plane = Plane(Point(0, 0, 0), Vector(1, 0, 0))

        p = solve(line, plane)

        self.assertIsInstance(p, Point)

        self.assertAlmostEqual(p.x, 0)
        self.assertAlmostEqual(p.y, 0)
        self.assertAlmostEqual(p.z, 0)

    def test_4(self):
        line = Line(Point(0, 0, 0), Vector(1, 1, 1))
        plane = Plane(Point(1, 0, 0), Vector(-1, 0, 0))

        p = solve(line, plane)

        self.assertIsInstance(p, Point)

        self.assertAlmostEqual(p.x, 1)
        self.assertAlmostEqual(p.y, 1)
        self.assertAlmostEqual(p.z, 1)

    def test_5(self):
        line = Line(Point(0, 0, 0), Vector(1, 0, 0))
        plane = Plane(Point(0, 0, 0), Vector(0, 1, 0))

        l = solve(line, plane)

        self.assertIsInstance(l, Line)

        self.assertAlmostEqual(l.direction.dx, 1)
        self.assertAlmostEqual(l.direction.dy, 0)
        self.assertAlmostEqual(l.direction.dz, 0)

    def test_6(self):
        line = Line(Point(0, 1, 0), Vector(1, 0, 0))
        plane = Plane(Point(0, 0, 0), Vector(0, 1, 0))

        n = solve(line, plane)

        self.assertIsNone(n)
