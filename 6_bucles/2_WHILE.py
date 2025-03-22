# CONDICIÓN WHILE

i = 1
while i < 10:
	print(i)
	i += 1

# ------------- #

# EJEMPLO UTIL

n = 1
par = impar = 0
while n != 0:
    n = int(input('Ingrese un número: '))
    
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1

print(f'Escribiste {par} pares y {impar} impares')
