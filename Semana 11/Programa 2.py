# Programa 2: Ordenación de Arreglo Multidimensional

# Definimos la matriz 3x3
matriz = [
    [9, 3, 7],
    [5, 1, 8],
    [6, 2, 4]
]

# Función para ordenar una fila usando Bubble Sort
def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]  # Intercambio
    return fila

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Pedir al usuario qué fila quiere ordenar
fila_a_ordenar = int(input("\nIngrese el número de la fila a ordenar (1, 2 o 3): ")) - 1

if 0 <= fila_a_ordenar < len(matriz):
    # Ordenar la fila seleccionada
    matriz[fila_a_ordenar] = bubble_sort(matriz[fila_a_ordenar])

    # Mostrar la matriz resultante
    print("\nMatriz con la fila ordenada:")
    for fila in matriz:
        print(fila)
else:
    print("\n❌ Fila inválida. Debe ser 1, 2 o 3.")
