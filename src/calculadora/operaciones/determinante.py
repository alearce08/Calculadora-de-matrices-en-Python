import numpy as np

from calculadora.operacion import Operacion


class Determinante(Operacion):
    """Calcula el determinante de dos matrices."""

    def __init__(self):
        self.matrices = [None, None]

    def SetMatrix(self, index, matrix):
        """Guarda una de las matrices que se van a utilizar."""
        if index not in (0, 1):
            raise IndexError("El índice debe ser 0 o 1")

        self.matrices[index] = matrix

    def Compute(self):
        """Calcula y devuelve el determinante de las dos matrices."""
        if any(matrix is None for matrix in self.matrices):
            raise ValueError("Se necesitan dos matrices")

        resultados = {}
        nombres = ("matrixA", "matrixB")

        for nombre, matrix in zip(nombres, self.matrices):
            if matrix["rows"] != matrix["cols"]:
                raise ValueError(f"{nombre} debe ser cuadrada")

            data = np.array(matrix["data"], dtype=float)
            result = np.linalg.det(data)

            if np.isclose(result, 0):
                result = 0.0

            resultados[nombre] = round(float(result), 10)

        return resultados

    def Clear(self):
        """Elimina las matrices guardadas."""
        self.matrices = [None, None]
