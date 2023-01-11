lista = []
cantidad_alumnos = int(input("Ingrese la cantidad de alumnos: "))
while len(lista) < cantidad_alumnos:
    opcion = input("Agregar alumno (Y) o terminar (N): ")
    if opcion == "Y" or opcion == "y":
        try:
            nombre = input("Ingrese el nombre del alumno: ").capitalize()
            calificaciones = []
            for i in range(3):
                opcion2 = input("Agregar calificacion (Y) o terminar (N): ")
                if opcion2 == "Y":
                    calificacion = int(input(f"Ingrese la calificación de {nombre}: "))
                    calificaciones.append(calificacion)
                    print("Calificación agregada")
                elif opcion2 == "N":
                    break
                else: 
                    print("Se ha ingresado una opcion no válida")
                    continue
        except:
            print("Dato requerido, inténtelo de nuevo")
            continue
        alumno = {
            "nombre":nombre,
            "calificaciones":calificaciones,
            "promedio":sum(calificaciones)/len(calificaciones)
            }
        lista.append(alumno)
        print("Alumno agregado")
    elif opcion == "N" or opcion == "n":
        print(f"El programa ha terminado con {len(lista)} alumnos")
        break
    else: 
        print("Se ha ingresado una opcion no válida")
        continue
print(f"Los promedios de los {len(lista)} alumnos son: ")
for i in lista:
    print(f"{i.get('nombre')}: {i.get('promedio'): .2f}")