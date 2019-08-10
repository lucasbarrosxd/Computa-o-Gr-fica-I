"""
Trabalho 1 - 06/08/2019

Dados dois vetores V e W quaisquer, calcular dois pontos P1 e P2, tal que P1 está na reta de suporte do vetor V, P2
está na reta de suporte do vetor W, o segmento de reta P1P2 é perpendicular ao segmento de reta OP1, e a distância
entre P1 e P2 é dada por L.
"""

from python.raycaster.basic import Vector


def solve(vector_1, vector_2, distance):
    """Método para calcular os pontos P1 e P2 descritos na tarefa."""
    # Validação de argumentos.
    if not isinstance(vector_1, Vector):
        raise TypeError()

    """Uma reta em um espaço tri-dimensional pode ser representada através de um ponto que está sobre essa reta, e
    um vetor que represente sua direção. Como vetores sempre utilizam a origem como ponto de referência, as retas de
    apoio dos vetores V ambas passam pelo ponto (0, 0, 0). As direções das retas de suporte são os próprios vetores V e
    W. Logo podemos encontrar as duas equações de reta:
    
    OP1:
        P = O + t * V, onde t é um coeficiente qualquer para se determinar um ponto sobre a reta.
    (1) P = t * V
    
    OP2:
        P = O + s * W, onde s é um coeficiente qualquer para se determinar um ponto sobre a reta.
    (2) P = s * W
    
    Ainda há mais uma reta que podemos encontrar: a reta de suporte do segmento de reta P1P2. Primeiro, sabemos que
    esse segmento é perpendicular ao segmento OP1, logo o produto escalar entre os dois vetores é zero:
    
    (3) V . P1P2 = 0
    
    Também sabemos que o vetor P1P2 pode ser encontrado a partir da diferença dos dois pontos:
    
        P1P2 = P2 - P1
    (4) P1P2 = s * W - t * V  // substituindo por (1) e (2)
    
    Agora podemos substituir (4) em (3):
    
        V . P1P2 = 0
        V . (s * W - t * V) = 0
        s * (V . W) = t * (V . V)
    (5) t = s * (V . W) / (V . V)
    
    Agora, sabemos que o tamanho do segmento P1P2 é L, logo podemos calcular:
    
        ||P1P2|| = L
        P1P2 . P1P2 = L²
        (s * W - t * V) . (s * W - t * V) = L²
        s² * (W . W) - 2 * s * t * (V . W) + t² * (V . V) = L²
        s² * (W . W) - 2 * s² * (V . W)² / (V . V) + s² * (V . W)² / (V . V) = L²
        s² * ((W . W) * (V . V) - (V . W)²) / (V . V) = L²
    (6) s = ± sqrt(L² * (V . V) / ((W . W) * (V . V) - (V . W)²))
    
    Agora que temos, em (6), s a partir de elementos conhecidos, podemos encontrar s, consequentemente P2,
    consequentemente P1.
    """
