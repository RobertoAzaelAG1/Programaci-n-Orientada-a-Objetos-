from coches import Coches, CochesBD


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

    def datosCoches(self, tipo):
        self.borrarPantalla()
        print(f"\n\t... ingresar los datos del {tipo}")
        cochesitos = {}
        cochesitos["marca"] = input("Marca:").upper().strip()
        cochesitos["color"] = input("Color:").upper().strip()
        cochesitos["modelo"] = input("Modelo:").upper().strip()
        cochesitos["velocidad"] = input("Velocidad (km/h):").strip()
        cochesitos["potencia"] = input("Potencia:").strip()
        cochesitos["asientos"] = input("Numero de Asientos:").strip()
        return cochesitos

    def menuCoches(self):
        opcion = True
        while opcion:
            self.borrarPantalla()
            opcion = self.menuAcciones("Coches")
            match opcion:
                case "1":
                    cochesitos = self.datosCoches("Coche")
                    coche = Coches(
                        cochesitos["color"], cochesitos["marca"], cochesitos["velocidad"],
                        cochesitos["potencia"], cochesitos["asientos"], cochesitos["modelo"]
                    )
                    cocheBD = CochesBD(
                        coche.marca, coche.color, coche.modelo,
                        coche.velocidad, coche.potencia, coche.asientos
                    )
                    respuesta = cocheBD.insertar()
                    self.respuestaSql(respuesta)
                    del cocheBD
                    del coche
                case "2":
                    self.borrarPantalla()
                    id = input("Ingresa el ID del coche a eliminar:").strip()
                    respuesta = CochesBD.eliminar(id)
                    self.respuestaSql(respuesta)
                case "3":
                    id = input("Ingresa el ID del coche a actualizar:").strip()
                    cochesitos = self.datosCoches("Coche")
                    coche = Coches(
                        cochesitos["color"], cochesitos["marca"], cochesitos["velocidad"],
                        cochesitos["potencia"], cochesitos["asientos"], cochesitos["modelo"]
                    )
                    cocheBD = CochesBD(
                        coche.marca, coche.color, coche.modelo,
                        coche.velocidad, coche.potencia, coche.asientos
                    )
                    respuesta = cocheBD.actualizar(id)
                    self.respuestaSql(respuesta)
                    del cocheBD
                    del coche
                case "4":
                    self.borrarPantalla()
                    registros = CochesBD.consultar()
                    if len(registros) > 0:
                        num_coches = 1
                        for fila in registros:
                            print(
                                f"Coche # {num_coches}\n\t ID:{fila[0]}\n\t Marca:{fila[1]}"
                                f"\n\t Color:{fila[2]}\n\t Modelo:{fila[3]}\n\t Velocidad:{fila[4]}"
                                f"\n\t Potencia:{fila[5]}\n\t Asientos:{fila[6]}"
                            )
                            num_coches += 1
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
            opcion = input("\n\t\t\t... Menu Principal ... \n\n\t 1.-Coches \n\t 2.-Salir \n \t\tElige una Opcion:").strip()
            match opcion:
                case "1":
                    self.borrarPantalla()
                    self.menuCoches()
                case "2":
                    self.borrarPantalla()
                    print("\n\t... Salir del sistema ... ")
                    opcion = False
                case _:
                    input("\n\t... Opcion invalida vuelva intentarlo porfavor ...")


if __name__ == "__main__":
    app = App()
