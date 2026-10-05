
# formas de importar en python 
# # la forma general
# import funciones
# import operaciones as op

# funciones.saludar("Emerson Espinoza")
# dato2 = input("ingrese un nombre: ")
# funciones.saludar(dato2)
# resultado_op = op.multiplicar(4, 7)
# print(resultado_op)

# resultado_suma = op.sumar(50, 70)
# print(resultado_suma)



# # importar de forma especifica
from operaciones import sumar , restar
from funciones import saludar
from operaciones import *

resultado = sumar(30, 40)
print(resultado)

resultado1 = restar(40, 60)
print(resultado1)

resultado_multi = multiplicar(4, 6)
print(resultado_multi)

saludar("Eimer")

# probando subtotal y descuento
pre = float(input("Precio: "))
canti = int(input("Cantidad: "))
subtotal = calcular_subtotal(pre, canti)

total = aplicar_descuento(subtotal)
print(f"el total es : {total}")