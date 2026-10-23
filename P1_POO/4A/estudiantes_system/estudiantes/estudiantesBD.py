from conexionBD import conexion, cursor


class EstudiantesBD:
    def __init__(self, nombre, nota):
        self._nombre = nombre
        self._nota = nota

    def insertar(self):
        try:
            cursor.execute("insert into estudiante (nombre, nota) values (%s, %s)", (self._nombre, self._nota))
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def consultar():
        try:
            cursor.execute("select nombre, nota from estudiante")
            return cursor.fetchall()
        except:
            return []
        
    @staticmethod
    def eliminar(nombre):
        try:
            cursor.execute("delete from estudiante where nombre=%s", (nombre,))
            conexion.commit()
            return True
        except:
            return False

    def actualizar(self, nombreAnterior):
        try:
            cursor.execute("update estudiante set nombre=%s, nota=%s where nombre=%s", (self._nombre, self._nota, nombreAnterior))
            conexion.commit()
            return True
        except:
            return False
