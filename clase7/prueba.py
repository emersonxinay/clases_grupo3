# # for i in range(5):
# #     pass

# # print(i)
# def contador(n):
#     i = 0
#     suma = 0
#     while i < n:
#         suma = suma + i
#         i = i+ 1

#     return suma

# a = int(input("Ingrese un número: "))
# print(contador(a))
# valor_cantador = contador(5)
# multiplicar = a * valor_cantador
# print(valor_cantador)
# print(multiplicar)
# (contador(3))

# def saludar(nombre):
#     return  " "+ nombre+ " " + "saludos" 

# print(saludar("Juan"))
# print(saludar("Emerson"))

# lista = [3, 500, 400, 400, 500, 3, 5, 6,80]
# conjuntos = {3, 500, 400, 400, 500, 3, 5, 6,80}
# print(lista)
# lista_limpiada_repetidos = list(set(lista))
# print(lista_limpiada_repetidos)
# print(conjuntos)


# calcular el promedio del estudiante 
notas = [14, 15, 2]
precios = [5, 10.6, 20]
def promedio(n):
    # return f"resultado = {(sum(n)/len(n)):.2f} "
    return sum(n)/len(n)

print(promedio(notas))
resultado = promedio(notas)
if resultado >= 11:
    print("Aprobo")
else:
    print("Desaprobo")

print(promedio(precios))
