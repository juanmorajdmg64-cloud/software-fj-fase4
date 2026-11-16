from servicios import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)

print("=== SOFTWARE FJ ===")

servicios = [
    ReservaSala("Sala Innovacion", 20000, 3),
    AlquilerEquipo("Portatil Lenovo", 15000, 2),
    AsesoriaEspecializada(
        "Python Avanzado",
        30000,
        2,
        "avanzado"
    )
]

for servicio in servicios:

    print("\n------------------")
    print(servicio.describir())
    print(
        f"Costo: ${servicio.calcular_costo():,.0f}"
    )
