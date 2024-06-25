from ConexionBd import MySQLConnector

class Sala:
    def __init__(self, pelicula, fecha, hora):
        self.asientos = []
        self.capacidad = 0
        self.nombre = ""
        self.pelicula = pelicula 
        self.fecha = fecha
        self.hora = hora 

    #ASIENTO
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
            
            '''
            query = db.execute_query("SELECT titulo FROM peliculas;")
            for datos in query:
                print(f"{datos[0]}")
            '''
            
            query = db.execute_query("SELECT * FROM tickets where funcion_id in (SELECT funciones.id FROM funciones JOIN peliculas ON peliculas.id = funciones.pelicula_id WHERE peliculas.titulo = 'Gladiator' AND funciones.hora = '18:00:00' AND funciones.fecha = '2024-05-23');")            
           
            for datos in query:
                id_ticket = datos[0]
                cliente_id = datos[1] 
                funcion_id = datos[2]
                asiento_id = datos[3]
                precio = datos[4]
                fecha_compra = datos[5]

                query2 = db.execute_query(f"SELECT fila, numero FROM asientos WHERE id='{asiento_id}'")
                for datos in query2:
                    fila = datos[0]
                    numero = datos[1]
                
                query3 = db.execute_query(f"SELECT nombre FROM clientes WHERE id={cliente_id}")
                for datos in query3:
                    usuario = datos[0]

                print(f"{id_ticket}, {cliente_id}, {funcion_id}, {asiento_id}, {precio}, {fecha_compra}, {fila}, {numero}, {usuario}")

                cadaAsiento = Asiento(fila, numero, usuario, precio, fecha_compra)

                self.addAsiento(cadaAsiento) 

            query4 = db.execute_query(f"select count(*),nombre from salas join asientos on salas.id = asientos.sala_id join funciones on salas.id = funciones.sala_id where funciones.id = '{funcion_id}';")
            for datos in query4:
                self.capacidad = datos[0]
                self.nombre = datos[1]
        
        db.disconnect() 
    
    def mostrar_info_asiento (self, fila, numero):
        info = ""

        for asiento in self.getAsientos():
            print(f"{fila} == {asiento.getFila()}) & ({numero} == {asiento.getNumero()}")
            if (fila == asiento.getFila()) & (numero == asiento.getNumero()):
                info = "Asiento vendido"

        return info


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

    #CAPACIDAD
    def setCapacidad(self, capacidad):
     self.capacidad = capacidad
        
    def getCapacidad(self):
        return self.capacidad
        
    #NOMBRE
    def setNombre(self, nombre):
        self.nombre = nombre
        
    def getNombre(self):
        return self.nombre
    #NOMBR
        
        
class Asiento:
    def __init__(self, fila, numero, usuario, precio, fecha_compra):
        self.fila = fila
        self.numero = numero
        self.usuario = usuario
        self.precio = precio
        self.fecha_compra = fecha_compra
        
    #FILA
    def setFila(self, fila):
        self.fila = fila
        
    def getFila(self):
        return self.fila

    #NUMERO
    def setNumero(self, numero):
        self.numerp = numero
        
    def getNumero(self):
        return self.numero
        
    #USUARIO
    def setUsuario(self, usuario):
        self.usuario = usuario
        
    def getUsuario(self):
        return self.usuario
    
    #PRECIO
    def setPrecio(self, precio):
        self.precio = precio
        
    def getPrecio(self):
        return self.precio
        
    #COMPRA
    def setFecha_Compra(self, fecha_compra):
        self.fecha_compra = fecha_compra
      
    def getFecha_Compra(self):
        return self.fecha_compra 

