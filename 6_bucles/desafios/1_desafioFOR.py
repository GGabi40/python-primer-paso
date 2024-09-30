# DESAFÍOS BUCLE FOR
# ------------------ #

# EJERCICIO 1

# Crea un programa que muestre por pantalla 
# una cuenta regresiva para la explosión de 
# fuegos artificiales, yendo desde 10 hasta 0, 
# con una pausa de 1 segundo entre ellas.

# SOLUCIÓN

from time import sleep
import emoji

print('¡Arranca la cuenta regresiva!')

for i in range(10, 0, -1):
    print(i)
    sleep(1)

print(emoji.emojize(':fireworks:') * 20)

# EJERCICIO 2

# Crea un programa que muestre por pantalla 
# todos los numeros pares que están en el 
# intervalo entre 1 y 50.

# SOLUCIÓN

print('\n')
for i in range(2, 50, 2):
    print(i)

# EJERCICIO 3

# Crea un programa que calcule la suma entre 
# todos los numeros impares que son múltiplos 
# de 3 y que se encuentran en el 
# intervalo de 1 a 500.

# SOLUCIÓN

print('\n')

suma = 0

for i in range(1, 501, 2):
    if(i % 3 == 0):
        suma += i

print(f'La suma total: {suma}')


# EJERCICIO 4

# Crea un programa que lea seis numeros 
# enteros y muestre la suma solamente 
# de aquellos que son pares. Si el 
# valor es impar, hay que desconsiderar.

# SOLUCIÓN

print('\n')

suma = 0
for i in range(0, 6):
    numero = int(input(f'Ingrese el {i+1} numero: '))
    if(numero % 2 == 0):
        suma += numero

print(f'La suma total: {suma}')


# EJERCICIO 5

# Crea un programa que lea el primer 
# termino y lea la razón de una Progresión Aritmética. 
# Al final, muestre los 10 primeros terminos
# de estas progresión

# SOLUCIÓN

print('\n')

print('=' * 20)
print('PA'.center(20))
print('=' * 20)

primero = int(input('Ingrese el primer término: '))
razon = int(input('Razón: '))
decimo = primero + (10-1) * razon

for c in range(primero, decimo+razon, razon):
    print(f'{c}', end=' -> ')

print('Terminó.')

# EJERCICIO 6

# Crea un programa que lea un numero entero 
# y diga si es o no un numero primo

# SOLUCIÓN

numero = int(input('Ingrese un numero: '))
primo = True

for i in range(2, numero):
    if(numero % i == 0):
        primo = False

print(f'{numero} es primo' if primo else f'{numero} NO es primo')


# EJERCICIO 7

# Crea un programa que lea una frase cualquiera 
# y diga si es un palíndromo.
# Palíndromo: se lee igual de atrás para adelante
# Hay que desconsiderar los espacios.

# SOLUCIÓN

print('\n')

frase = input('Ingrese una frase: ').strip().upper()

fraseArray = frase.split()
fraseSinEspacio = ''.join(fraseArray)
inverso = fraseSinEspacio[::-1]

#for letra in range(len(fraseSinEspacio)-1, -1, -1):
#    inverso += fraseSinEspacio[letra]

print(f'FRASE: \033[33m{frase}\033[m al revés: \033[1m{inverso}\033[m')

print(f'\033[32m{frase}\033[m es un Palíndromo' if fraseSinEspacio == inverso else f'\033[31m{frase}\033[m NO es un Palíndromo')


# EJERCICIO 8

# Crea un programa que lea el año de 
# nacimiento de siete personas. Al final, 
# muestre cuántas personas todavía 
# son menores y cuántas mayores.

# SOLUCIÓN


print('\n')

from datetime import date

contadorMayor, contadorMenor = [0, 0]
añoActual = date.today().year

for i in range(7):
    añoNacimiento = int(input((f'Año de nacimiento de persona {i+1}: ')))
    edad = añoActual - añoNacimiento
    if(edad > 18):
        contadorMayor += 1
    else:
        contadorMenor += 1

print(f'La cant de mayores de edad es de: {contadorMayor}, de menores: {contadorMenor}')



# EJERCICIO 9

# Crea un programa que lea el peso de 
# 5 personas y que al final, muestre cuál 
# fue el mayor peso y cuál el menor peso.

# SOLUCIÓN

print('\n')

mayor = 0
menor = 0
persona = 0
personaBajo = 0

for i in range(5):
    peso = float(input((f'Peso en kg de persona {i+1}: ')))
   
    if(i == 0):
        mayor = peso
        menor = peso
        personaBajo = i
        persona = i
    else:
        if(peso > mayor):
            mayor = peso
            persona = i
        
        if(peso < menor):
            menor = peso
            personaBajo = i

print(f'El mayor peso, pesa: {mayor} kg, de la persona {persona}')
print(f'El menor peso, pesa: {menor} kg, de la persona {personaBajo}')


# EJERCICIO 10

# Desarrollar un programa que lea el 
# nombre, edad y sexo de 4 personas. 
# Al final mostrar:
#   Média de edad del grupo
#   El nombre del hombre más grande
#   Cuántas mujeres tienen menos de 20 años.

# SOLUCIÓN

accEdad = 0
cantMenoresMujeres = 0

for i in range(4):
    nombre = input(f'Nombre de persona {i+1}: ').strip().capitalize()
    edad = int(input(f'Edad de persona {i+1}: '))
    sexo = int(input(f'Sexo de persona {i+1}: \n\033[32m[ 1 ] Hombre\n[ 2 ] Mujer\n[ 3 ] No Binario\033[m\n'))

    accEdad += edad

    if(sexo == 1):
        if(i == 0):
            mayorHombre = edad
            nombreMayorHombre = nombre
        else:
            if(edad > mayorHombre):
                mayorHombre = edad
                nombreMayorHombre = nombre
    elif(sexo == 2):
        if(edad < 20):
            cantMenoresMujeres += 1

mediaEdad = accEdad / 4

print(f'La média de edad del grupo es de: {mediaEdad}')
print(f'El hombre más grande del grupo es {nombreMayorHombre}, tiene: {mayorHombre}')
print(f'La cant de mujeres menor de 20 años es de: {cantMenoresMujeres}')
