import random
from math import isclose
from icecream import ic

def generarMatriz(n):
	matriz = []

	for i in range(0, n):
		row = []
		for x in range(0, n):
			if x >= i:
				elemento= random.randint(0, 100)
				row.append(elemento)
			else:
				row.append(0)
		matriz.append(row)
	

	for i in range(1, n):
		for j in range(0, i):
			matriz[i][j] = matriz[j][i]

	return matriz

def factorizarLU(matriz, columns, rows):
	matrizU = []
	matrizL = []
	valoresParaL = []
	#matrizU = matriz
	for i in range(rows):
		vector = []
		for j in range(columns):
			vector.append(matriz[i][j])
		matrizU.append(vector)
	
	#generar matriz de identidad primero para la matriz L
	for i in range(columns):
		vector=[]
		for j in range(rows):
			vector.append(0)
		matrizL.append(vector)

	for i in range(columns):
		matrizL[i][i] = 1

	#calculamos la matriz U
	for j in range(columns):
		divisor=matrizU[j][j]
		for i in range(j+1, rows):
			factor = matrizU[j][i] / divisor
			for x in range(columns):
				matrizU[i][x] = matrizU[i][x] - matrizU[j][x] * (matrizU[j][i])/divisor
				if isclose(matrizU[i][x], 0, abs_tol = 1e-011):
					matrizU[i][x] = 0 
					valorParaL = {
						"factor" : factor,
						"posFila": i,
						"posColumna": j
					}
					if not valorParaL in valoresParaL:
						valoresParaL.append(valorParaL)


	#ahora insertamos en la matriz L
	for i in valoresParaL:
		columna = i['posColumna']
		fila = i['posFila']
		matrizL[fila][columna] = i['factor']

	# ic(valoresParaL)
	# ic(matrizL)
	# ic(matrizU)

	return matrizL, matrizU

