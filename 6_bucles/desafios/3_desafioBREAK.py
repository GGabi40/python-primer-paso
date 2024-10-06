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
    
    while jugador not in 'parimpar':
        print('Elija una opcion valida.')
        jugador = str(input('Par o Impar: ')).lower().strip()
        
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

contador18 = contHombres = contMujeres = 0

while True:
    sexo = input('Ingrese el sexo: [M/F]\n').upper().strip()[0]
    
    while sexo not in 'MF':
        print('Ingrese un valor valido: ')
        sexo = input('[M / F]\n').upper().strip()[0]
        
    edad = int(input('Ingrese la edad: '))
    while edad < 0:
        print('Ingrese un valor valido: ')
        edad = int(input('Ingrese la edad: '))
        
    if(sexo == 'M'):
        contHombres += 1
    if(edad >= 18):
        contador18 += 1
    if(sexo == 'F' and edad < 20):
            contMujeres += 1
    
    salir = int(input('Presione 0 para salir o 1 para continuar.\n'))
    if(salir == 0):
        break

print(f'Hay {contHombres} hombres.')
print(f'Hay {contMujeres} mujeres menores de 20 años.')
print(f'Hay {contador18} personas mayores a 18 años.')


# EJERCICIO 5

# Crear un programa que lea el nombre 
# y el precio de vários productos. El 
# programa deberá preguntar si el usuario 
# va a seguir. Al final, mostrar:
#   A. Cuál es el total que se gastó en la compra.
#   B. Cuántos productos cuestan más de $1.000.
#   C. Cuál es el producto más barato.

# SOLUCIÓN

print('=' *20)
print('Tienda kiosquino')
print('=' *20)

total = totalCaro = 0

while True:
    nombre = input('Ingrese el nombre del producto: ').capitalize().strip()
    precio = float(input('Ingrese el precio del producto: $ '))
    
    masBaratoPrecio = precio
    masBaratoNombre = nombre
    
    total += precio
    
    if precio > 1000:
        totalCaro += 1
    if precio < masBaratoPrecio:
        masBaratoPrecio = precio
        masBaratoNombre = nombre
    
    salir = int(input('Presione 0 para salir o 1 para continuar.\n'))
    if salir == 0:
        break

print(f'-{*10}FIN-{*10}')
print(f'El total que se gastó en la compra fue de: $ {total}')
print(f'Productos que cuestan más de $1.000: {totalCaro}')
print(f'El producto más barato: {masBaratoNombre}, cuesta $ {masBaratoPrecio}')



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

print('-=' *20)
print('Cajero Automatico'.center(40))
print('-=' *20)

print('\n')

contadores = [0, 0, 0, 0]
billetes = [50, 20, 10, 1]

sacar = float(input('Cuanto desea sacar? '))
total = sacar
totalBilletes = 0

for i in range(len(billetes)):
    while total >= billetes[i]:
        total -= billetes[i]
        contadores[i] += 1

print(f'Se sacarán:')
for i in range(len(contadores)):
    if contadores[i] > 0:
        print(f'{contadores[i]} billetes de {billetes[i]}')

