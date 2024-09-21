# DESAFIO 1

# Crea un programa que haga la computadora
# "pensar" en un número entero entre 0 y 5 
# y pedile al usuario intente descubrir el 
# número elegido por la computadora. 
#   El programa deberá escribir en la 
# pantalla si el usuario ganó o perdió

# -- SOLUCIÓN --

import random;

numeroAleatorio = random.randrange(0, 6);

respuesta = int(input('El número está listo. Cuál pensas que es? '));

print('¡Ganaste!' if respuesta == numeroAleatorio else f'Perdiste, el numero era: {numeroAleatorio}');


# DESAFIO 2

# Crea un programa que lea la velocidad
# de un auto.
# Si sobrepasa los 80 km/h, mostra un
# mensaje diciendo que fue multado.
# La multa costará $ 7.00 por cada Km
# por encima del límite.

# -- SOLUCIÓN --

print('\n');

velocidad = random.randrange(30, 140);
limite = 80
multa = 7.00;

print('¡ALTO! Control policial.');

if (velocidad >= limite):
    print(f'Ibas a {velocidad} km/h. Tenés una multa por exceso de velocidad su costo será de $ {(velocidad - limite) * multa:.2f}');
    print('ATRAPADO.');
else:
    print(f'Ibas a {velocidad} km/h. Tu velocidad está bien, siga camino.');


# DESAFIO 3

# Crea un programa que lea un numero
# entero y muestre por pantalla si
# es par o impar

# -- SOLUCIÓN --

print('\n');

num = int(input('Ingrese un numero: '));

print(f'{num} es un numero par.' if num % 2 == 0 else f'{num} es impar.');


# DESAFIO 4

# Crea un programa que pregunte la distancia
# de un viaje en Km.
# Calcule el precio del pasaje, cobrando
# $ 0.50 por Km para viajes de hasta 200 Km. 
# Y $ 0.45 para viajes más largos.

# -- SOLUCIÓN --

print('\n');

distancia = float(input('Ingrese la distancia de tu viaje: '));
precio = 0.50;

if(distancia <= 200):
    print(f'El costo es de {precio} por Km. Un total de {precio * distancia}');
else:
    precio = 0.45;
    print(f'El precio del pasaje es de {precio} por Km. Un total de {precio * (distancia - 200)}')


# DESAFIO 6

# Crea un programa que lea un año cualquiera
# y muestre si es bisiesto

# -- SOLUCIÓN --

print('\n');

año = int(input('Ingrese un año: '));

print('Año bisiesto.' if año % 4 == 0 else 'No es bisiesto.');


# DESAFIO 7

# Crea un programa que lea 3 numeros
# y muestre cual es el mayor y cuál 
# es el menor

# -- SOLUCIÓN --

print('\n');

nro1 = int(input('Ingrese un numero entero: '));
nro2 = int(input('Ingrese otro numero entero: '));
nro3 = int(input('Ingrese el tercer numero entero: '));

# -- mayor
if (nro1 > nro2 and nro1 > nro3):
    print(f'{nro1} es el mayor');
elif (nro2 > nro1 and nro2 > nro3):
    print(f'{nro2} es el mayor');
elif (nro3 > nro2 and nro3 > nro1):
    print(f'{nro3} es el mayor');
else:
    print('Hay un igual.')

# -- menor
if(nro1 < nro2 and nro1 < nro3):
    print(f'{nro1} es el menor');
elif (nro2 < nro1 and nro2 < nro3):
    print(f'{nro2} es el menor');
elif (nro3 < nro2 and nro3 < nro1):
    print(f'{nro3} es el menor');



# DESAFIO 8

# Crea un programa que pregunte el sueldo
# de un empleado y calcule el valor de su
# aumento.
#   Para sueldos superiores a $ 1.250,00 calcule 
#   un aumento de 10%.
#   Para sueldos inferiores o iguales, el 
#   aumento será de 15%

# -- SOLUCIÓN --

print('\n');

sueldo = float(input('Ingrese sueldo del empleado: '));

if(sueldo > 1250):
    aumento = 0.10;
else:
    aumento = 0.15;

print(f'El aumento será de {aumento*100}%, por ello, el nuevo sueldo será de: {sueldo + (sueldo * aumento):.2f}');


# DESAFIO 9

# Crea un programa que lea la longitud de
# 3 rectas y diga al usuario si ellas
# pueden o no formar un triángulo.

# -- SOLUCIÓN --

print('\n');

r1 = float(input('Ingrese la primera longitud: '));
r2 = float(input('Ingrese la segunda longitud: '));
r3 = float(input('Ingrese la tercera longitud: '));

""" PRINCIPIO MATEMÁTICO:
la suma de dos de sus lados debe ser 
mayor a la longitud del tercer lado. 
"""

if (r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2):
    print('Se puede formar un triángulo.');
else:
    print('No se puede formar un triángulo.');
