for i in range(1,2):
	# Lo que ocurre
    print(f'hola, iteración numero {i}')

# Bucle i en intervalo(1, 10)
	# Lo que ocurre
	
# range() # Es un intervalo que recibe hasta 3 argumentos:

# ARGUMENTOS -> range(start, stop, step)
					# (inicio, fin, paso)
# inicio -> por defecto es 0, opcional.
# fin -> obligatorio. Necesita posición para parar.
# paso -> por defecto es 1, opcional.

# range(10) -> Arranca en 0, termina en 10
# range(1, 10) -> Arranca en 1, termina en 10
# range(0,10,2) -> Arranca en 0 hasta 10 con paso 2
# range(6, 0, -1) -> Arranca en 6, hasta 0 con paso -1

inicio = int(input('Ingrese un numero de inicio: '))
fin = int(input('Ingrese un numero de fin: '))
paso = int(input('Ingrese un numero de paso: '))

for c in range(inicio, fin+1, paso):
    print(c)
print('FIM')