# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 18:18:06 2024

@author: VaNXiroX
"""

import tkinter as tk
from tkinter import messagebox


def limpiar_campos():
    tbNombre.delete(0, tk.END)
    tbApellidos.delete(0, tk.END)
    tbEdad.delete(0, tk.END)
    tbEstatura.delete(0, tk.END)
    tbTelefono.delete(0, tk.END)
    var_genero.set(0)  

def borrar_fun():
    limpiar_campos()

def guardar_valores():

    nombres = tbNombre.get()
    apellidos = tbApellidos.get()
    edad = tbEdad.get()
    estatura = tbEstatura.get()
    telefono = tbTelefono.get()

    genero = ""
    if var_genero.get() == 1:
        genero = "Hombre"
    elif var_genero.get() == 2:
        genero = "Mujer"
    elif var_genero.get()== 3:
        genero = "Helicoptero_apache"
        
    datos = f"Nombres: {nombres}\nApellidos: {apellidos}\nEdad: {edad} años\nEstatura: {estatura}\nTeléfono: {telefono}\nGénero: {genero}\n"


    with open("302024Datos.txt", "a") as archivo:
        archivo.write(datos + "\n\n")

   
    messagebox.showinfo("Información", "Datos guardados con éxito: \n\n" + datos)

    limpiar_campos()


ventana = tk.Tk()
ventana.geometry("520x500")
ventana.title("Formulario Vr.01")


var_genero = tk.IntVar()


lbNombre = tk.Label(ventana, text="Nombres:")
lbNombre.pack()
tbNombre = tk.Entry(ventana)
tbNombre.pack()

lbApellidos = tk.Label(ventana, text="Apellidos:")
lbApellidos.pack()
tbApellidos = tk.Entry(ventana)
tbApellidos.pack()

lbTelefono = tk.Label(ventana, text="Teléfono:")
lbTelefono.pack()
tbTelefono = tk.Entry(ventana)
tbTelefono.pack()

lbEdad = tk.Label(ventana, text="Edad:")
lbEdad.pack()
tbEdad = tk.Entry(ventana)
tbEdad.pack()

lbEstatura = tk.Label(ventana, text="Estatura:")
lbEstatura.pack()
tbEstatura = tk.Entry(ventana)
tbEstatura.pack()

lbGenero = tk.Label(ventana, text="Género")
lbGenero.pack()

rbHombre = tk.Radiobutton(ventana, text="Hombre", variable=var_genero, value=1)
rbHombre.pack()

rbMujer = tk.Radiobutton(ventana, text="Mujer", variable=var_genero, value=2)
rbMujer.pack()

rbHelicoptero_apache = tk.Radiobutton(ventana, text="Helicoptero Apache", variable=var_genero, value=3)
rbHelicoptero_apache.pack()

btnBorrar = tk.Button(ventana, text="Borrar valores", command=borrar_fun)
btnBorrar.pack()

btnGuardar = tk.Button(ventana, text="Guardar", command=guardar_valores)
btnGuardar.pack()


ventana.mainloop()