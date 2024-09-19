# DESAFIO 1

# Crie un Script python que lea un 
# numero real cualquiera y muestre 
# en pantalla su porción entera.
# Ejemplo: escriba un numero: 6.127
# el numero tiene como parte entera el 6

# -- SOLUCIÓN --

from math import floor;

num = float(input('Ingrese un numero flotante: '));
print(f'El numero {num}, tiene como parte entera el {floor(num)}');


# DESAFIO 2

# Crie un Script python que lea la
# medida del cateto opuesto y del 
# cateto adyacente de un triángulo 
# rectángulo, calcule y muestre la 
# hipotenusa.

# -- SOLUCIÓN --
print('\n');
from math import sqrt;

cateto1 = float(input('Ingrese el primer cateto: '));
cateto2 = float(input('Ingrese el segundo cateto: '));
hipotenusa = sqrt(pow(cateto1, 2) + pow(cateto2, 2));

print(f'La hipotenusa es {hipotenusa:.2f}');


# DESAFIO 3

# Crie un Script python que lea un 
# ángulo cualquiera y muestre en 
# pantalla el valor del seno, coseno 
# y tangente de este ángulo.

# -- SOLUCIÓN --
print('\n');
from math import sin, cos, tan, radians;

angulo = float(input('Ingrese un ángulo: '));
seno = sin(radians(angulo));
coseno = cos(radians(angulo));
tangente = tan(radians(angulo));

print(f'El ángulo {angulo} tiene el seno de {seno:.2f}°, el coseno {coseno:.2f}° y la tangente {tangente:.2f}°');

# DESAFIO 4

# Un profesor quiere sortear uno de sus 
# cuatro alumnos para borrar la pizarra. 
# Hace un programa que lo ayude, leyendo 
# sus nombres y escribiendo el elegido.

# -- SOLUCIÓN --

import random;

print('\n');
alumno1 = input('Primer alumno: ');
alumno2 = input('Segundo alumno: ');
alumno3 = input('Tercer alumno: ');
alumno4 = input('Cuarto alumno: ');

alumnos = [alumno1, alumno2, alumno3, alumno4];

elegido = random.choice(alumnos); # Retorna un elemento aleatorio de una secuencia no vacía

print(f'El elegido para borrar la pizarra fue: {elegido}');


# DESAFIO 5

# El mismo profesor del desafío anterior 
# quiere sortear la orden de presentación 
# de trabajo de los alumnos. Hace un 
# programa que lea el nombre de los cuatro 
# alumnos y muestre el orden sorteado.

# -- SOLUCIÓN --

random.shuffle(alumnos); # mezcla mi lista
print(f'El orden de presentación es: {alumnos}');

# DESAFIO 6

# Crie un Script python que abre y reproduce
# un archivo MP3

# ***** VER COMO ES ACTUALIZADO

""" import pygame;
pygame.init();
pygame.mixer.music.load('coffee-completed.mp3');
pygame.mixer.music.play();
#input();
pygame.event.wait(); """