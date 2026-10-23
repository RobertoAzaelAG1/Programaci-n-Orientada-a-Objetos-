import mysql.connector 

conexion = None
cursor = None

try:
    conexion=mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="bd_estudiantes"

    )
    cursor=conexion.cursor(buffered=True)


except Exception as error:
    print(f"....No fue posible conectarse con la base de datos: {error}....")
