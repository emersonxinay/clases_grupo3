

def sumar(a, b):
    suma = a + b 
    return suma

def restar(x, y):
    resta = x - y
    return resta

# multi = 30
def multiplicar(m=10, k=5):
    multi = m*k
    return multi

def calcular_subtotal(precio, cantidad):
    return precio * cantidad 

def aplicar_descuento(total):
    if total > 500:
        descuento = total * 0.15
        return total - descuento
    else: 
        return total

pi = 3.14

# multi = 60
# print(multi)

# invocando a la función 

if __name__ == "__main__":

    dato1 = int(input("Dato1: "))
    dato2 = int(input("Dato2: "))
    print(sumar(2, 5))
    print(sumar(dato1, dato2))

    resultado1 = sumar(dato1, dato2)
    print(resultado1)

    print(multiplicar(4))
    print(multiplicar())

