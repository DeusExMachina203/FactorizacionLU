﻿from tkinter import*
import customtkinter

#ABRIR PANEL DE FACTORIZACIÓN LU
def OpenE():
    #CREAR VIÑETA
    raizE=customtkinter.CTk()
    raizE.title("Factorización LU")
    raizE.geometry("530x350")
    
    #COMBO BOX
    def combobox_callback(choice):
        print("combobox dropdown clicked:", choice)
    combobox = customtkinter.CTkComboBox(master=raizE,values=["4","5","6","7","8","9","10"],command=combobox_callback)
    combobox.set("Ingrese n - [4-10]")  # Valor inicial

    #TITULO
    tituloE = customtkinter.CTkLabel(raizE, text = "Generar matriz aleatoria", font = ("Cascadia Code SemiBold",25))

    #BOTON
    b = Button(raizE,text = 'Iniciar')

    #PACK
    tituloE.pack()
    combobox.pack(pady=45)
    b.pack()
   
    #Mianloop
    raizE.mainloop()


 #ABRIR PANEL DE INSTRUCCIONES DEL PROGRAMA
def OpenI():
    raizE=customtkinter.CTk()
    raizE.title("Instrucciones")
    raizE.geometry("500x500")
    
     #TITULO
    tituloE =  customtkinter.CTkLabel(raizE, text = "Instrucciones del programa", font = ("Cascadia Code SemiBold",18))
    #FRAME
    frame = customtkinter.CTkFrame(raizE)
    texto="""
¡Bienvenidos a la aplicación Factorización LU!
Pida el ingreso de n[4, 10] y genere aleatoriamente
los elementos de una matriz simétrica A de orden n.
El programa va mostrar una matriz triangular 
inferior L y una matriz triangular superior U 
(en caso existan); en caso contrario, se va mostrar la 
factorización P^T LU.

¿Que es Factorización LU?
También conocida como descomposición LU,es la 
factorización de cualquier matriz A como producto 
de dos matrices. Una de ellas triangular superior U
y otra como triangular inferior L invertible con 
unos en su diagonal resultando en A=LU. Además, si
A es invertible entonces la factorización
es única (Grossman & Flores, 2012).

Integrantes:
Achin Angeles, Luciano Valentino   (U202113624)
Tapia Pescoran, Andrea Katherina   (U202120058)
De Loayza Zamudio, Ernesto David   (U202121772)
Paredes Espinoza, Fernando Samuel  (U202122837)

"""

    label = customtkinter.CTkLabel(frame,text=texto,font = ("Cascadia Code SemiBold",12))
    #PACK
    tituloE.pack(pady=20)
    label.pack()
    frame.pack()
    #Mainloop
    raizE.mainloop()

# MAIN
raiz= customtkinter.CTk()
raiz.title("PROGRAMA TA1")
raiz.geometry("500x500")

titulo=customtkinter.CTkLabel(master=raiz,text="Factorización LU",font=("Cascadia Code SemiBold",25),pady=50)

#botones
Encriptar = customtkinter.CTkButton(raiz,text="Generar Matriz",command=OpenE, width = 120, height = 50)
Informacion = customtkinter.CTkButton (raiz, text = "Informacion del programa",command= OpenI, width = 190, height = 50)

#PACK 
titulo.pack()
Encriptar.pack(pady = 50)
Informacion.pack(pady = 50)

#LOOP 
raiz.mainloop()
