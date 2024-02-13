import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import tkinter.messagebox as messagebox
import ttkthemes
from ttkthemes import ThemedTk
from tkinter import Scrollbar
#ventana principal
ventana = tk.Tk()
titulo_centrado = " " * 100+ "GUITARSTORE" + " " * 40
ventana.title(titulo_centrado)
ventana.geometry("800x550")
ventana.resizable(False,False)
ventana.iconbitmap("logo.ico") 


# Contenedor principal para el contenido
principal = tk.Frame(ventana)
principal.pack(fill=tk.BOTH, expand=True)

# fondo de la ventana
ruta_fondo = "fondo1.png"
imagen_fondo = tk.PhotoImage(file=ruta_fondo)

fondo_principal = tk.Label(principal, image=imagen_fondo)
fondo_principal.place(relwidth=1, relheight=1)

# Crear un LabelFrame para los Instrumentos===========================================
lfi = tk.LabelFrame(principal, width=750, height=250, relief=tk.SUNKEN)#lfi=LabelFrame Instruments
lfi.place(x=20, y=190)
#fondo del labelframe
flf=tk.PhotoImage(file="fondo.png")
fondolabel=tk.Label(lfi,image=flf)
fondolabel.place(x=0,y=-220)
# Crear un Menu de INSTRUMENTOS
def Intrumentos_cuerda(event):
    def scroll(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def activar_scroll(event):
        canvas.bind_all("<MouseWheel>", scroll)

    def desactivar_scroll(event):
        canvas.unbind_all("<MouseWheel>")
    seleccion = event.widget.get()
    combobox_values = event.widget.cget("values")
    if seleccion in combobox_values[1]:#GUITARRAS
        # Crear un nuevo marco dentro del labelframe, nuevo_marco=frame principal
        nuevo_marco = tk.Frame(lfi, width=750, height=250, bg="red")
        nuevo_marco.place(x=0, y=0)
        # Creamos un canvas dentro del frame principal
        canvas = tk.Canvas(nuevo_marco, bg="pink", width=750, height=250)
        canvas.place(x=0, y=0)
        flf=tk.PhotoImage(file="fondo.png")
        fondolabel=tk.Label(canvas,image=flf)
        fondolabel.image=flf
        fondolabel.place(x=0,y=-220)
        
        # Frame interior para el contenido del canvas
        frame_interior = tk.Frame(canvas, width=750, height=250)
        canvas.create_window((0, 0), window=frame_interior, anchor="nw")
        flf=tk.PhotoImage(file="fondo.png").zoom(2)
        fondolabel=tk.Label(frame_interior,image=flf)
        fondolabel.image=flf
        fondolabel.place(x=0,y=-220)
        # Configurar el scrollbar
        scrollbar_vertical = Scrollbar(nuevo_marco, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar_vertical.place(x=733,y=0)
       # Configuramos el canvas y el scrollbar para que funcionen juntos
        canvas.config(yscrollcommand=scrollbar_vertical.set)

        # Conectamos el evento de entrada del ratón para activar el scroll
        canvas.bind("<Enter>", activar_scroll)
        canvas.bind("<Leave>", desactivar_scroll)
            #OBJETOS GENRALES
        decompras=tk.PhotoImage(file="carrito.png")
        decompras2=decompras.subsample(15)
        
        #OBJETO 1
        ic1=tk.PhotoImage(file="GIBSON LPTR00WSNH1.png")
        Ric1=ic1.subsample(8)
        l_ic1=tk.Label(frame_interior,width=110, height=130, image=Ric1, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic1.image=Ric1
        l_ic1.grid(row=1,column=1,padx=20)
        bic1=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic1.image=decompras2
        bic1.grid(row=4, column=1)
        pic1=tk.Label(frame_interior, text="Precio: 250,00$")
        pic1.grid(row=3, column=1)
        #OBJETO 2
        ic2=tk.PhotoImage(file="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT.png")
        Ric2=ic2.subsample(8)
        l_ic2=tk.Label(frame_interior,width=110, height=130, image=Ric2, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic2.image=Ric2
        l_ic2.grid(row=1,column=3, padx=20)
        bic2=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic2.grid(row=4,column=3)
        pic2=tk.Label(frame_interior, text="Precio: 250,00$")
        pic2.grid(row=3,column=3)
        #OBJETO 3
        ic3=tk.PhotoImage(file="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT.png")
        Ric3=ic3.subsample(8)
        l_ic3=tk.Label(frame_interior,width=110, height=130, image=Ric3, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic3.image=Ric3
        l_ic3.grid(row=1,column=5, padx=20)
        bic3=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic3.grid(row=4,column=5)
        pic3=tk.Label(frame_interior, text="Precio: 250,00$")
        pic3.grid(row=3,column=5)
        #OBJETO 4
        ic4=tk.PhotoImage(file="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT.png")
        Ric4=ic4.subsample(8)
        l_ic4=tk.Label(frame_interior,width=110, height=130, image=Ric4, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic4.image=Ric4
        l_ic4.grid(row=1,column=7, padx=20)
        bic4=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic4.grid(row=4,column=7)
        pic4=tk.Label(frame_interior, text="Precio: 250,00$")
        pic4.grid(row=3,column=7)
        #OBJETO 5
        ic5=tk.PhotoImage(file="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT.png")
        Ric5=ic5.subsample(8)
        l_ic5=tk.Label(frame_interior,width=110, height=130, image=Ric5, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic5.image=Ric5
        l_ic5.grid(row=1,column=9, padx=20)
        bic5=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic5.grid(row=4,column=9)
        pic5=tk.Label(frame_interior, text="Precio: 250,00$")
        pic5.grid(row=3,column=9)
        #OBJETO 6
        ic6=tk.PhotoImage(file="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT.png")
        Ric6=ic6.subsample(8)
        l_ic6=tk.Label(frame_interior,width=110, height=130, image=Ric6, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic6.image=Ric6
        l_ic6.grid(row=5,column=1, padx=20)
        pic6=tk.Label(frame_interior, text="Precio: 250,00$")
        pic6.grid(row=6,column=1)
        bic6=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic6.grid(row=7,column=1)
        #toolip1
        def mostrar_tooltip1(event):
            tooltip1.place(x=10,y=35)
        def ocultar_tooltip1(event):
            tooltip1.place_forget()
            # Crear una etiqueta para el tooltip
        tooltip1 = tk.Label(frame_interior, text="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT", bg="white", relief=tk.SOLID, borderwidth=1, font=("arial",10))
        l_ic1.bind("<Enter>", mostrar_tooltip1)
        l_ic1.bind("<Leave>", ocultar_tooltip1)
        #toolip2
        def mostrar_tooltip2(event):
            tooltip2.place(x=10,y=35)
        def ocultar_tooltip2(event):
            tooltip2.place_forget()
            # Crear una etiqueta para el tooltip
        tooltip2 = tk.Label(frame_interior, text="GIBSON LPTR00WSNH1", bg="white", relief=tk.SOLID, borderwidth=1, font=("arial",10))
        l_ic2.bind("<Enter>", mostrar_tooltip2)
        l_ic2.bind("<Leave>", ocultar_tooltip2)
        
        # Crear un botón "Regresar"
        boton_regresar = tk.Button(nuevo_marco, text="Regresar", command=lambda: nuevo_marco.destroy())
        boton_regresar.place(x=10, y=10)
    elif seleccion in combobox_values[2]:#BAJOS
        # Crear un nuevo marco dentro del labelframe, nuevo_marco=frame principal
        nuevo_marco = tk.Frame(lfi, width=750, height=250, bg="red")
        nuevo_marco.place(x=0, y=0)
        # Creamos un canvas dentro del frame principal
        canvas = tk.Canvas(nuevo_marco, bg="pink", width=750, height=250)
        canvas.place(x=0, y=0)
        flf=tk.PhotoImage(file="fondo.png")
        fondolabel=tk.Label(canvas,image=flf)
        fondolabel.image=flf
        fondolabel.place(x=0,y=-220)
        
        # Frame interior para el contenido del canvas
        frame_interior = tk.Frame(canvas, width=750, height=250)
        canvas.create_window((0, 0), window=frame_interior, anchor="nw")
        flf=tk.PhotoImage(file="fondo.png").zoom(2)
        fondolabel=tk.Label(frame_interior,image=flf)
        fondolabel.image=flf
        fondolabel.place(x=0,y=-220)
        # Configurar el scrollbar
        scrollbar_vertical = Scrollbar(nuevo_marco, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar_vertical.place(x=733,y=0)
       # Configuramos el canvas y el scrollbar para que funcionen juntos
        canvas.config(yscrollcommand=scrollbar_vertical.set)

        # Conectamos el evento de entrada del ratón para activar el scroll
        canvas.bind("<Enter>", activar_scroll)
        canvas.bind("<Leave>", desactivar_scroll)
        #OBJETOS GENRALES
        decompras=tk.PhotoImage(file="carrito.png")
        decompras2=decompras.subsample(15)
        
        #OBJETO 1
        ic1=tk.PhotoImage(file="GIBSON LPTR00WSNH1.png")
        Ric1=ic1.subsample(8)
        l_ic1=tk.Label(frame_interior,width=110, height=130, image=Ric1, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic1.image=Ric1
        l_ic1.grid(row=1,column=1,padx=20)
        bic1=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic1.image=decompras2
        bic1.grid(row=4, column=1)
        pic1=tk.Label(frame_interior, text="Precio: 250,00$")
        pic1.grid(row=3, column=1)
        #OBJETO 2
        ic2=tk.PhotoImage(file="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT.png")
        Ric2=ic2.subsample(8)
        l_ic2=tk.Label(frame_interior,width=110, height=130, image=Ric2, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic2.image=Ric2
        l_ic2.grid(row=1,column=3, padx=20)
        bic2=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic2.grid(row=4,column=3)
        pic2=tk.Label(frame_interior, text="Precio: 250,00$")
        pic2.grid(row=3,column=3)
        #OBJETO 3
        ic3=tk.PhotoImage(file="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT.png")
        Ric3=ic3.subsample(8)
        l_ic3=tk.Label(frame_interior,width=110, height=130, image=Ric3, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic3.image=Ric3
        l_ic3.grid(row=1,column=5, padx=20)
        bic3=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic3.grid(row=4,column=5)
        pic3=tk.Label(frame_interior, text="Precio: 250,00$")
        pic3.grid(row=3,column=5)
        #OBJETO 4
        ic4=tk.PhotoImage(file="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT.png")
        Ric4=ic4.subsample(8)
        l_ic4=tk.Label(frame_interior,width=110, height=130, image=Ric4, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic4.image=Ric4
        l_ic4.grid(row=1,column=7, padx=20)
        bic4=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic4.grid(row=4,column=7)
        pic4=tk.Label(frame_interior, text="Precio: 250,00$")
        pic4.grid(row=3,column=7)
        #OBJETO 5
        ic5=tk.PhotoImage(file="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT.png")
        Ric5=ic5.subsample(8)
        l_ic5=tk.Label(frame_interior,width=110, height=130, image=Ric5, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic5.image=Ric5
        l_ic5.grid(row=1,column=9, padx=20)
        bic5=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic5.grid(row=4,column=9)
        pic5=tk.Label(frame_interior, text="Precio: 250,00$")
        pic5.grid(row=3,column=9)
        #OBJETO 6
        ic6=tk.PhotoImage(file="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT.png")
        Ric6=ic6.subsample(8)
        l_ic6=tk.Label(frame_interior,width=110, height=130, image=Ric6, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic6.image=Ric6
        l_ic6.grid(row=5,column=1, padx=20)
        pic6=tk.Label(frame_interior, text="Precio: 250,00$")
        pic6.grid(row=6,column=1)
        bic6=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic6.grid(row=7,column=1)
        #toolip1
        def mostrar_tooltip1(event):
            tooltip1.place(x=10,y=35)
        def ocultar_tooltip1(event):
            tooltip1.place_forget()
            # Crear una etiqueta para el tooltip
        tooltip1 = tk.Label(frame_interior, text="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT", bg="white", relief=tk.SOLID, borderwidth=1, font=("arial",10))
        l_ic1.bind("<Enter>", mostrar_tooltip1)
        l_ic1.bind("<Leave>", ocultar_tooltip1)
        #toolip2
        def mostrar_tooltip2(event):
            tooltip2.place(x=10,y=35)
        def ocultar_tooltip2(event):
            tooltip2.place_forget()
            # Crear una etiqueta para el tooltip
        tooltip2 = tk.Label(frame_interior, text="GIBSON LPTR00WSNH1", bg="white", relief=tk.SOLID, borderwidth=1, font=("arial",10))
        l_ic2.bind("<Enter>", mostrar_tooltip2)
        l_ic2.bind("<Leave>", ocultar_tooltip2)
        
        # Crear un botón "Regresar"
        boton_regresar = tk.Button(nuevo_marco, text="Regresar", command=lambda: nuevo_marco.destroy())
        boton_regresar.place(x=10, y=10)
    elif seleccion in combobox_values[3]:#VIOLINES
        # Crear un nuevo marco dentro del labelframe, nuevo_marco=frame principal
        nuevo_marco = tk.Frame(lfi, width=750, height=250, bg="red")
        nuevo_marco.place(x=0, y=0)
        # Creamos un canvas dentro del frame principal
        canvas = tk.Canvas(nuevo_marco, bg="pink", width=750, height=250)
        canvas.place(x=0, y=0)
        flf=tk.PhotoImage(file="fondo.png")
        fondolabel=tk.Label(canvas,image=flf)
        fondolabel.image=flf
        fondolabel.place(x=0,y=-220)
        
        # Frame interior para el contenido del canvas
        frame_interior = tk.Frame(canvas, width=750, height=250)
        canvas.create_window((0, 0), window=frame_interior, anchor="nw")
        flf=tk.PhotoImage(file="fondo.png").zoom(2)
        fondolabel=tk.Label(frame_interior,image=flf)
        fondolabel.image=flf
        fondolabel.place(x=0,y=-220)
        # Configurar el scrollbar
        scrollbar_vertical = Scrollbar(nuevo_marco, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar_vertical.place(x=733,y=0)
       # Configuramos el canvas y el scrollbar para que funcionen juntos
        canvas.config(yscrollcommand=scrollbar_vertical.set)

        # Conectamos el evento de entrada del ratón para activar el scroll
        canvas.bind("<Enter>", activar_scroll)
        canvas.bind("<Leave>", desactivar_scroll)
        #OBJETOS GENRALES
        decompras=tk.PhotoImage(file="carrito.png")
        decompras2=decompras.subsample(15)
        
        #OBJETO 1
        ic1=tk.PhotoImage(file="GIBSON LPTR00WSNH1.png")
        Ric1=ic1.subsample(8)
        l_ic1=tk.Label(frame_interior,width=110, height=130, image=Ric1, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic1.image=Ric1
        l_ic1.grid(row=1,column=1,padx=20)
        bic1=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic1.image=decompras2
        bic1.grid(row=4, column=1)
        pic1=tk.Label(frame_interior, text="Precio: 250,00$")
        pic1.grid(row=3, column=1)
        #OBJETO 2
        ic2=tk.PhotoImage(file="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT.png")
        Ric2=ic2.subsample(8)
        l_ic2=tk.Label(frame_interior,width=110, height=130, image=Ric2, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic2.image=Ric2
        l_ic2.grid(row=1,column=3, padx=20)
        bic2=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic2.grid(row=4,column=3)
        pic2=tk.Label(frame_interior, text="Precio: 250,00$")
        pic2.grid(row=3,column=3)
        #OBJETO 3
        ic3=tk.PhotoImage(file="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT.png")
        Ric3=ic3.subsample(8)
        l_ic3=tk.Label(frame_interior,width=110, height=130, image=Ric3, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic3.image=Ric3
        l_ic3.grid(row=1,column=5, padx=20)
        bic3=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic3.grid(row=4,column=5)
        pic3=tk.Label(frame_interior, text="Precio: 250,00$")
        pic3.grid(row=3,column=5)
        #OBJETO 4
        ic4=tk.PhotoImage(file="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT.png")
        Ric4=ic4.subsample(8)
        l_ic4=tk.Label(frame_interior,width=110, height=130, image=Ric4, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic4.image=Ric4
        l_ic4.grid(row=1,column=7, padx=20)
        bic4=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic4.grid(row=4,column=7)
        pic4=tk.Label(frame_interior, text="Precio: 250,00$")
        pic4.grid(row=3,column=7)
        #OBJETO 5
        ic5=tk.PhotoImage(file="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT.png")
        Ric5=ic5.subsample(8)
        l_ic5=tk.Label(frame_interior,width=110, height=130, image=Ric5, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic5.image=Ric5
        l_ic5.grid(row=1,column=9, padx=20)
        bic5=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic5.grid(row=4,column=9)
        pic5=tk.Label(frame_interior, text="Precio: 250,00$")
        pic5.grid(row=3,column=9)
        #OBJETO 6
        ic6=tk.PhotoImage(file="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT.png")
        Ric6=ic6.subsample(8)
        l_ic6=tk.Label(frame_interior,width=110, height=130, image=Ric6, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic6.image=Ric6
        l_ic6.grid(row=5,column=1, padx=20)
        pic6=tk.Label(frame_interior, text="Precio: 250,00$")
        pic6.grid(row=6,column=1)
        bic6=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic6.grid(row=7,column=1)
        #toolip1
        def mostrar_tooltip1(event):
            tooltip1.place(x=10,y=35)
        def ocultar_tooltip1(event):
            tooltip1.place_forget()
            # Crear una etiqueta para el tooltip
        tooltip1 = tk.Label(frame_interior, text="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT", bg="white", relief=tk.SOLID, borderwidth=1, font=("arial",10))
        l_ic1.bind("<Enter>", mostrar_tooltip1)
        l_ic1.bind("<Leave>", ocultar_tooltip1)
        #toolip2
        def mostrar_tooltip2(event):
            tooltip2.place(x=10,y=35)
        def ocultar_tooltip2(event):
            tooltip2.place_forget()
            # Crear una etiqueta para el tooltip
        tooltip2 = tk.Label(frame_interior, text="GIBSON LPTR00WSNH1", bg="white", relief=tk.SOLID, borderwidth=1, font=("arial",10))
        l_ic2.bind("<Enter>", mostrar_tooltip2)
        l_ic2.bind("<Leave>", ocultar_tooltip2)
        
        # Crear un botón "Regresar"
        boton_regresar = tk.Button(nuevo_marco, text="Regresar", command=lambda: nuevo_marco.destroy())
        boton_regresar.place(x=10, y=10)
    elif seleccion in combobox_values[4]:#UKELELES
        # Crear un nuevo marco dentro del labelframe, nuevo_marco=frame principal
        nuevo_marco = tk.Frame(lfi, width=750, height=250, bg="red")
        nuevo_marco.place(x=0, y=0)
        # Creamos un canvas dentro del frame principal
        canvas = tk.Canvas(nuevo_marco, bg="pink", width=750, height=250)
        canvas.place(x=0, y=0)
        flf=tk.PhotoImage(file="fondo.png")
        fondolabel=tk.Label(canvas,image=flf)
        fondolabel.image=flf
        fondolabel.place(x=0,y=-220)
        
        # Frame interior para el contenido del canvas
        frame_interior = tk.Frame(canvas, width=750, height=250)
        canvas.create_window((0, 0), window=frame_interior, anchor="nw")
        flf=tk.PhotoImage(file="fondo.png").zoom(2)
        fondolabel=tk.Label(frame_interior,image=flf)
        fondolabel.image=flf
        fondolabel.place(x=0,y=-220)
        # Configurar el scrollbar
        scrollbar_vertical = Scrollbar(nuevo_marco, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar_vertical.place(x=733,y=0)
       # Configuramos el canvas y el scrollbar para que funcionen juntos
        canvas.config(yscrollcommand=scrollbar_vertical.set)

        # Conectamos el evento de entrada del ratón para activar el scroll
        canvas.bind("<Enter>", activar_scroll)
        canvas.bind("<Leave>", desactivar_scroll)
        #OBJETOS GENRALES
        decompras=tk.PhotoImage(file="carrito.png")
        decompras2=decompras.subsample(15)
        
        #OBJETO 1
        ic1=tk.PhotoImage(file="GIBSON LPTR00WSNH1.png")
        Ric1=ic1.subsample(8)
        l_ic1=tk.Label(frame_interior,width=110, height=130, image=Ric1, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic1.image=Ric1
        l_ic1.grid(row=1,column=1,padx=20)
        bic1=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic1.image=decompras2
        bic1.grid(row=4, column=1)
        pic1=tk.Label(frame_interior, text="Precio: 250,00$")
        pic1.grid(row=3, column=1)
        #OBJETO 2
        ic2=tk.PhotoImage(file="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT.png")
        Ric2=ic2.subsample(8)
        l_ic2=tk.Label(frame_interior,width=110, height=130, image=Ric2, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic2.image=Ric2
        l_ic2.grid(row=1,column=3, padx=20)
        bic2=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic2.grid(row=4,column=3)
        pic2=tk.Label(frame_interior, text="Precio: 250,00$")
        pic2.grid(row=3,column=3)
        #OBJETO 3
        ic3=tk.PhotoImage(file="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT.png")
        Ric3=ic3.subsample(8)
        l_ic3=tk.Label(frame_interior,width=110, height=130, image=Ric3, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic3.image=Ric3
        l_ic3.grid(row=1,column=5, padx=20)
        bic3=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic3.grid(row=4,column=5)
        pic3=tk.Label(frame_interior, text="Precio: 250,00$")
        pic3.grid(row=3,column=5)
        #OBJETO 4
        ic4=tk.PhotoImage(file="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT.png")
        Ric4=ic4.subsample(8)
        l_ic4=tk.Label(frame_interior,width=110, height=130, image=Ric4, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic4.image=Ric4
        l_ic4.grid(row=1,column=7, padx=20)
        bic4=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic4.grid(row=4,column=7)
        pic4=tk.Label(frame_interior, text="Precio: 250,00$")
        pic4.grid(row=3,column=7)
        #OBJETO 5
        ic5=tk.PhotoImage(file="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT.png")
        Ric5=ic5.subsample(8)
        l_ic5=tk.Label(frame_interior,width=110, height=130, image=Ric5, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic5.image=Ric5
        l_ic5.grid(row=1,column=9, padx=20)
        bic5=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic5.grid(row=4,column=9)
        pic5=tk.Label(frame_interior, text="Precio: 250,00$")
        pic5.grid(row=3,column=9)
        #OBJETO 6
        ic6=tk.PhotoImage(file="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT.png")
        Ric6=ic6.subsample(8)
        l_ic6=tk.Label(frame_interior,width=110, height=130, image=Ric6, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic6.image=Ric6
        l_ic6.grid(row=5,column=1, padx=20)
        pic6=tk.Label(frame_interior, text="Precio: 250,00$")
        pic6.grid(row=6,column=1)
        bic6=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic6.grid(row=7,column=1)
        #toolip1
        def mostrar_tooltip1(event):
            tooltip1.place(x=10,y=35)
        def ocultar_tooltip1(event):
            tooltip1.place_forget()
            # Crear una etiqueta para el tooltip
        tooltip1 = tk.Label(frame_interior, text="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT", bg="white", relief=tk.SOLID, borderwidth=1, font=("arial",10))
        l_ic1.bind("<Enter>", mostrar_tooltip1)
        l_ic1.bind("<Leave>", ocultar_tooltip1)
        #toolip2
        def mostrar_tooltip2(event):
            tooltip2.place(x=10,y=35)
        def ocultar_tooltip2(event):
            tooltip2.place_forget()
            # Crear una etiqueta para el tooltip
        tooltip2 = tk.Label(frame_interior, text="GIBSON LPTR00WSNH1", bg="white", relief=tk.SOLID, borderwidth=1, font=("arial",10))
        l_ic2.bind("<Enter>", mostrar_tooltip2)
        l_ic2.bind("<Leave>", ocultar_tooltip2)
        
        # Crear un botón "Regresar"
        boton_regresar = tk.Button(nuevo_marco, text="Regresar", command=lambda: nuevo_marco.destroy())
        boton_regresar.place(x=10, y=10)
def Intrumentos_percusion(event):
    def scroll(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def activar_scroll(event):
        canvas.bind_all("<MouseWheel>", scroll)

    def desactivar_scroll(event):
        canvas.unbind_all("<MouseWheel>")
    seleccion = event.widget.get()
    combobox_values = event.widget.cget("values")
    if seleccion in combobox_values[1]:#BATERIAS ACUSTICAS
        # Crear un nuevo marco dentro del labelframe, nuevo_marco=frame principal
        nuevo_marco = tk.Frame(lfi, width=750, height=250, bg="red")
        nuevo_marco.place(x=0, y=0)
        # Creamos un canvas dentro del frame principal
        canvas = tk.Canvas(nuevo_marco, bg="pink", width=750, height=250)
        canvas.place(x=0, y=0)
        flf=tk.PhotoImage(file="fondo.png")
        fondolabel=tk.Label(canvas,image=flf)
        fondolabel.image=flf
        fondolabel.place(x=0,y=-220)
        
        # Frame interior para el contenido del canvas
        frame_interior = tk.Frame(canvas, width=750, height=250)
        canvas.create_window((0, 0), window=frame_interior, anchor="nw")
        flf=tk.PhotoImage(file="fondo.png").zoom(2)
        fondolabel=tk.Label(frame_interior,image=flf)
        fondolabel.image=flf
        fondolabel.place(x=0,y=-220)
        # Configurar el scrollbar
        scrollbar_vertical = Scrollbar(nuevo_marco, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar_vertical.place(x=733,y=0)
       # Configuramos el canvas y el scrollbar para que funcionen juntos
        canvas.config(yscrollcommand=scrollbar_vertical.set)

        # Conectamos el evento de entrada del ratón para activar el scroll
        canvas.bind("<Enter>", activar_scroll)
        canvas.bind("<Leave>", desactivar_scroll)
            #OBJETOS GENRALES
        decompras=tk.PhotoImage(file="carrito.png")
        decompras2=decompras.subsample(15)
        
        #OBJETO 1
        ic1=tk.PhotoImage(file="GIBSON LPTR00WSNH1.png")
        Ric1=ic1.subsample(8)
        l_ic1=tk.Label(frame_interior,width=110, height=130, image=Ric1, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic1.image=Ric1
        l_ic1.grid(row=1,column=1,padx=20)
        bic1=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic1.image=decompras2
        bic1.grid(row=4, column=1)
        pic1=tk.Label(frame_interior, text="Precio: 250,00$")
        pic1.grid(row=3, column=1)
        #OBJETO 2
        ic2=tk.PhotoImage(file="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT.png")
        Ric2=ic2.subsample(8)
        l_ic2=tk.Label(frame_interior,width=110, height=130, image=Ric2, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic2.image=Ric2
        l_ic2.grid(row=1,column=3, padx=20)
        bic2=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic2.grid(row=4,column=3)
        pic2=tk.Label(frame_interior, text="Precio: 250,00$")
        pic2.grid(row=3,column=3)
        #OBJETO 3
        ic3=tk.PhotoImage(file="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT.png")
        Ric3=ic3.subsample(8)
        l_ic3=tk.Label(frame_interior,width=110, height=130, image=Ric3, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic3.image=Ric3
        l_ic3.grid(row=1,column=5, padx=20)
        bic3=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic3.grid(row=4,column=5)
        pic3=tk.Label(frame_interior, text="Precio: 250,00$")
        pic3.grid(row=3,column=5)
        #OBJETO 4
        ic4=tk.PhotoImage(file="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT.png")
        Ric4=ic4.subsample(8)
        l_ic4=tk.Label(frame_interior,width=110, height=130, image=Ric4, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic4.image=Ric4
        l_ic4.grid(row=1,column=7, padx=20)
        bic4=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic4.grid(row=4,column=7)
        pic4=tk.Label(frame_interior, text="Precio: 250,00$")
        pic4.grid(row=3,column=7)
        #OBJETO 5
        ic5=tk.PhotoImage(file="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT.png")
        Ric5=ic5.subsample(8)
        l_ic5=tk.Label(frame_interior,width=110, height=130, image=Ric5, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic5.image=Ric5
        l_ic5.grid(row=1,column=9, padx=20)
        bic5=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic5.grid(row=4,column=9)
        pic5=tk.Label(frame_interior, text="Precio: 250,00$")
        pic5.grid(row=3,column=9)
        #OBJETO 6
        ic6=tk.PhotoImage(file="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT.png")
        Ric6=ic6.subsample(8)
        l_ic6=tk.Label(frame_interior,width=110, height=130, image=Ric6, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic6.image=Ric6
        l_ic6.grid(row=5,column=1, padx=20)
        pic6=tk.Label(frame_interior, text="Precio: 250,00$")
        pic6.grid(row=6,column=1)
        bic6=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic6.grid(row=7,column=1)
        #toolip1
        def mostrar_tooltip1(event):
            tooltip1.place(x=10,y=35)
        def ocultar_tooltip1(event):
            tooltip1.place_forget()
            # Crear una etiqueta para el tooltip
        tooltip1 = tk.Label(frame_interior, text="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT", bg="white", relief=tk.SOLID, borderwidth=1, font=("arial",10))
        l_ic1.bind("<Enter>", mostrar_tooltip1)
        l_ic1.bind("<Leave>", ocultar_tooltip1)
        #toolip2
        def mostrar_tooltip2(event):
            tooltip2.place(x=10,y=35)
        def ocultar_tooltip2(event):
            tooltip2.place_forget()
            # Crear una etiqueta para el tooltip
        tooltip2 = tk.Label(frame_interior, text="GIBSON LPTR00WSNH1", bg="white", relief=tk.SOLID, borderwidth=1, font=("arial",10))
        l_ic2.bind("<Enter>", mostrar_tooltip2)
        l_ic2.bind("<Leave>", ocultar_tooltip2)
        
        # Crear un botón "Regresar"
        boton_regresar = tk.Button(nuevo_marco, text="Regresar", command=lambda: nuevo_marco.destroy())
        boton_regresar.place(x=10, y=10)
    elif seleccion in combobox_values[2]:#BATERIAS ELECTRONICAS
        # Crear un nuevo marco dentro del labelframe, nuevo_marco=frame principal
        nuevo_marco = tk.Frame(lfi, width=750, height=250, bg="red")
        nuevo_marco.place(x=0, y=0)
        # Creamos un canvas dentro del frame principal
        canvas = tk.Canvas(nuevo_marco, bg="pink", width=750, height=250)
        canvas.place(x=0, y=0)
        flf=tk.PhotoImage(file="fondo.png")
        fondolabel=tk.Label(canvas,image=flf)
        fondolabel.image=flf
        fondolabel.place(x=0,y=-220)
        
        # Frame interior para el contenido del canvas
        frame_interior = tk.Frame(canvas, width=750, height=250)
        canvas.create_window((0, 0), window=frame_interior, anchor="nw")
        flf=tk.PhotoImage(file="fondo.png").zoom(2)
        fondolabel=tk.Label(frame_interior,image=flf)
        fondolabel.image=flf
        fondolabel.place(x=0,y=-220)
        # Configurar el scrollbar
        scrollbar_vertical = Scrollbar(nuevo_marco, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar_vertical.place(x=733,y=0)
       # Configuramos el canvas y el scrollbar para que funcionen juntos
        canvas.config(yscrollcommand=scrollbar_vertical.set)

        # Conectamos el evento de entrada del ratón para activar el scroll
        canvas.bind("<Enter>", activar_scroll)
        canvas.bind("<Leave>", desactivar_scroll)
        #OBJETOS GENRALES
        decompras=tk.PhotoImage(file="carrito.png")
        decompras2=decompras.subsample(15)
        
        #OBJETO 1
        ic1=tk.PhotoImage(file="GIBSON LPTR00WSNH1.png")
        Ric1=ic1.subsample(8)
        l_ic1=tk.Label(frame_interior,width=110, height=130, image=Ric1, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic1.image=Ric1
        l_ic1.grid(row=1,column=1,padx=20)
        bic1=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic1.image=decompras2
        bic1.grid(row=4, column=1)
        pic1=tk.Label(frame_interior, text="Precio: 250,00$")
        pic1.grid(row=3, column=1)
        #OBJETO 2
        ic2=tk.PhotoImage(file="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT.png")
        Ric2=ic2.subsample(8)
        l_ic2=tk.Label(frame_interior,width=110, height=130, image=Ric2, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic2.image=Ric2
        l_ic2.grid(row=1,column=3, padx=20)
        bic2=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic2.grid(row=4,column=3)
        pic2=tk.Label(frame_interior, text="Precio: 250,00$")
        pic2.grid(row=3,column=3)
        #OBJETO 3
        ic3=tk.PhotoImage(file="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT.png")
        Ric3=ic3.subsample(8)
        l_ic3=tk.Label(frame_interior,width=110, height=130, image=Ric3, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic3.image=Ric3
        l_ic3.grid(row=1,column=5, padx=20)
        bic3=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic3.grid(row=4,column=5)
        pic3=tk.Label(frame_interior, text="Precio: 250,00$")
        pic3.grid(row=3,column=5)
        #OBJETO 4
        ic4=tk.PhotoImage(file="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT.png")
        Ric4=ic4.subsample(8)
        l_ic4=tk.Label(frame_interior,width=110, height=130, image=Ric4, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic4.image=Ric4
        l_ic4.grid(row=1,column=7, padx=20)
        bic4=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic4.grid(row=4,column=7)
        pic4=tk.Label(frame_interior, text="Precio: 250,00$")
        pic4.grid(row=3,column=7)
        #OBJETO 5
        ic5=tk.PhotoImage(file="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT.png")
        Ric5=ic5.subsample(8)
        l_ic5=tk.Label(frame_interior,width=110, height=130, image=Ric5, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic5.image=Ric5
        l_ic5.grid(row=1,column=9, padx=20)
        bic5=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic5.grid(row=4,column=9)
        pic5=tk.Label(frame_interior, text="Precio: 250,00$")
        pic5.grid(row=3,column=9)
        #OBJETO 6
        ic6=tk.PhotoImage(file="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT.png")
        Ric6=ic6.subsample(8)
        l_ic6=tk.Label(frame_interior,width=110, height=130, image=Ric6, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic6.image=Ric6
        l_ic6.grid(row=5,column=1, padx=20)
        pic6=tk.Label(frame_interior, text="Precio: 250,00$")
        pic6.grid(row=6,column=1)
        bic6=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic6.grid(row=7,column=1)
        #toolip1
        def mostrar_tooltip1(event):
            tooltip1.place(x=10,y=35)
        def ocultar_tooltip1(event):
            tooltip1.place_forget()
            # Crear una etiqueta para el tooltip
        tooltip1 = tk.Label(frame_interior, text="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT", bg="white", relief=tk.SOLID, borderwidth=1, font=("arial",10))
        l_ic1.bind("<Enter>", mostrar_tooltip1)
        l_ic1.bind("<Leave>", ocultar_tooltip1)
        #toolip2
        def mostrar_tooltip2(event):
            tooltip2.place(x=10,y=35)
        def ocultar_tooltip2(event):
            tooltip2.place_forget()
            # Crear una etiqueta para el tooltip
        tooltip2 = tk.Label(frame_interior, text="GIBSON LPTR00WSNH1", bg="white", relief=tk.SOLID, borderwidth=1, font=("arial",10))
        l_ic2.bind("<Enter>", mostrar_tooltip2)
        l_ic2.bind("<Leave>", ocultar_tooltip2)
        
        # Crear un botón "Regresar"
        boton_regresar = tk.Button(nuevo_marco, text="Regresar", command=lambda: nuevo_marco.destroy())
        boton_regresar.place(x=10, y=10)
    elif seleccion in combobox_values[3]:#PLATILLOS
        # Crear un nuevo marco dentro del labelframe, nuevo_marco=frame principal
        nuevo_marco = tk.Frame(lfi, width=750, height=250, bg="red")
        nuevo_marco.place(x=0, y=0)
        # Creamos un canvas dentro del frame principal
        canvas = tk.Canvas(nuevo_marco, bg="pink", width=750, height=250)
        canvas.place(x=0, y=0)
        flf=tk.PhotoImage(file="fondo.png")
        fondolabel=tk.Label(canvas,image=flf)
        fondolabel.image=flf
        fondolabel.place(x=0,y=-220)
        
        # Frame interior para el contenido del canvas
        frame_interior = tk.Frame(canvas, width=750, height=250)
        canvas.create_window((0, 0), window=frame_interior, anchor="nw")
        flf=tk.PhotoImage(file="fondo.png").zoom(2)
        fondolabel=tk.Label(frame_interior,image=flf)
        fondolabel.image=flf
        fondolabel.place(x=0,y=-220)
        # Configurar el scrollbar
        scrollbar_vertical = Scrollbar(nuevo_marco, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar_vertical.place(x=733,y=0)
       # Configuramos el canvas y el scrollbar para que funcionen juntos
        canvas.config(yscrollcommand=scrollbar_vertical.set)

        # Conectamos el evento de entrada del ratón para activar el scroll
        canvas.bind("<Enter>", activar_scroll)
        canvas.bind("<Leave>", desactivar_scroll)
        #OBJETOS GENRALES
        decompras=tk.PhotoImage(file="carrito.png")
        decompras2=decompras.subsample(15)
        
        #OBJETO 1
        ic1=tk.PhotoImage(file="GIBSON LPTR00WSNH1.png")
        Ric1=ic1.subsample(8)
        l_ic1=tk.Label(frame_interior,width=110, height=130, image=Ric1, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic1.image=Ric1
        l_ic1.grid(row=1,column=1,padx=20)
        bic1=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic1.image=decompras2
        bic1.grid(row=4, column=1)
        pic1=tk.Label(frame_interior, text="Precio: 250,00$")
        pic1.grid(row=3, column=1)
        #OBJETO 2
        ic2=tk.PhotoImage(file="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT.png")
        Ric2=ic2.subsample(8)
        l_ic2=tk.Label(frame_interior,width=110, height=130, image=Ric2, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic2.image=Ric2
        l_ic2.grid(row=1,column=3, padx=20)
        bic2=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic2.grid(row=4,column=3)
        pic2=tk.Label(frame_interior, text="Precio: 250,00$")
        pic2.grid(row=3,column=3)
        #OBJETO 3
        ic3=tk.PhotoImage(file="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT.png")
        Ric3=ic3.subsample(8)
        l_ic3=tk.Label(frame_interior,width=110, height=130, image=Ric3, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic3.image=Ric3
        l_ic3.grid(row=1,column=5, padx=20)
        bic3=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic3.grid(row=4,column=5)
        pic3=tk.Label(frame_interior, text="Precio: 250,00$")
        pic3.grid(row=3,column=5)
        #OBJETO 4
        ic4=tk.PhotoImage(file="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT.png")
        Ric4=ic4.subsample(8)
        l_ic4=tk.Label(frame_interior,width=110, height=130, image=Ric4, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic4.image=Ric4
        l_ic4.grid(row=1,column=7, padx=20)
        bic4=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic4.grid(row=4,column=7)
        pic4=tk.Label(frame_interior, text="Precio: 250,00$")
        pic4.grid(row=3,column=7)
        #OBJETO 5
        ic5=tk.PhotoImage(file="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT.png")
        Ric5=ic5.subsample(8)
        l_ic5=tk.Label(frame_interior,width=110, height=130, image=Ric5, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic5.image=Ric5
        l_ic5.grid(row=1,column=9, padx=20)
        bic5=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic5.grid(row=4,column=9)
        pic5=tk.Label(frame_interior, text="Precio: 250,00$")
        pic5.grid(row=3,column=9)
        #OBJETO 6
        ic6=tk.PhotoImage(file="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT.png")
        Ric6=ic6.subsample(8)
        l_ic6=tk.Label(frame_interior,width=110, height=130, image=Ric6, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic6.image=Ric6
        l_ic6.grid(row=5,column=1, padx=20)
        pic6=tk.Label(frame_interior, text="Precio: 250,00$")
        pic6.grid(row=6,column=1)
        bic6=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic6.grid(row=7,column=1)
        #toolip1
        def mostrar_tooltip1(event):
            tooltip1.place(x=10,y=35)
        def ocultar_tooltip1(event):
            tooltip1.place_forget()
            # Crear una etiqueta para el tooltip
        tooltip1 = tk.Label(frame_interior, text="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT", bg="white", relief=tk.SOLID, borderwidth=1, font=("arial",10))
        l_ic1.bind("<Enter>", mostrar_tooltip1)
        l_ic1.bind("<Leave>", ocultar_tooltip1)
        #toolip2
        def mostrar_tooltip2(event):
            tooltip2.place(x=10,y=35)
        def ocultar_tooltip2(event):
            tooltip2.place_forget()
            # Crear una etiqueta para el tooltip
        tooltip2 = tk.Label(frame_interior, text="GIBSON LPTR00WSNH1", bg="white", relief=tk.SOLID, borderwidth=1, font=("arial",10))
        l_ic2.bind("<Enter>", mostrar_tooltip2)
        l_ic2.bind("<Leave>", ocultar_tooltip2)
        
        # Crear un botón "Regresar"
        boton_regresar = tk.Button(nuevo_marco, text="Regresar", command=lambda: nuevo_marco.destroy())
        boton_regresar.place(x=10, y=10)
    elif seleccion in combobox_values[4]:#pPERCUSION LATINA
        # Crear un nuevo marco dentro del labelframe, nuevo_marco=frame principal
        nuevo_marco = tk.Frame(lfi, width=750, height=250, bg="red")
        nuevo_marco.place(x=0, y=0)
        # Creamos un canvas dentro del frame principal
        canvas = tk.Canvas(nuevo_marco, bg="pink", width=750, height=250)
        canvas.place(x=0, y=0)
        flf=tk.PhotoImage(file="fondo.png")
        fondolabel=tk.Label(canvas,image=flf)
        fondolabel.image=flf
        fondolabel.place(x=0,y=-220)
        
        # Frame interior para el contenido del canvas
        frame_interior = tk.Frame(canvas, width=750, height=250)
        canvas.create_window((0, 0), window=frame_interior, anchor="nw")
        flf=tk.PhotoImage(file="fondo.png").zoom(2)
        fondolabel=tk.Label(frame_interior,image=flf)
        fondolabel.image=flf
        fondolabel.place(x=0,y=-220)
        # Configurar el scrollbar
        scrollbar_vertical = Scrollbar(nuevo_marco, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar_vertical.place(x=733,y=0)
       # Configuramos el canvas y el scrollbar para que funcionen juntos
        canvas.config(yscrollcommand=scrollbar_vertical.set)

        # Conectamos el evento de entrada del ratón para activar el scroll
        canvas.bind("<Enter>", activar_scroll)
        canvas.bind("<Leave>", desactivar_scroll)
        #OBJETOS GENRALES
        decompras=tk.PhotoImage(file="carrito.png")
        decompras2=decompras.subsample(15)
        
        #OBJETO 1
        ic1=tk.PhotoImage(file="GIBSON LPTR00WSNH1.png")
        Ric1=ic1.subsample(8)
        l_ic1=tk.Label(frame_interior,width=110, height=130, image=Ric1, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic1.image=Ric1
        l_ic1.grid(row=1,column=1,padx=20)
        bic1=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic1.image=decompras2
        bic1.grid(row=4, column=1)
        pic1=tk.Label(frame_interior, text="Precio: 250,00$")
        pic1.grid(row=3, column=1)
        #OBJETO 2
        ic2=tk.PhotoImage(file="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT.png")
        Ric2=ic2.subsample(8)
        l_ic2=tk.Label(frame_interior,width=110, height=130, image=Ric2, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic2.image=Ric2
        l_ic2.grid(row=1,column=3, padx=20)
        bic2=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic2.grid(row=4,column=3)
        pic2=tk.Label(frame_interior, text="Precio: 250,00$")
        pic2.grid(row=3,column=3)
        #OBJETO 3
        ic3=tk.PhotoImage(file="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT.png")
        Ric3=ic3.subsample(8)
        l_ic3=tk.Label(frame_interior,width=110, height=130, image=Ric3, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic3.image=Ric3
        l_ic3.grid(row=1,column=5, padx=20)
        bic3=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic3.grid(row=4,column=5)
        pic3=tk.Label(frame_interior, text="Precio: 250,00$")
        pic3.grid(row=3,column=5)
        #OBJETO 4
        ic4=tk.PhotoImage(file="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT.png")
        Ric4=ic4.subsample(8)
        l_ic4=tk.Label(frame_interior,width=110, height=130, image=Ric4, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic4.image=Ric4
        l_ic4.grid(row=1,column=7, padx=20)
        bic4=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic4.grid(row=4,column=7)
        pic4=tk.Label(frame_interior, text="Precio: 250,00$")
        pic4.grid(row=3,column=7)
        #OBJETO 5
        ic5=tk.PhotoImage(file="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT.png")
        Ric5=ic5.subsample(8)
        l_ic5=tk.Label(frame_interior,width=110, height=130, image=Ric5, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic5.image=Ric5
        l_ic5.grid(row=1,column=9, padx=20)
        bic5=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic5.grid(row=4,column=9)
        pic5=tk.Label(frame_interior, text="Precio: 250,00$")
        pic5.grid(row=3,column=9)
        #OBJETO 6
        ic6=tk.PhotoImage(file="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT.png")
        Ric6=ic6.subsample(8)
        l_ic6=tk.Label(frame_interior,width=110, height=130, image=Ric6, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic6.image=Ric6
        l_ic6.grid(row=5,column=1, padx=20)
        pic6=tk.Label(frame_interior, text="Precio: 250,00$")
        pic6.grid(row=6,column=1)
        bic6=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic6.grid(row=7,column=1)
        #toolip1
        def mostrar_tooltip1(event):
            tooltip1.place(x=10,y=35)
        def ocultar_tooltip1(event):
            tooltip1.place_forget()
            # Crear una etiqueta para el tooltip
        tooltip1 = tk.Label(frame_interior, text="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT", bg="white", relief=tk.SOLID, borderwidth=1, font=("arial",10))
        l_ic1.bind("<Enter>", mostrar_tooltip1)
        l_ic1.bind("<Leave>", ocultar_tooltip1)
        #toolip2
        def mostrar_tooltip2(event):
            tooltip2.place(x=10,y=35)
        def ocultar_tooltip2(event):
            tooltip2.place_forget()
            # Crear una etiqueta para el tooltip
        tooltip2 = tk.Label(frame_interior, text="GIBSON LPTR00WSNH1", bg="white", relief=tk.SOLID, borderwidth=1, font=("arial",10))
        l_ic2.bind("<Enter>", mostrar_tooltip2)
        l_ic2.bind("<Leave>", ocultar_tooltip2)
        
        # Crear un botón "Regresar"
        boton_regresar = tk.Button(nuevo_marco, text="Regresar", command=lambda: nuevo_marco.destroy())
        boton_regresar.place(x=10, y=10)
    elif seleccion in combobox_values[5]:#MARCHA
        # Crear un nuevo marco dentro del labelframe, nuevo_marco=frame principal
        nuevo_marco = tk.Frame(lfi, width=750, height=250, bg="red")
        nuevo_marco.place(x=0, y=0)
        # Creamos un canvas dentro del frame principal
        canvas = tk.Canvas(nuevo_marco, bg="pink", width=750, height=250)
        canvas.place(x=0, y=0)
        flf=tk.PhotoImage(file="fondo.png")
        fondolabel=tk.Label(canvas,image=flf)
        fondolabel.image=flf
        fondolabel.place(x=0,y=-220)
        
        # Frame interior para el contenido del canvas
        frame_interior = tk.Frame(canvas, width=750, height=250)
        canvas.create_window((0, 0), window=frame_interior, anchor="nw")
        flf=tk.PhotoImage(file="fondo.png").zoom(2)
        fondolabel=tk.Label(frame_interior,image=flf)
        fondolabel.image=flf
        fondolabel.place(x=0,y=-220)
        # Configurar el scrollbar
        scrollbar_vertical = Scrollbar(nuevo_marco, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar_vertical.place(x=733,y=0)
       # Configuramos el canvas y el scrollbar para que funcionen juntos
        canvas.config(yscrollcommand=scrollbar_vertical.set)

        # Conectamos el evento de entrada del ratón para activar el scroll
        canvas.bind("<Enter>", activar_scroll)
        canvas.bind("<Leave>", desactivar_scroll)
        #OBJETOS GENRALES
        decompras=tk.PhotoImage(file="carrito.png")
        decompras2=decompras.subsample(15)
        
        #OBJETO 1
        ic1=tk.PhotoImage(file="GIBSON LPTR00WSNH1.png")
        Ric1=ic1.subsample(8)
        l_ic1=tk.Label(frame_interior,width=110, height=130, image=Ric1, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic1.image=Ric1
        l_ic1.grid(row=1,column=1,padx=20)
        bic1=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic1.image=decompras2
        bic1.grid(row=4, column=1)
        pic1=tk.Label(frame_interior, text="Precio: 250,00$")
        pic1.grid(row=3, column=1)
        #OBJETO 2
        ic2=tk.PhotoImage(file="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT.png")
        Ric2=ic2.subsample(8)
        l_ic2=tk.Label(frame_interior,width=110, height=130, image=Ric2, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic2.image=Ric2
        l_ic2.grid(row=1,column=3, padx=20)
        bic2=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic2.grid(row=4,column=3)
        pic2=tk.Label(frame_interior, text="Precio: 250,00$")
        pic2.grid(row=3,column=3)
        #OBJETO 3
        ic3=tk.PhotoImage(file="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT.png")
        Ric3=ic3.subsample(8)
        l_ic3=tk.Label(frame_interior,width=110, height=130, image=Ric3, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic3.image=Ric3
        l_ic3.grid(row=1,column=5, padx=20)
        bic3=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic3.grid(row=4,column=5)
        pic3=tk.Label(frame_interior, text="Precio: 250,00$")
        pic3.grid(row=3,column=5)
        #OBJETO 4
        ic4=tk.PhotoImage(file="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT.png")
        Ric4=ic4.subsample(8)
        l_ic4=tk.Label(frame_interior,width=110, height=130, image=Ric4, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic4.image=Ric4
        l_ic4.grid(row=1,column=7, padx=20)
        bic4=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic4.grid(row=4,column=7)
        pic4=tk.Label(frame_interior, text="Precio: 250,00$")
        pic4.grid(row=3,column=7)
        #OBJETO 5
        ic5=tk.PhotoImage(file="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT.png")
        Ric5=ic5.subsample(8)
        l_ic5=tk.Label(frame_interior,width=110, height=130, image=Ric5, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic5.image=Ric5
        l_ic5.grid(row=1,column=9, padx=20)
        bic5=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic5.grid(row=4,column=9)
        pic5=tk.Label(frame_interior, text="Precio: 250,00$")
        pic5.grid(row=3,column=9)
        #OBJETO 6
        ic6=tk.PhotoImage(file="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT.png")
        Ric6=ic6.subsample(8)
        l_ic6=tk.Label(frame_interior,width=110, height=130, image=Ric6, bg="white", relief=tk.SOLID, borderwidth=1)
        l_ic6.image=Ric6
        l_ic6.grid(row=5,column=1, padx=20)
        pic6=tk.Label(frame_interior, text="Precio: 250,00$")
        pic6.grid(row=6,column=1)
        bic6=tk.Button(frame_interior, text="Añadir al carrito", image=decompras2, compound="right", bd=4, font=("Arial", 5))
        bic6.grid(row=7,column=1)
        #toolip1
        def mostrar_tooltip1(event):
            tooltip1.place(x=10,y=35)
        def ocultar_tooltip1(event):
            tooltip1.place_forget()
            # Crear una etiqueta para el tooltip
        tooltip1 = tk.Label(frame_interior, text="GIBSON MCRS4SWLWB J-45 STUDIO WALNUT", bg="white", relief=tk.SOLID, borderwidth=1, font=("arial",10))
        l_ic1.bind("<Enter>", mostrar_tooltip1)
        l_ic1.bind("<Leave>", ocultar_tooltip1)
        #toolip2
        def mostrar_tooltip2(event):
            tooltip2.place(x=10,y=35)
        def ocultar_tooltip2(event):
            tooltip2.place_forget()
            # Crear una etiqueta para el tooltip
        tooltip2 = tk.Label(frame_interior, text="GIBSON LPTR00WSNH1", bg="white", relief=tk.SOLID, borderwidth=1, font=("arial",10))
        l_ic2.bind("<Enter>", mostrar_tooltip2)
        l_ic2.bind("<Leave>", ocultar_tooltip2)
        
        # Crear un botón "Regresar"
        boton_regresar = tk.Button(nuevo_marco, text="Regresar", command=lambda: nuevo_marco.destroy())
        boton_regresar.place(x=10, y=10)
Guitarras_bajos=["Instrumentos de cuerda", "Guitarras", "Bajos", "Violines", "Ukeleles"]
Baterias=["Instrumentos de percusion", "Baterias Acusticas", "Baterias Electronicas", "Platillos","Percusion Latina", "Marcha"]
Teclado=["Teclados", "Teclados para Arreglos", "Teclados para Produccion", "Pianos Digitales", "Sintetizadores"]
Viento=["Instrumentos de viento", "Falutas", "Armonicas", "Melodicas","Trompetas", "Saxofones", "Clarinetes" ]
Cuerda=["Others", "Cuerdas", "Sellos", "Pedales"]
Instrumentos = ttk.Combobox(lfi, values=Guitarras_bajos)
Instrumentos.set(Guitarras_bajos[0])
Instrumentos.place(x=10,y=0)

Instrumentos2=ttk.Combobox(lfi,values=Baterias)
Instrumentos2.set(Baterias[0])
Instrumentos2.place(x=155,y=0)

Instrumentos3=ttk.Combobox(lfi,values=Teclado)
Instrumentos3.set(Teclado[0])
Instrumentos3.place(x=300,y=0)

Instrumentos4=ttk.Combobox(lfi,values=Viento)
Instrumentos4.set(Viento[0])
Instrumentos4.place(x=445,y=0)

Instrumentos5=ttk.Combobox(lfi,values=Cuerda)
Instrumentos5.set(Cuerda[0])
Instrumentos5.place(x=590,y=0)

# Vincular la selección de combobox a la función crear_marco
Instrumentos.bind("<<ComboboxSelected>>", Intrumentos_cuerda)
Instrumentos2.bind("<<ComboboxSelected>>", Intrumentos_percusion)
Instrumentos3.bind("<<ComboboxSelected>>")
Instrumentos4.bind("<<ComboboxSelected>>")
Instrumentos5.bind("<<ComboboxSelected>>")
#OFERTAS QUE VAN EN lfi============================================================0
                    #========================================================= 
    #OBJETOS GENRALES
carro=tk.PhotoImage(file="carrito.png")
carro2=carro.subsample(15)
of1=tk.PhotoImage(file="Samsung.png")
#OBJETO 1
r_of1=of1.subsample(8)
l_of1=tk.Label(lfi,width=110, height=130, image=r_of1, bg="white", relief=tk.SOLID, borderwidth=1)
l_of1.place(x=20,y=35)
bof1=tk.Button(lfi, text="Añadir al carrito", image=carro2, compound="left", bd=2, font=("Arial", 8))
bof1.place(x=20, y=190)
Lof1=tk.Label(lfi, text="%OFERTA%", bg="Red")
Lof1.place(x=80,y=30)
pof1=tk.Label(lfi, text="Precio: 120,00$")
pof1.place(x=30,y=170)


#OBJETO 2
of2=tk.PhotoImage(file="Skullcandy JIB TRUE 2 WIRELESS IN-EAR.png")
r_of2=of2.subsample(9)
l_of2=tk.Label(lfi,width=110, height=130, image=r_of2, bg="white", relief=tk.SOLID, borderwidth=1)
l_of2.place(x=155,y=35)
bof2=tk.Button(lfi, text="Añadir al carrito", image=carro2, compound="left", bd=2, font=("Arial", 8))
bof2.place(x=155, y=190)
Lof2=tk.Label(lfi, text="%OFERTA%", bg="Red")
Lof2.place(x=200,y=30)
pof2=tk.Label(lfi, text="Precio: 18,00$")
pof2.place(x=155,y=170)


#OBJETO3
of3=tk.PhotoImage(file="Teclado Mecánico Gamer Retroiluminado Xtrike Me 979.png")
r_of3=of3.subsample(9)
l_of3=tk.Label(lfi,width=110, height=130, image=r_of3, bg="white", relief=tk.SOLID, borderwidth=1)
l_of3.place(x=310,y=35)
bof3=tk.Button(lfi, text="Añadir al carrito", image=carro2, compound="left", bd=2, font=("Arial", 8))
bof3.place(x=310, y=190)
Lof3=tk.Label(lfi, text="%OFERTA%", bg="Red")
Lof3.place(x=370,y=30)
pof3=tk.Label(lfi, text="Precio: 29,99$")
pof3.place(x=310,y=170)

#OBJETO4
of4=tk.PhotoImage(file="MARINER-86-Utomhushögtalare.png")
r_of4=of4.subsample(10)
l_of4=tk.Label(lfi,width=110, height=130, image=r_of4, bg="white", relief=tk.SOLID, borderwidth=1)
l_of4.place(x=465,y=35)
bof4=tk.Button(lfi, text="Añadir al carrito", image=carro2, compound="left", bd=2, font=("Arial", 8))
bof4.place(x=465, y=190)
Lof4=tk.Label(lfi, text="%OFERTA%", bg="Red")
Lof4.place(x=530,y=30)
pof4=tk.Label(lfi, text="Precio: 30,00$")
pof4.place(x=465,y=170)


#OBJETO5
of5=tk.PhotoImage(file="Microfono Gamer Xtrike Me XMC-01.png")
r_of5=of5.subsample(8)
l_of5=tk.Label(lfi,width=110, height=130, image=r_of5, bg="white", relief=tk.SOLID, borderwidth=1)
l_of5.place(x=620,y=35)
bof5=tk.Button(lfi, text="Añadir al carrito", image=carro2, compound="left", bd=2, font=("Arial", 8))
bof5.place(x=620, y=190)
Lof5=tk.Label(lfi, text="%OFERTA%", bg="Red")
Lof5.place(x=680,y=30)
pof5=tk.Label(lfi, text="Precio: 40,99$")
pof5.place(x=610,y=170)
#toolip1
def mostrar_tooltip1(event):
    tooltip1.place(x=20,y=35)
def ocultar_tooltip1(event):
    tooltip1.place_forget()
    # Crear una etiqueta para el tooltip
tooltip1 = tk.Label(lfi, text="TELEVISOR-TV SAMSUNG 55″ LED CRYSTAL 4K UHD SMART WIFI", bg="white", relief=tk.SOLID, borderwidth=1, font=("arial",10))
l_of1.bind("<Enter>", mostrar_tooltip1)
l_of1.bind("<Leave>", ocultar_tooltip1)
#toolip2
def mostrar_tooltip2(event):
    tooltip2.place(x=145,y=35)
def ocultar_tooltip2(event):
    tooltip2.place_forget()
    # Crear una etiqueta para el tooltip
tooltip2 = tk.Label(lfi, text="Skullcandy JIB TRUE 2 WIRELESS IN-EAR", bg="white", relief=tk.SOLID, borderwidth=1, font=("arial",10))
l_of2.bind("<Enter>", mostrar_tooltip2)
l_of2.bind("<Leave>", ocultar_tooltip2)
#toolip3
def mostrar_tooltip3(event):
    tooltip3.place(x=300,y=35)
def ocultar_tooltip3(event):
    tooltip3.place_forget()
    # Crear una etiqueta para el tooltip
tooltip3 = tk.Label(lfi, text="Teclado Mecánico Gamer Retroiluminado Xtrike Me 979", bg="white", relief=tk.SOLID, borderwidth=1, font=("arial",10))
l_of3.bind("<Enter>", mostrar_tooltip3)
l_of3.bind("<Leave>", ocultar_tooltip3)
#toolip4
def mostrar_tooltip4(event):
    tooltip4.place(x=455,y=35)
def ocultar_tooltip4(event):
    tooltip4.place_forget()
    # Crear una etiqueta para el tooltip
tooltip4 = tk.Label(lfi, text="MARINER-86-Utomhushögtalare", bg="white", relief=tk.SOLID, borderwidth=1, font=("arial",10))
l_of4.bind("<Enter>", mostrar_tooltip4)
l_of4.bind("<Leave>", ocultar_tooltip4)
#toolip5
def mostrar_tooltip5(event):
    tooltip5.place(x=600,y=200)
def ocultar_tooltip5(event):
    tooltip5.place_forget()
    # Crear una etiqueta para el tooltip
tooltip5 = tk.Label(ventana, text="Microfono Gamer Xtrike Me XMC-01", bg="white", relief=tk.SOLID, borderwidth=1, font=("arial",10))
l_of5.bind("<Enter>", mostrar_tooltip5)
l_of5.bind("<Leave>", ocultar_tooltip5) 
                    #==================================================000
#===============================================================================

# Crear boton para registrarse==================================================
def registrarse():
    ventana_de_registro=tk.Toplevel(ventana)
    ventana_de_registro.title("INICIAR SESIÓN")
    ventana_de_registro.geometry("500x550")
    ventana_de_registro.resizable(False,False)
    ventana_de_registro.iconbitmap("logo.ico")
    label = tk.Label(ventana_de_registro, text="Ventana Opción " )
    label.pack(pady=20)
    
    boton_volver = tk.Button(ventana_de_registro, text="Volver a la ventana principal", command=ventana_de_registro.destroy)
    boton_volver.pack()

registro_imagen=tk.PhotoImage(file="singup.png")
sing_up=registro_imagen.subsample(15)
boton_inicio=tk.Button(principal, image=sing_up,bd=10, highlightthickness=1, padx=2, compound="left", command=registrarse )
boton_inicio.place(x=550,y=10)
boton_inicio.config(bg="white")
def mostrar_tooltip(event):
    tooltip.place(x=550,y=70)
def ocultar_tooltip(event):
    tooltip.place_forget()
# Crear una etiqueta para el tooltip
tooltip = tk.Label(ventana, text="Mi Cuenta", bg="white", relief=tk.SOLID, borderwidth=1, font=("norwester",10))
boton_inicio.bind("<Enter>", mostrar_tooltip)
boton_inicio.bind("<Leave>", ocultar_tooltip)
#crear boton para ir a comprar====================================================================================================================================================================
def ir_a_comprar():
    ventana_opcion = tk.Toplevel(ventana)
    ventana_opcion.title("Facturación")
    ventana_opcion.geometry("400x550")
    ventana_opcion.resizable(False,False)
    ventana_opcion.iconbitmap("logo.ico")
    
    label = tk.Label(ventana_opcion, text="Ventana Opción " )
    label.pack(pady=20)
    
    boton_volver = tk.Button(ventana_opcion, text="Volver a la ventana principal", command=ventana_opcion.destroy)
    boton_volver.pack()

fondo_carrito=tk.PhotoImage(file="carrito.png")
carrito_redimensiondao=fondo_carrito.subsample(15)
boton_comprar=tk.Button(principal, text="   Ver carrito  ", image=carrito_redimensiondao, compound=tk.RIGHT, command=ir_a_comprar, bd=10, highlightthickness=0, padx=2, font=("norwester", 10))
boton_comprar.place(x=650,y=10)
boton_comprar.config(bg="white")
#=================================================================================================================================================================================================
ventana.mainloop()