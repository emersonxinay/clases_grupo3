
# listas 
frutas = ["platano", 
          "uva", 
          "manzana", 
          "zandia"]
copia_frutas = frutas.copy()
# para acceder y mostar un dato 
print(frutas[2])
# modificar un dato de la lista

frutas[1] = "naranja"
print(frutas)
# agragar un dato a la lista

frutas.append("papaya")
print(frutas)

# eliminar un dato de la lista
frutas.remove("platano")
print(frutas)
# para eliminar el último dato
frutas.pop()
print(frutas)

# agregar un dato en base a un indice
frut = input("Ingrese su fruta a la base de datos: ")
indice = int(input("Ingrese el indice de la data: "))
frutas.insert(indice, frut)
print(frutas)

# agregar varios datos a la lista
frutas.extend(["kiwi", "toronja","huaba", "huaba","zapote", "caimito"])
print(frutas)

# para ubicar el indice de un dato
indice_dato = frutas.index("kiwi")
print(indice_dato)
# para contar datos repetidos
datos_repetidos= frutas.count("huaba")
print(datos_repetidos)

# ordenar alfabeticamente
frutas.sort(reverse=True)
print(frutas)
# para revertir el orden
frutas.reverse()
print(frutas)

print(copia_frutas)

# recorrer las litas
for x in frutas:
    print(f"nombre de la fruta: {x} ")

