# Programa 3: Matriz 3D de temperaturas en ciudades

# Matriz 3D: ciudades x días x semanas
# ciudades = ["Quito", "Guayaquil"]
# días = ["Lunes", "Martes", "Miércoles"]
# semanas = 2 semanas

temperaturas = [
    [   # Quito
        [15, 16],  # Lunes (semana 1 y 2)
        [17, 18],  # Martes
        [19, 20]   # Miércoles
    ],
    [   # Guayaquil
        [28, 29],  # Lunes
        [30, 31],  # Martes
        [32, 33]   # Miércoles
    ]
]

ciudades = ["Quito", "Guayaquil"]
dias = ["Lunes", "Martes", "Miércoles"]
num_semanas = 2

print("=== Temperaturas registradas ===\n")
for i, ciudad in enumerate(ciudades):
    print(f"Ciudad: {ciudad}")
    for semana in range(num_semanas):
        print(f"  Semana {semana + 1}:")
        for dia in range(len(dias)):
            print(f"    {dias[dia]}: {temperaturas[i][dia][semana]} °C")
    print()

print("=== Promedio de temperaturas por ciudad y semana ===\n")
# Recorremos ciudades
for i, ciudad in enumerate(ciudades):
    print(f"Ciudad: {ciudad}")
    # Recorremos semanas
    for semana in range(num_semanas):
        suma = 0
        contador = 0
        # Recorremos días
        for dia in range(len(dias)):
            temp = temperaturas[i][dia][semana]
            suma += temp
            contador += 1
        promedio = suma / contador
        print(f"  Semana {semana + 1}: {promedio:.2f} °C")
    print()
