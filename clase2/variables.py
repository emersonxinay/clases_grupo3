
# imprimir en python 
print("Hola mundo", False, 20.5)
print("hola mundo", "chao mundo", 20, True  )

# declarando variables 
nombre = "Emerson"
precio = 20.5
estudias = True 
edad = 20 

frutas = ["motor y motivo", [], 20, 20.5, "negrita linda", {}]
paises = {"peru":"lima", "chile":"santiago"}
print(type(frutas))
print(type(paises))

# procesando los datos 
multi = precio * edad

# salida de datos 
print(multi)

# entrada dinamicas 
dato1 = int(input("Ingrese un número: "))
sumar = dato1 + 20 
print(sumar)

# operaciones matematicas 
print("Operaciones matematicas")
a = float(input("Ingrese primer número: "))
b = float(input("Ingrese segundo número: "))

sumar = a + b
restar = a - b
multi = a * b
division_exacta = a/b 
division_entera = a//b 
potencia = a**b
resto_modulo = a % b 
raiz_cuadrada = a ** 0.5
print(nombre == "Emerson")
if nombre == "Emerson":
    print("Si son iguales")
# imprimir con interpolación 
print(f"la suma es: {sumar} ")
print(f"La resta es: {restar} ")
print("la suma es: ", sumar )
print(sumar)

GRAVEDAD = 9.8
