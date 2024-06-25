import mysql.connector
from mysql.connector import Error

# Configuración de la conexión

class MySQLConnector:
    def __init__(self, user, password, host, database):
        self.config = {
            'user': user, #'root'
            'password': password,#'28022005'
            'host': host, #'localhost'
            'database': database #'TrabajoCine'
        }
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(**self.config)
            if self.connection.is_connected():
                print("Conexión exitosa a la base de datos")
                self.cursor = self.connection.cursor()
                return True
        except Error as e:
            print("Error al conectar a MySQL", e)
            return False

    def disconnect(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Conexión a MySQL cerrada")

    def execute_query(self, query):
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Error as e:
            print("Error al ejecutar la consulta", e)
            return None


    
