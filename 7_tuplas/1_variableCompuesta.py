# Las variables Compuestas almacenan 
# varios valores:

tupla = ('hola', 'como', 'va')

print(tupla)
print(tupla[0])
print(tupla[1:])

# son inmutables.

for i in tupla:
    print(i)

# Otra manera de imprimir:
for i in range(len(tupla)):
    print(tupla[i])
    
# Otra manera de imprimir:
for i, frase in enumerate(tupla):
    print(f'La frase {frase}, en la posicion {i}')


# Organizarlo:
print(sorted(tupla))


#########

a = (1,2,3,4)
b = (5,6,7,8)
c = a + b

print(c)
print(c.count(5)) # cuantas veces aparece el 5 en 
# mi tupla

print(c.index(5)) # en que posicion aparece el 5

#########
# Eliminar una tupla:
pessoa = ('Gabi', 24, 'F', 44.58)
print(pessoa)
del(pessoa)

