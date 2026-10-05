# condiciones 
# edad = int(input("Ingrese edad: "))

# if edad >= 18:
#     print("Eres mayor")
# else:
#     print("Eres menor")

# edad = 10
# tiene_id = True
# es_vip = False

# if (edad >= 18 and es_vip) or  not (tiene_id):
#     print("PUEDES ENTRAR")
# else:
#     print("ACCESO DENEGADO")


# nota = int(input("Ingrese número: "))
# if nota > 0:
#     print("Positivo")
# elif  nota < 0:
#     print("negativo")
# elif nota == 0 :
#     print("es cero")
# else :
#     print("dato invalido")

# llueve = False
# if not llueve:
#     print("no llueve")

puerta_abierta = input("Tu puerta esta abierta? (si o no ) :")

if puerta_abierta == "si":
    print("La puerta abierta")
    luz_encendida = input("Tu luz esta encendida? (si o no): ")
    if luz_encendida == "si":
        print("Luz encendida")
    elif luz_encendida == "no":
        print("no esta encendida")
    else: 
        print("luz apagada")
else:
    print("Puerta cerrada")



