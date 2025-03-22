# DESAFÍOS BUCLE WHILE
# ------------------ #

# EJERCICIO 1

# Crea un programa que lea el sexo 
# de una persona pero solo acepte 
# respuestas 'M' o 'F'. Si escribe mal, 
# pedile que escriba nuevamente el 
# valor correcto.

# SOLUCIÓN

respuesta = input('Ingrese M o F: ').strip().upper()[0]

while respuesta not in 'MmFf':
    respuesta = input('Invalido. Por favor ingrese M o F: ').strip().upper()[0]

print('Válido!')



# EJERCICIO 2

# Mejore el juego en el
# cuál la computadora "piensa" en 
# un número entre 0 a 10. Sólo que 
# ahora el jugador va a intentar 
# adivinar hasta lograrlo, mostrando al 
# final cuántas veces intentó vencer.

# SOLUCIÓN

from random import randrange;
from time import sleep;

numeroAleatorio = randrange(0, 10)
contador = 0

print('=-' * 20)
print('Tu número está listo. Intente adivinar...')
print('=-' * 20)

respuestaCorrecta = False
while not respuestaCorrecta:
    respuesta = int(input('Es un numero de 0 a 10. ¿Cuál pensás que es? '))
    contador += 1

    print('PROCESANDO...\n')
    sleep(0.5)

    if(respuesta == numeroAleatorio):
        print(f'¡Ganaste! Lo hiciste en \033[33m{contador} intentos\033[m.')
        respuestaCorrecta = True
    else:
        print(f'Perdiste, intente nuevamente...')
        if(respuesta < numeroAleatorio):
            print(f'Probá con un numero \033[34mmás grande\033[m.\n')
        else:
            print(f'Probá con un numero \033[34mmás chico\033[m.\n')



# EJERCICIO 3

# Crear un programa que lea dos valores y
# muestre un menú en pantalla:
# [1] Sumar
# [2] Multiplicar
# [3] Mayor
# [4] Nuevos números
# [5] Salir del programa
# El programa debe realizar la 
# operación solicitada en cada caso

# SOLUCIÓN

num1 = int(input('Ingrese un numero: '))
num2 = int(input('Ingrese otro numero: '))

opciones = 0
while(opciones != 5):
    print('\nSeleccione una opción:')
    opciones = int(input('\033[34m[1] Sumar\n[2] Multiplicar\n[3] Mayor\n[4] Nuevos Números\n[5] Salir del programa\033[m\n'))
    
    if(opciones == 1):
        print(f'Elegiste \033[33mSUMA\033[m.\n\tEl resultado de la suma {num1} + {num2} = {num1+num2}.\n')
    elif(opciones == 2):
        print(f'Elegiste \033[33mMULTIPLICAR\033[m.\n\tEl resultado de la multiplicación {num1} * {num2} = {num1*num2}.\n')
    elif(opciones == 3):
        if(num1>num2):
            mayor = num1
        else:
            mayor = num2
        print(f'Elegiste \033[33mQUIEN ES MAYOR\033[m.\n\tEntre los numeros {num1} y {num2}, el mayor es {mayor}.\n')
    elif(opciones == 4):
        print('Elegiste ingresar \033[33mnuevos números\033[m.')
        num1 = int(input('Ingrese un numero: '))
        num2 = int(input('Ingrese otro numero: '))
    elif(opciones == 5):
        print('\033[36m¡Gracias por utilizar el programa!\033[m')
    else:
        print('\033[41mOpción inválida.\033[m\n')


# EJERCICIO 4

# Crear un programa que lea un numero
# y haga su factorial.
# Ejemplo: 5! = 5x4x3x2x1 = 120

# SOLUCIÓN

num = int(input('Ingrese un numero: '))
resultado = 1
i = num

print(f'{num}! = ', end='')
while i > 0:
    resultado *= i
    print(f'{i}', end='')
    
    print(f' x ' if i > 1 else ' = ', end='')
        
    i = i - 1

print(f'{resultado}')


# EJERCICIO 5

# Rehacer el ejercicio de la Progresión Aritmético
# leyendo el término y la razón de una PA, 
# mostrando los 10 primeros términos de la 
# progresión utilizando la estructura WHILE

# SOLUCIÓN

print('Generador de PA')
print('-=' *20)

primer = int(input('Primer término: '))
razon = int(input('Razón de la PA: '))
termino = primer
contador = 1

while contador <= 10:
    print(f'{termino} -> ', end='')
    termino += razon
    contador += 1



# EJERCICIO 6

# Mejorar el desafío anterior, preguntandole 
# al usuario si quiere mostrar más términos.
# El programa encierra cuando él diga que 
# quiere mostrar Los términos.

# SOLUCIÓN


print('Generador de PA')
print('-=' *20)

primer = int(input('Primer término: '))
razon = int(input('Razón de la PA: '))
termino = primer
contador = 1
fin = 10

while contador <= fin:
    print(f'{termino} -> ', end='')
    if contador > fin-1:
        print(f'PAUSA')
        demas = int(input(f'Cuántos términos más deseas mostrar? '))
        
        if(demas > 0):
            contador = 1
            fin = demas+1
    else:
        print('', end='')
    termino += razon
    contador += 1


# EJERCICIO 7

# Escribir un programa que lea un número 
# n entero y muestre en pantalla los 
# n primeros elementos de una 
# Secuencia de Fibonacci.
# Ejemplo: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
    #    siempre arranca 0 y 1, luego el proximo es la suma del primero y el segundo
# SOLUCIÓN

numTerminos = int(input('Ingrese cuántos términos querés ver: '))
t1 = 0
t2 = 1
contador = 3

print(f'{t1} -> {t2}', end='')

while contador <= numTerminos:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    contador += 1

print(f' -> FIN.')

# EJERCICIO 8

# Escribir un programa que lea vários números 
# enteros por teclado. El programa solo 
# dejará cuándo el usuario escriba el valor 999, 
# que es la condición de parada. Al final, 
# muestre cuántos números fueron ingresados 
# y cuál fue la suma entre ellas 
# (desconsiderar el 999)

# SOLUCIÓN

num = int(input('Ingrese un número: \nPara salir, ingrese 999\n'))
contador = suma = 0

while num != 999:
    contador += 1
    suma += num
    num = int(input('\nIngrese otro número: \nPara salir, ingrese 999\n'))
    
print(f'Se ingresaron {contador} números.')
print(f'La suma de todos los números es de: {suma}.')


# EJERCICIO 9

# Escribir un programa que lea vários números 
# enteros por teclado. Al final de su ejecución, 
# mostrar la media entre todos los valores 
# y cuál fue el mayor y el menor valores leídos.
# El programa debe preguntar al usuario 
# si quiere o no seguir escribiendo numeros.
# (desconsiderar el 999)

# SOLUCIÓN

respuesta = 'S'
contador = suma = 0

while respuesta == 'S':
    num = int(input('\nIngrese un número: '))
    contador += 1
    suma += num
    
    if contador == 1:
        mayor = num
        menor = num
    else:
        if(num > mayor):
            mayor = num
        if(menor > num):
            menor = num
    
    respuesta = input('Querés seguir ingresando números? [S/N]\n').upper().strip()[0]
    

media = suma / contador
print(f'Se ingresaron {contador} números.')
print(f'El mayor número fue: {mayor}.')
print(f'El menor número fue: {menor}.')
print(f'La suma de todos los números es de: {suma}.')
print(f'La media de todos estos números es de: {media:.2f}.')

