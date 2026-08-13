from calculadora.operacion import Operacion


class Suma(Operacion):
    """Realiza la suma de dos matrices."""

    def __init__(self):
        self.matrices = [None, None]

    def SetMatrix(self, index, matrix):
        """Guarda una de las matrices que se van a sumar."""
        if index not in (0, 1):
            raise IndexError("El índice debe ser 0 o 1")

        self.matrices[index] = matrix

    def Compute(self):
        """Suma las matrices y devuelve el resultado."""
        matrix_a = self.matrices[0]
        matrix_b = self.matrices[1]

        if matrix_a is None or matrix_b is None:
            raise ValueError("Se necesitan dos matrices para realizar la suma")

        if matrix_a["rows"] != matrix_b["rows"] or matrix_a["cols"] != matrix_b["cols"]:
            raise ValueError("Las matrices deben tener las mismas dimensiones")

        data = []

        for row in range(matrix_a["rows"]):
            new_row = []

            for col in range(matrix_a["cols"]):
                value = matrix_a["data"][row][col] + matrix_b["data"][row][col]
                new_row.append(value)

            data.append(new_row)

        return {
            "rows": matrix_a["rows"],
            "cols": matrix_a["cols"],
            "data": data,
        }

    def Clear(self):
        """Elimina las matrices guardadas."""
        self.matrices = [None, None]
