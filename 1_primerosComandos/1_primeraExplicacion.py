# COMANDO PRINT()
print('Hola Mundo'); # Hola Mundo
print(4 + 2); # 6
print('4' + '2'); # 42
print('Hola', 2); # Hola 2

print('\n'); # Salto de linea

nome = 'Gabi'
edad = 24
peso = 44
print(nome, edad, peso); # Gabi 24 44

# PIDIENDO DATOS AL USUARIO
# COMANDO INPUT()
nome = input('Cómo te llamas?');
edad = input('Cuántos años tenés?');
peso = input('Cual es tu peso?');

print(nome, edad, peso);

# -----
# Utilizando f en print();
# Al utilizarlo, podrás acceder a los datos 
# más facilmente al momento de imprimirlo.

print(f'Otra manera de printear:\n\t{nome} {edad} {peso}');

print(f'Otra manera de printear:\n\t{nome} {edad} {peso}');

# -----
# Utilizando int en input();
# Utilizando el int para transformar lo obtenido por
# input:

anio = int(input('Qué anio nasciste?'));

# este int() transforma el dato String que se
# obtendría de input y lo transforma a un Entero
print(f'El dato año es de tipo: {type(anio)}');