from estudiantes import Estudiantes, EstudiantesBD


def borrarPantalla():
    print("\033c")


def espereTecla():
    input("... ¡Oprime cualquier tecla para continuar! ...")


def menuAcciones(tipo):
    print(f"\n\t\t\t... Menu de {tipo} ... \n")
    opcion = input("\n\t 1.-Agregar \n\t 2.-Borrar \n\t 3.-Modificar \n\t 4.-Mostrar \n\t 5.-Salir \n\t").strip()
    return opcion


def respuestaSql(respuesta):
    if respuesta:
        input("\n\t... Accion realizada con exito ... \n")
    else:
        input("\n\t... Accion NO realizada con exito ... \n")


def datosEstudiantes(tipo):
    borrarPantalla()
    print(f"\n\t... ingresar los datos del {tipo}")
    estudiantito = {}
    estudiantito["nombre"] = input("Nombre:").strip()
    estudiantito["nota"] = input("Nota:").strip()
    return estudiantito


def menuEstudiantes():
    opcion = True
    while opcion:
        borrarPantalla()
        opcion = menuAcciones("Estudiantes")
        match opcion:
            case "1":
                estudiantito = datosEstudiantes("Estudiante")
                Estudiantes.nombre = estudiantito["nombre"]
                Estudiantes.nota = estudiantito["nota"]
                respuesta = EstudiantesBD.insertar(Estudiantes.getNombre(), Estudiantes.getNota())
                respuestaSql(respuesta)
            case "2":
                borrarPantalla()
                nombre = input("Ingresa el nombre del estudiante a eliminar:").strip()
                respuesta = EstudiantesBD.eliminar(nombre)
                respuestaSql(respuesta)
            case "3":
                nombreAnterior = input("Ingresa el nombre actual del estudiante:").strip()
                estudiantito = datosEstudiantes("Estudiante")
                Estudiantes.nombre = estudiantito["nombre"]
                Estudiantes.nota = estudiantito["nota"]
                respuesta = EstudiantesBD.actualizar(
                    Estudiantes.getNombre(),
                    Estudiantes.getNota(),
                    nombreAnterior
                )
                respuestaSql(respuesta)
            case "4":
                borrarPantalla()
                registros = EstudiantesBD.consultar()
                if len(registros) > 0:
                    num_estudiantes = 1
                    for fila in registros:
                        print(f"Estudiante # {num_estudiantes}\n\t Nombre: {fila[0]}\n\t Nota: {fila[1]}")
                        num_estudiantes += 1
                    espereTecla()
                else:
                    print("\n\n\t... ¡no existen datos que mostrar por el momento...!")
                    espereTecla()
            case "5":
                opcion = False
            case _:
                input("\n\t... Opcion invalida vuelva intentarlo porfavor ...")


def main():
    opcion = True
    while opcion:
        borrarPantalla()
        print("Menu Principal")
        opcion = input("\n\t\t\t... Menu Principal ... \n\n\t 1.-Estudiantes \n\t 2.-Salir \n \t\tElige una Opcion:").strip()
        match opcion:
            case "1":
                borrarPantalla()
                menuEstudiantes()
            case "2":
                borrarPantalla()
                print("\n\t... Salir del sistema ... ")
                opcion = False
            case _:
                input("\n\t... Opcion invalida vuelva intentarlo porfavor ...")


if __name__ == "__main__":
    main()
