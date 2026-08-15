import numpy as np

from calculadora.operacion import Operacion


class Inversa(Operacion):
    """Calcula la inversa de dos matrices."""

    def __init__(self):
        self.matrices = [None, None]

    def SetMatrix(self, index, matrix):
        """Guarda una de las matrices que se van a utilizar."""
        if index not in (0, 1):
            raise IndexError("El índice debe ser 0 o 1")

        self.matrices[index] = matrix

    def Compute(self):
        """Calcula y devuelve la inversa de las dos matrices."""
        if any(matrix is None for matrix in self.matrices):
            raise ValueError("Se necesitan dos matrices")

        resultados = {}
        nombres = ("matrixA", "matrixB")

        for nombre, matrix in zip(nombres, self.matrices):
            if matrix["rows"] != matrix["cols"]:
                raise ValueError(f"{nombre} debe ser cuadrada")

            data = np.array(matrix["data"], dtype=float)
            determinant = np.linalg.det(data)

            if np.isclose(determinant, 0):
                raise ValueError(f"{nombre} no tiene inversa")

            result = np.linalg.inv(data)
            result = np.round(result, 10)

            resultados[nombre] = {
                "rows": matrix["rows"],
                "cols": matrix["cols"],
                "data": result.tolist(),
            }

        return resultados

    def Clear(self):
        """Elimina las matrices guardadas."""
        self.matrices = [None, None]
