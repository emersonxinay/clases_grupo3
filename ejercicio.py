cantidad_productos = int(input("¿Cuántos productos diferentes desea registrar? "))

total = 0
total_unidades = 0

for i in range(cantidad_productos):
    print(f"\nProducto {i + 1}")
    nombre = input("Nombre del producto: ")
    cantidad = int(input("Cantidad comprada: "))
    while cantidad <= 0:
        print("La cantidad debe ser mayor que cero.")
        cantidad = int(input("Ingrese nuevamente la cantidad: "))
    precio = float(input("Precio unitario: "))
    while precio <= 0:
        print("El precio debe ser mayor que cero.")
        precio = float(input("Ingrese nuevamente el precio: "))
    subtotal = cantidad * precio

    total += subtotal
    total_unidades += cantidad

    print(f"Subtotal de {nombre}: S/ {subtotal:.2f}")

# Calcular descuento

if total > 500:
    descuento = total * 0.15
elif total >= 250:
    descuento = total * 0.08
else:
    descuento = 0

# Calcular total final
total_final = total - descuento

# Mostrar resultados
print("\n========== RESUMEN DE COMPRA ==========")
print(f"Total inicial: S/ {total:.2f}")
print(f"Descuento aplicado: S/ {descuento:.2f}")
print(f"Total final a pagar: S/ {total_final:.2f}")
print(f"Cantidad total de unidades: {total_unidades}")