from abc import ABC, abstractmethod


class Operacion(ABC):
    """Clase base para las operaciones con matrices."""

    @abstractmethod
    def SetMatrix(self, index, matrix):
        """Guarda una matriz en la posición indicada."""
        raise NotImplementedError

    @abstractmethod
    def Compute(self):
        """Realiza la operación con las matrices."""
        raise NotImplementedError

    @abstractmethod
    def Clear(self):
        """Limpia las matrices guardadas."""
        raise NotImplementedError
