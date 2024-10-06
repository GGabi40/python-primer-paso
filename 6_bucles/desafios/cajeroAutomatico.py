# EJERCICIO 6

# Crear un programa que simule el 
# funcionamiento de un caja electrónico. 
# En el inicio, preguntar al usuario cuál 
# será el valor que se quiere sacar (num entero) 
# y el programa va a informar cuántos billetes 
# de cada valor serán entregados.
#   PD: considerar que el caja posee billetes 
#   de $ 50; $ 20; $ 10; $ 1

# SOLUCIÓN

print('-=' *20)
print('Cajero Automatico'.center(40))
print('-=' *20)

print('\n')

contadores = [0, 0, 0, 0]
billetes = [50, 20, 10, 1]

sacar = float(input('Cuanto desea sacar? '))

while sacar <= 0:
    print('Es impossible realizar esta operacion. Ingrese un valor valido.')
    sacar = float(input('Cuanto desea sacar? '))

total = sacar
totalBilletes = 0

for i in range(len(billetes)):
    while total >= billetes[i]:
        total -= billetes[i]
        contadores[i] += 1

print(f'Se sacarán:')
for i in range(len(contadores)):
    if contadores[i] > 0:
        print(f'{contadores[i]} billetes de {billetes[i]}')
