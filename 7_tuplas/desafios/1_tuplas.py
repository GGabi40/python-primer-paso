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
from random import randint

numerosAleatorios = ()

for i in range(5):
    numeroNuevo = randint(0,10)
    numerosAleatorios.append(numeroNuevo)
    print(numerosAleatorios)



# EJERCICIO 4

# Crea un programa que lea 4 valores por teclado 
# y los guarde en una tupla. Al final, mostrar:
#   A. Cuantas veces aparecio el valor 9
#   B. En que posicion fue tipeado el primer valor 3
#   C. Cuales fueron los numeros pares

# SOLUCION


# EJERCICIO 5

# Crea un programa que tenga una tupla unica con 
# nombres de productos y sus respectivos precios 
# en la secuencia.
#   Al final, mostrar la lita de los precios, 
# organizando los datos en forma tabular.

# SOLUCION


# EJERCICIO 6

# Crea un programa que tenga una tupla con varias palabras
# (sin tildes), despues, mostrar cuales son las vocales 
# de cada palabra.

# SOLUCION

