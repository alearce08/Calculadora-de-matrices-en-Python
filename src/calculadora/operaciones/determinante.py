import numpy as np

from calculadora.operacion import Operacion


class Determinante(Operacion):
    """Calcula el determinante de una matriz."""

    def __init__(self):
        self.matrix = None

    def SetMatrix(self, index, matrix):
        """Guarda la matriz que se va a utilizar."""
        if index != 0:
            raise IndexError("El índice debe ser 0")

        self.matrix = matrix

    def Compute(self):
        """Calcula y devuelve el determinante."""
        if self.matrix is None:
            raise ValueError("Se necesita una matriz")

        if self.matrix["rows"] != self.matrix["cols"]:
            raise ValueError("La matriz debe ser cuadrada")

        data = np.array(self.matrix["data"], dtype=float)
        result = np.linalg.det(data)

        if np.isclose(result, 0):
            result = 0.0

        return round(float(result), 10)

    def Clear(self):
        """Elimina la matriz guardada."""
        self.matrix = None
