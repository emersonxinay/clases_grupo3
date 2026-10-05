# caso de sistema de estudiantes 
Situación real

Una academia necesita un programa para registrar estudiantes y controlar sus notas.

El programa debe permitir:

========== SISTEMA DE ESTUDIANTES ==========

1. Registrar estudiante
2. Mostrar estudiantes
3. Buscar estudiante
4. Mostrar aprobados
5. Calcular promedio
6. Eliminar estudiante
7. Salir

Cada estudiante tendrá:

Nombre
Edad
Nota

Y se almacenará así:

{
    "nombre": "Juan",
    "edad": 18,
    "nota": 17
}
## solución del sistema
```python
estudiantes = []


def mostrar_menu():
    print("\n========== SISTEMA DE ESTUDIANTES ==========")
    print("1. Registrar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Buscar estudiante")
    print("4. Mostrar aprobados")
    print("5. Calcular promedio")
    print("6. Eliminar estudiante")
    print("7. Salir")


def agregar_estudiante():

    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    nota = float(input("Nota: "))

    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "nota": nota
    }

    estudiantes.append(estudiante)

    print("Estudiante registrado correctamente.")


def mostrar_estudiantes():

    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
        return

    for estudiante in estudiantes:

        print(
            estudiante["nombre"],
            "-",
            estudiante["edad"],
            "años - Nota:",
            estudiante["nota"]
        )


def buscar_estudiante():

    nombre_buscar = input("Nombre del estudiante: ")

    for estudiante in estudiantes:

        if estudiante["nombre"].lower() == nombre_buscar.lower():

            print("\nEstudiante encontrado")
            print("Nombre:", estudiante["nombre"])
            print("Edad:", estudiante["edad"])
            print("Nota:", estudiante["nota"])

            if estudiante["nota"] >= 11:
                print("Estado: Aprobado")
            else:
                print("Estado: Desaprobado")

            return

    print("Estudiante no encontrado.")


def mostrar_aprobados():

    encontrados = False

    for estudiante in estudiantes:

        if estudiante["nota"] >= 11:
            print(estudiante["nombre"])
            encontrados = True

    if encontrados == False:
        print("No hay estudiantes aprobados.")


def calcular_promedio():

    if len(estudiantes) == 0:
        print("No hay estudiantes.")
        return

    total = 0

    for estudiante in estudiantes:
        total += estudiante["nota"]

    promedio = total / len(estudiantes)

    print("Promedio:", promedio)


def eliminar_estudiante():

    nombre_eliminar = input("Nombre del estudiante: ")

    for estudiante in estudiantes:

        if estudiante["nombre"].lower() == nombre_eliminar.lower():

            estudiantes.remove(estudiante)

            print("Estudiante eliminado.")
            return

    print("Estudiante no encontrado.")


while True:

    mostrar_menu()

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_estudiante()

    elif opcion == "2":
        mostrar_estudiantes()

    elif opcion == "3":
        buscar_estudiante()

    elif opcion == "4":
        mostrar_aprobados()

    elif opcion == "5":
        calcular_promedio()

    elif opcion == "6":
        eliminar_estudiante()

    elif opcion == "7":
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida.")

```