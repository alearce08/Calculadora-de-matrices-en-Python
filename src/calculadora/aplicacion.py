from calculadora.operaciones.determinante import Determinante
from calculadora.operaciones.inversa import Inversa
from calculadora.operaciones.multiplicacion import Multiplicacion
from calculadora.operaciones.suma import Suma


class Aplicacion:
    """Administra las operaciones disponibles en la calculadora."""

    def __init__(self):
        self.operaciones = {
            "suma": Suma(),
            "multiplicacion": Multiplicacion(),
            "determinante": Determinante(),
            "inversa": Inversa(),
        }

    def ejecutar(self, nombre, matrices):
        """Ejecuta la operación seleccionada."""
        if nombre not in self.operaciones:
            raise ValueError("La operación solicitada no existe")

        operacion = self.operaciones[nombre]
        operacion.Clear()

        for index, matrix in enumerate(matrices):
            operacion.SetMatrix(index, matrix)

        result = operacion.Compute()
        operacion.Clear()

        return result
