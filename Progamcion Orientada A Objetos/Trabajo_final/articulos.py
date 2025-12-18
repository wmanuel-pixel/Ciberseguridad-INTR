import mysql.connector
import db as db_helper

class Articulos:

    def __init__(self, host="localhost", user="root", passwd="", database="articulos_db"):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.database = database

    def abrir(self):
        return db_helper.get_connection(host=self.host, user=self.user, passwd=self.passwd, database=self.database)

    def alta(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "INSERT INTO articulos(descripcion, precio) VALUES (%s,%s)"
        cursor.execute(sql, datos)
        cone.commit()
        cursor.close()
        cone.close()

    def consulta(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "SELECT descripcion, precio FROM articulos WHERE codigo=%s"
        cursor.execute(sql, datos)
        rows = cursor.fetchall()
        cursor.close()
        cone.close()
        return rows

    def recuperar_todos(self):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "SELECT codigo, descripcion, precio FROM articulos"
        cursor.execute(sql)
        rows = cursor.fetchall()
        cursor.close()
        cone.close()
        return rows