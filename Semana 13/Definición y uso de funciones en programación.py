# temperaturas.py

# Este programa calcula la temperatura promedio de varias ciudades
# en un periodo de semanas.
# Ejemplo: Quito, Guayaquil y Cuenca durante 4 semanas.

def calcular_promedio_temperaturas(datos):
    """
    Función que recibe un diccionario con temperaturas semanales de ciudades
    y devuelve el promedio de cada ciudad.
    """
    promedios = {}

    for ciudad, semanas in datos.items():
        # Unimos todas las temperaturas de todas las semanas en una sola lista
        todas_temperaturas = [temp for semana in semanas for temp in semana]

        # Calculamos el promedio
        promedio = sum(todas_temperaturas) / len(todas_temperaturas)
        promedios[ciudad] = promedio

    return promedios


# Ejemplo de uso
if __name__ == "__main__":
    # Datos de ejemplo: 3 ciudades, 4 semanas, cada semana con 7 días
    datos_temperaturas = {
        "Quito": [
            [18, 19, 20, 21, 18, 19, 20],
            [19, 20, 21, 22, 19, 18, 20],
            [18, 19, 20, 19, 20, 21, 19],
            [20, 21, 22, 21, 20, 19, 20],
        ],
        "Guayaquil": [
            [28, 29, 30, 31, 29, 30, 31],
            [30, 31, 32, 30, 31, 29, 30],
            [29, 30, 31, 30, 31, 32, 30],
            [31, 32, 33, 31, 32, 30, 31],
        ],
        "Cuenca": [
            [16, 17, 18, 17, 16, 17, 18],
            [17, 18, 19, 18, 17, 16, 17],
            [18, 19, 20, 19, 18, 17, 18],
            [19, 20, 21, 20, 19, 18, 19],
        ]
    }

    # Llamamos a la función
    promedios = calcular_promedio_temperaturas(datos_temperaturas)

    # Mostramos los resultados
    print("Resultados de temperaturas promedio:")
    for ciudad, promedio in promedios.items():
        print(f"{ciudad}: {promedio:.2f}°C")
