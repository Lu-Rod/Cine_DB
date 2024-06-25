from ConexionBd import MySQLConnector

class Sala:
    def __init__(self, pelicula, fecha, hora):
        self.asientos = []
        self.pelicula = pelicula
        self.fecha = fecha
        self.hora = hora

    #ASIENTOS
    def setAsientos(self, asientos):
        self.asientos = asientos

    def getAsientos(self):
        return self.asientos
    
    # Agregar un asiento
    def addAsiento(self, asiento):
      self.asientos.append(asiento)

    # Quita un asiento
    def removeAsiento(self, asiento):
        self.asientos.remove(asiento)

    # crear metodo que cargue los asientos desde SQL
    def cargarAsientos(self):
        #llamo a la consulta sql con pel, fec, hor
        #ejecuto el query con una estructura de control para 
        #usar addAsiento(self,asiento)
        #previamente cree objeto Asiento
        db = MySQLConnector('root', '28022005', 'localhost', 'cinedb')
    
        if db.connect():
            result = db.execute_query("SELECT DATABASE();")
        
        print("Conectado a la base de datos:", result)
        db.disconnect()
    
    
    #PELICULA
    def setPelicula(self, pelicula):
        self.pelicula = pelicula
        
    def getPelicula(self):
        return self.pelicula

    #FECHA
    def setFecha(self, fecha):
        self.fecha = fecha
        
    def getFecha(self):
        return self.fecha
    
    #HORA
    def setHora(self, hora):
        self.hora = hora
    
    def getHora(self):
        return self.hora
        
class Asiento:
    def __init__(self, fila, numero, usuario):
        self.fila = fila
        self.numero = numero
        self.usuario = usuario
