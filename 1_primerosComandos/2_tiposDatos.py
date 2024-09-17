# Solicitando al usuario que ingrese dos números enteros
n1 = int(input('Ingrese un número: '))  # El int() convierte el valor ingresado (que es un string) a un número entero
n2 = int(input('Ingrese otro número: '))  # Igual que en n1, el valor se convierte a entero

# Solicitando un tercer número pero sin convertirlo a entero
otroNumero = input("Ingrese un tercer número: ")  # Este valor se ingresa como texto (string)
print('El tercer número es de tipo: ', type(otroNumero))  # Aquí verificamos el tipo de dato del tercer número con type()

# Sumando los dos primeros números
resultado = n1 + n2  # Se suman los dos números enteros
print(n1.is_integer())  # Aquí se verifica si n1 es un número entero utilizando el método is_integer()

# Imprimiendo el resultado de la suma de dos maneras distintas
print('La suma entre {} y {} es = {}'.format(n1, n2, resultado))  # Se usa el método format() para insertar los valores
print(f'La suma entre {n1} y {n2} es = {resultado}')  # Aquí se utiliza f-string, que permite insertar variables directamente en el string

# -----

print("\n")  # Salto de línea

# Solicitando al usuario un valor decimal (flotante)
n = float(input('Ingrese un valor: '))  # El float() convierte el valor ingresado a un número decimal (flotante)
print(n)  # Se imprime el número decimal ingresado

# -----

print("\n")

# Solicitando al usuario que ingrese un texto
letra = input('Ingrese algo: ')  # Se recibe una cadena de texto como entrada
print(letra.isupper())  # Verifica si el texto está en mayúsculas
print(letra.islower())  # Verifica si el texto está en minúsculas
print(letra.isnumeric())  # Verifica si el texto ingresado es un valor numérico (solo dígitos)
