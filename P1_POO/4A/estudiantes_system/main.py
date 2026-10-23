from estudiantes import Estudiantes, EstudiantesBD, estudiantesBD


class App:
    def __init__(self):
        self.main()

    def borrarPantalla(self):
        print("\033c")

    def espereTecla(self):
        input("... ¡Oprime cualquier tecla para continuar! ...")

    def menuAcciones(self, tipo):
        print(f"\n\t\t\t... Menu de {tipo} ... \n")
        opcion = input("\n\t 1.-Agregar \n\t 2.-Borrar \n\t 3.-Modificar \n\t 4.-Mostrar \n\t 5.-Salir \n\t").strip()
        return opcion

    def respuestaSql(self, respuesta):
        if respuesta:
            input("\n\t... Accion realizada con exito ... \n")
        else:
            input("\n\t... Accion NO realizada con exito ... \n")

    def datosEstudiantes(self, tipo):
        self.borrarPantalla()
        print(f"\n\t... ingresar los datos del {tipo}")
        estudiantito = {}
        estudiantito["nombre"] = input("Nombre:").strip()
        estudiantito["nota"] = input("Nota:").strip()
        return estudiantito

    def menuEstudiantes(self):
        opcion = True
        while opcion:
            self.borrarPantalla()
            opcion = self.menuAcciones("Estudiantes")
            match opcion:
                case "1":
                    estudiantito = self.datosEstudiantes("Estudiante")
                    estudiante = Estudiantes(estudiantito["nombre"], estudiantito["nota"])
                    estudianteBD = EstudiantesBD(estudiante.nombre, estudiante.nota)
                    respuesta = estudianteBD.insertar()
                    self.respuestaSql(respuesta)
                    del estudianteBD
                    del estudiante
                case "2":
                    self.borrarPantalla()
                    nombre = input("Ingresa el nombre del estudiante a eliminar:").strip()
                    respuesta = EstudiantesBD.eliminar(nombre)
                    self.respuestaSql(respuesta)
                case "3":
                    nombreAnterior = input("Ingresa el nombre actual del estudiante:").strip()
                    estudiantito = self.datosEstudiantes("Estudiante")
                    estudiante = Estudiantes(estudiantito["nombre"], estudiantito["nota"])
                    estudianteBD = EstudiantesBD(estudiante.nombre, estudiante.nota)
                    respuesta = estudianteBD.actualizar(nombreAnterior)
                    self.respuestaSql(respuesta)
                    del estudianteBD
                    del estudiante
                case "4":
                    self.borrarPantalla()
                    registros = estudiantesBD.EstudiantesBD.consultar()
                    if len(registros) > 0:
                        num_estudiantes = 1
                        for fila in registros:
                            print(f"Estudiante # {num_estudiantes}\n\t Nombre: {fila[0]}\n\t Nota: {fila[1]}")
                            num_estudiantes += 1
                        self.espereTecla()
                    else:
                        print("\n\n\t... ¡no existen datos que mostrar por el momento...!")
                        self.espereTecla()
                case "5":
                    opcion = False
                case _:
                    input("\n\t... Opcion invalida vuelva intentarlo porfavor ...")

    def main(self):
        opcion = True
        while opcion:
            self.borrarPantalla()
            print("Menu Principal")
            opcion = input("\n\t\t\t... Menu Principal ... \n\n\t 1.-Estudiantes \n\t 2.-Salir \n \t\tElige una Opcion:").strip()
            match opcion:
                case "1":
                    self.borrarPantalla()
                    self.menuEstudiantes()
                case "2":
                    self.borrarPantalla()
                    print("\n\t... Salir del sistema ... ")
                    opcion = False
                case _:
                    input("\n\t... Opcion invalida vuelva intentarlo porfavor ...")


if __name__ == "__main__":
    app = App()
