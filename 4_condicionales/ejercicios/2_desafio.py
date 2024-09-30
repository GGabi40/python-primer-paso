### CONDICIONALES ANIDADOS
colores = {
    'limpia': '\033[m',
    'amarillo': '\033[33m',
    'azul': '\033[34m',
    'negrita': '\033[1m',
    'FondoRojo': '\033[30;41m',
    'FondoAmarillo': '\033[43m',
    'FondoVerde': '\033[1;44m',
    'Invertido': '\033[7;40m'
}

from time import sleep;

# DESAFIO 1

# Crea un programa para aprobar un empréstimo 
# bancário para la compra de una casa.
# El programa va a preguntar el valor de la casa, 
# el sueldo del comprador y en cuántos años 
# podrá pagar.
#   Calcule el valor de la prestación mensual, 
#   sabiendo que ella no podrá exceder el 30% 
#   del sueldo, si pasa esto, el empréstimo 
#   será denegado.

# -- SOLUCIÓN --

sueldo = float(input('Ingrese su sueldo: '))
prestamo = float(input('Ingrese el valor de la casa: '))
años = int(input('Ingrese en cuántos años pagarás la casa: '))

cantMeses = años * 12
prestacionMensual = prestamo / cantMeses
porcentajeSueldo = (100 * prestacionMensual)  / sueldo

print(f"""\nEl valor del préstamo $ {prestamo}, será pago mensualmente por {cantMeses} meses en el valor de
       $ {prestacionMensual:.2f}, esto representa un {colores['amarillo']}{porcentajeSueldo:.2f}%{colores["limpia"]} de su sueldo.""")

print('\nProcesando...')

print('\n');

for i in range(5):
    print('.', end='', flush=True);
    sleep(0.2);

print('\n');


if(porcentajeSueldo > 30):
    print(f'{colores["FondoRojo"]}El préstamo no está autorizado{colores["limpia"]}, ya que no debe exceder el 30% de su sueldo.')
else:
    print(f'{colores["FondoVerde"]}El préstamo autorizado.{colores["limpia"]}')



# DESAFIO 2

# Escribir un programa que lea el 
# un número entero cualquiera y pida 
# para el usuario elegir cuál será 
# la base de conversión:
#   1. Binario
#   2. Octal
#   3. Hexadecimal

# -- SOLUCIÓN --

print('\n')
salir = 0

while(salir == 0):
    print('-=' *20)
    print(f'\n{colores["azul"]}CONVERSOR DE NÚMEROS{colores["limpia"]}\n');
    print('-=' *20)
    numero = int(input('\nIngrese un numero entero: '))
    convertir = int(input("""En qué desea convertir? \n\t1. Binario\n\t2. Octal\n\t3. Hexadecimal\n"""))

    if(convertir == 1): 
        print(f'\nEl valor Binario de {numero} es: {bin(numero)[2:]}')
    elif(convertir == 2):
        print(f'\nEl valor Octal de {numero} es: {oct(numero)[2:]}')
    elif(convertir == 3):
        print(f'\nEl valor Octal de {numero} es: {hex(numero)[2:]}')
    else:
        print(f'\n{colores["FondoRojo"]}Ingrese un valor válido.{colores["limpia"]}')
    
    salir = int(input('¿Desea Continuar?\n\t0. Continuar\n\t1. Salir '))

print(f'\n{colores["FondoAmarillo"]}Fin de bucle.{colores["limpia"]}')


# DESAFIO 3

# Escribir un programa que lea dos
# números enteros y los compare mostrando 
# un mensaje por pantalla:
#   El primer valor es mayor
#   El segundo valor es mayor
#   No existe valor mayor, los dos son iguales

# -- SOLUCIÓN --

print('\n')

nro1 = int(input('Ingrese un numero entero: '))
nro2 = int(input('Ingrese otro numero entero: '))

if(nro1 > nro2):
    print(f'{nro1} es mayor que {nro2}')
elif(nro2 > nro1):
    print(f'{nro2} es mayor que {nro1}')
else:
    print('Los dos son iguales')


# DESAFIO 4

# Hacer un programa que lea el año 
# de nacimiento de un joven e informe, 
# de acuerdo con su edad:
#   Si todavía no se puede anotar al sevicio militar.
#   Si ya es hora de que se anote al sevicio militar.
#   Si ya pasó la hora de que se anote al sevicio militar.

