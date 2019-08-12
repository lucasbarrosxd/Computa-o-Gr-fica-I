"""
Trabalho 2 - 08/08/2019

Dados um Cilindro C (P0, P1, r) e uma reta R (Pr, v), calcular o(s) ponto(s) P de interseção.
"""

# Importar arquivos do projeto.
from python.raycaster.basic import Point, Vector, Line
from python.raycaster.object import Cylinder
# Importar bibliotecas.
import math
import unittest

"""
SOLUÇÃO:

Primeiro, montamos o problema. Vamos estabeler o vetor u = P1 - P0, e em seguida definimos o ponto P' que é a
projeção do ponto P sobre o vetor u. Agora já temos as seguintes equações:

(1) P = Pr + t * v      // Equação da reta R.
(2) P' = P0 + s * u     // Equação da reta do cilindro C/vetor u.
(3) ||PP'|| = r         // A distância entre P e P' é igual ao raio r do cilindro C.
(4) PP'.u = 0           // O vetor u é perpendicular ao vetor PP'.
(*) 0 <= s <= 1         // Garante que o ponto encontrado está no cilindro.

Agora podemos começar a resolver o problema. As equações de reta são mais complicadas de usar, então podemos começar
por (3) ou (4):

(3) ||PP'|| = r
    PP'.PP' = r²
    (P' - P).(P' - P) = r²
    (P0 + s * u - Pr - t * v).(P0 + s * u - Pr - t * v) = r²
    ((P0 - Pr) + s * u - t * v).((P0 - Pr) + s * u - t * v) = r²
    (PrP0 + s * u - t * v).(PrP0 + s * u - t * v) = r²                 // PrP0 = vetor w para faciliar os cálculos.
    w.w + s² * u.u + t² * v.v + 2s * w.u - 2t * w.v - 2ts * u.v = r²

Chegamos a um ponto em que só temos duas variáveis: os coeficients t e s. Mas a equação é da forma quadrática, o que
deixa difícil calcular o valor de t. Vamos tentar desenvolver a equação (4):

(4) PP'.u = 0
    (P' - P).u = 0
    (P0 + s * u - Pr - t * v).u = 0
    ((P0 - Pr) + s * u - t * v).u = 0
    (w + s * u - t * v).u = 0
    w.u + s * u.u - t * v.u = 0
    s = (t * v.u - w.u) / u.u

Conseguimos encontrar um valor para o coeficiente s. Podemos voltar para a equação (3) e substituí-lo lá:

    w.w + s² * u.u + t² * v.v + 2s * w.u - 2t * w.v - 2ts * u.v = r²
    s² * u.u + s * (2w.u - 2t * u.v) + (w.w + t² * v.v - 2t * w.v - r²) = 0
    (t² * (v.u)² - 2t * (v.u) * (w.u) + (w.u)²) / u.u
        + 2(2t * (u.v) * (w.u) - t² * (u.v)² - (w.u)²) / u.u
        + (w.w + t² * v.v - 2t * w.v - r²) = 0
    (t² * (v.u)² - 2t * (v.u) * (w.u) + (w.u)²) / u.u
        - 2(t² * (u.v)² - 2t * (u.v) * (w.u) + (w.u)²) / u.u
        + (w.w + t² * v.v - 2t * w.v - r²) = 0
    (- t² * (u.v)² + 2t * (u.v) * (w.u) - (w.u)²) / u.u + w.w + t² * v.v - 2t * w.v - r² = 0
    t² * (v.v - (u.v)² / u.u) + t * 2 * ((u.v) * (w.u) / (u.u) - w.v) + (w.w - (w.u)² / u.u - r²) = 0

Chegamos em uma equação de 2º grau que só possui o coeficiente t. Agora podemos resolvê-la, mas com algumas
ressalvas. Como sempre, o valor de delta da equação deve ser analisado, pois para encontrar t precisamos do
valor de ± sqrt(delta):

* Se delta for maior que 0, há duas interseções. Uma usando + sqrt(delta) e outra usando - sqrt(delta).
* Se delta for igual a 0, há uma interseção, pois + sqrt(delta) = - sqrt(delta) = 0.
* Se delta for menor que 0, não é possível resolver sqrt(delta). Isso implica que não há interseção.

Continuando, fazemos o cálculo de delta:

    delta = b² - 4 * a * c
    delta = (2 * ((u.v) * (w.u) / (u.u) - w.v))² - 4 * (v.v - (u.v)² / u.u) * (w.w - (w.u)² / u.u - r²)
    delta = 4 * ((u.v)² * (w.u)² / (u.u)² - 2 * (u.v) * (w.u) * (w.v) / (u.u) + (w.v)²)
        - 4 * (
            (v.v) * (w.w) - (v.v) * (w.u)² / (u.u) - (v.v) * r²
            - (w.w) * (u.v)² / (u.u) + (u.v)² * (w.u)² / (u.u)² + r² * (u.v)² / (u.u)
        )
    delta = 4 * ((w.v)² - 2 * (u.v) * (w.u) * (w.v) / (u.u) - (v.v) * (w.w) + (v.v) * (w.u)² / (u.u) + r² * (v.v)
        + (w.w) * (u.v)² / (u.u) - r² * (u.v)² / (u.u))

Encontramos o delta. O próximo passo é rezar bastante pra esse treco estar certo. Feito isso, podemos calcular o
coeficiente t:

    t = (2 * ((u.v) * (w.u) / (u.u) - w.v) ± sqrt(delta)) / (2 * (v.v - (u.v)² / u.u))

Agora é só substituir t na equação da reta R e podemos encontrar o ponto P. Mas ainda há alguns problemas. Primeiro, na
solução de t há o seguinte denominador:

    2 * (v.v - (u.v)² / u.u)

Caso este valor seja igual a zero, torna-se impossível solucionar a equação. O único meio para que esse denominador
seja igual a zero é se a segunda parte da multiplicação for igual a zero. Podemos desenvolvê-la para ver se achamaos
algo interessante:

    v.v - (u.v)² / u.u = 0
    v.v = (u.v)² / u.u
    v.v * u.u = (u.v)²

Coincidentemente, essa equação já foi analisada no Trabalho 1, então podemos pular os cálculos. O resultado é que ela
só é verdade quando os vetores v e u forem colineares. Ou seja, quando v e u forem colineares, não há solução.
    
Ainda é necessário calcular se 0 <= s <= 1 para saber se nossas respostas são válidas. Como já encontramos s em função
de t, basta substituir t na equação. Feito isso, só falta calcular os pontos de interseção através da equação da reta.
"""


