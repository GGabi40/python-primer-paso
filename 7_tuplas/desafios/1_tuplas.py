# DESAFÍOS TUPLAS
# ------------------ #

# EJERCICIO 1

# Crea un programa que tenga una tupa
# totalmente rellenada con un 
# contaje por extenso, desde 0 hasta 20.
#   Tu programa debera leer un numero por 
#   teclado (entre 0 y 20) y 
#   mostrarlo por extenso

# SOLUCION

numeros_escritos = (
    'cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez',
    'once', 'doce', 'trece', 'catorce', 'quince', 'dieciséis', 'diecisiete', 'dieciocho', 'diecinueve', 'veinte'
)

usuario = int(input('Ingrese un numero de 0 a 20: '))

print(f'El numero {usuario} escrito por extenso es: {numeros_escritos[usuario]}')



# EJERCICIO 2

# Crea una tupla rellenada con los 20 primeros
# puestos de la Tabla del Campeonato Brasileno de Futbol,
# en orden. Despues, mostrar:
#   OK - Solo los primeros 5 puestos.
#   OK - Los ultimos 4 puestos.
#   OK - Una lista con los equipos en orden alfabetico.
#   OK - En que posicion de la tabla esta el equipo Chapecoense.

# SOLUCION

print('')

equipos = (
    'Botafogo', 'Palmeiras', 'Fortaleza', 'Flamengo', 'Sao Paulo',
    'Internacional', 'Bahia', 'Cruzeiro', 'Vasco da Gama', 'Cambuense',
    'Gremio', 'Criciuma', 'Bragantino', 'Juventude', 'Athletico Paranaense',
    'Fluminense', 'Vitoria', 'Corinthians', 'Cuiaba', 'Avai'
)

print(f'Los primeros 5 puestos: ')
for i in range(5):
    print(f'{i+1}. {equipos[i]}')

print(f'\nLos ultimos 4 puestos: ')
for i in range(16,20):
    print(f'{i+1}. {equipos[i]}')
    
print(f'\nLista en orden Alfabetica: ')
print(sorted(equipos))

equipoBusqueda = str(input('\nDe que equipo te gustaria buscar la posicion en la tabla? ')).capitalize().strip()
if(equipoBusqueda in equipos):
    print(f'{equipoBusqueda} esta en la posicion {equipos.index(equipoBusqueda)}')
else:
    print(f'{equipoBusqueda} no esta en el ranking.')


# EJERCICIO 3

# Crea un programa que genera 5 numeros aleatorios y
# los pone en una tupla.
# Despues de esto, poner la lista de numeros generados 
# y tambien indique el menor y el mayor valor que estan 
# en la tupla

# SOLUCION

print('')
from random import sample
# sample: method returns a list with a specified 
# number of randomly selected items from a sequence.

numerosAleatorios = (sample(range(20), 5))

print(f'Los numeros aleatorios fueron: {numerosAleatorios}')
print(f'El mayor numero es: {max(numerosAleatorios)}')
print(f'El menor numero es: {min(numerosAleatorios)}')


print('\n')

# EJERCICIO 4

# Crea un programa que lea 4 valores por teclado OK
# y los guarde en una tupla. Al final, mostrar:
#   A. Cuantas veces aparecio el valor 9 OK
#   B. En que posicion fue tipeado el primer valor 3 OK
#   C. Cuales fueron los numeros pares

# SOLUCION

tupla = tuple(int(input('Ingrese un numero: '))for t in range(1, 5))

pares = 0
for i in range(0,4):
    if tupla[i] % 2 == 0:
        pares = pares+1


print(f'El numero 9 apareció {tupla.count(9)} veces')
print(f'El numero 3 apareció en la posición {tupla.index(3)+1}.' if 3 in tupla else f'No había 3 en la tupla.')
print(f'Hay {pares} numeros pares')


print('\n')


# EJERCICIO 5

# Crea un programa que tenga una tupla unica con 
# nombres de productos y sus respectivos precios 
# en la secuencia.
#   Al final, mostrar la lita de los precios, 
# organizando los datos en forma tabular.

# SOLUCION

print(f'{'\033[32m'}~~{'\033[m'}'*20)
print(f'{"Lista de precios":^40}')
print(f'{'\033[32m'}~~{'\033[m'}'*20)

productos = (
            'Lapis', 1.80,
            'lapicera', 2.90,
            'regla', 9.00,
            'papel A4', 1.20,
            'papel oficio', 2.10
            )

for i in range(0, len(productos)):
    if i % 2 == 0:
        print(f'{productos[i].title():.<30}', end='')
    else:
        print(f'U$D {productos[i]:.2f}')


# EJERCICIO 6

# Crea un programa que tenga una tupla con varias palabras
# (sin tildes), despues, mostrar cuales son las vocales 
# de cada palabra.

# SOLUCION

tupla = (
    'papa',
    'pierna',
    'pereba',
    'naranja',
    'cerebelo'
    )

for i in tupla:
    print(f'Las vocales de la palabra {i.upper()} son: ', end='')
    for letra in i:
        if letra in 'aeiou':
            print(f' {letra}', end='')
    print('')