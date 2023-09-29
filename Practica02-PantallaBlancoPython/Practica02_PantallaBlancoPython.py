import tkinter as tk

#pantalla en blanco
Pantalla = tk.Tk()
Pantalla.title("Hola mundo")
Pantalla.geometry("520x480")




#cuadro de texto y boton
entrada=tk.Entry()
entrada.place(x=50,y=50,width=150)
boton=tk.Button(text="Aceptar")
boton.place(x=50,y=100)



Pantalla.mainloop()

