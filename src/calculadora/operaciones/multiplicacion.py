from calculadora.operacion import Operacion


class Multiplicacion(Operacion):
    """Realiza la multiplicación de dos matrices."""

    def __init__(self):
        self.matrices = [None, None]

    def SetMatrix(self, index, matrix):
        """Guarda una de las matrices que se van a multiplicar."""
        if index not in (0, 1):
            raise IndexError("El índice debe ser 0 o 1")

        self.matrices[index] = matrix

    def Compute(self):
        """Multiplica las matrices y devuelve el resultado."""
        matrix_a = self.matrices[0]
        matrix_b = self.matrices[1]

        if matrix_a is None or matrix_b is None:
            raise ValueError("Se necesitan dos matrices para multiplicar")

        if matrix_a["cols"] != matrix_b["rows"]:
            raise ValueError("Las dimensiones de las matrices no son compatibles")

        data = []

        for row in range(matrix_a["rows"]):
            new_row = []

            for col in range(matrix_b["cols"]):
                value = 0

                for k in range(matrix_a["cols"]):
                    value += matrix_a["data"][row][k] * matrix_b["data"][k][col]

                new_row.append(value)

            data.append(new_row)

        return {
            "rows": matrix_a["rows"],
            "cols": matrix_b["cols"],
            "data": data,
        }

    def Clear(self):
        """Elimina las matrices guardadas."""
        self.matrices = [None, None]
