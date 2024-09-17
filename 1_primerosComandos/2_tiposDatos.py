n1 = int(input('Ingrese un numero: '));
n2 = int(input('Ingrese otro numero: '));

otroNumero =  input("Ingrese un tercer numero: ");
print(' el tercer numero es: ', type(otroNumero));

resultado = n1 + n2;
print(n1.is_integer());

print('La suma entre {} y {} es = {}'.format(n1, n2, resultado));
print(f'La suma entre {n1} y {n2} es = {resultado}');

#################

print("\n");
n = float(input('Ingrese un valor: '));
print(n);

#################

print("\n");
letra = input('Ingrese algo: ');
print(letra.isupper()); # Pregunta si está en mayuscula
print(letra.islower()); # Pregunta si está en minuscula
print(letra.isnumeric());# Pregunta si es un valor numérico
