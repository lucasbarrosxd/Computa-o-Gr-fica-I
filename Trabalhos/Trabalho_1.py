"""
Trabalho 1 - 06/08/2019

Dados dois vetores V e W, calcular os pontos P1 e P2 tal que P1 está na reta de suporte do vetor V, P2
está na reta de suporte do vetor W, o segmento de reta P1P2 é perpendicular à reta de suporte do vetor V, e
a distância entre P1 e P2 é L.
"""

# Importar arquivos do projeto.
from python.raycaster.basic import Point, Vector, Line
# Importar bibliotecas.
import math
import unittest

"""
SOLUÇÃO:

Uma reta em um espaço tri-dimensional pode ser representada através de um ponto que está sobre essa reta, e
um vetor que represente sua direção. Como vetores sempre utilizam a origem como ponto de referência, as retas de
suporte dos vetores v e w ambas passam pelo ponto (0, 0, 0). As direções das retas de suporte são os próprios vetores
v e w. Logo podemos montar as duas equações de reta:

OP1:
    P = O + t * v, onde t é um coeficiente qualquer para se determinar um ponto sobre a reta.
(1) P = t * v

OP2:
    P = O + s * w, onde s é um coeficiente qualquer para se determinar um ponto sobre a reta.
(2) P = s * w

    Outra informação que nós temos é que o segmento P1P2 é perpendicular ao vetor v:

(3) P1P2.v = 0

    E finalmente, o tamanho do segmento P1P2 é igual a L:
    
(4) ||P1P2|| = L

    Podemos começar desenvolvendo (3) e (4), pois são as equações que contém informações sobre os dois pontos:
    
(3) P1P2.v = 0
    (P2 - P1).v = 0
    (s * w - t * v).v = 0
    s * v.w - t * v.v = 0
    s = t * v.v / v.w
    
(4) ||P1P2|| = L
    P1P2.P1P2 = L²
    (P2 - P1).(P2 - P1) = L²
    (s * w - t * v).(s * w - t * v) = L²
    s² * w.w - 2st * w.v + t² * v.v = L²
    t² * (w.w) * (v.v)² / (v.w)² - 2t² * (w.v) * (v.v) / (v.w) + t² * (v.v) = L²     // substituindo s
    t² * ((w.w) * (v.v)² / (v.w)² - (v.v)) = L²
    t = ± sqrt((L² * (v.w)²) / ((w.w) * (v.v)² - (v.v) * (v.w)²))
    t = ± L * sqrt((v.w)² / ((w.w) * (v.v)² - (v.v) * (v.w)²))
    
Agora que temos o coeficiente t, podemos calcular o coeficiente s:

    s = t * v.v / v.w
    s = (± L) * sqrt((v.w)² / ((w.w) * (v.v)² - (v.v) * (v.w)²)) * v.v / v.w
    s = ± L * sqrt((v.v) / ((w.w) * (v.v) - (v.w)²))
    
Só temos que prestar atenção em algumas ressalvas: primeiro, as duas equações de t e s possuem denominadores:

t:
    (v.v) * ((w.w) * (v.v) - (v.w)²)

s:
    (w.w) * (v.v) - (v.w)²

Caso resulte em zero, é impossível resolver a equação, o que implicaria que não existe P1 ou P2 que satisfaça todos os
requisitos do problema.

Em t, há duas partes que caso sejam iguais a zero, zerariam o denominador:

    (v.v)
    ((w.w) * (v.v) - (v.w)²)
    
Felizmente, (v.v) nunca é zero para qualquer vetor, mas ainda temos de analisar a segunda equação:

    (w.w) * (v.v) - (v.w)² = 0              // suposição
    (w.w) * (v.v) = (v.w) * (v.w)

Aqui fica um pouco mais complicado... Vamos supor que a tripla (a, b, c) = v e a tripla (d, e, f) = w, logo:

    (v.v) = a² + b² + c²
    (w.w) = d² + e² + f²
    (v.w) = ad + be + cf

Podemos substituir os valores na equação calculada previamente:

    (d² + e² + f²) * (a² + b² + c²) = (ad + be + cf)²
    a²d² + b²d² + c²d² + a²e² + b²e² + c²e² + a²f² + b²f² + c²f² = a²d² + b²e² + c²f² + 2abde + 2acdf + 2bcef
    b²d² + c²d² + a²e² + c²e² + a²f² + b²f² = 2abde + 2acdf + 2bcef
    (b²d² - 2abde + a²e²) + (c²d² - 2acdf + a²f²) + (c²e² - 2bcef + b²f²) = 0
    (bd - ae)² + (cd - af)² + (ce - bf)² = 0

Como um quadrado de qualquer é número é sempre maior ou igual a zero, para que a equação acima seja verdadeira é
necessário que todos os termos dentro dos quadrados sejam iguais a zero:

    bd - ae = 0
    cd - af = 0
    ce - bf = 0

Essas equações podem ser desenvolvidas para:

    a/d = b/e = c/f

O que implica que os vetores são colineares. Ou seja, voltando lá pra trás, esse é o único jeito de não haver solução
para t. Acontece que para s é o mesmo caso, pois o denominador de s possui a mesma equação. Em resumo, o único jeito
de não haver solução para P1 e P2 por conta do denominador é caso v e w sejam colineares.

Mas ainda há outra coisa que é necessário verificar. Os coeficientes t e w possuem raízes quadradas nas suas resoluções,
e caso o valor dentro dessas raízes seja menor que zero, não é possível resolvê-las com números reais. Logo temos que
verificar.

Raiz na solução de t:

    sqrt((v.w)² / ((w.w) * (v.v)² - (v.v) * (v.w)²))

O numerador é um quadrado, logo é sempre positivo, e já vimos quando v e w foram substituídos por triplas, que o
denominador é sempre maior ou igual a zero, logo não há problema aqui.

Raiz na solução de s:

    sqrt((v.v) / ((w.w) * (v.v) - (v.w)²))

Novamente, o denominador é sempre maior ou igual a zero. O numerados é o produto escalar de um vetor por ele mesmo,
então também é sempre maior ou igual a zero. Também não há problemas aqui.

Agora que encontramos e validamos t e s, basta substituí-los nas suas equações de reta para encontrar os pontos.
"""


