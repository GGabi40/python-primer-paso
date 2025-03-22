
# --- LISTAS:
# Son como las tuplas, pero se puede modificar. Utiliza [ ], a diferencia de la tupla.

#             0             1        2 
combo_dos = ['hamburguesa', 'gaseosa', 'flan']
print(combo_dos[2]) # flan

combo_dos[2] = "pizza"
print(combo_dos[2]) # pizza


## Métodos para agregar elementos:

# .append() -> Agrega un elemento al final de la lista.
combo_dos.append('papas')

print(combo_dos) # ['hamburguesa', 'gaseosa', 'flan', 'papas']


# .insert() -> Agrega un elemento en una posición especifica.
combo_dos.insert(0, 'pancho')

print(combo_dos) # ['pancho', 'hamburguesa', 'gaseosa', 'flan', 'papas']


## Métodos para eliminar elementos:

combo_dos = ['hamburguesa', 'gaseosa', 'flan']

# del
del combo_dos[2] # elimina 'flan'


# .pop() -> elimina el ultimo elemento, pero si se pasa un indice por parámetro,
# elimina al elemento que se encuentre en este índice.
combo_dos.pop(2) # elimina 'flan'


#.remove()
combo_dos.remove('gaseosa') # elimina gaseosa

# Para evitar errores:
if 'flan' in combo:
	combo.remove('flan')


## Crear una lista numérica:
valores = list(range(2,11))

# list -> crea una lista [ ]
# range() -> crea una secuencia numerica desde 2 hasta 10

print(valores) # [2, 3, 4, 5, 6, 7, 8, 9, 10]

# --- #
numeros = [ 6, 5, 1, 2, 4, 7]

# Para ordenarlos en orden numérica -> utilizar .sort()
ordenados = numeros.sort()

# Para ordenarlos en orden NO numérica -> utilizar .sort(reverse=True)
invertido = numeros.sort(reverse=True)