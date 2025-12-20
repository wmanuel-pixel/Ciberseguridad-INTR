import mysql.connector
from mysql.connector import errorcode

DEFAULT_HOST = "localhost"
DEFAULT_USER = "root"
DEFAULT_PASS = ""
DEFAULT_DB = "articulos_db"

def ensure_database_and_table(host=DEFAULT_HOST, user=DEFAULT_USER, passwd=DEFAULT_PASS, database=DEFAULT_DB):
    
    try:
        conn = mysql.connector.connect(host=host, user=user, passwd=passwd)
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{database}` DEFAULT CHARACTER SET 'utf8' ")
        conn.database = database
        
        create_table = (
            "CREATE TABLE IF NOT EXISTS articulos ("
            "codigo INT AUTO_INCREMENT PRIMARY KEY, "
            "descripcion VARCHAR(255) NOT NULL, "
            "precio DECIMAL(10,2) NOT NULL"
            ") ENGINE=InnoDB"
        )
        cursor.execute(create_table)
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        raise

def get_connection(host=DEFAULT_HOST, user=DEFAULT_USER, passwd=DEFAULT_PASS, database=DEFAULT_DB):
    ensure_database_and_table(host=host, user=user, passwd=passwd, database=database)
    return mysql.connector.connect(host=host, user=user, passwd=passwd, database=database)
