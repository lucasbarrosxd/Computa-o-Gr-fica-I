# Importar bibliotecas.
# # Tipagem.
from numbers import Integral, Real
from typing import Text, Tuple, Union


class RGB:
    def __init__(self, r: Integral, g: Integral, b: Integral) -> None:
        self.r = r
        self.g = g
        self.b = b

    @property
    def r(self) -> Integral:
        return self._r

    @r.setter
    def r(self, value: Integral) -> None:
        self._r = max(0, min(value, 255))

    @property
    def g(self) -> Integral:
        return self._g

    @g.setter
    def g(self, value: Integral) -> None:
        self._g = max(0, min(value, 255))

    @property
    def b(self) -> Integral:
        return self._b

    @b.setter
    def b(self, value: Integral) -> None:
        self._b = max(0, min(value, 255))

    @property
    def tuple(self) -> Tuple[Integral, Integral, Integral]:
        return self.r, self.g, self.b

    @tuple.setter
    def tuple(self, value: Tuple[Integral, Integral, Integral]) -> None:
        self.r = value[0]
        self.g = value[1]
        self.b = value[2]

    @property
    def tuplef(self) -> Tuple[Real, Real, Real]:
        return self.r / 255, self.g / 255, self.b / 255

    @tuplef.setter
    def tuplef(self, value: Tuple[Real, Real, Real]):
        self.r = round(value[0] * 255)
        self.g = round(value[1] * 255)
        self.b = round(value[2] * 255)

    def __add__(self, other: "RGB") -> "RGB":
        # Verificar tipo do argumento.
        if isinstance(other, RGB):
            # Argumento é uma cor.
            # Soma de cores é uma cor.
            return RGB(self.r + other.r, self.g + other.g, self.b + other.b)
        else:
            raise TypeError(
                "Classe '{0}' não possui suporte para adição com objetos de tipo '{1}'."
                .format(self.__class__.__name__, type(other))
            )

    def __mul__(self, other: Union["RGB", Real]) -> "RGB":
        # Verificar tipo do argumento.
        if isinstance(other, RGB):
            # Argumento é uma cor.
            # Multiplicação dos componentes de cada cor é uma cor.
            return RGB(
                round(self.r * other.r / 255),
                round(self.g * other.g / 255),
                round(self.b * other.b / 255)
            )
        elif isinstance(other, Real):
            # Argumento é um número real.
            # Multiplicação dos componentes da cor por um coeficiente.
            return RGB(
                round(self.r * other),
                round(self.g * other),
                round(self.b * other)
            )
        else:
            raise TypeError(
                "Classe '{0}' não possui suporte para multiplicação com objetos de tipo '{1}'."
                .format(self.__class__.__name__, type(other))
            )

    __rmul__ = __mul__

    def __str__(self) -> Text:
        return "({0}, {1}, {2})".format(self.r, self.g, self.b)
