import numpy as np

from calculadora.operacion import Operacion


class Inversa(Operacion):
    """Calcula la inversa de una matriz."""

    def __init__(self):
        self.matrix = None

    def SetMatrix(self, index, matrix):
        """Guarda la matriz que se va a utilizar."""
        if index != 0:
            raise IndexError("El índice debe ser 0")

        self.matrix = matrix

    def Compute(self):
        """Calcula y devuelve la matriz inversa."""
        if self.matrix is None:
            raise ValueError("Se necesita una matriz")

        if self.matrix["rows"] != self.matrix["cols"]:
            raise ValueError("La matriz debe ser cuadrada")

        data = np.array(self.matrix["data"], dtype=float)
        determinant = np.linalg.det(data)

        if np.isclose(determinant, 0):
            raise ValueError("La matriz no tiene inversa")

        result = np.linalg.inv(data)
        result = np.round(result, 10)

        return {
            "rows": self.matrix["rows"],
            "cols": self.matrix["cols"],
            "data": result.tolist(),
        }

    def Clear(self):
        """Elimina la matriz guardada."""
        self.matrix = None
