import random

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

	return matriz;

def factorizarLU(matriz, columns, rows):
	matrizU = []
	#matrizU = matriz
	for i in range(rows):
		vector = []
		for j in range(columns):
			vector.append(matriz[i][j])
		matrizU.append(vector)
		
	matrizL = []
	#generar matriz de identidad primero para la matriz L
	for i in range(columns):
		vector=[]
		for j in range(rows):
			vector.append(0)
		matrizL.append(vector)

	for i in range(columns):
		matrizL[i][i] = 1

	for j in range(columns):
		divisor=matrizU[j][j]
		for i in range(j+1, rows):
			factor = matrizU[i][j] / divisor
			#print(matrizU[i][j], "/", divisor, "=", factor)
			for x in range(columns):
				print(matrizU[i][x], "-", matrizU[j][x], "*", factor)
				matrizU[i][x] = matrizU[i][x] - matrizU[j][x] * (factor)
				
	for i in range(rows):
		print(matrizU[i])