# El programa también debe mostrar el tiempo 
# que falta o pasó de este plazo.

# -- SOLUCIÓN --

from datetime import date;
print('\n')
nacimiento = int(input('Ingrese tu año de nacimiento: '))

edad = date.today().year - nacimiento

if (edad < 18):
    print(f'Tenés {edad} años. Todavía no se puede anotar al servicio miliar.')
    tiempoFalta = 18 - edad
    print(f'Todavía faltan {tiempoFalta} años para esto.')
elif(edad == 18):
    print(f'Tenés {edad} años. Ya es hora de que se anotar al servicio miliar.')
else:
    print(f'Tenés {edad} años. Ya pasó la hora de que se anote al sevicio militar.')
    tiempoPasado = edad - 18
    print(f'Se han pasado {tiempoPasado} años.');


# DESAFIO 5

# Hacer un programa que lea dos notas de un
# alumno y calcule su média, mostrando 
# un mensaje en el final, de acuerdo a su média:
#   Abajo de 5.0: REPROBADO
#   Entre 5.0 y 6.9: A RECUPERAR
#   7.0 o Superior : APROBADO

# -- SOLUCIÓN --

print('\n')

nota1 =  float(input('Ingrese la primera nota: '))
nota2 =  float(input('Ingrese la segunda nota: '))

media = (nota1 + nota2) / 2

if(media >= 7):
    print(f'{colores["FondoVerde"]}APROBADO.{colores["limpia"]}')
elif(media < 5):
    print(f'{colores["FondoRojo"]}REPROBADO.{colores["limpia"]}')
elif(7 > media >= 5):
    print(f'{colores["FondoAmarillo"]}HACER RECUPERATORIO.{colores["limpia"]}')
else:
    print('Algo pasó...')

# DESAFIO 6

# La Confederación Nacional de Natación
# necesita de un programa que lea el año
# de nacimiento de un atleta y muestre su 
# categoria de acuerdo a su edad:
#   Hasta 9 años: Mirin
#   Hasta 14 años: Infantil
#   Hasta 19 años: Junior
#   Hasta 20 años: Senior
#   Arriba: Master

# -- SOLUCIÓN --

print('\n')
nacimiento = int(input('Ingrese tu año de nacimiento: '))
edad = date.today().year - nacimiento

if(edad <= 9):
    print(f'{edad} años. CATEGORÍA: MIRÍN')
elif(edad <= 14):
    print(f'{edad} años. CATEGORÍA: INFANTIL')
elif(edad <= 19):
    print(f'{edad} años. CATEGORÍA: JUNIOR')
elif(edad <= 19):
    print(f'{edad} años. CATEGORÍA: SENIOR')
elif(edad > 20):
    print(f'{edad} años. CATEGORÍA: MASTER')


# DESAFIO 7

# Rehacer el desafío de los triángulos, 
# acrescentando el recurso de mostrar qué tipo 
# de triángulo será formado:
#   Equilatero: Todos lados iguales
#   Isósceles: Dos lados iguales
#   Escaleno: Todos lados diferentes

# -- SOLUCIÓN --

print('\n');

r1 = float(input('Ingrese la primera longitud: '))
r2 = float(input('Ingrese la segunda longitud: '))
r3 = float(input('Ingrese la tercera longitud: '))
bandera = False

if(r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2):
    print('Se PUEDE formar un triángulo.')
    bandera = True
else:
    print('NO se PUEDE formar un triángulo.')

if(bandera):
    if (r1 == r2 == r3):
        print('Triángulo Equilátero.')
    elif(r1 == r2 or r2 == r3 or r1 == r2):
        print('Triángulo Isósceles.')
    else:
        print('Triángulo Escaleno.')


# DESAFIO 8

# Desarrolle una lógica que lea 
# el peso y la altura de una persona,
# calcule su IMC y muestre su status, 
# de acuerdo con la tabla:
#   Abajo de 18.5: Por debajo del peso
#   Entre 18.5 y 25: Peso ideal
#   Desde 25 hasta 30: Sobrepeso
#   Desde 30 hasta 40: Obesidad
#   Arriba de 40: Obesidad mórbida

# -- SOLUCIÓN --


print('\n');

peso = float(input('Ingrese su peso en Kg: '))
altura = float(input('Ingrese su altura em Metros: '))

imc = peso / altura**2

