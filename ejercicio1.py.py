import tkinter as tk

def mostrar_mensaje():
    edad = entry_edad.get()
    mensaje.config(text=f"Hola Perla, tienes {edad} años")

ventana = tk.Tk()
ventana.title("Ejercicio 1")
ventana.geometry("300x200")

label_nombre = tk.Label(ventana, text="Mi nombre es Perla")
label_nombre.pack()

entry_edad = tk.Entry(ventana)
entry_edad.pack()

boton = tk.Button(ventana, text="Mostrar mensaje", command=mostrar_mensaje)
boton.pack()

mensaje = tk.Label(ventana, text="")
mensaje.pack()

ventana.mainloop()