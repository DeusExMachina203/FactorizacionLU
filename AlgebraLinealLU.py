from tkinter import *
import customtkinter
import moduloMate

n = 4
matriz = []


class OneTable(customtkinter.CTkToplevel):
    def __init__(self, root, total_rows, total_columns, matriz):
        for i in range(total_rows):
            for j in range(total_columns):
                    self.e = Entry(root, width=10, fg='blue',
                                   font=('Arial', 20, 'bold'))
                    self.e.grid(row=i, column=j)
                    self.e.insert(END, round(matriz[i][j],5))

#aumentar tamaño
class Table(customtkinter.CTkToplevel):
    def __init__(self, root, total_rows, total_columns, matriz, matrizL, matrizU,matrizP,IsPTLU):
        if IsPTLU:
            for i in range(total_rows):
                for j in range(total_columns + 1 + total_columns + 1 + total_columns+1+total_columns):
                    if i < total_rows and j < total_columns:
                        self.e = Entry(root, width=6, fg='blue',
                                       font=('Arial', 10, 'bold'))
                        self.e.grid(row=i, column=j)
                        self.e.insert(END, round(matriz[i][j],5))
                    else:
                        self.e = Entry(root, width=6, fg='blue',
                                       font=('Arial', 10, 'bold'))
                        self.e.grid(row=i, column=j)
                        if i == 2 and j == total_columns:
                            self.e.insert(END, '=')
                        elif j > total_columns and j < total_columns * 2 + 1:
                            self.e.insert(END, round(matrizP[i][j-total_columns - 1],4))
                        elif i == 2 and j == total_columns * 2 + 1:
                            self.e.insert(END, '*')
                        elif j > total_columns * 2 + 1 and j < total_columns * 3 + 2:
                            self.e.insert(END, round(matrizL[i][j - total_columns * 2 - 2],4))

                        elif i == 2 and j == total_columns * 3 + 2:
                            self.e.insert(END, '*')
                        elif j > total_columns * 3 + 2 and j < total_columns * 4 + 3:
                            self.e.insert(END, round(matrizU[i][j - total_columns * 3 - 3],4))
                        else:
                            self.e.insert(END, ' ')
        else:
        # code for creating table
            for i in range(total_rows):
                for j in range(total_columns + 1 + total_columns + 1 + total_columns):
                    if i < total_rows and j < total_columns:
                        self.e = Entry(root, width=6, fg='blue',
                                       font=('Arial', 10, 'bold'))
                        self.e.grid(row=i, column=j)
                        self.e.insert(END, round(matriz[i][j],4))
                    else:
                        self.e = Entry(root, width=6, fg='blue',
                                       font=('Arial', 10, 'bold'))
                        self.e.grid(row=i, column=j)
                        if i == 2 and j == total_columns:
                            self.e.insert(END, '=')
                        elif j > total_columns and j < total_columns * 2 + 1:
                            self.e.insert(END, round(matrizL[i][j-total_columns - 1],4))
                        elif i == 2 and j == total_columns * 2 + 1:
                            self.e.insert(END, '*')
                        elif j > total_columns * 2 + 1 and j < total_columns * 3 + 2:
                            self.e.insert(END, round(matrizU[i][j - total_columns * 2 - 2],4))
                        else:
                            self.e.insert(END, ' ')





def OpenM(matriz):

    raizM = customtkinter.CTk()
    raizM.geometry("1260x720")
    #3 frames iniciales

    VistaTab=customtkinter.CTkTabview(raizM,height=(1))
    VistaTab.add("Matriz (A)")
    VistaTab.set("Matriz (A)")
    
    #Parte 3 matrices
    frameAll = customtkinter.CTkFrame(raizM)


      #Parte 3 matriz Permutacióin
    if (IsPTLU):
        raizM.title("Matriz generada (  A  = P^T * L * U  )")

        VistaTab.add("Matriz (P)")
        VistaTab.add("Matriz (L)")
        VistaTab.add("Matriz (U)")

        tituloFactorizacion = customtkinter.CTkLabel(raizM, text="Factorización PA=LU ( A = P^T * L * U)", font=("Cascadia Code SemiBold", 18))
        # PACK
        tituloFactorizacion.pack(pady=20)
        frameAll.pack(pady=20)
        VistaTab.pack(pady=10)

        # Matriz
        tM = Table(frameAll, n, n, matriz, matrizL, matrizU,matrizP,IsPTLU)
        tO = OneTable(VistaTab.tab("Matriz (A)"), n, n, matriz)
        tP=  OneTable(VistaTab.tab("Matriz (P)"), n, n, matrizP)
        tL = OneTable(VistaTab.tab("Matriz (L)"), n, n, matrizL)
        tU = OneTable(VistaTab.tab("Matriz (U)"), n, n, matrizU)
    else:
        raizM.title("Matriz generada (  A  = L * U  )")
        tituloFactorizacion = customtkinter.CTkLabel(raizM, text="Factorización LU ( A = L * U)", font=("Cascadia Code SemiBold", 18))
        
        VistaTab.add("Matriz (L)")
        VistaTab.add("Matriz (U)")
        
        # PACK
        tituloFactorizacion.pack(pady=20)
        frameAll.pack(pady=20)
        VistaTab.pack(pady=10)

        # Matriz
        tM = Table(frameAll, n, n, matriz, matrizL, matrizU,matrizP,IsPTLU)
        tO = OneTable(VistaTab.tab("Matriz (A)"), n, n, matriz)
        tL = OneTable(VistaTab.tab("Matriz (L)"), n, n, matrizL)
        tU = OneTable(VistaTab.tab("Matriz (U)"), n, n, matrizU)





    # Mianloop
    raizM.mainloop()