if(imc < 18.5):
    print(f'IMC de {imc:.2f}. Está por debajo del peso ideal.')
elif(imc >= 18.5 and imc < 25):
    print(f'IMC de {imc:.2f}. Está en su peso ideal.')
elif(imc >= 25 and imc < 30):
    print(f'IMC de {imc:.2f}. Tiene sobrepeso.')
elif(imc >= 30 and imc < 40):
    print(f'IMC de {imc:.2f}. Tiene Obesidad.')
else:
    print(f'IMC de {imc:.2f}. Tiene Obesidad Mórbida.')



# DESAFIO 9

# Desarrolle un programa que calcule el 
# valor que se debe pagar por un producto, 
# considerando su precio normal y 
# modo de pago:
#   Efectivo: 10% descuento
#   Débito: 5% descuento
#   Crédito 2x: precio normal
#   Crédito 3x o más: 20% de interés

# -- SOLUCIÓN --

print('\n');

precio = float(input('Ingrese el precio del producto: '))
opcionPago = int(input('Ingrese el modo de pago:\n\t1. Efectivo\n\t2. Débito\n\t3. Crédito en x2\n\t4. Crédito en x3\n'))

if opcionPago == 1:
    print(f'\n¡Pagarás en Efectivo! 10% de Descuento. El precio final del producto es de {colores["amarillo"]}$ {precio-(precio*0.10)}{colores["limpia"]}.')
elif opcionPago == 2:
    print(f'\n¡Pagarás con Débito! 5% de Descuento. El precio final del producto es de {colores["amarillo"]}$ {precio-(precio*0.05)}{colores["limpia"]}.')
elif opcionPago == 3:
    print(f'\n¡Pagarás con Crédito! El precio final del producto es de {colores["amarillo"]}$ {precio}{colores["limpia"]}.')
elif opcionPago == 4:
    print(f'\n¡Pagarás con Crédito en x2! Se agregan intereses. El precio final del producto es de {colores["amarillo"]}$ {precio + (precio*0.20)}{colores["limpia"]}.')
else:
    print("Opción no válida")


# DESAFIO 10

# Desarrolle un programa que haga la 
# computadora jugar Jokenpo con vos.
#   Piedra, papel o tijera

# -- SOLUCIÓN --

print('\n')

from random import choice


print(f'{colores["azul"]}-={colores["limpia"]}' * 30)
print(f'\n{colores["Invertido"]}Piedra, Papel o Tijeras{colores["limpia"]}\n')
print(f'{colores["azul"]}-={colores["limpia"]}' * 30)
print(f'\n¿Estás Listo?\n')

juegosPosibles = ['piedra', 'papel', 'tijeras']
reglas = {
    'piedra': 'tijeras',
    'papel': 'piedra',
    'tijeras': 'papel'
}
computadoraElige = choice(juegosPosibles)

salir = 0
while(salir == 0):
    jugadorElige = input('¿Qué elegis jugar? PIEDRA, PAPEL O TIJERAS?\n').lower().strip()

    print('\nPROCESANDO...\n')
    sleep(1)

    if jugadorElige not in reglas:
        print(f'{colores["FondoRojo"]}Elija una opción correcta.{colores["limpia"]}')
    else:
        if(computadoraElige == jugadorElige):
            print(f'{colores["azul"]}¡EMPATE!{colores["limpia"]} \nLa computadora eligió {colores["amarillo"]}{computadoraElige}{colores["limpia"]} y el jugador {colores["amarillo"]}{jugadorElige}{colores["limpia"]}\n')
        elif(reglas[jugadorElige] == computadoraElige):
            print(f'{colores["FondoVerde"]}¡GANASTE!{colores["limpia"]} \nLa computadora eligió {colores["amarillo"]}{computadoraElige}{colores["limpia"]} y el jugador {colores["amarillo"]}{jugadorElige}{colores["limpia"]}\n')
        else:
            print(f'{colores["FondoRojo"]}¡PERDISTE!{colores["limpia"]} \nLa computadora eligió {colores["amarillo"]}{computadoraElige}{colores["limpia"]} y el jugador {colores["amarillo"]}{jugadorElige}{colores["limpia"]}\n')
    
    sleep(1)
    salir = int(input('\nDesea salir?\n\t0. Seguir jugando\n\t1. Salir del juego\n'))

print(f'{colores["negrita"]}\nMuchas gracias por jugar.{colores["limpia"]}')
