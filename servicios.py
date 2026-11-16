from abc import ABC, abstractmethod
from excepciones import ServicioError


class Servicio(ABC):
    """
    Clase abstracta que representa un servicio de Software FJ.
    """

    def __init__(self, nombre, tarifa_base):

        if not nombre.strip():
            raise ServicioError(
                "El nombre del servicio no puede estar vacío."
            )

        if tarifa_base <= 0:
            raise ServicioError(
                "La tarifa base debe ser mayor que cero."
            )

        self.nombre = nombre
        self.tarifa_base = tarifa_base

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def describir(self):
        pass
