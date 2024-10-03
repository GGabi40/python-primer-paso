# DESAFÍOS BREAK
# --------------- #

# EJERCICIO 1

# Escribir un programa que lea varios 
# numeros enteros por teclado. El programa solo 
# va a parar cuando el ususario ingrese 999, que 
# es la condición de parada (bandera). Al final,
# mostrará cuántos numeros fueron ingresados y 
# cuál fue la suma entre ellas.
# Desconsiderar el valor de la bandera (999)

# SOLUCIÓN

suma = cont = 0
print('Ingrese 999 para salir.')
while True:
    num = int(input('Ingrese un numero: '))
    if num == 999:
        print('\nSaliendo del bucle...')
        break
    else:
        cont += 1
        suma += num

print(f'Se ingresó: {cont} numeros.')
print(f'La suma de todos los valores: {suma}')


# EJERCICIO 2

# Hacer un programa que muestre la
# tabla de multiplicar de varios numeros, 
# uno por vez para cada valor ingresado 
# por el usuario. El programa será 
# interrumpido cuándo el numero solicitado 
# sea negativo.

# SOLUCIÓN

print('')

while True:
    num = int(input('Ingrese el valor para la tabla: '))
    if num < 0:
        print('\nSaliendo del bucle...')
        break
    else:
        print('='*20)
        for i in range(11):
            print(f'{num} x {i} = {num*i}')
        print('='*20)
        print('Ingrese un numero negativo para salir.')


# EJERCICIO 3

# Hacer un programa que juegue par o impar 
# con la computadora. El juego sólo será 
# interrumpido cuándo el jugador PIERDA, 
# mostrando el total de victorias que conquistó 
# al final del juego.

# SOLUCIÓN

print('\033[34m~\033[m'*40)
print('\tBienvenido al \033[32mPar o Impar\033[m')
print('\033[34m~\033[m'*40)

from random import randint

victorias = 0
perdió = False

while not perdió:
    computadora = randint(0, 10)
    jugador = str(input('Su número está listo. Elija: Par o Impar: ')).lower().strip()
    print(f'\n¡Eligió \033[32m{jugador.upper()}\033[m!')
    print('\033[35m¡La computadora ya eligió un número!\033[m\n')
    
    jugadorNum = int(input('Ingrese su número: '))
    juego = computadora + jugadorNum
    
    reglas = {
        'par': juego % 2 == 0,
        'impar': juego % 2 != 0
    }
    
    print(f'\nJugó {jugadorNum} y la computadora jugó {computadora}')
    if(reglas['par'] and jugador == 'par'):
        print('\033[32m¡Ganó!\033[m\n')
        victorias += 1
    elif(reglas['impar'] and jugador == 'impar'):
        print('\033[32m¡Ganó!\033[m\n')
        victorias += 1
    else:
        perdió = True
        print('\n\033[31mPerdió\033[m :(')
        print(f'Tuviste un total de: \033[1;33m{victorias} victorias\033[m.\n')


# EJERCICIO 4

# Crear un programa que lea la edad y 
# el sexo de várias personas registradas, 
# el programa deberá preguntar si el usuario 
# quiere o no seguir. Al final, mostrar:
#   A. Cuántas personas tienen más de 18 años.
#   B. Cuántos hombres fueron registrados.
#   C. Cuántas mujeres tienen menos de 20 años.

# SOLUCIÓN



# EJERCICIO 5

# Crear un programa que lea el nombre 
# y el precio de vários productos. El 
# programa deberá preguntar si el usuario 
# va a seguir. Al final, mostrar:
#   A. Cuál es el total que se gastó en la compra.
#   B. Cuántos productos cuestan más de $1.000.
#   C. Cuál es el producto más barato.

# SOLUCIÓN



# EJERCICIO 6

# Crear un programa que simule el 
# funcionamiento de un caja electrónico. 
# En el inicio, preguntar al usuario cuál 
# será el valor que se quiere sacar (num entero) 
# y el programa va a informar cuántos billetes 
# de cada valor serán entregados.
#   PD: considerar que el caja posee billetes 
#   de $ 50; $ 20; $ 10; $ 1

# SOLUCIÓN


# EJERCICIO 7