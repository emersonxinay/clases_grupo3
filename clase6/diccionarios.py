
persona = {
    "nombre":"Emerson",
    "ciudad":"Lima",
    "edad":25,
    "contraseña":"1234"
}
# mostrar dato
print(persona["contraseña"])
print(persona)
# modificar un valor 

persona["contraseña"] = "123456"
print(persona)

# agregar un dato al diccionario
persona["pais"]="Perú"
print(persona)

# para eliminar un dato
del persona["edad"]
print(persona)

# recorrer un diccionario
# mostrar claves 
for x in persona:
    print(x)

# mostrar los valores 
for valor in persona.values():
    print(valor)

# mostrar clave y valor
for clave, valor in persona.items():
    print(f"{clave} = {valor} " )

print(persona)
# buscar si un dato existe o no existe
print(persona.get("ciudades", "no existe esa clave"))

# # datos sets - conjuntos 
ventas = {2000, 300, 300, 400, 400, 400, 800 }
print(ventas)
listas = [2, 4, 4, 6, 6, 20, 40, 20]
print(listas)
datos_unicos = set(listas)
print(datos_unicos)