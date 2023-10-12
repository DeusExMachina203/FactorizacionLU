import random
from math import isclose
from copy import deepcopy


def generarMatriz(n):
    matriz = []
    for i in range(0, n):
        row = []
        for x in range(0, n):
            if x >= i:
                elemento = random.randint(0, 100)
                row.append(elemento)
            else:
                row.append(0)
        matriz.append(row)
    for i in range(1, n):
        for j in range(0, i):
            matriz[i][j] = matriz[j][i]
    print("Matriz Generada")
    for row in matriz:  # Imprimiar matriz generada
        print(row)
    return matriz


def factorizarLU(matriz, columns, rows):
    matrizU = deepcopy(matriz)  # Copia de la matriz original
    matrizL = []
    valoresParaL = []

    # generar matriz de identidad primero para la matriz L
    for i in range(columns):
        vector = []
        for j in range(rows):
            vector.append(0)
        matrizL.append(vector)

    for i in range(columns):
        matrizL[i][i] = 1

    # calculamos la matriz U
    for j in range(columns):
        for i in range(j + 1, rows):
            if matrizU[j][j] == 0:  # evitar dividir columnas entre 0
                return None
            factor = matrizU[i][j] / matrizU[j][j]
            for x in range(j, columns):
                matrizU[i][x] -= factor * (matrizU[j][x])
                if isclose(matrizU[i][x], 0, abs_tol=1e-011):  # si el valor es aprox 0 registrarlo como 0
                    valorParaL = {
                        "factor": factor,
                        "posFila": i,
                        "posColumna": j
                    }
                    if not valorParaL in valoresParaL:
                        valoresParaL.append(valorParaL)

    # ahora insertamos en la matriz L
    for i in valoresParaL:
        columna = i['posColumna']
        fila = i['posFila']
        matrizL[fila][columna] = i['factor']

    print("Matriz L")
    for row in matrizL:  # Imprimiar matriz generada
        print(row)
    print("Matriz U")
    for row in matrizU:  # Imprimiar matriz generada
        print(row)
    return matrizL, matrizU


def factorizarP(matriz, filas):  # Sacar P*A (1.-Hallar P / 2.- Multiplicar matrices)
    matrizU = deepcopy(matriz)  # copia de la matriz original
    matrizCopy = deepcopy(matriz)  # auxiliar para sacar filas
    matrizP = [[0] * filas for _ in range(filas)]  # valores para P
    matrizPT = [[0] * filas for _ in range(filas)]  # valores para P^T
    matrizI = [[0] * filas for _ in range(filas)]
    for i in range(filas):
        matrizP[i][i] = 1  # declarar como matriz identidad
        matrizI[i][i] = 1

    for i in range(filas):
        if matrizCopy[i][i] == 0:
            # Verificar si la fila empieza con 0
            for j in range(i + 1, filas):
                if matrizCopy[j][i] != 0:
                    matrizCopy[i], matrizCopy[j] = matrizCopy[j], matrizCopy[
                        i]  # cambiar filas de la matriz permutación
                    matrizP[i], matrizP[j] = matrizP[j], matrizP[i]  # cambiar filas de la matriz permutación
                    break
                else:
                    # Si no hay filas inadecuadas
                    return None
    MultiplicacionPA = [[0 for _ in range(filas)] for _ in range(filas)]

    # Realizar la multiplicación de matrices
    for i in range(filas):
        for j in range(filas):
            for k in range(filas):
                MultiplicacionPA[i][j] += matrizP[i][k] * matrizU[k][j]


    if (matrizP == matrizI):  # Si no hubo permutaciones
        return False, MultiplicacionPA, matrizPT
    else:  # Si hubo permutaciones
        print("Se detecto Factorización PA=LU")
        print("\nMatriz P")
        for row in matrizP:  # Imprimiar matriz generada
            print(row)
        for i in range(filas):
            for j in range(filas):
                matrizPT[j][i] = matrizP[i][j]
        print("\nMatriz P^T")
        for row in matrizPT:  # Imprimiar matriz generada
            print(row)
        return True, MultiplicacionPA, matrizPT
