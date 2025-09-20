
def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


if __name__ == "__main__":
    compra1 = float(input("Ingrese el monto de la primera compra: $"))
    descuento1 = calcular_descuento(compra1)
    total1 = compra1 - descuento1
    print("\nCompra 1:")
    print(f"  Monto de la compra: ${compra1:.2f}")
    print(f"  Descuento aplicado (10%): ${descuento1:.2f}")
    print(f"  Total a pagar: ${total1:.2f}\n")

    compra2 = float(input("Ingrese el monto de la segunda compra: $"))
    porcentaje = float(input("Ingrese el porcentaje de descuento: "))
    descuento2 = calcular_descuento(compra2, porcentaje)
    total2 = compra2 - descuento2
    print("\nCompra 2:")
    print(f"  Monto de la compra: ${compra2:.2f}")
    print(f"  Descuento aplicado ({porcentaje}%): ${descuento2:.2f}")
    print(f"  Total a pagar: ${total2:.2f}")

