# coding: utf-8
import os
os.system('clear')

def nulo(m):
        if f == c != 0: 
		t = 0
		for k in m:
			for i in range(c):
				if k[i] == 0:
					t = t + 1 
		if t == f * c:
			return "La matriz es nula"
def cuadrado(m):
	if f == c != 1 and f == c != 0:
		return "Es una Matriz Cuadrada"
def identi(m):
        if f == c != 1 and f == c != 0:
		p = 0
		for i in range(len(m)):
			if m[i][i] == 1:
				p = p + 1
		if p == len(m):
			return"La matriz es identidad"
def escala(m):
        if f == c != 1 and f == c != 0:
		h = 0
		r = m[0][0]
		for j in range(len(m)):
			if m[j][j] == r:
				h = h + 1
			if h == len(m):
				return "La matriz es escalar"
def tsuperior(m):
        if f == c != 1 and f == c != 0:
		z = 1
		s = 0
		for k in range(1,len(m)):
			for l in range(0,z):
				if m[k][l] == 0:
					s = s + 1
				else:
					break		
			z = z + 1
		if s == t:
			return "Es una matriz triangular superior"
def tinferior(m):
        if f == c != 1 and f == c != 0:
		w = 0			
		for o in range(len(m)-1):
			for ll in range(c):
				if m[o][c-1-ll] == 0:
					w = w + 1
				else:
					break	
		if w == t:
			return "Es una matriz triangular inferior"
def diagonal(m):
        if f == c != 1 and f == c != 0:
		if tsuperior(m) and tinferior(m) and not escala(m) and not identi(m):
			return "Es una matriz diagonal"
def escalonada(m):
        if f == c != 1 and f == c != 0:
		cont1 = 0
		are = []
		for pe in range(c):
			for ky in m:
				if ky[pe] == 0:
					cont1 = cont1 + 1 
			are.append(cont1)
			cont1 = 0 
		for ok in range(len(are)-1):
			if are[ok] < are[ok+1] and are[ok] != 0:
				#print "La cantidad de ceros encontradas en cada columna es: %s" % are
				print "La matriz es escalonada por columnas"
				break
def fescalo(m):
        if f == c != 1 and f == c != 0:
		cont = 0
		ar = []
		for k in m:
			for i in range(c):
				if k[i] == 0:
					cont = cont + 1 
			ar.append(cont)
			cont = 0
		for lk in range(c-1):
			if ar[lk] < ar[lk+1] and ar[lk] != 0:
				#print "La cantidad de ceros encontradas en cada fila es: %s" % ar
				print "La matriz es escalonada por filas"
				break
def principales(a,b):
	if a != b:
		print"Es una Matriz Rectangular"
	
	if a == 1:
		print"Es una matriz fila"
	if b == 1:
		print"Es una matriz columna"
matriz = []
f = input("Ingrese el numero de filas: ")
c = input("Ingrese el numero de columnas: ")
for i in range(f):
	tmp = []
	for j in range(c):
		elemento = input("Elemento %s,%s: " % (i,j))
		tmp.append(elemento)
	matriz.append(tmp)
for k in matriz:
	print k
print"==========================="
if f == c != 1 and f == c != 0:
   if f == 2:
      t = 1
   else:
      t = 3*(f-2)
   print"Cantidad de ceros para matriz Triangular Superior o Inferior"
   print"======================"
   print "La cantidad es: %s" % t
      
"""if f == c:
	matrix = []
	for tsi in range(f):
		tmp = []
		for j in range(c):
			elemento = input("Elemento %s,%s: " % (tsi,j))
			tmp.append(elemento)
		matrix.append(tmp)
	ct = 0
	for k in matrix:
		for i in range(c):
			if k[i] == 0:
				ct = ct + 1
	print"Cantidad de ceros para matriz Triangular Superior o Inferior"
	print"======================"
	print "La cantidad es: %s" % ct"""
while True:
	print"""
	MENU DE OPCIONES
	================
	¿Qué desea hacer?
	1: Matriz nulo
	2: Matrices: Rectangular, Fila y Columna
	3: Matriz Cuadrada
	4: Matriz Identidad
	5: Matriz Escalar
	6: Matriz Triangular Superior
	7: Matriz Triangular Inferior
	8: Matriz Diagonal
	9: Matriz Escalonada por Columnas
	10: Matriz Escalonada por Filas
	11: Salir
	"""
	op = input("Ingrese la opción: ")
	if op == 11:
		break
	if op == 1:
		print nulo(matriz)
	elif op == 2:
		print principales(f,c)
	elif op == 3:
		print cuadrado(matriz)
	elif op == 4:
		print identi(matriz)
	elif op == 5:
		print escala(matriz)
	elif op == 6:
		print tsuperior(matriz)
	elif op == 7:
		print tinferior(matriz)
	elif op == 8:
		print diagonal(matriz)
	elif op == 9:
		print escalonada(matriz)
	elif op == 10:
		print fescalo(matriz)
