import mysql.connector
from mysql.connector import Error

class Articulos:
    def abrir(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="bd1"
        )

    def alta(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "INSERT INTO articulos(descripcion, precio) VALUES (%s, %s)"
        cursor.execute(sql, datos)
        cone.commit()
        cursor.close()
        cone.close()

    def consulta(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "SELECT descripcion, precio FROM articulos WHERE codigo=%s"
        cursor.execute(sql, datos)
        respuesta = cursor.fetchall()
        cursor.close()
        cone.close()
        return respuesta

    def recuperar_todos(self):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "SELECT codigo, descripcion, precio FROM articulos"
        cursor.execute(sql)
        respuesta = cursor.fetchall()
        cursor.close()
        cone.close()
        return respuesta

    def baja(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "DELETE FROM articulos WHERE codigo=%s"
        cursor.execute(sql, datos)
        cone.commit()
        count = cursor.rowcount
        cursor.close()
        cone.close()
        return count

    def modificacion(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "UPDATE articulos SET descripcion=%s, precio=%s WHERE codigo=%s"
        cursor.execute(sql, datos)
        cone.commit()
        count = cursor.rowcount
        cursor.close()
        cone.close()
        return count
