import tkinter as tk
from tkinter import ttk, messagebox
from LogicaSalas import Sala


class TabFuncion:
    def __init__(self, ancho, largo, titulo):
        self.ancho = ancho
        self.largo = largo
        self.titulo = titulo
        
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
        self.combo1['values'] = ("Shrek", "Titanic", "Intensamente 2")

        ttk.Label(self.tab_elegir_funcion, text="Fecha").grid(column=0, row=2, padx=10, pady=10, sticky=tk.W)
        self.combo2 = ttk.Combobox(self.tab_elegir_funcion, state="readonly")
        self.combo2.grid(column=1, row=2, padx=10, pady=10, sticky=tk.W)
        self.combo2['values'] = ("17/06/24", "18/06/24", "19/06/24")

        ttk.Label(self.tab_elegir_funcion, text="Hora").grid(column=0, row=3, padx=10, pady=10, sticky=tk.W)
        self.combo3 = ttk.Combobox(self.tab_elegir_funcion, state="readonly")
        self.combo3.grid(column=1, row=3, padx=10, pady=10, sticky=tk.W)
        self.combo3['values'] = ("13:00", "15:00", "17:00") 

        ttk.Button(self.tab_elegir_funcion, text="Confirmar función", command=self.mostrar_sala).grid(column=0, row=5, columnspan=2, padx=10, pady=10, sticky=tk.W+tk.E)
            
    def setup_tab_ver_asiento(self,sala):
        # Configuración de widgets para la pestaña "Ver Asientos"
        ttk.Label(self.tab_ver_asiento, text="Aquí se mostrarán los asientos disponibles").pack(padx=10, pady=10)
        
        #aqui se muestran los asientos con los datos que traiga del sql!
        print(f"la película {sala.getPelicula()}")
        sala.cargarAsientos()




    def mostrar_sala(self):
        pelicula = self.combo1.get()
        fecha = self.combo2.get()
        hora = self.combo3.get()
        
        # Inicializo el objeto de la clase Sala
        laSala = Sala(pelicula, fecha, hora) 

        confirmar = messagebox.askyesno("Confirmar función", f"¿Desea confirmar la película {laSala.getPelicula()} el día {fecha} a la hora {hora}?")
        
        print(f"Confirmar tiene {confirmar}")
        if confirmar:
            self.tab_control.tab(1, state="normal")
            self.tab_control.select(1)
            self.setup_tab_ver_asiento(laSala)


    def iniciar(self):
        self.root.mainloop()


