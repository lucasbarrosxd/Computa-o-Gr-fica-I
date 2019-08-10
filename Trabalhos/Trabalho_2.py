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

Primeiro, montando o problema melhor, vamos estabeler o vetor u = P1 - P0. Em seguida definimos o ponto P' que é a
projeção do ponto P sobre o vetor u. Agora já temos as seguintes equações:

(1) P = Pr + t * v      // Equação da reta R.
(2) P' = P0 + s * u     // Equação da reta do cilindro C/vetor u.
(3) ||PP'|| = r         // A distância entre P e P' é igual ao raio r do cilindro C.
(4) PP'.u = 0           // O vetor u é perpendicular ao vetor PP'.
(*) 0 <= s <= 1         // Garante que o ponto encontrado está no cilindro.

Agora podemos começar a resolver o problema. As equações de reta são mais complicadas de usar, então podemos começar
por (3) ou (4). No caso será usada a equação (3):

(3) ||PP'|| = r
    PP'.PP' = r²
    (P' - P).(P' - P) = r²
    (P0 + s * u - Pr - t * v).(P0 + s * u - Pr - t * v) = r²
    ((P0 - Pr) + s * u - t * v).((P0 - Pr) + s * u - t * v) = r²
    (PrP0 + s * u - t * v).(PrP0 + s * u - t * v) = r²                 // PrP0 = vetor w para faciliar os cálculos.
    w.w + s² * u.u + t² * v.v + 2s * w.u - 2t * w.v - 2ts * u.v = r²

Chegamos a um ponto em que só temos duas variáveis, t e s. Mas a equação está de forma quadrática, o que deixa difícil
calcular o valor de t. Vamos tentar desenvolver a equação (4):

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

Chegamos em uma equação de 2º grau. Agora podemos calcular o valor de t, mas com algumas ressalvas. Como sempre, o
valor de delta da equação deve ser analisado, pois para encontrar t precisamos do valor de ± sqrt(delta), logo:

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
coeficiente t, e consequentemente os possíveis valores de P. Mas ainda é necessário calcular se 0 <= s <= 1 para saber
se nossas respostas são válida.
"""


def solve(cylinder, line):
    if not isinstance(cylinder, Cylinder):
        raise TypeError("Argumento 'cylinder' deve ser de tipo 'Cylinder'.")
    if not isinstance(line, Line):
        raise TypeError("Argumento 'line' deve ser de tipo 'Line'.")

    v = line.direction
    u = cylinder.top - cylinder.bottom
    w = cylinder.bottom - line.origin

    delta = (w * v) ** 2 - 2 * (u * v) * (w * u) * (w * v) / (u * u) - (v * v) * (w * w) + (v * v) * (w * u) ** 2 / (
            u * u) + cylinder.radius ** 2 * ((v * v) - (u * v) ** 2 / (u * u)) + (w * w) * (u * v) ** 2 / (u * u)

    if delta < 0:
        # Não há interseção.
        return None
    else:
        t = ((w * v) - (u * v) * (w * u) / (u * u)) / ((v * v) - (u * v) ** 2 / (u * u))

        if math.isclose(delta, 0):
            # Há apenas uma interseção possível.
            s = (t * (v * u) - (w * u)) / (u * u)

            if 0 <= s <= 1:
                # A interseção é válida.
                return line(t)
            else:
                # A interseção não é válida.
                return None
        else:
            # Há duas interseções possíveis.
            t1 = t - math.sqrt(delta)
            t2 = t + math.sqrt(delta)

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
                # Nenhuma das interseções são válidas.
                return None


class Tests(unittest.TestCase):
    def test_1(self):
        cyli = Cylinder(Point(0, 0, 0), Point(0, 5, 0), 1)
        line = Line(Point(-2, 1, 0), Vector(1, 0, 0))

        p1, p2 = solve(cyli, line)

        # Validar p1
        self.assertAlmostEqual(p1.x, -1)
        self.assertAlmostEqual(p1.y, 1)
        self.assertAlmostEqual(p1.z, 0)

        # Validar p2
        self.assertAlmostEqual(p2.x, 1)
        self.assertAlmostEqual(p2.y, 1)
        self.assertAlmostEqual(p2.z, 0)


if __name__ == '__main__':
    unittest.main()
