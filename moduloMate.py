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

	for i in range(0, n):
		print(matriz[i])

	return matriz;