def solve(vector1, vector2, distance):
    if not isinstance(vector1, Vector):
        raise TypeError("Argumento 'vector1' deve ser de tipo 'Vector'.")
    if not isinstance(vector2, Vector):
        raise TypeError("Argumento 'vector2' deve ser de tipo 'Vector'.")
    if not (isinstance(distance, (int, float, complex)) and not isinstance(distance, bool)):
        raise TypeError("Argumento 'distance' deve ser de tipo numérico.")

    v = vector1
    w = vector2

    if math.isclose((v * v) * (w * w), (v * w) ** 2):
        # Não há solução pois os vetores são colineares.
        return None
    else:
        t = distance * math.sqrt(((v * w) ** 2) / ((v * v) * ((w * w) * (v * v) - ((v * w) ** 2))))
        s = distance * math.sqrt((v * v) / ((w * w) * (v * v) - ((v * w) ** 2)))

        lv = Line(Point(0, 0, 0), v)
        lw = Line(Point(0, 0, 0), w)

        return (lv(t), lw(s)), (lv(-t), lw(-s))


class Tests(unittest.TestCase):
    def test_1(self):
        v = Vector(1, 1, 0)
        w = Vector(1, 0, 0)

        pair1, pair2 = solve(v, w, 10)
        p1, p2 = pair1
        p3, p4 = pair2

        self.assertAlmostEqual(p1.x, 5 * math.sqrt(2))
        self.assertAlmostEqual(p1.y, 5 * math.sqrt(2))
        self.assertAlmostEqual(p1.z, 0)

        self.assertAlmostEqual(p2.x, 10 * math.sqrt(2))
        self.assertAlmostEqual(p2.y, 0)
        self.assertAlmostEqual(p2.z, 0)

        self.assertAlmostEqual(p3.x, -5 * math.sqrt(2))
        self.assertAlmostEqual(p3.y, -5 * math.sqrt(2))
        self.assertAlmostEqual(p3.z, 0)

        self.assertAlmostEqual(p4.x, -10 * math.sqrt(2))
        self.assertAlmostEqual(p4.y, 0)
        self.assertAlmostEqual(p4.z, 0)


if __name__ == '__main__':
    unittest.main()
