# Variables Compuestas: Es una variable que almacena varios valores.

# --- TUPLAS:
# Se arranca con un paréntesis y son inmutables.

# indices:     0            1         2
combo = ('hamburguesa', 'gaseosa', 'flan')

print(combo[1:]) # muestra desde gaseosa hasta flan
print(combo[-1]) # muestra el ultimo elemento, en este caso: flan


# Metodos:
len() # me muestra la longitud de un array

print(len(combo)) # 3

# Bucles:
for i in combo:
	print(i) # imprime cada elemento del array

# Otra manera de imprimir:
for i, combo in enumerate(combo):
    print(f'La comida {combo}, en la posicion {i}')
  
 
# Organiza mi tupla en orden alfabetica o numerica
print(sorted(combo))