# DESAFIO 1

# Crea un programa que lea el 
# nombre de una persona y muestre:
#       El nombre con todas las letras mayusculas;
#       El nombre con todas las letras minusculas;
#       Cuántas letras tiene (NO considerar espacios);
#       Cuántas letras tiene el primer nombre;

# -- SOLUCIÓN --

nombreCompleto = input('Ingrese nombre y apellido: ');
print(f'Tu nombre en Mayúscula: {nombreCompleto.upper()}');
print(f'Tu nombre en Minuscula: {nombreCompleto.lower()}');

sinEspacio = nombreCompleto.split();
sinEspacio = ''.join(sinEspacio);
print(f'Tu nombre completo posee un total de: {len(sinEspacio)} letras');

""" 
Otra alternativa: 
print(f'Tu nombre completo posee un total de: {len(nombreCompleto) - nombreCompleto.count(' ')} letras');
"""

primerNombre = nombreCompleto.split();
print(f'Tu primer nombre posee un total de: {len(primerNombre[0])} letras');

# DESAFIO 2

# Crea un programa que lea un 
# numero de 0 a 9999 y muestre en pantalla cada 
# uno de los digitos separados.
#   Ejemplo: 1834
#       unidad = 4;
#       decena = 3;
#       centena = 8;
#       millar = 4;

# -- SOLUCIÓN --

print('\n');
numero = int(input('Ingrese un numero de 0 a 9999: '));
print(f'Unidad: {numero % 10}');
print(f'Decena: {numero // 10 % 10}');
print(f'Centena: {numero // 100 % 10}');
print(f'Millar: {numero // 1000 % 10}');

""" ---> LÓGICA:
Primero lo divido por 10 y me devuelve 
el resultado sin coma (Divisón Entera),
luego agarro el resultado y verifico
cuál es el resto de la división por 10,
este es el número que busco.
Ejemplo: 123
    123 // 10 == 12
    12 % 10 == 2
"""

# DESAFIO 2

# Crea un programa que lea el 
# nombre de una ciudad y diga si arranca 
# o NO con el nombre "SANTO"

# -- SOLUCIÓN --

print('\n');
palabraReservada = 'SANTO';
nombreCiudad = input('Ingrese el nombre de la ciudad: ').strip();
fraccionado = nombreCiudad.upper().split();

print(f'El nombre de la ciudad tiene Santo? {fraccionado[0] == palabraReservada.upper()}');

""" Otra Alternativa:
print(f'El nombre de la ciudad tiene Santo? {nombreCiudad[:5].upper() == palabraReservada.upper()}');
"""


# DESAFIO 3

# Crea un programa que lea el 
# nombre de una persona y diga si 
# su nombre posee "SILVA"

# -- SOLUCIÓN --

print('\n');
palabraReservada = 'SILVA';
nombrePersona = input('Ingrese tu nombre: ').strip();

print(f'Hay Silva? {nombrePersona.upper().find(palabraReservada) != -1}');

""" Otra Alternativa:
print(f'Hay Silva? {palabraReservada in nombrePersona.upper()}');
"""

# DESAFIO 4

# Crea un programa que lea una 
# frase por teclado y muestre: 
#       Cuántas veces aparece la letra "A";
#       En qué posición aparece por primera vez;
#       En qué posición aparece por última vez;

# -- SOLUCIÓN --

print('\n');
frase = input('Ingrese una frase: ').lower().strip();
print(f'La letra a aparece: {frase.count('a')} veces');
print(f'La letra a aparece por primera vez en la posición: {frase.find('a')}.');
print(f'La letra a aparece por última vez en la posición: {frase.rfind('a')}.');



# DESAFIO 5

# Crea un programa que lea el 
# nombre completo de una persona mostrando
# el primer y último nombre separdamente.
#   Ejemplo: Ana Maria de Souza
#       primeiro = Ana
#       último = Souza

# -- SOLUCIÓN --

print('\n');
nombre = input('Ingrese tu nombre: ').strip();
separado = nombre.split();
longitud = len(separado);

print(f'Tu primer nombre: {separado[0]}');
print(f'Tu último nombre: {separado[longitud-1]}');
