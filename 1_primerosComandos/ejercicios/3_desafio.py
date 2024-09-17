# DESAFÍO 1

# Programa que lea un numero entero
# y muestre su numero
# sucesor y antecesor.

# RESOLUCIÓN

nro = int(input('Ingrese un numero: '));
print(f'El sucesor de este numero es {nro+1}');
print(f'El antecesor de este numero es {nro-1}');

# ---------
# DESAFÍO 2

# Crear un algoritmo que lea un numero 
# y muestre su doble, triple y raiz cuadrada

# RESOLUCIÓN

print('\n');
print(f'Su doble es {nro*2}');
print(f'Su tiple es {nro*3}');
print(f'Su raiz cuadrada es {nro**1/2}');
print(f'OTRA MANERA: Su raiz cuadrada es {(pow(nro, 1/2)):.2f}');


# ---------
# DESAFÍO 3

# Desarrollar un programa que lea 
# las dos notas de un alumno y calcule 
# y muestre su promedio

# RESOLUCIÓN (agregué más de lo que pedía)

print('\n');
nota = 0;
acumulador = 0;
contador = 0;

while(nota != -1) :
    nota = float(input('Ingrese la nota del alumno: '));
    print('Para salir, ingrese -1');
    if (nota == -1) :
        break;
    else: 
        acumulador = acumulador + nota;
        contador = contador + 1;

if (contador > 0) :
    promedio = acumulador / contador;
    print(f'El promedio del alumno fue de: {promedio}');
else :
    print('No ingresaste ninguna nota. Finalizando programa');

# ---------
# DESAFÍO 4

# Desarrollar un programa que lea 
# un valor en metros y lo exhiba 
# convertido en centimetros y milimetros

# RESOLUCIÓN

print('\n');
metros = float(input('Ingrese el valor en metros: '));
print(f'Valor en centimetros: {metros*100} cm');
print(f'Valor en milimetros: {metros*1000} mm');

# ---------
# DESAFÍO 5

# Desarrollar un programa que lea 
# un numero entero cualquiera y 
# muestre en pantalla su tabla 
# de multiplicación

# RESOLUCIÓN

print('\n');
i = 0;
for i in range(11) :
    print(f'{nro} x {i} == {nro*i}');

"""
BUCLE for en Python:

for elemento in iterable:
     Hacer algo con el elemento

Ejemplo:
mi_lista = [1, 2, 3]
for n in mi_lista:
    print(n)

Función range() -> es una función integrada que crea 
una secuencia ordenada de enteros que podemos utilizar 
para crear iteraciones similares a las que hemos visto 
para otros lenguajes de programación.

range(inicio, fin, paso)

Inicio: es el valor inicial de la secuencia (0 si no se especifica).
Fin: es el valor final de la secuencia, el cual no se incluye en el resultado.
Paso: indica el incremento entre elementos de la secuencia (1 si no se especifica).

https://www.programaenpython.com/fundamentos/bucles-for-en-python/
"""

# ---------
# DESAFÍO 6

# Desarrollar un programa que lea 
# cuánto dinero tiene una persona 
# en su billetera y muestre cuántos 
# dólares ella puede comprar
#       Considerar: U$D 1.00 = R$ 3.27

# RESOLUCIÓN

print('\n');
reales = float(input('Cuánto tenés de dinero? '));
dolar = 3.27;
resultado = (reales / dolar);

print(f'Podés comprar: {resultado:.2f} U$D.');

# ---------
# DESAFÍO 7

# Desarrollar un programa que lea 
# el ancho y la altura de una pared 
# en metros, calcule su área y la 
# cantidad de pintura necesaria para pintar. 
#       Sabiendo que cada Litro de pintura pinta 
#      un área de 2m^2

# RESOLUCIÓN

print('\n');
anchoPared = float(input('Ingrese el ancho en metros: '));
alturaPared = float(input('Ingrese la altura en metros: '));
area = anchoPared * alturaPared;

print(f'Necesitas un total de {area / 2} Litros de pintura para pintar {area} m^2.');

# ---------
# DESAFÍO 8

# Desarrollar un programa que lea 
# el precio de un producto y muestre 
# su nuevo precio con 5% de descuento.

# RESOLUCIÓN

print('\n');
precio = float(input('Ingrese el precio del producto: '));
descuento = 0.05;

print(f'El precio del producto con descuento va a ser de R$ {precio - (precio * descuento)}');

# ---------
# DESAFÍO 9

# Desarrollar un programa que lea 
# el sueldo de un empleado y muestre
# su nuevo sueldo con 15% de aumento 

# RESOLUCIÓN

print('\n');
sueldo = float(input('Ingrese el sueldo del empleado: '));
aumento = 0.15;

print(f'El nuevo sueldo del empleado es de R$ {(sueldo * aumento) + sueldo}');
