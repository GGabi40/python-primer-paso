# Los operadores aritméticos en Python permiten realizar operaciones matemáticas
# comunes, tales como la suma, resta, multiplicación, entre otras.
# A continuación te muestro los operadores más utilizados y ejemplos de su uso:

# SUMA (+)
# Este operador se utiliza para sumar dos valores.
a = 10
b = 5
suma = a + b
print(f'La suma de {a} + {b} es {suma}')  # Resultado: 15

# RESTA (-)
# Este operador se utiliza para restar un valor de otro.
resta = a - b
print(f'La resta de {a} - {b} es {resta}')  # Resultado: 5

# MULTIPLICACIÓN (*)
# Este operador se utiliza para multiplicar dos valores.
multiplicacion = a * b
print(f'La multiplicación de {a} * {b} es {multiplicacion}')  # Resultado: 50

# DIVISIÓN (/)
# Este operador se utiliza para dividir un valor entre otro.
division = a / b
print(f'La división de {a} / {b} es {division}')  # Resultado: 2.0

# DIVISIÓN ENTERA (//)
# La división entera devuelve solo la parte entera del resultado.
division_entera = a // b
print(f'La división entera de {a} // {b} es {division_entera}')  # Resultado: 2

# MÓDULO O RESTO (%)
# El operador de módulo devuelve el resto de la división entre dos números.
modulo = a % b
print(f'El módulo de {a} % {b} es {modulo}')  # Resultado: 0

# EXPONENTIACIÓN (**)
# Este operador se utiliza para elevar un número a la potencia de otro.
potencia = a ** b
print(f'La potencia de {a} ** {b} es {potencia}')  # Resultado: 100000

# Tambien se puede utilizar la función pow(numero, potencia);
print(f'La potencia de {a} ** {b} es {pow(a, b)}');

# *** Orden de precedencia ***

# 1. () → Paréntesis
# 2. ** → Potenciación
# 3. * ;  / ;   // ;  % → Multiplicación, división, división entera y resto
# 4. + ; -

# **** Con Strings ****

resultado = 'oi'*5;
print(resultado);

resultado = '='* 20;
print(resultado);

nome = input('Ingrese tu nombre: ');

# Centrado:
print(f'Hola, {nome:*^20}');
# Alineado a la derecha:
print(f'Hola, {nome:*>20}');
# Alineado a la izquierda:
print(f'Hola, {nome:*<20}');

# Repite el nombre 10 veces:
print(f'Que onda, {nome*10}');
# Repite el nombre 10 veces con espacio:
print(f'Que onda, {(nome.capitalize() + ' ') * 10}');
