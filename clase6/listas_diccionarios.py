# ==========================================
# SISTEMA DE VENTAS
# ==========================================

# 1. LISTA
# Productos disponibles en la tienda
productos = ["Laptop", "Mouse", "Teclado", "Monitor"]


# 2. DICCIONARIO
# Información de cada producto
inventario = {
    "Laptop": {
        "precio": 2500,
        "stock": 10,
        "categoria": "Computadoras"
    },
    "Mouse": {
        "precio": 80,
        "stock": 25,
        "categoria": "Accesorios"
    },
    "Teclado": {
        "precio": 120,
        "stock": 15,
        "categoria": "Accesorios"
    },
    "Monitor": {
        "precio": 900,
        "stock": 8,
        "categoria": "Pantallas"
    }
}


# 3. SET
# Obtener categorías sin repetir
categorias = {
    datos["categoria"]
    for datos in inventario.values()
}

print("Categorías disponibles:")
print(categorias)


# 4. TUPLA
# Coordenadas de la tienda
ubicacion = (-12.0464, -77.0428)

latitud, longitud = ubicacion

print("\nUbicación de la tienda:")
print("Latitud:", latitud)
print("Longitud:", longitud)


# 5. MATRIZ
# Ventas de 3 días
# Filas = días
# Columnas = productos
ventas = [
    [2, 5, 3, 1],  # Lunes
    [1, 8, 4, 2],  # Martes
    [3, 6, 2, 3]   # Miércoles
]

print("\nVentas por día:")

for fila in ventas:
    print(fila)


# ==========================================
# CÁLCULOS
# ==========================================

# Total de unidades vendidas
total_unidades = 0

for fila in ventas:
    total_unidades += sum(fila)

print("\nTotal de unidades vendidas:", total_unidades)


# Total vendido por producto
totales_productos = []

for columna in range(len(productos)):

    total = 0

    for fila in ventas:
        total += fila[columna]

    totales_productos.append(total)


print("\nVentas por producto:")

for i in range(len(productos)):
    print(productos[i], ":", totales_productos[i])


# ==========================================
# CALCULAR INGRESOS
# ==========================================

ingresos = 0

for i in range(len(productos)):

    producto = productos[i]
    cantidad = totales_productos[i]

    precio = inventario[producto]["precio"]

    ingresos += cantidad * precio


print("\nIngresos totales: S/.", ingresos)