def solve(cylinder, line):
    if not isinstance(cylinder, Cylinder):
        raise TypeError("Argumento 'cylinder' deve ser de tipo 'Cylinder'.")
    if not isinstance(line, Line):
        raise TypeError("Argumento 'line' deve ser de tipo 'Line'.")

    v = line.direction
    u = cylinder.top - cylinder.bottom
    w = cylinder.bottom - line.origin

    a = (v * v) - (((u * v) ** 2) / (u * u))
    b = 2 * (((u * v) * (w * u) / (u * u)) - w * v)
    c = (w * w) - ((w * u) ** 2) / (u * u) - (cylinder.radius ** 2)

    delta = b * b - 4 * a * c

    if delta < 0:
        # Não há interseção, a reta e o cilindro não se encontram.
        return None
    else:
        if math.isclose(a, 0):
            # Não há interseção pois os vetores da reta e do cilindro são colineares.
            return None
        else:
            if math.isclose(delta, 0):
                # Há apenas uma interseção tangencial possível.
                t = (- b) / (2 * a)
                s = (t * (v * u) - (w * u)) / (u * u)

                if 0 <= s <= 1:
                    # A interseção é válida.
                    return line(t)
                else:
                    # A interseção não é válida.
                    return None
            else:
                # Há duas interseções possíveis.
                t1 = (- b - math.sqrt(delta)) / (2 * a)
                t2 = (- b + math.sqrt(delta)) / (2 * a)

                s1 = (t1 * (v * u) - (w * u)) / (u * u)
                s2 = (t2 * (v * u) - (w * u)) / (u * u)

                if 0 <= s1 <= 1 and 0 <= s2 <= 1:
                    # As duas interseções são válidas.
                    return line(t1), line(t2)
                elif 0 <= s1 <= 1:
                    # Apenas a primeira interseção é válida.
                    return line(t1)
                elif 0 <= s2 <= 1:
                    # Apenas a segunda interseção é válida.
                    return line(t2)
                else:
                    # Nenhuma das interseções é válida.
                    return None


