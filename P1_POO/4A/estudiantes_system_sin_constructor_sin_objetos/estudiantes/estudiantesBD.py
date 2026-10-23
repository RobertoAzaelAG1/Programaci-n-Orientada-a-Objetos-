from conexionBD import conexion, cursor


class EstudiantesBD:
    @staticmethod
    def insertar(nombre, nota):
        try:
            cursor.execute(
                "insert into estudiante (nombre, nota) values (%s, %s)",
                (nombre, nota)
            )
            conexion.commit()
            return True
        except Exception as error:
            print(f"No fue posible agregar al estudiante: {error}")
            return False

    @staticmethod
    def consultar():
        try:
            cursor.execute("select nombre, nota from estudiante")
            return cursor.fetchall()
        except Exception as error:
            print(f"No fue posible consultar los estudiantes: {error}")
            return []

    @staticmethod
    def eliminar(nombre):
        try:
            cursor.execute("delete from estudiante where nombre=%s", (nombre,))
            if cursor.rowcount > 0:
                conexion.commit()
                return True
            return False
        except Exception as error:
            print(f"No fue posible eliminar al estudiante: {error}")
            return False

    @staticmethod
    def actualizar(nombre, nota, nombreAnterior):
        try:
            cursor.execute(
                "update estudiante set nombre=%s, nota=%s where nombre=%s",
                (nombre, nota, nombreAnterior)
            )
            if cursor.rowcount > 0:
                conexion.commit()
                return True
            return False
        except Exception as error:
            print(f"No fue posible modificar al estudiante: {error}")
            return False
