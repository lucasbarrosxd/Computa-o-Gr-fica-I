"""
Trabalho 1 - 06/08/2019

Dados dois vetores v e w, calcular os pontos P1 e P2 tal que P1 está na reta Rv = (O, v), P2 está na reta Rw = (O, w),
o segmento de reta P1P2 é perpendicular à reta Rv e a distância entre P1 e P2 é L.
"""

# Importar arquivos do projeto.
from python.raycaster.physics import Point, Vector, Line
# Importar bibliotecas.
import math
import unittest

"""
SOLUÇÃO:

Iniciamos o problema com as seguintes equações:

    P1 = O + t * v
(1) P1 = t * v                     // Equação da reta de suporte do vetor v.
    P2 = O + s * w
(2) P2 = s * w                     // Equação da reta de suporte do vetor w.
(3) P1P2 • v = 0                   // Produto escalar de vetores perpendiculares é zero.
(4) ||P1P2|| = L                   // Distância entre os pontos P1 e P2 é L.

Podemos começar desenvolvendo (3) e (4), pois são as equações que contém informações sobre os dois pontos:
    
(3) P1P2 • v = 0
    (P2 - P1) • v = 0
    (s * w - t * v) • v = 0
    s * v • w - t * v • v = 0
    s = t * v • v / v • w         ⬌ v • w ≠ 0
    
(4) ||P1P2|| = L
    P1P2 • P1P2 = L²
    (P2 - P1) • (P2 - P1) = L²
    (s * w - t * v) • (s * w - t * v) = L²
    s² * w • w - 2st * w • v + t² * v • v = L²
    t² * ((w • w) * (v • v)² / (v • w)² - (v • v)) = L²                          ⬌ v • w ≠ 0                   // Substituindo por (3)
    t² * ((w • w) * (v • v)² - (v • v) * (v • w)²) = L² * (v • w)²               ⬌ v • w ≠ 0
    t² = L² * (v • w)² / ((w • w) * (v • v)² - (v • v) * (v • w)²)               ⬌ v • w ≠ 0, v ≠ 0, w ≠ 0
    t = ± sqrt((L² * (v • w)²) / ((v • v) * ((w • w) * (v • v) - (v • w)²)))     ⬌ v • w ≠ 0, v ≠ 0, w ≠ 0, (w • w) * (v • v) - (v • w)² ≥ 0
    t = ± L * v • w / sqrt((v • v) * ((w • w) * (v • v) - (v • w)²))             ⬌ v • w ≠ 0, v ≠ 0, w ≠ 0, (w • w) * (v • v) - (v • w)² ≥ 0
    
Agora que temos o coeficiente t, podemos calcular o coeficiente s:

    s = t * v • v / v • w                                                ⬌ v • w ≠ 0
    s = ± L * v • v / sqrt((v • v) * ((w • w) * (v • v) - (v • w)²))     ⬌ v • w ≠ 0, v ≠ 0, w ≠ 0, (w • w) * (v • v) - (v • w)² ≥ 0
    s = ± L * sqrt((v • v) / ((w • w) * (v • v) - (v • w)²))             ⬌ v • w ≠ 0, v ≠ 0, w ≠ 0, (w • w) * (v • v) - (v • w)² ≥ 0

Agora basta substituí-los nas equações de reta para encontrar os pontos P1 e P2, mas ainda é necessário verificar os
casos não válidos:

v = 0:
    P1 = t * v                                     // Equação antes de introduzirmos '⬌ v ≠ 0'.
    P1 = t * 0
    P1 = 0                                         // Para qualquer valor de t.
    
    s² * w • w - 2st * w • v + t² * v • v = L²     // Equação antes de introduzirmos '⬌ v ≠ 0'.
    s² * w • w - 2st * 0 + t² * 0 = L²
    s² * w • w = L²
    s² = L² / w • w                                ⬌ w ≠ 0
    s = ± sqrt(L² / w • w)                         ⬌ w ≠ 0
    s = ± L * sqrt(1 / w • w)                      ⬌ w ≠ 0
    
    w = 0:
        s² * w • w = L²                            // Equação antes de introduzirmos '⬌ w ≠ 0'.
        s² * 0 = L²
        0 = L²
        
        Caso 0 = L², quaisquer valores de t e s são soluções.

w = 0:
    P2 = s * w                                     // Equação antes de introduzirmos '⬌ w ≠ 0'.
    P2 = s * 0
    P2 = 0                                         // Para qualquer valor de s.
    
    s² * w • w - 2st * w • v + t² * v • v = L²     // Equação antes de introduzirmos '⬌ w ≠ 0'.
    s² * 0 - 2st * 0 + t² * v • v = L²
    t² * v • v = L²
    t² = L² / v • v                                ⬌ w ≠ 0
    t = ± sqrt(L² / v • w)
    

Daqui é possível calcular t e s e solucionar o problema, mas é necessário alguns cuidados matemáticos:

  - Os coeficientes t e s são descritos por equações que possuem denominadores que podem ser iguais a zero. Caso
    isso aconteça, eles têm que ser solucionados de outra forma.
  - A equação (3) possui um denominador que pode ser igual a zero. Caso isso aconteça, é necessário analisar a
    equação para ver se ela é solucionável.

Para que aconteça o primeiro caso, é necessário que um dos dois denominadores seja zero:

    sqrt((v.v) * ((w.w) * (v.v) - (v.w)²))      // Denominador do coeficiente t
    sqrt((w.w) * (v.v) - (v.w)²)                // Denominador do coeficiente s

Para que aconteça o segundo caso, é necessário que o denominador de (3) seja zero:

    v.w                                         // Denominador de (3)

Analisando as equações acima, é fácil ver duas situações em que pelo menos uma das equações zera:

  - v = (0, 0, 0)     // v.v = 0, v.w = 0, w.w * v.v - (v.w)² = 0
  - w = (0, 0, 0)     // v.w = 0, w.w * v.v - (v.w)² = 0

Para v.v e v.w não há outros casos, mas para a equação w.w * v.v - (v.w)² = 0 é possível que ainda existam
outros casos em que v ≠ 0 e w ≠ 0, então vamos analisá-la:

    w.w * v.v - (v.w)² = 0
    w.w * v.v = v.w) * v.w

Vamos supor que a v = (a, b, c) e w = (d, e, f):

    v.v = a² + b² + c²
    w.w = d² + e² + f²
    v.w = ad + be + cf

Podemos substituir os valores na equação calculada previamente:

    (d² + e² + f²) * (a² + b² + c²) = (ad + be + cf)²
    a²d² + b²d² + c²d² + a²e² + b²e² + c²e² + a²f² + b²f² + c²f² = a²d² + b²e² + c²f² + 2abde + 2acdf + 2bcef
    b²d² + c²d² + a²e² + c²e² + a²f² + b²f² = 2abde + 2acdf + 2bcef
    (b²d² - 2abde + a²e²) + (c²d² - 2acdf + a²f²) + (c²e² - 2bcef + b²f²) = 0
    (bd - ae)² + (cd - af)² + (ce - bf)² = 0

Como um quadrado de qualquer número real é sempre maior ou igual a zero, para que a equação acima seja verdadeira é
necessário que todos os termos dentro dos quadrados sejam iguais a zero:

    bd - ae = 0
    cd - af = 0
    ce - bf = 0

É fácil ver que v = 0, (a, b, c) = (0, 0, 0) e w = 0, (d, e, f) = (0, 0, 0) satisfazem as equações acima, como já
haviamos determinado antes. Mas as equações acima podem ser desenvolvidas para:

    a/d = b/e = c/f

O que significa que v e w são paralelos. Logo, quando v e w são paralelos, não é possível resolver as equações dos
coeficientes t e s.

Agora achamos todos os casos que invalidam a nossa solução inicial:

  - Quando v ou w = 0
  - Quando v e w são paralelos

Quando v ou w são paralelos, apesar das equações dos coeficientes t e s não poderem ser solucionadas, antes disso
ocorre que a equação que encontramos em (3) não é solucionável, logo temos que analisá-la para ver o que acontece:

Quando v = 0:
    s = t * v.v / v.w     // A equação deixa de ser do primeiro grau, resolvemos a equação de grau zero.
    s * v.w - t * v.v = 0
    s * 0 - t * v.v = 0
    - t * v.v = 0

Caso - t * v.v = 0, qualquer valor de s é solução para (3) (note que não resolvemos (4) ainda). Como v.v = 0, a
equação é sempre 0 (note que o coeficiente t é indeterminado, qualquer valor de t é solução). Finalmente, vamos para
(4). Não podemos substituir (3) em (4), logo resolvemos (4) a partir do momento antes da substituição:

    s² * w.w - 2st * w.v + t² * v.v = L²
    s² * w.w - 2st * 0 + t² * 0 = L²
    s² * w.w = L²
    s = ± L / sqrt(w.w)

Quando v = 0, encontramos que t pode ser qualquer valor, e s = ± L / sqrt(w.w). Note que s possui w em seu denominador,
logo quando w = 0 (único cenário em que esse denominador pode zerar) a equação deixa de ser do 1º grau e temos que
resolver a equação de grau zero:

    s * sqrt(w.w) ± L = 0
    s * 0 ± L = 0
    ± L = 0

Logo, quando L = 0, qualquer valor de s é solução. Quando L ≠ 0, nenhum valor de s é solução.

Quando w = 0:
    s = t * v.v / v.w     // A equação deixa de ser do primeiro grau, resolvemos a equação de grau zero.
    s * v.w - t * v.v = 0
    s * 0 - t * v.v = 0
    - t * v.v = 0

Quando t = 0 e/ou v = 0, qualquer valor de s é solução. Caso contrário, nenhum valor de s é solução. Lembrando que
ainda não analisamos (4):

    s² * w.w - 2st * w.v + t² * v.v = L²
    s² * 0 - 2st * 0 + t² * v.v = L²
    t² * v.v = L²

Já vimos que s só possui solução quando v = 0, logo t² * v.v = 0:

    0 = L²

Logo, s

    t = ± L * v.w / sqrt((v.v) * ((w.w) * (v.v) - (v.w)²))

O denominador é zero
    

Mas ainda há outra coisa que é necessário verificar. Os coeficientes t e w possuem raízes quadradas nas suas resoluções,
e caso o valor dentro dessas raízes seja menor que zero, não é possível resolvê-las com números reais. Logo temos que
verificar.

Raiz na solução de t:

    sqrt((v.w)² / ((w.w) * (v.v)² - (v.v) * (v.w)²))

O numerador é um quadrado, logo é sempre positivo, e já vimos quando v e w foram substituídos por triplas, que o
denominador é sempre maior ou igual a zero, logo não há problema aqui.

Raiz na solução de s:

    sqrt((v.v) / ((w.w) * (v.v) - (v.w)²))

Novamente, o denominador é sempre maior ou igual a zero. O numerador é o produto escalar de um vetor por ele mesmo,
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

        (pv1, pw1), (pv2, pw2) = solve(v, w, 10)

        self.assertAlmostEqual(pv1.x, 5 * math.sqrt(2))
        self.assertAlmostEqual(pv1.y, 5 * math.sqrt(2))
        self.assertAlmostEqual(pv1.z, 0)

        self.assertAlmostEqual(pw1.x, 10 * math.sqrt(2))
        self.assertAlmostEqual(pw1.y, 0)
        self.assertAlmostEqual(pw1.z, 0)

        self.assertAlmostEqual(pv2.x, -5 * math.sqrt(2))
        self.assertAlmostEqual(pv2.y, -5 * math.sqrt(2))
        self.assertAlmostEqual(pv2.z, 0)

        self.assertAlmostEqual(pw2.x, -10 * math.sqrt(2))
        self.assertAlmostEqual(pw2.y, 0)
        self.assertAlmostEqual(pw2.z, 0)

    def test_2(self):
        v = Vector(1, 0, 0)
        w = Vector(2, 0, 0)

        result = solve(v, w, 1)

        self.assertIsNone(result)

    def test_3(self):
        v = Vector(1, 0, 0)
        w = Vector(0, 1, 0)

        (pv1, pw1), (pv2, pw2) = solve(v, w, 100)

        self.assertAlmostEqual(pv1.x, 0)
        self.assertAlmostEqual(pv1.y, 0)
        self.assertAlmostEqual(pv1.z, 0)

        self.assertAlmostEqual(pw1.x, 0)
        self.assertAlmostEqual(pw1.y, 100)
        self.assertAlmostEqual(pw1.z, 0)

        self.assertAlmostEqual(pv2.x, 0)
        self.assertAlmostEqual(pv2.y, 0)
        self.assertAlmostEqual(pv2.z, 0)

        self.assertAlmostEqual(pw2.x, 0)
        self.assertAlmostEqual(pw2.y, -100)
        self.assertAlmostEqual(pw2.z, 0)

    def test_4(self):
        v = Vector(3, 4, 0)
        w = Vector(1, 0, 0)

        (pv1, pw1), (pv2, pw2) = solve(v, w, 100)

        self.assertAlmostEqual(pv1.x, 45)
        self.assertAlmostEqual(pv1.y, 60)
        self.assertAlmostEqual(pv1.z, 0)

        self.assertAlmostEqual(pw1.x, 125)
        self.assertAlmostEqual(pw1.y, 0)
        self.assertAlmostEqual(pw1.z, 0)

        self.assertAlmostEqual(pv2.x, -45)
        self.assertAlmostEqual(pv2.y, -60)
        self.assertAlmostEqual(pv2.z, 0)

        self.assertAlmostEqual(pw2.x, -125)
        self.assertAlmostEqual(pw2.y, 0)
        self.assertAlmostEqual(pw2.z, 0)
