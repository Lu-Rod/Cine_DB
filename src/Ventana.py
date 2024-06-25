import tkinter as tk
from tkinter import ttk, messagebox
from LogicaSalas import Sala 

class TabFuncion:
    def __init__(self, ancho, largo, titulo):
        self.ancho = ancho
        self.largo = largo
        self.titulo = titulo
        self.sala = None
        
        # Crear la ventana principal
        self.root = tk.Tk()
        self.root.title(self.titulo)
        self.root.geometry(f"{self.ancho}x{self.largo}")
        
        # Crear el control de pestañas
        self.tab_control = ttk.Notebook(self.root)

        # Crear las pestañas
        self.tab_elegir_funcion = ttk.Frame(self.tab_control)
        self.tab_ver_asiento = ttk.Frame(self.tab_control)

        # Añadir las pestañas al control
        self.tab_control.add(self.tab_elegir_funcion, text="Elegir Función")
        self.tab_control.add(self.tab_ver_asiento, text="Ver Asientos")
        self.tab_control.tab(1, state="disabled")

        self.tab_control.pack(expand=1, fill="both")

        # Configurar las pestañas
        self.setup_tab_elegir_funcion()
        
        #self.setup_tab_ver_asiento()

    def setup_tab_elegir_funcion(self):
        # Configuración de widgets para la pestaña "Elegir Función"
        ttk.Label(self.tab_elegir_funcion, text="Funciones").grid(column=0, row=1, padx=10, pady=10, sticky=tk.W)
        self.combo1 = ttk.Combobox(self.tab_elegir_funcion, state="readonly")
        self.combo1.grid(column=1, row=1, padx=10, pady=10, sticky=tk.W)
        self.combo1['values'] = ("Gladiator", "Shrek", "Titanic", "Intensamente 2")
        self.combo1.set("Gladiator")

        ttk.Label(self.tab_elegir_funcion, text="Fecha").grid(column=0, row=2, padx=10, pady=10, sticky=tk.W)
        self.combo2 = ttk.Combobox(self.tab_elegir_funcion, state="readonly")
        self.combo2.grid(column=1, row=2, padx=10, pady=10, sticky=tk.W)
        self.combo2['values'] = ("23/05/24", "18/06/24", "19/06/24")
        self.combo2.set("23/05/24")

        ttk.Label(self.tab_elegir_funcion, text="Hora").grid(column=0, row=3, padx=10, pady=10, sticky=tk.W)
        self.combo3 = ttk.Combobox(self.tab_elegir_funcion, state="readonly")
        self.combo3.grid(column=1, row=3, padx=10, pady=10, sticky=tk.W)
        self.combo3['values'] = ("13:00", "15:00", "18:00")
        self.combo3.set("18:00")


        ttk.Button(self.tab_elegir_funcion, text="Confirmar función", command=self.mostrar_sala).grid(column=0, row=5, columnspan=2, padx=10, pady=10, sticky=tk.W+tk.E)
            
    def setup_tab_ver_asiento(self):
        s = ttk.Style()
        s.configure("Disponible.TButton", foreground="#469B40")
        s.map("Disponible.TButton", foreground=[("active", "#469B40")])
        
        s.configure("NoDisponible.TButton", foreground="#ff0000")
        s.map("NoDisponible.TButton", foreground=[("active", "#ff0000")])

        # Configuración de widgets para la pestaña "Ver Asientos"
        
        #aqui se muestran los asientos con los datos que traiga del sql!
        print(f"la película {self.sala.getPelicula()}")
        self.sala.cargarAsientos() 
    
        #PARTE GRAFICA  
        texto = f"La capacidad de la sala {self.sala.getNombre()} es {self.sala.getCapacidad()}"
        ttk.Label(self.tab_ver_asiento, text=texto).grid(column=0, row=0, columnspan=2, padx=10, pady=10, sticky=tk.W+tk.E)
        
        cant_filas = int(self.sala.getCapacidad()/10)
        print(f"capacidad {self.sala.getCapacidad()}  capacidad mod 10 {cant_filas}")
        #lista_botones=[]

        for f in range(cant_filas):
            print(f)
            for c in range(10):
                #if c==0:
                #    lista_botones.append([])  

                print(f,c)
                if f == 0:
                    fila = "A"
                elif f == 1:
                    fila = "B"
                else:
                    fila = "C"
                
                texto = f"{fila}{c}"
                #boton = BotonAsiento(fila,c,texto)
                #boton.setBoton(ttk.Button(self.tab_ver_asiento, text=texto, command=lambda f=fila, c=c: self.mostrar_asiento(f, c)).grid(column=c, row=f+1, columnspan=1, padx=3, pady=3, sticky=tk.W+tk.E))
                
                
                if self.sala.mostrar_info_asiento(fila, c)=="Asiento disponible":
                    ttk.Button(self.tab_ver_asiento, text=texto, style="Disponible.TButton",command=lambda f=fila, c=c: self.mostrar_asiento(f, c)).grid(column=c, row=f+1, columnspan=1, padx=3, pady=3, sticky=tk.W+tk.E)   
                else: 
                    ttk.Button(self.tab_ver_asiento, text=texto, style="NoDisponible.TButton",command=lambda f=fila, c=c: self.mostrar_asiento(f, c)).grid(column=c, row=f+1, columnspan=1, padx=3, pady=3, sticky=tk.W+tk.E)
                
                #lista_botones[f].append(boton)


    def mostrar_asiento(self, fila, numero):
        info = f"{fila} y {numero} "+self.sala.mostrar_info_asiento(fila, numero)
        messagebox.showinfo("Info Asiento", info)


    def mostrar_sala(self):
        pelicula = self.combo1.get()
        fecha = self.combo2.get()
        hora = self.combo3.get()
        
        # Inicializo el objeto de la clase Sala
        self.sala = Sala(pelicula, fecha, hora) 

        confirmar = messagebox.askyesno("Confirmar función", f"¿Desea confirmar la película {self.sala.getPelicula()} el día {fecha} a la hora {hora}?")
        
        print(f"Confirmar tiene {confirmar}")
        if confirmar:
            self.tab_control.tab(1, state="normal")
            self.tab_control.select(1)
            self.setup_tab_ver_asiento()


    def iniciar(self):
        self.root.mainloop()


class BotonAsiento:
    def __init__(self, fila, numero, texto):
        self.fila = fila
        self.numero = numero
        self.texto = texto
        self.boton = None
    
    #FILA
    def setFila(self, fila):
        self.fila = fila
        
    def getFila(self):
        return self.fila

    #NUMERO
    def setNumero(self, numero):
        self.numero = numero
        
    def getNumero(self):
        return self.numero

    #Texto
    def setTexto(self, texto):
        self.texto = texto
        
    def getTexto(self):
        return self.texto

#BOTOON
    def setBoton(self, boton):
        self.boton = boton

    def getBoton(self):
        return self.boton