class Tests(unittest.TestCase):
    def test_1(self):
        cyli = Cylinder(Point(0, 0, 0), Point(0, 2, 0), 1)
        line = Line(Point(-2, 1, 0), Vector(1, 0, 0))

        p1, p2 = solve(cyli, line)

        self.assertAlmostEqual(p1.x, -1)
        self.assertAlmostEqual(p1.y, 1)
        self.assertAlmostEqual(p1.z, 0)

        self.assertAlmostEqual(p2.x, 1)
        self.assertAlmostEqual(p2.y, 1)
        self.assertAlmostEqual(p2.z, 0)

    def test_2(self):
        cyli = Cylinder(Point(0, 0, 0), Point(0, 2, 0), 1)
        line = Line(Point(-2, 2, 0), Vector(1, 0, 0))

        p1, p2 = solve(cyli, line)

        self.assertAlmostEqual(p1.x, -1)
        self.assertAlmostEqual(p1.y, 2)
        self.assertAlmostEqual(p1.z, 0)

        self.assertAlmostEqual(p2.x, 1)
        self.assertAlmostEqual(p2.y, 2)
        self.assertAlmostEqual(p2.z, 0)

    def test_3(self):
        cyli = Cylinder(Point(0, 0, 0), Point(0, 2, 0), 1)
        line = Line(Point(-2, 3, 0), Vector(1, 0, 0))

        result = solve(cyli, line)

        self.assertIsNone(result)

    def test_4(self):
        cyli = Cylinder(Point(1, 0, 1), Point(1, 2, 1), 1)
        line = Line(Point(0, 1, 0), Vector(0, 0, 1))

        p1 = solve(cyli, line)

        self.assertAlmostEqual(p1.x, 0)
        self.assertAlmostEqual(p1.y, 1)
        self.assertAlmostEqual(p1.z, 1)

    def test_5(self):
        cyli = Cylinder(Point(1, 0, 1), Point(1, 2, 1), 1)
        line = Line(Point(0, 0, 0), Vector(0, 0, 1))

        p1 = solve(cyli, line)

        self.assertAlmostEqual(p1.x, 0)
        self.assertAlmostEqual(p1.y, 0)
        self.assertAlmostEqual(p1.z, 1)

    def test_6(self):
        cyli = Cylinder(Point(1, 0, 1), Point(1, 2, 1), 1)
        line = Line(Point(-1, 1, 0), Vector(0, 0, 1))

        result = solve(cyli, line)

        self.assertIsNone(result)

    def test_7(self):
        cyli = Cylinder(Point(1, 0, 1), Point(1, 2, 1), 1)
        line = Line(Point(0, 0, 0), Vector(0, 1, 1))

        p1 = solve(cyli, line)

        self.assertAlmostEqual(p1.x, 0)
        self.assertAlmostEqual(p1.y, 1)
        self.assertAlmostEqual(p1.z, 1)

    def test_8(self):
        cyli = Cylinder(Point(0, 0, 2), Point(0, 1, 2), 1)
        line = Line(Point(0, 0, 0), Vector(0, 1, 1))

        p1 = solve(cyli, line)

        self.assertAlmostEqual(p1.x, 0)
        self.assertAlmostEqual(p1.y, 1)
        self.assertAlmostEqual(p1.z, 1)

    def test_9(self):
        cyli = Cylinder(Point(0, 0, 3), Point(0, 1, 3), 1)
        line = Line(Point(0, 0, 0), Vector(0, 1, 1))

        result = solve(cyli, line)

        self.assertIsNone(result)

    def test_10(self):
        cyli = Cylinder(Point(0, 0, 2), Point(0, 1, 2), 1)
        line = Line(Point(0, 0, 0), Vector(0, 1, 0))

        result = solve(cyli, line)

        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
