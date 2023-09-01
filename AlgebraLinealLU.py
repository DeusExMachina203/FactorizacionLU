from tkinter import*
import customtkinter
import moduloMate

n = 4
matriz = []

class Table(customtkinter.CTkToplevel):
    
    def __init__(self,root, total_rows, total_columns, matriz):
 
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
 
                self.e = Entry(root, width=16, fg='blue',
                font=('Arial',10,'bold'))
                print(i,j)
                self.e.grid(row=i, column=j)
                self.e.insert(END, matriz[i][j])

#ABRIR VENTANA CON LA MATRIZ GENERADA
def OpenM(matriz):
    raizM=customtkinter.CTk()
    raizM.title("Matriz generada")
    
    #TITULO
    tituloM =  customtkinter.CTkLabel(raizM, text = "Matriz generada", font = ("Cascadia Code SemiBold",18))
    #FRAME
    frame = customtkinter.CTkFrame(raiz)
    #Matriz
    print('nuevo')
    t = Table(raizM, n, n, matriz)
    #PACK
    #tituloM.pack(pady=20)
    frame.pack()
    #Mianloop
    raizM.mainloop()

#ABRIR PANEL DE FACTORIZACIÓN LU
def OpenE():
    values = {'n': 4}
    global n
    #CREAR VIÑETA
    raizE=customtkinter.CTk()
    raizE.title("Factorización LU")
    raizE.geometry("530x350")
    
    #COMBO BOX
    def combobox_callback(choice):
        global n
        n = int(choice)
        print(n)
        
    combobox = customtkinter.CTkComboBox(master=raizE,values=["4","5","6","7","8","9","10"],command=combobox_callback)
    combobox.set("Ingrese n - [4-10]")  # Valor inicial

    #TITULO
    tituloE = customtkinter.CTkLabel(raizE, text = "Generar matriz aleatoria", font = ("Cascadia Code SemiBold",25))

    #BOTON
    def button_callback():
        global n
        global matriz
        print(n)
        matriz = moduloMate.generarMatriz(n)
        OpenM(matriz)

    b = Button(raizE,text = 'Iniciar', command = lambda: button_callback())

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