# ABRIR PANEL DE FACTORIZACIÓN LU
def OpenE():
    values = {'n': 4}
    global n
    # CREAR VIÑETA
    raizE = customtkinter.CTk()
    raizE.title("Factorización LU")
    raizE.geometry("530x350")

    # COMBO BOX
    def combobox_callback(choice):
        global n
        n = int(choice)

    combobox = customtkinter.CTkComboBox(master=raizE, values=["4", "5", "6", "7", "8", "9", "10"],
                                         command=combobox_callback)
    combobox.set("Ingrese n - [4-10]")  # Valor inicial

    # TITULO
    tituloE = customtkinter.CTkLabel(raizE, text="Generar matriz aleatoria", font=("Cascadia Code SemiBold", 25))

    # BOTON
    def button_callback():
        matriz_ejemploPALU = [ #Matriz para verificar PA=LU
            [0, 0, 0,-4],
            [5, 1, 1,-1],
            [3, 1, -1,-2],
            [-3,4,6,2]
        ]
        global n
        global matriz
        global matrizL
        global matrizU
        global matrizP
        global IsPTLU
        matriz = moduloMate.generarMatriz(n) #generar matriz


        try: #EMPEZAR REALIZANDO FACTORIZACION LU
            (matrizL, matrizU) = moduloMate.factorizarLU(matriz, n, n)
            
            #declarar matriz P como default
            matrizP = [[0] * n for _ in range(n)]
            for i in range(n):
                matrizP[i][i] = 1  # declarar como matriz identidad
            IsPTLU=False;


        except: #SI NO ES POSIBLE REALIZARSE(By Division by zero) RECURRIR A LA FACTORIZACIÓN PA=LU
            print("NO ES POSIBLE REALIZAR FACTORIZACIÓN LU, PROCEDIENDO A CAMBIAR FILAS")
            m, matrizP = moduloMate.factorizarP(matriz,n)
            (matrizL, matrizU) = moduloMate.factorizarLU(m, n, n)
            IsPTLU=True;

        OpenM(matriz)

    b = Button(raizE, text='Iniciar', command=lambda: button_callback())

    # PACK
    tituloE.pack()
    combobox.pack(pady=45)
    b.pack()

    # Mianloop
    raizE.mainloop()


# ABRIR PANEL DE INSTRUCCIONES DEL PROGRAMA
def OpenI():
    raizE = customtkinter.CTk()
    raizE.title("Instrucciones")
    raizE.geometry("500x500")

    # TITULO
    tituloE = customtkinter.CTkLabel(raizE, text="Instrucciones del programa", font=("Cascadia Code SemiBold", 18))
    # FRAME
    frame = customtkinter.CTkFrame(raizE)
    texto = """
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

    label = customtkinter.CTkLabel(frame, text=texto, font=("Cascadia Code SemiBold", 12))
    # PACK
    tituloE.pack(pady=20)
    label.pack()
    frame.pack()
    # Mainloop
    raizE.mainloop()


# MAIN
raiz = customtkinter.CTk()
raiz.title("PROGRAMA TA1")
raiz.geometry("500x500")

titulo = customtkinter.CTkLabel(master=raiz, text="Factorización LU", font=("Cascadia Code SemiBold", 25), pady=50)

# botones
Encriptar = customtkinter.CTkButton(raiz, text="Generar Matriz", command=OpenE, width=120, height=50)
Informacion = customtkinter.CTkButton(raiz, text="Informacion del programa", command=OpenI, width=190, height=50)

# PACK
titulo.pack()
Encriptar.pack(pady=50)
Informacion.pack(pady=50)

# LOOP
raiz.mainloop()
