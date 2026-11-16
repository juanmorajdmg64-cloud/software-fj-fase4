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


class ReservaSala(Servicio):

    def __init__(self, nombre, tarifa_base, horas):

        super().__init__(nombre, tarifa_base)

        if horas <= 0:
            raise ServicioError(
                "Las horas deben ser mayores que cero."
            )

        self.horas = horas

    def calcular_costo(self):
        return self.tarifa_base * self.horas

    def describir(self):
        return (
            f"Reserva de sala por "
            f"{self.horas} horas."
        )


class AlquilerEquipo(Servicio):

    def __init__(self, nombre, tarifa_base, dias):

        super().__init__(nombre, tarifa_base)

        if dias <= 0:
            raise ServicioError(
                "Los dias deben ser mayores que cero."
            )

        self.dias = dias

    def calcular_costo(self):
        return self.tarifa_base * self.dias

    def describir(self):
        return (
            f"Alquiler de equipo por "
            f"{self.dias} dias."
        )

class AsesoriaEspecializada(Servicio):

    def __init__(self, nombre, tarifa_base, horas, nivel):

        super().__init__(nombre, tarifa_base)

        if horas <= 0:
            raise ServicioError(
                "Las horas deben ser mayores que cero."
            )

        self.horas = horas
        self.nivel = nivel

    def calcular_costo(self):

        factores = {
            "basico": 1,
            "intermedio": 1.5,
            "avanzado": 2
        }

        return (
            self.tarifa_base *
            self.horas *
            factores.get(
                self.nivel.lower(), 1
            )
        )

    def describir(self):
        return (
            f"Asesoria {self.nivel} "
            f"de {self.horas} horas."
        )
