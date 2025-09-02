# Programa 1: Búsqueda en Arreglo Multidimensional

# Definimos la matriz 3x3
matriz = [
    [4, 7, 9],
    [1, 5, 3],
    [8, 2, 6]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):          # Recorre filas
        for j in range(len(matriz[i])):   # Recorre columnas
            if matriz[i][j] == valor:
                return (i, j)  # Devuelve la posición si lo encuentra
    return None  # Si no se encuentra

# Mostrar la matriz
print("Matriz:")
for fila in matriz:
    print(fila)

# Pedir al usuario un valor a buscar
valor_buscado = int(input("\nIngrese el número que desea buscar en la matriz: "))

# Llamamos a la función
posicion = buscar_valor(matriz, valor_buscado)

# Mostramos el resultado
if posicion:
    fila_humana = posicion[0] + 1
    columna_humana = posicion[1] + 1
    print(f"\n✅ El valor {valor_buscado} se encontró en la posición: Fila {fila_humana}, Columna {columna_humana}.")
else:
    print(f"\n❌ El valor {valor_buscado} no se encontró en la matriz.")
