class Vector:
    def __init__(self, dx, dy, dz):
        if not (isinstance(dx, (int, float, complex)) and not isinstance(dx, bool)):
            raise TypeError("Parâmetro 'dx' deve ser de tipo numérico.")
        if not (isinstance(dy, (int, float, complex)) and not isinstance(dy, bool)):
            raise TypeError("Parâmetro 'dy' deve ser de tipo numérico.")
        if not (isinstance(dz, (int, float, complex)) and not isinstance(dz, bool)):
            raise TypeError("Parâmetro 'dz' deve ser de tipo numérico.")

        # Checar se o vetor está sendo definido como (0, 0, 0).
        if dx == 0 and dy == 0 and dz == 0:
            raise ValueError("Vetor não pode ter todos os valores iguais a zero.")

        self._dx = dx
        self._dy = dy
        self._dz = dz
    
    @property
    def dx(self):
        return self._dx

    @dx.setter
    def dx(self, value):
        if not (isinstance(value, (int, float, complex)) and not isinstance(value, bool)):
            raise TypeError("Parâmetro 'dx' deve ser de tipo numérico.")

        # Checar se o vetor está sendo definido como (0, 0, 0).
        if value == 0 and self.dy == 0 and self.dz == 0:
            raise ValueError("Vetor não pode ter todos os valores iguais a zero.")

        self._dx = value

    @property
    def dy(self):
        return self._dy

    @dy.setter
    def dy(self, value):
        if not (isinstance(value, (int, float, complex)) and not isinstance(value, bool)):
            raise TypeError("Parâmetro 'dy' deve ser de tipo numérico.")

        # Checar se o vetor está sendo definido como (0, 0, 0).
        if value == 0 and self.dz == 0 and self.dx == 0:
            raise ValueError("Vetor não pode ter todos os valores iguais a zero.")

        self._dy = value

    @property
    def dz(self):
        return self._dz

    @dz.setter
    def dz(self, value):
        if not (isinstance(value, (int, float, complex)) and not isinstance(value, bool)):
            raise TypeError("Parâmetro 'dz' deve ser de tipo numérico.")

        # Checar se o vetor está sendo definido como (0, 0, 0).
        if value == 0 and self.dx == 0 and self.dy == 0:
            raise ValueError("Vetor não pode ter todos os valores iguais a zero.")

        self._dz = value

    def __str__(self):
        return "({0}, {1}, {2})".format(self.dx, self.dy, self.dz)

    def __add__(self, other):
        # Argumento é um vetor.
        if isinstance(other, Vector):
            # Adição de dois vetores.
            return Vector(self.dx + other.dx, self.dy + other.dy, self.dz + other.dz)
        else:
            raise TypeError(
                "Classe '{0}' não possui suporte para adição com objetos de tipo '{1}'."
                .format(self.__class__.__name__, type(other))
            )

    def __radd__(self, other):
        # Delegar para outro método.
        return self.__add__(other)

    def __iadd__(self, other):
        # Delegar para outro método.
        self.__add__(other)

    def __mul__(self, other):
        # Argumento é um vetor.
        if isinstance(other, Vector):
            # Produto escalar de dois vetores.
            return scalar_prod(self, other)
        # Argumento é um número.
        elif isinstance(other, (int, float, complex)) and not isinstance(other, bool):
            # Produto de um escalar por um vetor.
            return Vector(self.dx * other, self.dy * other, self.dz * other)
        else:
            raise TypeError(
                "Classe '{0}' não possui suporte para multiplicação com objetos de tipo '{1}'."
                .format(self.__class__.__name__, type(other))
            )

    def __rmul__(self, other):
        # Delegar para outro método.
        return self.__mul__(other)

    def __imul__(self, other):
        # Delegar para outro método.
        self.__mul__(other)

    def __truediv__(self, other):
        # Argumento é um número.
        if isinstance(other, (int, float, complex)) and not isinstance(other, bool):
            # Divisão de um vetor por um escalar.
            return Vector(self.dx / other, self.dy / other, self.dz / other)
        else:
            raise TypeError(
                "Classe '{0}' não possui suporte para divisão com objetos de tipo '{1}'."
                .format(self.__class__.__name__, type(other))
            )

    def __itruediv__(self, other):
        # Delegar para outro método.
        self.__truediv__(other)

    def __pow__(self, other):
        # Argumento é um vetor.
        if isinstance(other, Vector):
            # Produto vetorial de dois vetores.
            return cross_prod(self, other)
        else:
            raise TypeError(
                "Classe '{0}' não possui suporte para produto vetorial com objetos de tipo '{1}'."
                .format(self.__class__.__name__, type(other))
            )

    def __ipow__(self, other):
        # Delegar para outro método.
        self.__pow__(other)

    def norm(self):
        return (self.dx ** 2 + self.dy ** 2 + self.dz ** 2) ** 0.5


def scalar_prod(vector1, vector2):
    if not isinstance(vector1, Vector):
        raise TypeError("Argumento 'vector1' deve ser de tipo 'Vector'.")
    if not isinstance(vector2, Vector):
        raise TypeError("Argumento 'vector2' deve ser de tipo 'Vector'.")

    return vector1.dx * vector2.dx + vector1.dy * vector2.dy + vector1.dz * vector2.dz


def cross_prod(vector1, vector2):
    if not isinstance(vector1, Vector):
        raise TypeError("Argumento 'vector1' deve ser de tipo 'Vector'.")
    if not isinstance(vector2, Vector):
        raise TypeError("Argumento 'vector2' deve ser de tipo 'Vector'.")

    try:
        return Vector(
            vector1.dy * vector2.dz - vector1.dz * vector2.dy,
            vector1.dz * vector2.dx - vector1.dx * vector2.dz,
            vector1.dx * vector2.dy - vector1.dy * vector2.dx
        )
    except ValueError:
        # Vetores são colineares, logo não existe produto vetorial.
        return None
