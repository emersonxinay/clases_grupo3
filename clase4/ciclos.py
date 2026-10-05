
# ciclos con python
# nombre = "emerson"
# while True:
#     print(f"hackeado por {nombre}")

# evitando bucle infinito
# inicio = 1
# while inicio < 5:
#     print(inicio)
#     # inicio = inicio + 1
#     inicio += 1

# print(inicio)

# acumulando datos 
# suma = 0 
# inicio = 1
# while inicio < 6:
#     suma = suma + inicio
    
#     inicio = inicio + 1 

# print(suma)
# print(inicio)

# num = 0 
# dato2 = input("Ingrese el final: ")
# while num <= int(dato2):
#     num = int(input("número: "))
# else:
#     print(f"numero ingresado es: {num} ")


# clave = input("Ingrese su clave: ")
# while clave == "emerson":
#     print("Bienvenido al programa")
# else:
#     print("Clave incorrecta")

# clave = input("Ingrese su clave: ")
# while clave != "emerson":
#     clave = input("Vuelve a ingresar su contraseña: ")
    
# else:
#     print(f"Bienvenido al programa, la contraseña correcta es: {clave} ")



# ciclos for con funcion range 
# n = int(input("ingrese un numero: "))
# for inicio in range(1, 3, 2):
#     print("*"* (n-inicio))

# con un argumento de rango dentro de for
# n1 = int(input("número inicial: "))
# n2 = int(input("número final: "))
# n3 = int(input("número que salta: "))

# for i in range(n1):
#     print(i)

# # con dos argumentos 
# for z in range(n1, n2):
#     print(z)

# # # con 3 argumentos 
# for x in range(n1, n2, n3 ):
#     print(x)
    
# ****
# ***
# **
# *
n = int(input("número inicial: "))
# n2 = int(input("número final: "))
# n3 = int(input("número que salta: "))

for i in range(n , 0, -1):
    print(" "*(n-i) + "*"*(2*i-1))
