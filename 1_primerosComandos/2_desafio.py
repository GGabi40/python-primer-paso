# DESAFIO 1

# Crie un Script python que lea
# el nombre de una persona y muestre
# un mensaje de bienvenido de acuerdo
# con el valor escrito.

# -- SOLUCIÓN --
nome = input("Cómo te llamas?\n");
print('\t¡Bienvenido/a!', nome);

print("\n");
print("\n");

# DESAFIO 2

# Crie un Script python que lea
# el día, el mes y el año de nacimiento
# de una persona y muestre un
# mensaje con la fecha formatada

# -- SOLUCIÓN --
dia = input("Qué día nasciste?\n");
mes = input("Qué mes nasciste?\n");
anio = input("Qué año nasciste?\n");

print(f'\tNaciste el día {dia} del mes {mes} del año {anio}. Está bien?');

print("\n");
print("\n");

# DESAFIO 3

# Crie un Script python que lea
# dos numeros y mostrar la suma entre ellos

# -- SOLUCIÓN --
nro1 = int(input('Decime un numero\n'));
nro2 = int(input('Decime otro numero\n'));
resultado = nro1 + nro2;

print(f'\tLa suma de dos numeros es = {resultado} ');
