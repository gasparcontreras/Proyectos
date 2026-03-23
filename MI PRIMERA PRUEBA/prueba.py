def cargar_alumnos():
    alumnos = []
    n = int(input("¿Cuántos alumnos desea cargar?: "))

    for i in range(n):
        print(f"\nAlumno {i+1}")
        nombre = input("Nombre completo: ")

        notas = []
        for j in range(3):
            while True:
                try:
                    nota = float(input(f"Ingrese la nota {j+1} (0-10): "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("La nota debe estar entre 0 y 10.")
                except ValueError:
                    print("Ingrese un número válido.")

        promedio = sum(notas) / 3

        alumno = {
            "Nombre": nombre,
            "Notas": notas,
            "Promedio": promedio
        }

        alumnos.append(alumno)

    return alumnos


def evaluar_aprobados(alumnos):
    aprobados = 0
    desaprobados = 0

    for alumno in alumnos:
        if alumno["Promedio"] >= 4:
            aprobados += 1
        else:
            desaprobados += 1

    print(f"\nAprobados: {aprobados}")
    print(f"Desaprobados: {desaprobados}")


def promedio_curso(alumnos):
    if not alumnos:
        return 0

    suma = sum(alumno["Promedio"] for alumno in alumnos)
    return suma / len(alumnos)


def mejor_y_peor_promedio(alumnos):
    if not alumnos:
        return

    mejor = max(alumnos, key=lambda x: x["Promedio"])
    peor = min(alumnos, key=lambda x: x["Promedio"])

    print("\nAlumno con mejor promedio:")
    print(mejor["Nombre"], "->", mejor["Promedio"])

    print("\nAlumno con peor promedio:")
    print(peor["Nombre"], "->", peor["Promedio"])


def buscar_alumno(alumnos):
    texto = input("\nIngrese nombre completo o parcial a buscar: ").lower()
    encontrados = []

    for alumno in alumnos:
        if texto in alumno["Nombre"].lower():
            encontrados.append(alumno)

    if encontrados:
        print("\nResultados encontrados")
        for alumno in encontrados:
            print("Nombre:", alumno["Nombre"])
            print("Notas:", alumno["Notas"])
            print("Promedio:", alumno["Promedio"])
    else:
        print("No se encontraron coincidencias.")


##DEVOLVEMOS TOD

alumnos = cargar_alumnos()

evaluar_aprobados(alumnos)

print("\nPromedio general del curso:", promedio_curso(alumnos))

mejor_y_peor_promedio(alumnos)

buscar_alumno(alumnos)

